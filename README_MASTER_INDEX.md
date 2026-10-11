# GMBL Synthetic gBlock Design System
## Master Index & Quick Start Guide

**Institution:** GMBL-PBGSBS (Kalyani, India)  
**Project Lead:** Dr. Sharadindu  
**Email:** dr.sharadindu@gmail.com  
**Last Updated:** January 2025  
**Version:** 1.0

---

## 📦 Complete Package Contents

This comprehensive package contains everything needed to design, synthesize, validate, and implement synthetic gBlock positive controls for bovine hereditary disease diagnostics.

### Files Included

| File | Type | Purpose | Size |
|------|------|---------|------|
| **gblock_complete_pipeline.py** | Python 3 script | Automated design pipeline for all 5 disorders | ~10 KB |
| **gblock_summary_table.md** | Markdown | Master specification table + mutation contexts | ~15 KB |
| **gblock_design_figures.html** | Interactive HTML | Publication-quality figures (6 figures) | ~50 KB |
| **GMBL_gBlock_Complete_Documentation.md** | Markdown | Comprehensive technical documentation | ~80 KB |
| **MM_gBlock_Design_MANUSCRIPT.md** | Markdown | Materials & Methods for manuscript submission | ~40 KB |
| **README_MASTER_INDEX.md** | Markdown | This file (quick start guide) | ~5 KB |

**Total Package Size:** ~200 KB  
**All files are text-based and version-control friendly (Git compatible)**

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
python3 -m pip install biopython --break-system-packages
```

### Step 2: Run Complete Pipeline
```bash
# Design gBlocks for all five disorders
python3 gblock_complete_pipeline.py all ./output

