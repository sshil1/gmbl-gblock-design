### **Materials and Methods**

#### **1\. Reference Sequences and GenBank Accessions**

All reference sequences were obtained from NCBI GenBank and verified for Bos taurus or species-specific transcripts. The following accessions were used for gBlock design: Brachyspina (FANCI gene, NC\_037348.1), CVM (SLC35A3 mRNA, AY160683.1), HH1 (APAF1 mRNA, NM\_001192283.1), HH3 (SMC2 genomic, AC\_000165.1), and HH4 (GART mRNA, NM\_001081610.1). All sequences were downloaded using the Entrez utilities (NCBI, version 2024).

#### **2\. Primer Design and Validation**

Diagnostic PCR primers were obtained from published sources and validated using NCBI BLAST (v2.14.1). Primer sequences are presented in Supplementary Table 1\. All primer pairs demonstrated zero-mismatch or ≤3-mismatch alignment to their respective target sequences. Forward and reverse primer Tm values were calculated using nearest-neighbor thermodynamics. Optimal annealing temperatures for each disorder were determined empirically using gradient PCR (55–65°C range).

#### **3\. Mutation Site Identification and Genomic Coordinates**

Disease-specific mutations were identified in the reference sequences using sequence alignment and in silico analysis. Exact genomic coordinates were determined relative to the NCBI reference assembly for Bos taurus (ARS-UCD1.2 or UMD3.1, as applicable). For Brachyspina, the deletion spans genomic coordinates 20,773,882–20,777,227 on chromosome 18 (NC\_037348.1), encompassing exons 25–27 and totaling 3,345 bp. For CVM, the G→T substitution occurs at position 9,870 (0-based) in the SLC35A3 mRNA sequence, corresponding to codon 187\. For HH1, the C→T stop-gain mutation occurs in exon 14 of the APAF1 gene, resulting in a premature termination codon (p.Gln579X). For HH4, the A→C missense mutation affects codon 290 of the GART gene (p.Asn290Thr).

#### **4\. gBlock Design Pipeline**

gBlock sequences were designed using a custom BioPython (v1.87)-based pipeline written in Python 3.12.3. The pipeline performs the following sequential steps: (i) fetch complete reference sequence from NCBI Entrez utilities; (ii) locate PCR primer binding sites allowing up to 3 mismatches using bidirectional sequence alignment; (iii) define amplicon boundaries from primer positions plus primer lengths; (iv) extract the amplicon sequence plus 100–150 bp of flanking genomic sequence upstream and downstream for PCR stability; (v) introduce the disease-specific mutation (point mutation or deletion junction) into the extracted sequence; (vi) validate synthesis feasibility by checking GC content (25–75%), maximum homopolymer run length (\<10 bp), and total length (500–3000 bp).

#### **5\. Quality Control and In Silico Validation**

All gBlock sequences were assessed for synthesis feasibility using the IDT Design Tool quality parameters. GC content was calculated using the Bio.SeqUtils.gc\_fraction function. Homopolymer runs were identified using regular expression matching for stretches of ≥10 identical consecutive nucleotides. Restriction enzyme recognition sites were identified and mapped using the Bio.Restriction.Analysis module with a RestrictionBatch containing relevant enzymes (PstI for CVM, MseI for HH4). Expected restriction fragment sizes were computed in silico by identifying all enzyme cut positions within the PCR product and calculating resulting fragment sizes.

For CVM, the PCR-PIRA mechanism was validated by simulating the actual PCR product (concatenating forward primer sequence \+ template downstream sequence) rather than analyzing the raw genomic template. This revealed the presence of the PstI site (CTGCAG) in the WT PCR product and its absence (CTGCAT) in the CVM mutant PCR product, consistent with published digest patterns.

#### **6\. gBlock Synthesis and Ordering**

All gBlocks were designed to IDT specifications for synthetic gene fragments (gBlock®). Sequences were ordered as blunt-ended, double-stranded DNA at 2 nmol per gBlock. Standard purification (desalting) was selected. Sequences were resuspended in 1× TE buffer (pH 8.0) and stored at −20°C. Concentration was verified by spectrophotometry (OD260/OD280 ratio ≈ 1.8). All gBlocks met synthesis quality requirements before dispatch from IDT.

