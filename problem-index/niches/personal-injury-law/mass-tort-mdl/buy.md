# Census Sheet Auto-Completion

**Niche:** [[niches/personal-injury-law/mass-tort-mdl/profile|Mass Tort / MDL]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mass tort paralegals stop manually transcribing medical records into MDL census sheets — NLP extraction fills 70-80% of census fields automatically from collected records, turning weeks of data entry into hours of review.
**Tags:** #bert #transformers #large-language-models #transfer-learning #automation #quick-win

## The Problem
Every MDL requires plaintiff fact sheets (census sheets) — standardized court-mandated forms with 50-150 data fields per plaintiff covering demographics, exposure history, medical history, treating physicians, diagnosis dates, and treatment details. A firm with 3,000 qualified plaintiffs must complete 3,000 of these forms. Each form takes a paralegal 2-4 hours to complete because the data must be extracted from medical records, pharmacy records, employment records, and military service records (for military-related torts). At 3,000 plaintiffs and 3 hours each, that is 9,000 paralegal hours — approximately 4.5 full-time employees working for an entire year on nothing but data entry.

## What Already Exists
Document extraction tools like Rossum, ABBYY, and Amazon Textract handle structured document extraction. LLM-based tools (GPT-4, Claude) can extract information from unstructured medical records. Filevine's mass tort module has census templates but no auto-population from source documents. E-discovery platforms (Relativity) handle large document sets but are designed for document review, not data extraction into structured forms.

## The Customization Gap
The missing layer is a mass-tort-specific extraction pipeline that maps medical record content to census sheet fields. It must understand that "Patient presented on 3/15/2019 with bilateral tinnitus, audiogram showing 40dB hearing loss at 4kHz" maps to Census Field 42 (diagnosis date), Field 43 (diagnosis), Field 44 (diagnostic test), and Field 45 (test result). The mapping changes per MDL — Camp Lejeune census sheets have different fields than 3M earplug census sheets. The tool needs to be configurable per litigation: define the census schema, map source document types to census fields, run extraction, and present results for paralegal review and correction. Confidence scores per field tell the paralegal which extractions to trust and which to verify manually.

## Target Customer
Mass tort paralegals and census completion teams at firms with 500+ plaintiff portfolios who are currently spending thousands of hours on manual data transcription from medical records to census forms.

## Impact If Solved
Reduces census completion labor by 60-75% — from 3 hours per plaintiff to 45-60 minutes of review and correction. For a 3,000-plaintiff portfolio, that saves 6,000-7,000 paralegal hours ($180K-$350K in labor costs at $30-50/hour paralegal rates). Accelerates census submission timelines, which directly impacts the firm's ability to meet MDL court deadlines and participate in settlement negotiations.
