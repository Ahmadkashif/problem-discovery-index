# Adjudication Quality Practice

**Niche:** [[niches/neobanks/the-risk-analyst/profile|The Risk Analyst]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fields that make consequential judgements at volume measure inter-rater agreement and calibrate their reviewers, and risk operations measures cases per hour.
**Tags:** #worker-facing #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #descriptive-statistics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to give the analyst the evidence and the time to decide correctly rather than a screenshot and a throughput target — and whoever does that changes who gets access to their own wages.

## The Problem
Wherever people make consequential judgements at volume, the mature practice measures the judgement rather than the throughput: inter-rater agreement is assessed, reviewers are calibrated against known cases, decisions are audited against outcomes, and disagreement is investigated as information. Clinical review, insurance claims adjudication, benefits assessment and content moderation have all developed some version of this. Risk operations at digital banks measures cases closed per hour and has no measure of whether the decisions were correct.

## What Already Exists
Inter-rater reliability measurement; calibration exercises against known cases; decision quality auditing against outcomes; disagreement investigation and escalation; and reviewer performance management on accuracy.

## The Customization Gap
The adaptation is to decisions whose correctness is revealed by the ledger. It requires: (1) ground truth available from the institution's own subsequent records — the frozen account that resumes normal behaviour, the reinstated one that commits fraud — which is a far better outcome signal than most adjudication fields have and is entirely unused here; (2) a strong asymmetry in the visible consequences, since fraud losses are counted and wrongly frozen customers are not, which biases any quality measure built naively on loss; (3) throughput pressure created by a queue that grows with the customer base, so accuracy measurement must coexist with a real capacity constraint; (4) regulatory obligations that constrain what a reviewer may do, unlike a clinical judgement; and (5) reviewers who are frequently outsourced or high-turnover, which makes calibration a continuous requirement rather than a periodic one.

## Target Customer
Risk operations leadership, business process outsourcing providers serving this function, and quality management vendors for whom financial risk review is an adjacent market.

## Impact If Solved
Every field making consequential judgements at volume measures the judgement, and this one measures the hour. The ledger supplies a better outcome signal than most adjudication fields have and it is entirely unused.
