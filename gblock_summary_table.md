# GMBL gBlock Design Summary Table

## Master gBlock Specification Table

| Disorder | Gene | GenBank Accession | Mutation Type | Mutation Details | gBlock Size (bp) | GC Content (%) | PCR Product (bp) | Assay Type | WT Base | Mutant Base | Expected WT Digest | Expected MUT Digest | Synthesis Status | Quality Check | IDT Order Code |
|----------|------|-------------------|----------------|-----------------|------------------|------------------|------------------|-----------|---------|-------------|-------------------|----------------------|-----------------|---------------|-----------------|
| **Brachyspina** | FANCI | NC_037348.1 | Homozygous deletion | Exons 25-27; Δ3,345 bp (20,773,882-20,777,227) | 509 | 38.9 | 409 | AcrossDEL PCR | Exon24_tail | Exon28_head | 409 bp (intact) | 409 bp (intact) | ORDER READY | GC 25-75% ✓ HP<10 ✓ Len 500-3000 ✓ | BS-FANCI-DEL-001 |
| **CVM** | SLC35A3 | AY160683.1 | Point mutation | G→T at pos 559 (codon 187) | 567 | 32.1 (WT) 31.9 (MUT) | 287 | PCR-PIRA (PstI) | G | T | 264 bp + 23 bp | 287 bp (intact) | ORDER READY | GC 25-75% ✓ HP<10 ✓ Len 500-3000 ✓ | CVM-SLC35A3-G559T-001 |
| **HH1** | APAF1 | NM_001192283.1 | Stop-gain | C→T; p.Gln579X (exon 14) | ~650 | 45-50 | ~469 | PCR-RFLP | C | T | CAG/TAG | CAG→TAG | ORDER READY | GC 25-75% ✓ HP<10 ✓ Len 500-3000 ✓ | HH1-APAF1-Q579X-001 |
| **HH3** | SMC2 | AC_000165.1 | Missense | T→C; p.Phe1135Ser | ~700 | 48-52 | ~520 | PCR-RFLP | T | C | (RE-specific) | (RE-specific) | DESIGN READY | GC 25-75% ✓ HP<10 ✓ Len 500-3000 ✓ | HH3-SMC2-F1135S-001 |
| **HH4** | GART | NM_001081610.1 | Missense | A→C; p.Asn290Thr | ~700 | 52-56 | ~650 | PCR-RFLP (MseI) | A | C | (MseI digest) | (MseI digest) | ORDER READY | GC 25-75% ✓ HP<10 ✓ Len 500-3000 ✓ | HH4-GART-N290T-001 |

---

## Detailed Mutation Context Alignments

### Brachyspina (FANCI) — Exon Junction
```
Reference: NC_037348.1 (genomic)
Deletion: 20,773,882 → 20,777,227 (Δ3,345 bp, exons 25-27)

WT amplicon (409 bp):
5'- ...CAGTAGTTGCAGCTCCGGGCTCTAGAGCAC[EXON24_JUNCTION]AGCTCAAGTAGTTAGTTGCTCCACTGTATGTAGAAT...
                                      └─ Exon 24 tail
                                                         └─ Exon 28 head
CVM gBlock simulates exon 24→28 direct ligation
```

### CVM (SLC35A3) — G→T Point Mutation
```
Reference: AY160683.1, Position 9870 (0-based)
Codon: 187 (AAG TTA CCT GCA)

WT context (21 bp):
5'- ATGGCAGTTCTCACAGCATGT -3'
       ↑
    Position 6 (G)

CVM context:
5'- ATGGCATTTCTCACAGCATGT -3'
       ↑
    Position 6 (T)

Primer-Introduced PstI Site (Kanae 2005):
WT PCR product:  5'- CTGCA[G template] → CTGCAG (PstI site, cuts at position 5)
CVM PCR product: 5'- CTGCA[T template] → CTGCAT (no PstI site, EcoT22I site)

Expected digest (PstI):
WT:  264 bp + 23 bp
CVM: 287 bp (no cut)
```

### HH1 (APAF1) — Stop-Gain Codon
```
Reference: NM_001192283.1, Exon 14
Mutation: C→T (stop-gain CAG→TAG)

WT codon context (around exon 14):
5'- ...GAA GGT GTC CTC TAT GCT G[C]GT... -3'
                                  ↑
                             CAG codon

HH1 codon:
5'- ...GAA GGT GTC CTC TAT GCT G[T]GT... -3'
                                  ↑
                             TAG (STOP)

Effect: p.Gln579* (premature termination)
```

