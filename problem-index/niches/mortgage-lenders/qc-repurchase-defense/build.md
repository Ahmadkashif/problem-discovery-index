# A Rebuttal Engine Built on Every Past Resolution

**Niche:** [[niches/mortgage-lenders/qc-repurchase-defense/profile|Quality Control & Repurchase Defence]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each agency defect notice is answered from scratch by a QC analyst, although the lender has argued the same defect types many times and the outcomes are on record.
**Tags:** #large-language-models #bert #gradient-boosting #evaluation-metrics #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find a file's material defects before the agency does and to resolve the ones the agency finds by cure or fee rather than buyback, and whoever lowers the lender's repurchase cost per loan sold takes the account.

## The Problem
An agency notice cites a defect: income miscalculated, an undisclosed debt, an appraisal concern, a missing verification. Within 30 days the lender must cure it with new documentation, argue that the defect is immaterial or wrong, or accept the outcome. The analyst re-reads the file, finds the evidence, writes the response, and moves on. Whether the argument worked is recorded, if at all, in a spreadsheet.

## Why Nobody Has Built This
Volumes per lender are small (repurchase rates of 0.24–0.49% of loans), each case looks different in prose, and the outcome history is scattered across portal messages and email. QC vendors sell reviews; none owns the resolution record.

## What to Build
A system that classifies every incoming notice by defect type and guide section, retrieves the relevant file evidence and the underwriter's recorded reasoning, recalls how similar notices were resolved and which arguments and documents succeeded, estimates the probability of each outcome (cure, rescission, fee, repurchase), and drafts the response for the analyst to finish inside the deadline.

## Target Customer
QC and repurchase managers at agency sellers delivering 10,000+ loans a year; QC outsourcers who could offer it across clients.

## Impact If Built
Turning even a few repurchases a year into cures or fees saves tens of thousands of dollars each, and the classified history shows the lender which origination practices generate the notices in the first place.
