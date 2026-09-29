# Credit Risk Practice

**Niche:** [[niches/neobanks/risk-decisioning/profile|Risk Decisioning]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit risk management has decades of model governance, validation and monitoring required by regulation, and fraud decisioning at neobanks runs on tuned thresholds.
**Tags:** #compliance #evaluation-metrics #logistic-regression #confidence-intervals #hypothesis-testing #gradient-boosting #descriptive-statistics #causal-inference
**Contested on:** This niche is not terminal — judging a stranger at the door and judging an existing customer from their own ledger are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Credit risk modelling in banking is governed rigorously because regulators require it. Models are documented, independently validated before deployment, monitored for performance and drift, back-tested against realised outcomes, and reviewed periodically with findings tracked to closure. Fair lending analysis is standard. The practice exists because consequential automated decisions about consumers were recognised long ago as needing oversight. Fraud and account-risk decisioning at neobanks makes comparably consequential decisions with a fraction of that governance.

## What Already Exists
Model risk management frameworks with independent validation; back-testing against realised outcomes; performance and drift monitoring; fair lending and disparate impact analysis; and documented model inventories with review cycles.

## The Customization Gap
The adaptation is from a credit decision with a long outcome horizon to a fraud decision with an adversary. It requires: (1) an adversary who adapts, so a model validated once degrades by design rather than by drift — the monitoring must detect adaptation rather than distribution shift, which is the central difference from credit practice; (2) outcomes observable in days rather than months, which makes continuous validation feasible in a way credit back-testing never was and is an advantage the practice does not exploit; (3) decisions largely made by purchased components, so validation must cover vendor models the institution cannot inspect; (4) the error that is invisible — a wrongly declined or frozen customer — being the one with no natural feedback, unlike a credit default which announces itself; and (5) fairness analysis on fraud decisions, which is less established than in lending and increasingly expected.

## Target Customer
Risk and compliance leadership at digital banks, sponsor banks overseeing programmes, and model risk vendors for whom fraud decisioning is an adjacent market.

## Impact If Solved
Credit risk is governed because consequential automated consumer decisions were long ago recognised as needing oversight, and fraud decisioning makes comparable decisions with a fraction of it. Outcomes observable in days make continuous validation feasible where credit back-testing never was.
