# After-Hours PCP Handoff and Follow-Up System

**Niche:** [[niches/urgent-care/after-hours-weekend/profile|After-Hours & Weekend-Only Urgent Care]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** After-hours UC providers close the care coordination gap by auto-sending structured visit summaries to the patient's PCP Monday morning — ensuring that the patient who came in Friday night with chest pain and was cleared does not fall through the cracks.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #workflow-orchestration #automation #compliance

## The Problem
A patient visits an after-hours UC on Saturday evening for worsening abdominal pain. The provider evaluates, performs basic labs, rules out surgical emergency, prescribes pain management and anti-nausea medication, and instructs the patient to follow up with their PCP Monday. The visit is documented in the UC's EHR. But the patient's PCP — Dr. Williams at the family practice across town — has no idea this visit happened. The patient may or may not call Monday to schedule. If the condition worsens Sunday, the patient returns to the after-hours UC or goes to the ER, and neither knows about the other's prior evaluation. The after-hours UC provider carries clinical concern about this patient all weekend with no mechanism to ensure follow-up occurs.

## Why Nobody Has Built This
The PCP handoff problem exists in all urgent care, but it is most acute in after-hours settings where the follow-up gap is measured in days (Friday night to Monday morning) rather than hours. Health Information Exchanges (HIEs) theoretically solve this — all providers in a network can see shared records — but HIE participation among independent UCs and small PCPs is low, data exchange is batch-processed (not real-time), and the information is "pull" (the PCP must actively search for the UC visit) rather than "push" (the PCP is notified). Direct Messaging (the healthcare email protocol) exists but few UC EHRs implement it and few PCPs monitor their Direct inbox reliably. Building a PCP handoff system requires solving: identifying the patient's PCP from registration data, generating a structured visit summary from the clinical note, and delivering it through a channel the PCP will actually see — which varies by PCP (some want faxes, some want EHR messages, some want Direct messages).

## What to Build
An automated PCP handoff platform that integrates with the after-hours UC's EHR and: captures the patient's PCP information at registration (auto-populated from insurance data or patient-provided); generates a structured visit summary from the clinical documentation (chief complaint, findings, tests performed, diagnosis, treatment, follow-up instructions) formatted for PCP consumption; delivers the summary to the PCP via their preferred channel (fax for older practices, Direct messaging, EHR-to-EHR integration where available, or a secure web link with notification); and confirms delivery with a read-receipt or follow-up ping. For high-concern cases, the system auto-generates a Monday morning follow-up task and texts the patient a reminder to call their PCP. The after-hours provider can mark a visit as "high-priority handoff" to escalate the notification.

## Target Customer
After-hours and weekend-only UC owners and clinical directors concerned about follow-up care gaps, malpractice exposure from dropped handoffs, and patient outcomes for conditions requiring 24-48 hour re-evaluation.

## Impact If Built
Ensures 90%+ of after-hours UC visits result in PCP notification within 24 hours of the PCP's next business day, compared to the current estimated rate of under 15%. Reduces malpractice exposure from failed follow-up — "patient was instructed to follow up but never did and condition worsened" is a leading liability scenario in after-hours UC. Improves patient outcomes by closing the weekend care coordination gap for conditions that need Monday reassessment.
