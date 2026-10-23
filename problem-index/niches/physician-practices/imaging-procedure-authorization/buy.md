# Portal Automation Adapted to Each Benefit Manager's Question Tree

**Niche:** [[niches/physician-practices/imaging-procedure-authorization/profile|Imaging & Procedure Authorization]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic RPA can click through a portal; radiology benefit manager portals ask branching clinical questions whose answers must match the chart, or the request is pended.
**Tags:** #large-language-models #decision-trees #automation #workflow-orchestration #compliance
**Contested on:** Every serious competitor in this niche is fighting to get each ordered scan or procedure authorized before its scheduled date without a peer-to-peer, and whoever clears the most orders on first submission, or proves none was needed, takes the account.

## The Problem
EviCore and Carelon portals walk the submitter through clinical question trees. The answers determine approval or pend, so a wrong click becomes a clinical misstatement. Coordinators answer from memory of the chart, and approval rates vary by who submits.

## What Already Exists
RPA tools (UiPath, Automation Anywhere) and healthcare automation vendors that log into portals, plus clearinghouse authorization products for payers with electronic 278 transactions.

## The Customization Gap
The clinical layer needs:

- a map of each benefit manager's question trees by service, kept current as they change;
- each answer drawn from cited chart evidence, never inferred;
- a stop when the chart cannot support the answer, routing the order to the physician instead of submitting;
- capture of the decision and reference number back into the EHR.

## Target Customer
Authorization managers at groups that send most of their imaging and cardiology requests through radiology benefit managers.

## Impact If Solved
Consistent, evidence-backed answers could lift first-pass approval and cut portal time per request by ~50% (estimate).
