# Resume Parsing and Skill Normalization Layer

**Niche:** [[niches/staffing-agencies/candidate-matching-ranking/profile|Candidate-to-Requisition Matching & Ranking]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Resume parsers exist but extract unstructured text blobs rather than normalized, taxonomy-mapped skills that enable structured matching across a staffing agency's multi-industry candidate pool.
**Tags:** #bert #named-entity-recognition #nlp #data-integration #automation

## The Problem
A staffing agency's candidate database contains resumes in dozens of formats: Word documents, PDFs, LinkedIn exports, hand-typed application forms, and plain text email submissions. Existing ATS resume parsers (Sovren, DaXtra, Textkernel) extract contact information and employment history into structured fields, but skills are dumped into a free-text field with no normalization. "Microsoft Excel," "MS Excel," "Excel (Advanced)," and "Spreadsheet Software" all refer to the same skill but appear as different text strings. Across a 100K-candidate database, this fragmentation makes skill-based search unreliable and prevents structured matching.

## What Already Exists
Sovren (now Textkernel), DaXtra, and HireAbility provide resume parsing APIs that extract structured data from resumes. These tools achieve 85-95% accuracy on contact information and employment history extraction. Lightcast (formerly EMSI/Burning Glass) maintains a skills taxonomy with 30,000+ normalized skill concepts.

## The Customization Gap
The gap is between parsing (extracting text) and normalization (mapping extracted text to a canonical skill taxonomy). The staffing industry needs a parser that maps free-text skill mentions to a standardized taxonomy (preferably O*NET or Lightcast-based), understands synonyms and abbreviations specific to each industry vertical (in light industrial, "reach truck" = "Raymond reach" = "stand-up forklift"), infers skills from job titles and experience descriptions (a "Charge Nurse" implies supervision, triage, and specific clinical competencies even if not listed as skills), and outputs structured skill profiles that can be directly compared against job order requirements.

## Target Customer
Operations or technology leaders at staffing firms with 10K+ candidate records who need better skill data to support matching and reporting.

## Impact If Solved
Transforms unstructured resume data into a searchable, matchable skill database, improving candidate discoverability by 30-50% and enabling structured skill-gap reporting for candidates and clients.
