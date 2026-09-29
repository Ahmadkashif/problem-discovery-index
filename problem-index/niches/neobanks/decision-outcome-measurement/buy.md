# Model Monitoring Practice

**Niche:** [[niches/neobanks/decision-outcome-measurement/profile|Decision Outcome Measurement]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning operations solved logging predictions and joining them to outcomes years ago, and the institutions making the most consequential automated decisions do not do it.
**Tags:** #data-integration #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #change-point-detection #compliance #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to join several million decisions a year to the outcomes already sitting in the ledger — and whoever assembles that dataset has the only thing that makes every other decision in the institution improvable.

## The Problem
Logging every prediction with its features and joining it to the eventual outcome is a standard capability in any mature machine learning operation. Feature stores keep the inputs as they were at decision time, prediction logs record what was decided, outcome joins produce the training and evaluation set, and monitoring reports accuracy and drift continuously. The tooling is mature and widely deployed. Institutions making millions of consequential decisions about people's access to money largely do not have it, because the decisions are made inside vendor systems.

## What Already Exists
Prediction logging with point-in-time features; outcome joining pipelines; continuous performance and drift monitoring; feature stores preserving decision-time state; and automated retraining triggered by degradation.

## The Customization Gap
The adaptation is to decisions made by third parties with censored outcomes. It requires: (1) predictions made inside vendor systems the institution does not control, so logging must be contractually required and standardised across vendors — this procurement dimension is the substantive obstacle and is not a technical one; (2) outcomes that are censored by the decision itself, since a decline produces no evidence, which the standard pipeline assumes away and which requires deliberate exploration to resolve; (3) label definitions that are policy choices rather than facts, since what counts as a correct freeze is debatable and must be decided explicitly; (4) regulatory constraints on retention and use of the resulting dataset, which standard practice does not contend with; and (5) fairness monitoring as a required output, which most monitoring tooling treats as optional.

## Target Customer
Risk and data platform teams at digital banks, decisioning vendors who could offer this as a differentiator, and monitoring vendors for whom vendor-mediated decisions are an unserved case.

## Impact If Solved
The tooling is mature and the institutions making the most consequential automated decisions lack it because the decisions sit in vendor systems. Contractually requiring standardised prediction logging is a procurement obstacle rather than a technical one, and censored outcomes need deliberate exploration the standard pipeline assumes away.
