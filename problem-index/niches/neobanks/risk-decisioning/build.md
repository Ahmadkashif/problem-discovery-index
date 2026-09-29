# Vendor Scores and Tuned Thresholds

**Niche:** [[niches/neobanks/risk-decisioning/profile|Risk Decisioning]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decisions that determine who gets a bank account and whose wages are frozen are made by vendor scores, purchased rules and thresholds somebody tuned, almost none of which is evaluated against what actually happened.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #compliance #hypothesis-testing #causal-inference #revenue-impact
**Contested on:** This niche is not terminal — judging a stranger at the door and judging an existing customer from their own ledger are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
An applicant is declined because a vendor's score crossed a threshold. A member's account is frozen because a rule fired. A deposit is held because a model flagged it. Each of these is a prediction with a consequence, and the institution has almost no evidence about whether the prediction was correct. The vendor reports a score's general performance, not its performance on this population. The rules were written after incidents and are never retired. The thresholds were set during implementation. The whole apparatus is consequential, expensive and operating on faith.

## Why Nobody Has Built This
Risk decisioning is assembled from vendor components and the vendor owns the evaluation, which means the institution never developed the habit of evaluating its own decisions — buying the capability meant buying the measurement, and the measurement is generic. Outcomes live in operations while decisions live in risk, and no team owns the join, which is the corpus niche's subject. Every rule has an incident behind it, which makes removal feel dangerous. And a wrong decline produces no complaint the institution ever hears.

## What to Build
Make the decisions evaluable. Assemble the outcome record so every decision has a label, which is the prerequisite and is the corpus niche's build — nothing here is possible without it. Evaluate each vendor score on the institution's own population and outcomes, which frequently shows a score that performs well in general performing poorly here and is the fastest available improvement. Separate the two decision types, since onboarding and ongoing risk use different evidence and different adversaries and a single stack serves neither well — this separation is what the sub-niches develop. Report both error directions, because a declined good customer and an approved fraudster are both errors and only one of them is currently counted. Price the errors properly in the objective, since the cost of freezing a customer's wages includes the churn, the complaint, the regulatory exposure and the reputational damage, and is routinely set to the fraud loss alone. Retire rules on evidence rather than accumulating them, which is the fix note's subject. Handle the fairness dimension explicitly, since these decisions affect access to banking and disparate impact is both a regulatory and a moral exposure. Make decisions explainable to the front line, connecting to the support agent niche, because an unexplainable decision is an unmanageable one. Calibrate thresholds to a stated error trade-off rather than to a historical setting. And report decision quality to the board, since a firm whose central activity is decisioning should know how well it decides.

## Target Customer
Risk and product leadership at digital banks, the fraud and identity vendors whose scores are unevaluated in situ, and the sponsor banks accountable for the programme.

## Impact If Built
Buying the capability meant buying the measurement, and the measurement is generic rather than about this population. Evaluating vendor scores on the institution's own outcomes is the fastest available improvement, and pricing both error directions properly changes where the thresholds should sit.
