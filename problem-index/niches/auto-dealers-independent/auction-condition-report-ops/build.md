# Arbitration Says Whether the Report Was True and Nobody Adds It Up

**Niche:** [[niches/auto-dealers-independent/auction-condition-report-ops/profile|Wholesale Auction Condition Report Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thousands of inspectors describe millions of vehicles, buyers who disagree file arbitration, and the resulting verdict is the cleanest accuracy label in the used car industry.
**Tags:** #gradient-boosting #evaluation-metrics #causal-inference #confidence-intervals #logistic-regression

## The Problem
Wholesale vehicles sell on a condition report. An inspector walks the car, records panel damage, mechanical findings, tyre and glass condition and announcements, and assigns a composite grade. Independent dealers buy sight-unseen on that report — Pass 1 describes exactly this dependency — and when the vehicle arrives and does not match, the buyer files arbitration.

Arbitration is the label. It states, per vehicle, that the report was materially wrong, in what respect, and at what cost. The auction holds it joined to the report, to the inspector, to the seller, and to the realised price.

That is the only dataset in the used vehicle industry recording both what a vehicle's condition was said to be and whether that turned out to be true. Nothing in valuation, nothing in vehicle history, nothing at the manufacturers has an equivalent ground truth about condition assessment.

What is built on it is arbitration processing — resolving each case, charging it back, and tracking the rate as an operating metric.

What is not built is the obvious. Inspector accuracy is directly measurable and is not measured beyond crude rates. Arbitration risk is predictable before the vehicle runs — from the inspector, the seller, the vehicle's history, the damage type and the announcement pattern — which would let the auction re-inspect the risky ones instead of sampling. And the effect of the grade itself on realised price is estimable at the grade boundaries, which would tell the auction what a grading decision is actually worth to a seller.

Sellers, meanwhile, are graded by arbitration rate in aggregate, when the informative version is by damage type: which sellers systematically under-disclose which categories.

## Why Nobody Has Built This
Arbitration is a cost centre and is managed as one. The metric that gets attention is the rate, and the goal is to reduce it operationally — better training, more announcements, clearer policy — rather than to model it.

Measuring inspector accuracy is also industrially awkward. Inspection is high-turnover, often contracted, and a public accuracy ranking would be a labour relations problem before it was an analytical asset.

And the auction sits between two customers. Tightening grading protects buyers and costs sellers, who are the ones consigning volume. Nobody wants to build the analysis that makes that trade explicit.

## What to Build
The arbitration join as the accuracy system it already is.

**Score inspectors against arbitration.** Rate, severity and category of miss, adjusted for the vehicles they were assigned — because inspectors do not draw random vehicles and an unadjusted ranking is unfair and will be rejected.

**Predict arbitration risk pre-sale.** A pre-run risk score directs re-inspection where it pays, and turns a random sampling regime into a targeted one.

**Estimate the grade effect at the boundaries.** Vehicles just either side of a grade threshold are near-identical and priced differently. That discontinuity gives the auction a defensible number for what a grade is worth.

**Model seller disclosure by category.** Which consignors under-report frame damage, which under-report mechanical, which announce reliably. This is directly actionable in consignment terms.

**Feed risk back into the buyer's view.** A confidence attached to a grade — this vehicle's report is unusually likely to be contested — is worth real money to a sight-unseen buyer and is a genuine differentiator between platforms.

## Target Customer
VP of Inspection Services or Chief Operating Officer at a wholesale auction group. The commercial argument is that digital wholesale has made the condition report the entire product — buyers who never see the car are buying the report — and report trustworthiness is now the platform's competitive position.

## Impact If Built
Millions of vehicles a year change hands on a description written by an inspector whose accuracy has never been measured, in a market that has moved decisively to sight-unseen buying. The arbitration record makes accuracy measurable, risk predictable, and grading defensible — and it is already being collected as a complaint queue.
