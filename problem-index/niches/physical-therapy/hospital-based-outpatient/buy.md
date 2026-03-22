# PT-Specific Documentation Quality Layer for Epic/Cerner

**Niche:** [[niches/physical-therapy/hospital-based-outpatient/profile|Hospital-Based Outpatient PT]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hospital-based PTs get dedicated therapy documentation quality — outcome tracking, functional reporting, and treatment plan templates — that matches WebPT capability but lives inside their mandated Epic or Cerner platform.
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #compliance #workflow-orchestration

## The Problem
Hospital-based PTs are forced onto Epic Rehab or Cerner Rehab modules that were designed as generic rehabilitation documentation tools, not purpose-built PT platforms. The result: clunky treatment plan templates that don't match PT clinical workflows, no integrated outcome measure tracking (Oswestry, DASH, LEFS must be manually scored and entered), no automated functional limitation reporting for Medicare compliance, and no clinical decision support for treatment progression. Private practice PTs using WebPT or Prompt have significantly better documentation workflows than hospital-based PTs on Epic — an irony given that hospital systems spend orders of magnitude more on their EMR.

## What Already Exists
WebPT, Clinicient/Prompt, and Net Health are excellent PT-specific EMRs — but hospital systems won't adopt them because they require running a separate system outside the mandated enterprise EMR. Epic App Orchard has some rehab-adjacent apps, but none provide the depth of PT-specific clinical documentation that dedicated EMRs offer. In-house Epic build teams can create custom templates, but they prioritize surgical, ED, and primary care workflows over rehab.

## The Customization Gap
The gap is a PT-specific documentation enhancement layer that operates within Epic or Cerner's extension framework. It needs to provide: (1) standardized outcome measure calculators (auto-score Oswestry, DASH, LEFS, NPRS from patient-entered data and populate the medical record), (2) treatment plan templates organized by diagnosis and surgical protocol (ACL reconstruction week 1-4, week 5-8, etc.), (3) automated functional limitation reporting that extracts data from daily notes and generates the G-code/functional limitation documentation Medicare requires, (4) clinical decision support that flags when a patient's progress deviates from expected recovery trajectories, and (5) discharge summary generation that compiles the treatment episode into a report sendable to the referring surgeon. All must live inside Epic/Cerner, not as a separate application.

## Target Customer
Rehab department directors and therapy informatics specialists at hospital systems running Epic or Cerner who want PT documentation quality comparable to dedicated PT EMRs without leaving their enterprise platform.

## Impact If Solved
Reduces therapist documentation time by 10-15 minutes per day by automating outcome scoring, functional reporting, and treatment plan updates. Improves Medicare compliance by ensuring functional limitation documentation is consistently captured. Provides rehab department directors with clinical quality metrics (outcome improvement rates, protocol adherence) that are currently invisible inside the enterprise EMR.