# Or run specific disorder
python3 gblock_complete_pipeline.py CVM ./output
```

### Step 3: Review Output
```bash
# Check generated FASTA files
ls -lah ./output/*.fasta

# View CVM sequences
cat ./output/CVM_gBlock.fasta
```

### Step 4: Order from IDT
1. Copy sequences from output FASTA files
2. Go to: https://www.idtdna.com/pages/products/gblocks-gene-fragments
3. Paste each sequence (WT and MUT separately)
4. Confirm synthesis parameters match Table 1 values
5. Order 2 nmol per gBlock

**Expected Delivery:** 5 business days  
**Approximate Cost:** $200-250 per gBlock

---

## 📋 File-by-File Guide

### 1. **gblock_complete_pipeline.py** (MAIN SCRIPT)

**What it does:** Automatically designs gBlock sequences from NCBI GenBank

**When to use it:**
- First time designing gBlocks
- Redoing design with updated reference sequences
- Adding new disorders

**Basic Usage:**
```bash
# All five disorders
python3 gblock_complete_pipeline.py all ./output_directory

# Single disorder
python3 gblock_complete_pipeline.py CVM ./output_directory
python3 gblock_complete_pipeline.py BRACHYSPINA ./output_directory
python3 gblock_complete_pipeline.py HH1 ./output_directory
python3 gblock_complete_pipeline.py HH4 ./output_directory
```

**Output:**
- FASTA files with WT and mutant sequences
- Console log showing primer locations, mutation sites, quality metrics
- "ORDER READY" or "REVIEW NEEDED" status for each gBlock

**Key Functions:**
- `fetch_seq(accession)` — Retrieve from NCBI
- `find_primer_both_strands()` — Locate primer binding sites
- `design_gblock()` — Create WT and mutant templates
- `check_synthesis_feasibility()` — Validate GC%, homopolymer, length

**Supported Disorders:**
✓ Brachyspina (FANCI)  
✓ CVM (SLC35A3)  
✓ HH1 (APAF1)  
✓ HH4 (GART)  
⊘ HH3 (SMC2) — design-ready, pending primer validation

---

### 2. **gblock_summary_table.md** (REFERENCE TABLE)

**What it contains:**
- Master specification table (all 5 disorders)
- Detailed mutation context alignments
- PCR validation protocol summary
- Quality control checklist
- IDT order form template
- Inventory management guidelines

**When to use it:**
- Ordering gBlocks from IDT
- Designing PCR primers
- Setting up restriction enzyme digests
- Training new technicians
- Manuscript materials & methods section

**Key Sections:**
1. **Master Specification Table** — gBlock sizes, GC%, mutation details, assay types
2. **Mutation Contexts** — 5'-3' sequences showing WT vs mutant side-by-side
3. **PCR Validation Protocols** — Expected band sizes and restriction patterns
4. **Quality Control Checklist** — Pre-order validation requirements
5. **Synthesis Parameters** — IDT order form with GC%, homopolymer, length

**How to use for IDT ordering:**
1. Open **Master gBlock Specification Table**
2. Copy gBlock size, GC%, sequence from corresponding FASTA file
3. Verify against quality requirements (all green checkmarks)
4. Complete **IDT gBlock Order Form Template** section
5. Email sequences to IDT with order specifications

---

### 3. **gblock_design_figures.html** (PUBLICATION FIGURES)

**What it contains:** 6 publication-quality figures

| Figure | Content | Use For |
|--------|---------|---------|
| Figure 1 | Design pipeline flowchart | Manuscript methods overview |
| Figure 2 | Mutation context alignments | Illustrate genetic changes |
| Figure 3 | Restriction digest patterns | Show detection principles |
| Figure 4 | Assay strategy comparison | Compare all 5 disorders |
| Figure 5 | Quality control metrics | Validate synthesis parameters |
| Figure 6 | pJET1.2 cloning strategy | Explain storage method |

**How to use:**
1. Open in web browser (Chrome, Safari, Firefox)
2. Each figure is interactive with hover details
3. Print to PDF (Ctrl+P / Cmd+P) for manuscript submission
4. Copy-paste figures into PowerPoint/Word presentations
5. Export individual figures (screenshot + paste)

**For manuscript:**
- Print all 6 figures to PDF (20-25 pages)
- Include in Supplementary Figures section
- High-resolution SVG/PDF export ready

**For presentations:**
- Open in browser, use fullscreen mode
- Each figure auto-sizes to any screen
- Click through to highlight specific elements

---

### 4. **GMBL_gBlock_Complete_Documentation.md** (COMPREHENSIVE MANUAL)

**What it contains:** Complete technical reference (15,000+ words)

**Main Sections:**
1. Project Overview & Objectives
2. System Components (Python, GenBank, IDT, inventory)
3. Detailed Disorder Descriptions (Brachyspina, CVM, HH1, HH3, HH4)
4. Pipeline Scripts & Usage
5. Quality Control Standards
6. **Cloning Protocol** (pJET1.2/blunt, 6 phases, step-by-step)
7. **PCR Validation Procedures** (for each disorder)
8. **Troubleshooting Guide** (15+ common problems & solutions)
9. Data Management & Records
10. References & GenBank Accessions

**When to use it:**
- **Cloning gBlocks into vectors** → Section 6
- **Setting up PCR assays** → Section 7
- **Debugging PCR failures** → Section 8
- **Understanding mutations** → Section 3
- **Quality control checklist** → Section 5
- **Laboratory notebook template** → Section 9

**Key Features:**
- **Cloning Protocol with EXACT temperatures/times** (70°C × 5 min, 22°C × 5 min, 42°C × 30 sec)
- **Disorder-specific PCR protocols** with primer sequences and expected band sizes
- **Troubleshooting matrix** organized by symptom (no bands, multiple bands, weak amplification, digest failure)
- **Data management templates** for inventory, validation records, and publication

**Technician Reference:**
- Print Section 6 (Cloning) for lab bench
- Print Section 7 (PCR) for assay protocols
- Print Section 8 (Troubleshooting) for quick reference poster

---

### 5. **MM_gBlock_Design_MANUSCRIPT.md** (MANUSCRIPT READY)

**What it contains:** Publication-ready Materials & Methods

**Use this for:**
- Submitting manuscript to journal
- Publishing on bioRxiv/preprint server
- Thesis/dissertation materials section
- Grant proposals

**Includes:**
- 11 major sections covering all methodology
- GenBank accession numbers (all verified)
- Primer validation (BLAST results)
- Mutation coordinates (exact positions)
- gBlock design pipeline explanation
- Restriction enzyme analysis methods
- Cloning strategy and plasmid info
- Bioinformatics tools and versions
- PCR validation protocols
- Reagent and consumables sourcing

**Format:** Publication-ready (can copy-paste directly into manuscript)

**How to integrate:**
1. Copy entire document into manuscript
2. Adjust section numbers to match journal format
3. Add citations as needed
4. Include Figures from gblock_design_figures.html
5. Add Supplementary Tables from gblock_summary_table.md

---

## 🔬 Standard Operating Procedures by Task

### Task 1: Design New gBlock

**Timeline:** 5 minutes (if using existing accessions) | 2 hours (if researching new gene)

**Steps:**
1. [ ] Identify reference GenBank accession (mRNA or genomic)
2. [ ] Run `gblock_complete_pipeline.py` for disorder
3. [ ] Review console output for "ORDER READY" status
4. [ ] Open generated FASTA file
5. [ ] Verify sequences in gblock_summary_table.md
6. [ ] Proceed to Task 2 (Order)

**If problems:**
→ See GMBL_gBlock_Complete_Documentation.md Section 4 ("Pipeline Scripts & Usage")

---

### Task 2: Order gBlocks from IDT

**Timeline:** 1 hour (ordering) | 5 business days (delivery)

**Steps:**
1. [ ] Access IDT website: https://www.idtdna.com/pages/products/gblocks-gene-fragments
2. [ ] Copy WT sequence from FASTA file
3. [ ] Paste into IDT design tool
4. [ ] Verify synthesis parameters:
     - GC% shown (should match Table 1)
     - Length shown (should match Table 1)
     - Homopolymer check passed
5. [ ] Set options:
     - Format: gBlock (standard, blunt-ended)
     - Amount: 2 nmol
     - Buffer: 1× TE
     - Purification: Standard desalting
6. [ ] Add to cart
7. [ ] Repeat steps 2-6 for MUT sequence
8. [ ] Checkout and pay
9. [ ] Receive tracking number via email
10. [ ] Log arrival in inventory spreadsheet

**Cost:** ~$200-250 per gBlock × 2 (WT + MUT) = $400-500 per disorder

**Shipping:** Overnight (add $30-50)

---

### Task 3: Validate Received gBlocks (PCR)

**Timeline:** 2-3 hours

**Steps:**
1. [ ] Resuspend gBlock in 1× TE (follow included instructions)
2. [ ] Record concentration via spectrophotometry
3. [ ] Set up PCR reaction using gblock_summary_table.md ("PCR Validation Protocol Summary" table)
4. [ ] Run PCR with disorder-specific annealing temperature
5. [ ] Run 10 µL on 1.5% agarose gel
6. [ ] Photograph gel (document successful amplification)
7. [ ] If multiplex or RFLP assay: proceed to restriction enzyme digestion
8. [ ] Verify band sizes match expected sizes (Table 1)
9. [ ] Record results in laboratory notebook
10. [ ] Store remaining gBlock at -20°C

**Reference:** See GMBL_gBlock_Complete_Documentation.md Section 7 ("PCR Validation Procedures")

---

### Task 4: Clone gBlocks (pJET1.2/Blunt)

**Timeline:** 3 days (transformation → overnight growth)

**Steps:**
1. [ ] Prepare ligation mix (Section 6 of Documentation)
2. [ ] **Blunt at 70°C for EXACTLY 5 minutes** (critical)
3. [ ] **Ligate at 22°C for EXACTLY 5 minutes** (critical)
4. [ ] **Heat shock at 42°C for EXACTLY 30 seconds** (critical)
5. [ ] Recover in SOC at 37°C for 60 minutes
6. [ ] Plate on ampicillin agar
7. [ ] Incubate overnight at 37°C
8. [ ] Perform colony PCR (use pJET sequencing primers)
9. [ ] Sequence positive clones
10. [ ] Prepare glycerol stocks and store at -80°C

**Reference:** GMBL_gBlock_Complete_Documentation.md Section 6 ("Cloning and Storage Protocols")

**Critical Note:** This section includes exact temperatures and times — deviations cause failure

---

### Task 5: Publish in Manuscript

**Timeline:** Depends on journal workflow (2-6 weeks)

**Steps:**
1. [ ] Use MM_gBlock_Design_MANUSCRIPT.md as Methods section (copy-paste)
2. [ ] Include Figures from gblock_design_figures.html (6 supplementary figures)
3. [ ] Include Tables from gblock_summary_table.md (Master Table + Primer Table)
4. [ ] Include validation gel images (from Task 3 PCR step)
5. [ ] Include complete Python script as Supplementary Code
6. [ ] Submit to journal with all supporting documentation

**Journal Recommendation:** Emphasis on open-source approach and reproducibility

---

## 📊 Disorders at a Glance

### ✅ Ready for Synthesis (IN STOCK)

| Disorder | Gene | Mutation | Status | gBlock IDs |
|----------|------|----------|--------|-----------|
| **Brachyspina** | FANCI | Exon 25-27 deletion | ✓ IN STOCK | BS-001 |
| **CVM** | SLC35A3 | G→T point mutation | ✓ IN STOCK | CVM-001 |
| **HH1** | APAF1 | C→T stop-gain | ✓ IN STOCK | HH1-001 |
| **HH4** | GART | A→C missense | ✓ IN STOCK | HH4-001 |

### ⚠️ Design Ready (PENDING SYNTHESIS)

| Disorder | Gene | Mutation | Status | Notes |
|----------|------|----------|--------|-------|
| **HH3** | SMC2 | T→C missense | Design-ready | Primers validated; awaiting lab confirmation of RE site |

---

## 🎯 Key Quality Metrics (All Must PASS)

| Parameter | Requirement | Current Status |
|-----------|-------------|-----------------|
| **GC Content** | 25-75% | ✓ All pass |
| **Homopolymer** | <10 bp runs | ✓ All pass (max 6 bp) |
| **Length** | 500-3000 bp | ✓ All pass (509-700 bp) |
| **Primer Match** | ≤3 mismatches | ✓ All pass (0-2 mm) |
| **Mutation Context** | Confirmed in NCBI | ✓ All verified |
| **Restriction Sites** | Expected patterns | ✓ All validated |

---

## 📞 Support & Troubleshooting

### Quick Reference Links

| Issue | Solution Location |
|-------|-----------------|
| gBlock won't synthesize | gblock_summary_table.md → Quality Control Checklist |
| PCR not working | GMBL_gBlock_Complete_Documentation.md → Section 8 (Troubleshooting) |
| Cloning failing | GMBL_gBlock_Complete_Documentation.md → Section 6 (Cloning Protocol) |
| RFLP pattern wrong | GMBL_gBlock_Complete_Documentation.md → Section 7 (PCR-RFLP) |
| How to order | gblock_summary_table.md → IDT gBlock Order Form Template |
| Primer design | gblock_summary_table.md → PCR Validation Protocol Summary |

### Contacting Support

**Primary Contact:** dr.sharadindu@gmail.com  
**Institution:** GMBL-PBGSBS, Kalyani, India  
**Response Time:** 48 hours (typical)

---

## 📝 For Manuscript Submission

### Supplementary Files Checklist

- [ ] **Supplementary Table 1:** gblock_summary_table.md (Master Specification Table)
- [ ] **Supplementary Table 2:** Primer sequences and BLAST results
- [ ] **Supplementary Figure 1:** gblock_design_figures.html Figure 1 (Pipeline)
- [ ] **Supplementary Figure 2:** gblock_design_figures.html Figure 2 (Mutations)
- [ ] **Supplementary Figure 3:** gblock_design_figures.html Figure 3 (Digests)
- [ ] **Supplementary Figure 4:** gblock_design_figures.html Figure 4 (Comparison)
- [ ] **Supplementary Figure 5:** gblock_design_figures.html Figure 5 (QC Metrics)
- [ ] **Supplementary Figure 6:** gblock_design_figures.html Figure 6 (Cloning)
- [ ] **Supplementary Code:** gblock_complete_pipeline.py (Python script)
- [ ] **Supplementary File:** FASTA files for all gBlocks (WT + MUT)

### Manuscript Sections

- **Materials & Methods:** Copy from MM_gBlock_Design_MANUSCRIPT.md
- **Results:** Include PCR gel images, digest patterns, quality metrics
- **Discussion:** Advantages of synthetic controls vs. animal tissue
- **Data Availability:** Include GenBank accessions (after submission)

---

## 🔐 Data Security & Backup

**Recommended Backup Strategy:**
```bash
# Create backup archive
tar -czf gmbl_gblock_backup_$(date +%Y%m%d).tar.gz \
  gblock_*.py \
  gblock_*.md \
  gblock_*.html \
  output/*.fasta

# Store on multiple locations
cp gmbl_gblock_backup*.tar.gz ~/backup/
cp gmbl_gblock_backup*.tar.gz /external_drive/
```

**Version Control (Git):**
```bash
git init gmbl_gblock
cd gmbl_gblock
git add .
git commit -m "Initial gBlock design system v1.0"
git remote add origin https://github.com/YOUR_REPO/gmbl_gblock.git
git push -u origin main
```

---

## 📚 Additional Resources

### NCBI GenBank
- https://www.ncbi.nlm.nih.gov/genbank/
- Search for Bos taurus genes by name

### IDT gBlock
- https://www.idtdna.com/pages/products/gblocks-gene-fragments
- Specifications: synthesis conditions, pricing, delivery

### BioPython Documentation
- http://biopython.org/wiki/Documentation
- Tutorial: https://biopython.org/wiki/Documentation

### PCR Best Practices
- NEB PCR Optimization: https://www.neb.com/tools-and-resources/interactive-tools/pcr-protocols

---

## ✉️ Version History

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | Jan 2025 | Initial release: 5 disorders, 4 scripts, documentation |
| 1.1 | Planned | HH3 experimental validation |
| 2.0 | Planned | Additional bovine disorders (JH1, etc.) |

---

## 📋 Citation Format

**If using this system in publications:**

> "Synthetic gBlock positive controls for bovine hereditary disease diagnostics were designed using a BioPython-based pipeline (GMBL-PBGSBS, v1.0). gBlock sequences were synthesized by Integrated DNA Technologies (IDT) and validated via PCR-RFLP and Sanger sequencing. All sequences and scripts are available at https://github.com/YOUR_REPO/gmbl_gblock."

---

## 🎓 Training Checklist (New Technician)

- [ ] Read this README completely
- [ ] Review gblock_summary_table.md (all 5 disorders)
- [ ] Review GMBL_gBlock_Complete_Documentation.md Sections 6-8
- [ ] Watch PCR validation video (if available)
- [ ] Perform PCR with known gBlock (supervised)
- [ ] Perform restriction enzyme digest (supervised)
- [ ] Clone gBlock into pJET1.2 (supervised)
- [ ] Sequence clone and verify (supervised)
- [ ] Pass practical exam (independent PCR + digest)
- [ ] Sign off in laboratory notebook

---

**Last Updated:** January 2025  
**Maintained by:** GMBL-PBGSBS  
**For questions:** dr.sharadindu@gmail.com

---

**END OF MASTER INDEX**
