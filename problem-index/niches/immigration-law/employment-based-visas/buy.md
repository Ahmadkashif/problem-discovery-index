# PERM Recruitment Documentation Assembly

**Niche:** [[niches/immigration-law/employment-based-visas/profile|Employment-Based Visas]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** INSZoom tracks PERM cases but doesn't automate the assembly of the 50-200 page recruitment documentation binder that must be compiled in exact chronological order with specific formatting when an audit hits — paralegals spend 8-20 hours per audit assembling this from scattered files.
**Tags:** #workflow-orchestration #data-integration #automation #compliance #quick-win

## The Problem
When a PERM application is audited, the attorney has 30 days to submit a complete recruitment documentation package. This package includes: the supervised recruitment report, copies of all job postings (with dates posted and removed), tear sheets from newspaper ads, screenshots of online postings, the SWA job order, all resumes received (redacted for PII in some cases), a log of each applicant with disposition notes, interview records, the prevailing wage determination, and the employer's signed recruitment report summarizing the campaign results. These documents accumulate over a 6-12 month recruitment period and are stored across multiple systems: job board screenshots in a shared drive, resumes in email, disposition notes in a spreadsheet, newspaper tear sheets in a physical file, and the SWA job order confirmation in the DOL system. When the audit letter arrives, a paralegal must locate, organize, paginate, and compile these documents into a single binder with a specific chronological structure — a process that takes 8-20 hours per case.

## What Already Exists
INSZoom and LawLogix provide PERM case management with task tracking for recruitment steps (post job on Monster, post on employer website, file SWA job order) and deadline management. Document management systems (NetDocuments, iManage) store files. But these systems don't enforce a structured document collection workflow during the recruitment period that would make audit response assembly automatic. The task says "post job on Monster" but doesn't require the paralegal to upload the screenshot with metadata (date posted, date removed, URL) into a structured recruitment binder template at the time of posting.

## The Customization Gap
The missing layer is a structured recruitment documentation workflow that runs during the recruitment period (not at audit time): (1) each recruitment step in INSZoom triggers a structured document upload requirement with required metadata fields (date, source, URL, screenshot), (2) applicant resumes are uploaded with a disposition form (qualified/unqualified, reason, interview date if applicable) at the time of receipt rather than retrospectively, (3) the system maintains a real-time recruitment binder that is continuously assembled as documents arrive, and (4) when an audit letter arrives, the binder is export-ready in DOL-compliant format with a cover letter, table of contents, and exhibit labels — requiring only attorney review, not assembly. This is a customization of existing PERM case management: the task structure exists, but the document collection enforcement and auto-assembly are missing.

## Target Customer
Business immigration firms filing 30+ PERMs/year with a 20-30% audit rate, where each audit documentation assembly consumes 8-20 paralegal hours and the 30-day response deadline creates panic-driven workflows.

## Impact If Solved
Reduces audit response preparation from 8-20 hours to 1-2 hours of attorney review (the binder is already assembled). Eliminates the risk of missing the 30-day audit response deadline. For a firm handling 15-20 audits per year, this saves 120-360 paralegal hours annually ($15K-45K in labor costs) and eliminates the most stressful workflow in the practice.
