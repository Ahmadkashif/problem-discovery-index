# Underwriting and Screening Practice

**Niche:** [[niches/recommerce-platforms/acceptance-economics/profile|Acceptance Economics]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lending and insurance built screening at the point of acceptance because the cost of a bad case is incurred after you accept it, which is exactly this decision.
**Tags:** #gradient-boosting #logistic-regression #confidence-intervals #revenue-impact #evaluation-metrics #hypothesis-testing #convex-optimization #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to decide which items are worth accepting before the processing cost is spent — and whoever does that fixes the unit economics, because the cost is incurred at intake and the revenue is not.

## The Problem
Deciding whether to take on a case whose cost you will bear and whose value is uncertain is the underwriting problem, and lending and insurance built the whole apparatus for it: scoring at the point of application, acceptance thresholds tuned to a target economic outcome, differential pricing rather than binary decline, portfolio monitoring, and learning from the cases you declined as well as the ones you took. Recommerce acceptance uses a category list.

## What Already Exists
Application scoring with acceptance thresholds; risk-based differential pricing as an alternative to decline; portfolio-level acceptance policy tuned to target economics; reject inference for learning from declined cases; and the operational practice of declining well without losing the customer.

## The Customization Gap
The adaptation is to a low-value decision made at high volume on a physical item. It requires: (1) a scoring input that is a photograph rather than an application form, which is what makes this newly feasible and is the technical substitution; (2) differential treatment rather than binary decline — a reduced-processing tier or an outright purchase offer instead of consignment — which is the direct analogue of risk-based pricing and turns most declines into a different deal; (3) a decision cost proportionate to an item worth twenty dollars, which rules out any human review in the normal path; (4) reject inference through occasional acceptance of items the model would decline, which is how the model learns about the region it never observes and is a small deliberate cost; and (5) the seller relationship treated as the portfolio, since a seller whose items are declined stops sending the good ones too, which is a dependency lending does not have and which should moderate the threshold.

## Target Customer
Platform operations and finance functions, resale-as-a-service vendors, and the credit risk profession for whom this is a familiar structure in an unfamiliar setting.

## Impact If Solved
This is an underwriting decision run on a category list. Differential treatment rather than binary decline is the direct analogue of risk-based pricing, and the seller relationship as the real portfolio is the dependency that should moderate the threshold.
