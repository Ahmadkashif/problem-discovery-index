# Social Needs Screening Wired to the Referral That Follows

**Niche:** [[niches/healthcare-practice-software/fqhc-health-center-software/profile|FQHC & Community Health Center Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Validated social needs screening instruments and community resource directories are both mature purchasable products, and health centers screen thousands of patients into a data field that leads nowhere.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #descriptive-statistics #workflow-orchestration #compliance #worker-facing
**Contested on:** Every serious competitor selling to health centers is fighting to make the UDS report, the sliding-fee determination and the 340B claim all derive from the same encounter record without a parallel data collection exercise — and whoever removes that second exercise takes the account.

## The Problem
A patient screens positive for food insecurity and housing instability. The screening is recorded, counted, and reported. The patient is handed a printed list of community organisations. Whether any of them had capacity, whether the patient contacted them, and whether the need was met is unknown to everyone — the health center included. The screening was performed because it is required and because it is the right thing to do, and it has produced a number rather than an outcome. Staff know this, which is corrosive: asking a patient about hunger and then doing nothing visible teaches both parties that the question is bureaucratic.

## What Already Exists
The instruments are solved and free — PRAPARE, the Accountable Health Communities screening tool, and the AAFP's are all validated and widely implemented. Closed-loop referral platforms are a real product category with real deployments: Unite Us, findhelp and NowPow-descendant products maintain resource directories, accept referrals electronically and can return a status. Many health centers already have both a screening module and a directory subscription. The two are almost never connected, and where they are connected the connection is a link rather than a workflow.

## The Customization Gap
The adaptation is to make the referral a tracked obligation with the same seriousness as a lab order. It requires: (1) triggering a specific referral from a specific positive screen automatically, with the resource selected by live capacity and eligibility rather than by proximity on a list; (2) treating the referral as an open loop with a state and a clock, escalating when nothing comes back — the same state machine a specimen needs; (3) capturing outcome at the level that matters, which is whether the need was met rather than whether a referral was sent; (4) learning which resources actually close loops for which needs and populations from the health center's own referral history, and ranking accordingly, because a directory sorted by distance is a directory sorted by the wrong thing; and (5) reporting screening-to-resolution rate alongside screening rate, which is the number that makes the programme honest and which almost nobody publishes.

## Target Customer
FQHCs and health center networks already screening at scale under HRSA and value-based contract requirements, and the community resource platforms who would rather sell a closed loop than a directory.

## Impact If Solved
Screening-to-resolution rate is typically a fraction of screening rate, and simply measuring it reorders a health center's community partnerships within a quarter. Ranking resources by demonstrated closure rather than by proximity is achievable with data the center already generates, and it is the difference between a printed list and a referral that lands.
