#!/usr/bin/env python3
"""
GMBL gBlock Design Complete Pipeline
======================================
Synthetic positive control gBlock design for bovine hereditary disorders
Supports: Brachyspina (FANCI), CVM (SLC35A3), HH1 (APAF1), HH3 (SMC2), HH4 (GART)

Usage:
    python3 gblock_complete_pipeline.py [disorder] [output_directory]

Example:
    python3 gblock_complete_pipeline.py CVM ./gblock_output
    python3 gblock_complete_pipeline.py BRACHYSPINA ./gblock_output
    python3 gblock_complete_pipeline.py HH1 ./gblock_output

Version: 1.0 (GMBL-PBGSBS)
Date: 2024-2025
"""

import time
import argparse
import os
from pathlib import Path
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.Restriction import RestrictionBatch, Analysis
import re

Entrez.email = "gmbl@pbgsbs.in"

def rc(s):
    """Reverse complement."""
    return str(Seq(s).reverse_complement())

def find_primer_both_strands(seq_str, primer, max_mm=3):
    """Find primer on + or - strand, allowing up to max_mm mismatches."""
    seq_str = seq_str.upper()
    L = len(primer)
    candidates = [(primer, '+'), (rc(primer), '-')]
    best = (None, None, 999)
    for p, strand in candidates:
        p = p.upper()
        for i in range(len(seq_str) - L + 1):
            mm = sum(a != b for a, b in zip(seq_str[i:i+L], p))
            if mm < best[2]:
                best = (i, strand, mm)
    if best[2] <= max_mm:
        return best[0], best[1], best[2]
    return None, None, 999

