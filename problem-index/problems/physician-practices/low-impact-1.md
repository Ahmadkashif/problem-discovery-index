# Prior Authorization Packets Rebuilt for Every Payer

**Industry:** [[physician-practices|Physician Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every ordering practice assembles the same evidence packet (notes, imaging, failed therapies, scores) against each payer's written criteria by hand, while generic PA portals only move the form, not the argument.
**Tags:** #large-language-models #transformers #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #revenue-impact

## The Problem
A cardiologist orders a nuclear stress test, an orthopaedic surgeon an MRI of the knee, a rheumatologist an infusion of a biologic. Before any of these happens, a staff member checks whether the patient's plan requires authorization, finds the plan's medical policy, and reads its criteria: six weeks of conservative therapy documented, a specific symptom duration, an abnormal ECG, two failed conventional drugs. Then they search the chart for evidence of each criterion, copy it into a portal form or fax cover sheet, attach notes, and submit. The AMA's 2024 survey counted 39 authorizations per physician per week and about 13 hours of physician and staff time (AMA, 2024).

Most requests are approved in the end. Medicare Advantage plans denied 7.7% of 52.8M decisions in 2024, and 80.7% of appealed denials were overturned (KFF). The waste is in assembling a packet that would have passed if the evidence had been attached the first time, and in the peer-to-peer calls and appeals when it was not.

## What Already Exists
CoverMyMeds and Surescripts handle electronic PA for pharmacy-benefit drugs. Payer portals, Availity and radiology benefit managers (EviCore, Carelon) take medical requests. EHRs such as athenahealth and eClinicalWorks have authorization worklists, and automation vendors (Commure's Athelas, Cair Health, Infinitus, SuperDial) submit, call and track status. CMS-0057-F requires impacted payers to expose FHIR Prior Authorization APIs from 1 January 2027, under the HL7 Da Vinci guides.

## The Customisation Gap
The generic tools move a request. None of them builds the argument. The practice-specific layer is:

- reading each payer's current medical policy PDF and turning its criteria into a checklist for each CPT and diagnosis pair;
- finding the evidence for each criterion in this patient's chart, with page and date citations, including scanned outside records;
- knowing the specialty's patterns, such as step-therapy history for biologics, imaging prerequisites for MRI, or symptom-duration clocks for sleep studies;
- tracking which of the practice's clinicians hold gold-card exemptions under state law, since Texas now evaluates a year of requests at a 90% approval threshold;
- switching to the payer's API when it exists and to the portal or fax when it does not.

## Impact If Solved
A packet built right the first time could cut staff time per request from ~25 minutes to ~8 (estimate). For a practice handling 39 requests per physician per week, that frees ~10 staff hours per physician per week. Avoiding a share of the peer-to-peer calls and appeals that follow incomplete submissions gives physicians back another ~1 hour a week (estimate).
