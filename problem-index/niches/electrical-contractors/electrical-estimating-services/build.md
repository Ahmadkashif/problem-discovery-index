# Bid Outcomes Recovered as a Calibration Signal

**Niche:** [[niches/electrical-contractors/electrical-estimating-services/profile|Electrical Estimating Service Bureaus]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm produces thousands of estimates a year against real bids that are won or lost at known prices, and it almost never finds out which.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #feature-engineering #descriptive-statistics #data-integration #revenue-impact

## The Problem
An estimate is a prediction of what work will cost, delivered into a competitive bid where the market immediately renders a verdict — the contractor wins or loses, and the spread against the winning number is knowable. The bureau delivers, invoices, and moves on. It does not systematically learn whether its estimates were high, low, or well-placed, in aggregate or by project type, region, or estimator. So the firm's core competence is unmeasured, its estimators receive no feedback on the only thing that matters, and it cannot tell a prospective client anything about its accuracy beyond references.

## Why Nobody Has Built This
Bid results belong to the contractor and are commercially sensitive, and nothing in a takeoff engagement asks for them. Losing bidders often do not learn the winning number at all on private work, though public bid tabulations are published and cover a substantial share of the market. And the bureau's economics are per-estimate, which focuses everything on throughput and leaves no one accountable for the accuracy record.

## What to Build
An outcome capture layer combining two sources. Public bid tabulations are collected systematically — for public work they publish every bidder and price, which is a free, complete calibration set the bureau currently ignores entirely. For private work, clients contribute outcomes in exchange for something they want: their own bid positioning benchmarked against the anonymized population, which tells a contractor whether they are consistently leaving money on the table or consistently uncompetitive, and which no contractor can determine alone. The accumulated record supports accuracy and bias measurement by project type, region, scope, and estimator; identification of the scope categories where the firm systematically misprices, which is where training and review should concentrate; and calibrated ranges delivered with estimates rather than point numbers, which is materially more useful to a contractor setting a bid strategy. It also produces the only credible sales claim available in this segment.

## Target Customer
Managing directors and chief estimators at estimating bureaus, and the contractor principals who buy estimates and currently judge them by whether the job made money afterward.

## Impact If Built
Turns an unmeasured craft service into an evidenced one. Public bid tabulations alone make this cheap to start, and the bid positioning benchmark is a genuinely new product for contractors — who have no other way to learn where their pricing sits against a market that never tells them.