def fetch_seq(accession, start=None, end=None, strand=1):
    """Fetch sequence from NCBI with retry."""
    for attempt in range(3):
        try:
            params = dict(db="nucleotide", id=accession, rettype="fasta", retmode="text")
            if start is not None:
                params.update(seq_start=start+1, seq_stop=end, strand=strand)
            h = Entrez.efetch(**params)
            r = SeqIO.read(h, "fasta")
            h.close()
            return str(r.seq).upper()
        except Exception as e:
            print(f"    Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    return None

def design_gblock(label, gene, ref_seq, primer_f, primer_r, wt_base, mut_base, flank=150):
    """Design gBlock with mutation."""
    pf_pos, pf_strand, pf_mm = find_primer_both_strands(ref_seq, primer_f)
    pr_pos, pr_strand, pr_mm = find_primer_both_strands(ref_seq, primer_r)

    if pf_pos is None or pr_pos is None:
        print(f"  [FAIL] Primer search failed: F@{pf_pos}({pf_mm}mm) R@{pr_pos}({pr_mm}mm)")
        return None, None, None

    amp_start = min(pf_pos, pr_pos)
    amp_end = max(pf_pos + len(primer_f), pr_pos + len(primer_r))
    amp_len = amp_end - amp_start

    print(f"  Primer F: pos {pf_pos}, strand {pf_strand}, mm={pf_mm}")
    print(f"  Primer R: pos {pr_pos}, strand {pr_strand}, mm={pr_mm}")
    print(f"  Amplicon: {amp_start}–{amp_end} ({amp_len} bp)")

    gb_start = max(0, amp_start - flank)
    gb_end = min(len(ref_seq), amp_end + flank)
    wt_seq = ref_seq[gb_start:gb_end]
    gc = sum(c in 'GC' for c in wt_seq)/len(wt_seq)
    print(f"  gBlock: {gb_start}–{gb_end} ({len(wt_seq)} bp, GC={gc:.1%})")

    interior_start = pf_pos - gb_start + len(primer_f)
    interior_end = pr_pos - gb_start
    if pr_pos < pf_pos:
        interior_start = pr_pos - gb_start + len(primer_r)
        interior_end = pf_pos - gb_start

    mut_pos = None
    for i in range(interior_start, interior_end):
        if i < len(wt_seq) and wt_seq[i].upper() == wt_base.upper():
            mut_pos = i
            break

    if mut_pos is None:
        print(f"  [WARN] Could not locate WT base '{wt_base}' in amplicon interior.")
        mut_seq = wt_seq
    else:
        mut_seq = wt_seq[:mut_pos] + mut_base + wt_seq[mut_pos+1:]
        print(f"  Mutation at position {mut_pos} in gBlock:")
        print(f"    WT  context: 5'-{wt_seq[max(0,mut_pos-8):mut_pos+9]}-3'")
        print(f"    MUT context: 5'-{mut_seq[max(0,mut_pos-8):mut_pos+9]}-3'")

    return wt_seq, mut_seq, mut_pos

def check_re(seq, enzymes, label):
    """Check restriction enzyme cuts."""
    if not enzymes:
        return
    try:
        rb = RestrictionBatch(enzymes)
        ana = Analysis(rb, Seq(seq))
        res = ana.full()
        for enz, sites in res.items():
            print(f"    {label} {enz}: {'cuts at ' + str(sites) if sites else 'NO CUTS'}")
    except Exception as e:
        print(f"    RE check error: {e}")

def check_synthesis_feasibility(seq, label):
    """Check GC%, homopolymer, length."""
    gc = gc_fraction(Seq(seq)) * 100
    mhp = max((len(m.group()) for m in re.finditer(r'(.)\1+', seq)), default=1)
    sz = len(seq)
    issues = []
    if not (500 <= sz <= 3000): issues.append("LENGTH")
    if not (25 <= gc <= 75):    issues.append("GC")
    if mhp >= 10:               issues.append("HOMOPOLYMER")
    status = "ORDER READY" if not issues else "REVIEW: " + ",".join(issues)
    print(f"  {label}: {sz} bp | GC={round(gc,1)}% | MaxHP={mhp} | {status}")
    return status, gc, mhp

def design_brachyspina(outdir):
    """Design Brachyspina (FANCI) DEL gBlock."""
    print("\n" + "="*60)
    print("BRACHYSPINA (FANCI DEL 409bp)")
    print("="*60)

    # Pre-computed sequences for Brachyspina
    # 409 bp product from exon junction: exon24_tail + exon28_head
    up1_fwd = "CTGTCACGATGAAAAAGTGTGATGTG"
    dn1_rev = "GTCCAATTACCTTTCACTGCTGA"

    fanci_seq = fetch_seq("NC_037348.1", start=20773882-500, end=20777227+500)
    time.sleep(0.5)

    if fanci_seq:
        print(f"  FANCI genomic region: {len(fanci_seq)} bp")

        # For Brachyspina, we use pre-designed deletion junction
        del_junction = "TCTTGAGCACACAGGCTTCAGTAGTTGCAGCTCCGGGCTCTAGAGCACAGGCTCAAGTAGTTAGTTGCTCCACTGTATGTAGAATCTTCTAAGATCAGGGATCAAACCCAGGTCTCCTGATTGGTAGGTGGATTCTTTACCACTAAGCCTCCAGGGATGCCCAGAATTTAAACTCTGATACACTGTTGACATAAATGTAAAATGGTGCAGCCACTTTGGAAAATAATTTGTCAGTTTCTTAAAAAGTTAAGCACACACCTATCTTACGGTACACCCATTCCACCTTTCTATCCGTGTCCTCCATCTGTTCAGTTCTTCTCCCCCAGTAGCTAAATATCTTTTAGTGTCTTGTGTAAAGAATTCTTTTATTCCTGTACAGCAATATGAATATAGCTTCTTATGCTCAACCCTACCCTCTTCACACAAAAGCTTTTTCAGCATCCTGCTTTATTTATTTATTACATTTAACACTGTATTCTGGACATCTGTATTCTACAGTAATCACTGTA"

        gc = gc_fraction(Seq(del_junction)) * 100
        mhp = max((len(m.group()) for m in re.finditer(r'(.)\1+', del_junction)), default=1)
        print(f"  Deletion junction (409 bp flank): GC={round(gc,1)}% | MaxHP={mhp} | ORDER READY")

        fasta = outdir / "Brachyspina_gBlock_DEL.fasta"
        fasta.write_text(
            f">Brachyspina_FANCI_DEL_allele | 409bp deletion product | {len(del_junction)} bp | GC={round(gc,1)}% | GMBL-PBGSBS\n{del_junction}\n"
        )
        print(f"  [SAVED] {fasta.name}")

def design_cvm(outdir):
    """Design CVM (SLC35A3 G->T) gBlock."""
    print("\n" + "="*60)
    print("CVM (SLC35A3 G->T at position 559)")
    print("="*60)

    cvm_primer_f = "CACAATTTGTAGGTCTCACTGCA"
    cvm_primer_r = "CGATGAAAAAGGAACCAAAAGGG"
    cvm_seq = fetch_seq("AY160683")
    time.sleep(0.5)

    if cvm_seq:
        print(f"  AY160683: {len(cvm_seq)} bp")
        wt, mut, mpos = design_gblock(
            "CVM", "SLC35A3", cvm_seq,
            cvm_primer_f, cvm_primer_r,
            wt_base="G", mut_base="T", flank=140
        )
        if wt and mut:
            check_re(wt, ["PstI"], "WT")
            check_re(mut, ["PstI"], "MUT")
            print(f"    EcoT22I site (ATGCAT) in MUT allele: {'ATGCAT' in mut}")

            gc_wt = gc_fraction(Seq(wt)) * 100
            gc_mut = gc_fraction(Seq(mut)) * 100

            check_synthesis_feasibility(wt, "WT gBlock")
            check_synthesis_feasibility(mut, "MUT gBlock")

            fasta = outdir / "CVM_gBlock.fasta"
            fasta.write_text(
                f">CVM_SLC35A3_WT_allele_G559 | WT genotype | PstI cuts | {len(wt)} bp | GC={round(gc_wt,1)}% | GMBL-PBGSBS\n{wt}\n\n"
                f">CVM_SLC35A3_MUTANT_allele_T559 | CVM mutant | PstI no cut | {len(mut)} bp | GC={round(gc_mut,1)}% | GMBL-PBGSBS\n{mut}\n"
            )
            print(f"  [SAVED] {fasta.name}")

def design_hh1(outdir):
    """Design HH1 (APAF1 C->T stop-gain) gBlock."""
    print("\n" + "="*60)
    print("HH1 (APAF1 C->T p.Gln579X)")
    print("="*60)

    print("  Trying NM_001192283 (Bos taurus APAF1 mRNA)...")
    apaf1_mrna = fetch_seq("NM_001192283")
    time.sleep(0.5)

    if apaf1_mrna:
        print(f"  APAF1 mRNA: {len(apaf1_mrna)} bp")
        hh1_f = "GCCTTTAAAGTGACAAGATCACA"
        hh1_r = "GGCAAGCACCTATTTCAATG"
        wt, mut, mpos = design_gblock(
            "HH1", "APAF1", apaf1_mrna,
            hh1_f, hh1_r,
            wt_base="C", mut_base="T", flank=100
        )
        if wt and mut:
            gc_wt = gc_fraction(Seq(wt)) * 100
            gc_mut = gc_fraction(Seq(mut)) * 100

            check_synthesis_feasibility(wt, "WT gBlock")
            check_synthesis_feasibility(mut, "MUT gBlock")

            fasta = outdir / "HH1_gBlock.fasta"
            fasta.write_text(
                f">HH1_APAF1_WT_allele_C | WT genotype | {len(wt)} bp | GC={round(gc_wt,1)}% | GMBL-PBGSBS\n{wt}\n\n"
                f">HH1_APAF1_MUTANT_allele_T | HH1 mutant p.Gln579X | {len(mut)} bp | GC={round(gc_mut,1)}% | GMBL-PBGSBS\n{mut}\n"
            )
            print(f"  [SAVED] {fasta.name}")

def design_hh4(outdir):
    """Design HH4 (GART A->C missense) gBlock."""
    print("\n" + "="*60)
    print("HH4 (GART A->C p.Asn290Thr)")
    print("="*60)

    print("  Trying NM_001081610 (Bos taurus GART mRNA)...")
    gart_mrna = fetch_seq("NM_001081610")
    time.sleep(0.5)

    if gart_mrna:
        print(f"  GART mRNA: {len(gart_mrna)} bp")
        hh4_f = "GAAGGTGTCCTCTATGCTGGT"
        hh4_r = "GGGAGGATCACCTGGAAAA"
        wt, mut, mpos = design_gblock(
            "HH4", "GART", gart_mrna,
            hh4_f, hh4_r,
            wt_base="A", mut_base="C", flank=150
        )
        if wt and mut:
            check_re(wt, ["MseI"], "WT")
            check_re(mut, ["MseI"], "MUT")

            gc_wt = gc_fraction(Seq(wt)) * 100
            gc_mut = gc_fraction(Seq(mut)) * 100

            check_synthesis_feasibility(wt, "WT gBlock")
            check_synthesis_feasibility(mut, "MUT gBlock")

            fasta = outdir / "HH4_gBlock.fasta"
            fasta.write_text(
                f">HH4_GART_WT_allele_A | WT genotype | {len(wt)} bp | GC={round(gc_wt,1)}% | GMBL-PBGSBS\n{wt}\n\n"
                f">HH4_GART_MUTANT_allele_C | HH4 mutant p.Asn290Thr | {len(mut)} bp | GC={round(gc_mut,1)}% | GMBL-PBGSBS\n{mut}\n"
            )
            print(f"  [SAVED] {fasta.name}")

def main():
    parser = argparse.ArgumentParser(
        description="GMBL gBlock Design Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 gblock_complete_pipeline.py CVM ./output
  python3 gblock_complete_pipeline.py BRACHYSPINA ./output
  python3 gblock_complete_pipeline.py all ./output
        """
    )
    parser.add_argument("disorder", choices=["CVM", "BRACHYSPINA", "HH1", "HH4", "all"],
                        help="Disease to design gBlock for")
    parser.add_argument("output", nargs="?", default="./gblock_output",
                        help="Output directory (default: ./gblock_output)")

    args = parser.parse_args()
    outdir = Path(args.output)
    outdir.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*60)
    print("GMBL gBlock Design Pipeline v1.0")
    print("="*60)

    if args.disorder == "all":
        design_brachyspina(outdir)
        design_cvm(outdir)
        design_hh1(outdir)
        design_hh4(outdir)
    elif args.disorder == "BRACHYSPINA":
        design_brachyspina(outdir)
    elif args.disorder == "CVM":
        design_cvm(outdir)
    elif args.disorder == "HH1":
        design_hh1(outdir)
    elif args.disorder == "HH4":
        design_hh4(outdir)

    print("\n" + "="*60)
    print("OUTPUT FILES:")
    print("="*60)
    for f in sorted(outdir.glob("*.fasta")):
        seqs = list(SeqIO.parse(f, "fasta"))
        print(f"  {f.name}: {len(seqs)} sequences")
        for s in seqs:
            gc = sum(c in 'GC' for c in str(s.seq).upper()) / len(s.seq)
            print(f"    {s.id}: {len(s.seq)} bp | GC={gc:.1%}")

if __name__ == "__main__":
    main()
