# Automated Record Deduplication

**Niche:** [[niches/personal-injury-law/medical-records-review/profile|Medical Records Review]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Paralegals stop reviewing the same hospital visit three times — automated deduplication identifies when the ER record, the admitting physician's note, and the specialist's consultation all describe the same encounter, merging them into a single timeline entry.
**Tags:** #bert #transformers #feature-engineering #evaluation-metrics #automation #quick-win

## The Problem
A client visits a hospital ER after a car accident. The ER physician writes an assessment note. The radiology department generates an imaging report. The orthopedic resident writes a consultation note. The discharge nurse writes a discharge summary. The hospital's medical records department generates a combined visit report. When the PI firm requests records from the hospital, they may receive all five documents — each describing the same visit from a different provider's perspective, with overlapping but not identical information. Multiply this by 5-10 provider sources across a case, and the paralegal spends hours sorting through records that describe the same encounters multiple times. The problem is worse when records arrive in batches over weeks — the paralegal may review and summarize an ER visit from Provider A's records, then three weeks later receive the same visit documented in Provider B's records and not realize it's a duplicate until they've spent another 30 minutes reading it.

## What Already Exists
Document deduplication tools exist in e-discovery (Relativity's near-duplicate detection, Brainspace) but are designed for email and document review in corporate litigation — they compare text similarity, not medical encounter identity. OCR tools (ABBYY, Kofax) handle document digitization but not semantic deduplication. No existing tool understands that "Dr. Smith, ER attending, 3/15/2024, Dx: cervical strain" and "Orthopedic consult, 3/15/2024, impression: acute cervical sprain" describe the same encounter and should be linked.

## The Customization Gap
The missing layer is medical-encounter-aware deduplication. The tool must understand that deduplication in medical records is not text-similarity matching — it's encounter identity matching. Two records are "duplicates" (or more precisely, linked records of the same encounter) when they share the same date, facility, and patient but are written by different providers. The deduplication engine should: identify encounter-level groupings (date + facility + patient), link all documents from the same encounter, merge extracted data from each document into a single encounter summary (the ER note has the chief complaint, the radiology report has imaging findings, the discharge summary has the plan), and present the consolidated encounter to the paralegal instead of 3-5 separate documents. This requires entity extraction before deduplication — you have to understand what each document is about before you can determine which ones describe the same event.

## Target Customer
Medical records paralegals at PI firms who process high-volume record sets (500+ pages per case) and currently spend 20-30% of their review time re-reading documents that describe encounters they've already reviewed from a different provider's records.

## Impact If Solved
Reduces medical record review time by 20-30% on high-volume cases by eliminating duplicate encounter review. On a 2,000-page record set, deduplication may reduce the effective review volume to 1,200-1,400 unique pages. For a firm processing 50 record sets per month, that saves 40-80 paralegal hours monthly. Prevents the more subtle problem of inconsistent summaries — when the paralegal summarizes the same encounter differently from two different source documents, the case narrative contains contradictions.
