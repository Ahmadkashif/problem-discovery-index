# Ordering-Side Decision Support Turned Into Reading-Side Protocolling

**Niche:** [[niches/diagnostic-imaging-centers/exam-protocolling/profile|Exam Protocolling]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Imaging decision-support products already score orders against the ACR criteria inside health-system EHRs; the same content and logic, moved to the centre's side, can propose protocols and flag the wrong exam.
**Tags:** #large-language-models #bert #evaluation-metrics #workflow-orchestration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to attach the right protocol to every order before the patient arrives, and whoever cuts radiologist protocolling minutes per order most, with no rise in protocol-attributable repeats or recalls, takes the account.

## The Problem
Freestanding centres receive orders from physicians outside any health-system EHR, so ordering-side decision support never touched them. Since AUC was rescinded, nothing on the ordering side is obliged to.

## What Already Exists
CareSelect Imaging (Optum) and similar decision-support products, built for the AUC programme, map indications to the ACR Appropriateness Criteria (279 topics, 1,350+ variants) and score orders at entry in health-system EHRs.

## The Customization Gap
The adaptation has to run on the receiving side, on faxed and free-text orders rather than structured EHR order entry. It must map indications to the centre's protocol library, not just to an appropriateness score. It must check against the patient's benefit-manager guideline as well as the ACR's, with a licence or permission for each because both are copyrighted. It should also check against the documentation requirements payers expose through their CMS-0057-F Prior Authorization APIs from 2027. Output goes to a protocolling worklist, not a pop-up for the ordering physician.

## Target Customer
Operators and groups that want appropriateness and protocolling in one pass, through their RIS or reading-platform vendor.

## Impact If Solved
Reusing licensed criteria content and mappings cuts years of clinical content work from a protocol tool. It catches wrong-exam orders before authorization, which saves an amendment or a denial each time (estimate).