#### **7\. pJET1.2/Blunt Cloning Strategy**

Each gBlock was cloned into pJET1.2/blunt vector (Thermo Fisher, Cat\# K1423) using positive selection cloning. The vector contains an eco47IR lethal gene that is disrupted upon insert ligation, eliminating background colonies without requiring IPTG/X-Gal screening. Briefly, 1 µL gBlock (template) was mixed with 1 µL pJET1.2/blunt vector (25 ng/µL) and 1 µL T4 DNA ligase in 5 µL 2× rapid ligation buffer. Ligation was performed at 22°C for exactly 5 minutes. Ligation products (2 µL) were transformed into TOP10 competent cells (Invitrogen, Cat\# C404003) by calcium chloride heat shock (42°C for exactly 30 seconds). Transformed cells were recovered in SOC medium at 37°C for 60 minutes, then plated on ampicillin-containing agar (100 µg/mL). All colonies recovered on selection plates contained inserts, as verified by colony PCR using pJET1.2 sequencing primers (expected product \~630 bp \+ insert size).

#### **8\. PCR Validation and RFLP/PIRA Analysis**

PCR amplifications were performed in 25 µL reaction volumes containing 1× PCR buffer, 200 µM dNTPs, 400 nM each of forward and reverse primer, 0.2 U Taq polymerase, and 50–100 ng template DNA. Cycling conditions comprised initial denaturation (95°C × 2 minutes), 35 cycles of denaturation (95°C × 30 seconds), annealing (58–60°C × 30 seconds, disorder-dependent), and extension (72°C × 30 seconds), followed by final extension (72°C × 5 minutes). PCR products were resolved on 1.5–2.0% agarose gels and visualized by ethidium bromide staining.

For PCR-RFLP and PCR-PIRA assays, 10 µL PCR product was incubated with 1 µL restriction enzyme (10 U/µL) and 1 µL enzyme-specific buffer at 37°C for 60 minutes, then inactivated at 65°C for 20 minutes. Digest products were resolved on 2% agarose gels. For CVM, WT alleles were expected to yield 264 bp and 23 bp fragments (PstI digest), while CVM mutant alleles remained uncut at 287 bp. For HH4, MseI sensitivity (TTAA motif) was assessed for allele-specific digest patterns.

#### **9\. Bioinformatics Tools and Software**

All sequence analyses were performed using BioPython v1.87 (Cock et al., 2009\) under Python 3.12.3. NCBI sequence retrieval used the Entrez.efetch utility (NCBI, 2023). Primer specificity was verified using NCBI BLAST+ v2.14.1 against the Bos taurus genome (ARS-UCD1.2 reference). Sequence alignments and mutation context visualization were performed using standard BioPython Seq objects and custom Python scripts. Restriction enzyme recognition sites were identified using the Bio.Restriction module database. All custom Python scripts are provided in Supplementary Code.

#### **10\. Reagents and Consumables**

gBlock gene fragments were obtained from Integrated DNA Technologies (IDT, Coralville, Iowa, USA). Plasmid vectors and competent cells were purchased from Thermo Fisher Scientific (Waltham, Massachusetts, USA). Restriction enzymes (PstI, MseI) and buffers were obtained from New England Biolabs (NEB, Ipswich, Massachusetts, USA). PCR reagents (Taq polymerase, dNTPs, buffers) were obtained from GeNei (Bangalore, India). Agarose, ethidium bromide, and molecular biology reagents were standard laboratory grade (≥99% purity).

#### **11\. Data Availability**

All gBlock sequences are provided in FASTA format in Supplementary Files. GenBank accession numbers for reference sequences are listed in Supplementary Table 1\. Complete Python scripts for gBlock design, sequence analysis, and restriction enzyme mapping are provided in Supplementary Code. Validation PCR gel images and restriction digest patterns are documented in Supplementary Figures. All raw data and scripts are archived and available upon request from the corresponding author.

