# Evidence Staleness and Gap Detection

**Niche:** [[niches/cybersecurity-mssp/compliance-evidence-collection/profile|Compliance Evidence Collection]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Fix (Pain Point)
**One-liner:** MSSP compliance teams discover evidence gaps weeks before the audit — a vulnerability scan was not run in Q3, an access review was skipped in August, incident response testing was never documented — because no system tracks evidence collection completeness in real time.
**Tags:** #workflow-orchestration #compliance #automation #quick-win

## The Problem
A SOC 2 Type II audit requires evidence of controls operating continuously during the audit period. If the MSSP failed to run a quarterly vulnerability scan in Q3, that gap is discoverable by the auditor and results in a qualified opinion (audit exception). But the MSSP's compliance team does not discover the gap until they begin assembling the evidence binder 4-6 weeks before the audit. By then, it is too late to retroactively run the Q3 scan. The gap exists because no system tracks which evidence collection activities should have occurred and whether they actually did. Evidence is collected at audit time (retroactively assembling what should have been captured continuously), not generated continuously throughout the audit period.

## Why It's Still Broken
Compliance evidence collection is calendar-driven but not calendar-automated. The compliance team knows that vulnerability scans should be quarterly, access reviews should be semi-annual, and incident response tests should be annual — but these schedules are maintained in human memory or a SharePoint calendar, not enforced by any system. When a scan is delayed by a SOC workload spike, nobody flags the evidence gap until audit prep. The monitoring platforms (SIEM, vulnerability scanners) run on their own schedules disconnected from compliance calendar requirements.

## What a Fix Looks Like
A compliance evidence completeness dashboard that: (1) defines the evidence collection schedule for each client's compliance framework (quarterly scans, monthly access reviews, annual IR tests, continuous monitoring logs), (2) monitors whether each scheduled activity was completed (scan ran, review documented, test performed), (3) flags overdue activities in real time ("Client X's Q3 vulnerability scan is 2 weeks overdue"), (4) alerts the compliance team and SOC manager when a gap is forming (not after it has formed), and (5) generates a completeness report showing evidence coverage percentage across all controls for each client. Integrates with the MSSP's monitoring platforms to automatically detect when scheduled activities complete.

## Who Feels the Pain
MSSP compliance managers who discover evidence gaps during audit prep and must explain them to auditors, SOC managers whose teams are responsible for activities that generate compliance evidence, and MSSP executives whose service reputation depends on clean client audits.

## Impact If Fixed
Eliminates 90% of evidence gaps by catching them within days rather than months. Reduces audit exceptions (qualified opinions) by 70-80%, preserving client trust and MSSP reputation. Converts compliance evidence collection from a reactive audit-prep exercise to a continuous quality assurance process.