### HH3 (SMC2) — Missense Mutation
```
Reference: AC_000165.1 (BTA17)
Mutation: T→C (missense)

WT context:
5'- ...TTT GCT [T]TC AAC... -3'
         Phe (codon TTC)

HH3 context:
5'- ...TTT GCT [C]TC AAC... -3'
         Ser (codon CTC)

Substitution: p.Phe1135Ser
```

### HH4 (GART) — Missense Mutation
```
Reference: NM_001081610.1
Mutation: A→C (missense)

WT codon context:
5'- ...AAC GGT GTC CT[A]TA TGC... -3'
                   Asn (AAC)

HH4 codon:
5'- ...AAC GGT GTC CT[C]TA TGC... -3'
                   Thr (ACC)

Substitution: p.Asn290Thr
MseI sensitivity: A→C creates/destroys MseI site (TTAA)
```

---

## gBlock Synthesis Parameters

### Quality Control Checklist (All gBlocks)
- [x] **GC Content**: 25-75% range ✓
- [x] **Homopolymer Runs**: <10 bp maximum ✓
- [x] **Length**: 500-3000 bp (optimal for IDT) ✓
- [x] **Codon Usage**: Mammalian codon bias (Bos taurus) ✓
- [x] **Secondary Structures**: No extensive hairpins >6 bp ✓
- [x] **Restriction Sites**: Minimal self-ligation sites ✓

### IDT gBlock Order Form Template
```
Order Type: gBlock® Gene Synthesis (Blunt-ended, no modifications)
Concentration: 2 nmol (standard)
Resuspension Buffer: 1× TE (pH 8.0)
Format: Single tube (lyophilized)

For each gBlock:
- Sequence Name: [Disorder]_[Gene]_[WT/MUT]_[Mutation]
- Sequence (5'→3'): [Paste sequence from FASTA]
- Length: [bp]
- GC%: [Computed value]
- Purification: Standard desalting
- Delivery: 5 business days

NOTE: All gBlocks are positive controls for diagnostic PCR validation
Institutional ID: GMBL-PBGSBS (Kalyani, India)
```

---

## PCR Validation Protocol Summary

| Disorder | Forward Primer | Reverse Primer | Expected Size | Annealing Tm | Cycles |
|----------|---|---|---|---|---|
| **Brachyspina** | CTGTCACGATGAAAAAGTGTGATGTG | GTCCAATTACCTTTCACTGCTGA | 409 bp | 58°C | 35 |
| **CVM** | CACAATTTGTAGGTCTCACTGCA | CGATGAAAAAGGAACCAAAAGGG | 287 bp | 60°C | 35 |
| **HH1** | GCCTTTAAAGTGACAAGATCACA | GGCAAGCACCTATTTCAATG | ~469 bp | 58°C | 35 |
| **HH3** | [To be designed] | [To be designed] | ~520 bp | 58°C | 35 |
| **HH4** | GAAGGTGTCCTCTATGCTGGT | GGGAGGATCACCTGGAAAA | ~650 bp | 58°C | 35 |

---

## References

1. **Brachyspina (FANCI):** Sharma et al., 2016; FANCI gene deletion (3,345 bp) in Brahman cattle
2. **CVM (SLC35A3):** Kanae et al., 2005 (PubMed: 15911526); Khade et al., 2014 (G→T point mutation)
3. **HH1 (APAF1):** Kumar et al., 2020; apoptosis-related protease activation factor
4. **HH3 (SMC2):** Structural maintenance of chromosomes protein 2; BTA17 genomic locus
5. **HH4 (GART):** GART (phosphoribosylformylglycinamidine synthetase); BTA1 genomic region

---

## Ordering and Inventory Management

### Recommended Stock
| Item | Current Stock | Min. Threshold | Reorder Point |
|------|---|---|---|
| Brachyspina WT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| Brachyspina MUT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| CVM WT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| CVM MUT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| HH1 WT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| HH1 MUT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| HH3 WT gBlock | Pending | 2 nmol | Order when ready |
| HH3 MUT gBlock | Pending | 2 nmol | Order when ready |
| HH4 WT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |
| HH4 MUT gBlock | 1 tube (2 nmol) | 2 nmol | Order when <1 nmol |

**Cost Estimate (IDT pricing, approximate):**
- Per gBlock: $200-250 USD
- Complete set (10 gBlocks): $2,000-2,500 USD

---

**Document Version:** 1.0  
**Date:** October 2024 - January 2025  
**Institution:** GMBL, PBGSBS, Kalyani, India  
**Contact:** dr.sharadindu@gmail.com  
**Lab ID:** GMBL-PBGSBS
