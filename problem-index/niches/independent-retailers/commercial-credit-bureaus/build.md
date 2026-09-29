# Scores on Small Businesses Built From Data Small Businesses Do Not Generate

**Niche:** [[niches/independent-retailers/commercial-credit-bureaus/profile|Commercial Credit Bureaus]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The score that decides whether a 500,000-establishment industry gets terms is computed from trade lines most of those establishments never appear in.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #evaluation-metrics #causal-inference

## The Problem
A commercial credit score is built primarily from trade payment experience — suppliers reporting how their customers pay. That works well for businesses with many reporting suppliers. It works badly for the long tail, and independent retail is the long tail: a store buying from dozens of small wholesale reps, most of whom report nothing to anybody.

So the file is thin. Two or three trade lines, a filing record, a firmographic estimate of size that is often wrong by a factor. The score computed on it is applied with the same apparent confidence as one built on forty trade lines, and a supplier declining terms cannot tell the difference between a business with a bad record and a business with no record.

The consequence lands entirely on the small business. Thin-file firms get lower limits, worse terms, or a decline, which constrains the inventory they can buy — which Pass 1 identifies as the single largest cash-flow lever in independent retail.

## Why Nobody Has Built This
The economics point at the thick file. Revenue concentrates in customers underwriting mid-market and larger businesses, where the data is good and the scores work, and the product roadmap follows the revenue. The thin-file population is high volume and low value per query.

The score is also validated in aggregate. Overall discrimination looks strong because it is dominated by the well-covered population, and nobody publishes performance by file depth — which is where the failure is. A metric that is never segmented is a metric that hides its own worst region.

And the alternative data has never been assembled. What would inform a thin file — payment processing flows, marketplace and platform activity, verified operating signals — exists and sits with other companies, and acquiring it is a business development problem rather than a modelling one.

## What to Build
Segment the problem by file depth and model the thin file as its own regime.

**Report performance by data depth.** Publish, at least internally, how the score discriminates on files with two trade lines versus twenty. This is the measurement that does not exist and everything else follows from it.

**Separate "no evidence" from "bad evidence."** A thin file should produce a wide, honest interval, not a confident point that a downstream user reads as a judgment. Users making a credit decision can act on uncertainty if they are told about it; today they are given a number.

**Build thin-file models on different features.** Business age and continuity, filing and licence consistency, physical location stability, the firmographic neighbourhood, and any verified operating signals available. These are weak individually and the point is that they are what exists.

**Treat the decision loop as the experiment.** Scores drive credit decisions, and declined businesses have no observed outcome, so the training data is censored by the model's own past behaviour. That is a well-understood selection problem and it is not handled — which means the thin-file model has been learning from a population it selected.

**Value new data sources against the segment they fix.** The right question about a payments or platform data partnership is how much it improves thin-file discrimination specifically, and the current evaluation framework cannot answer it.

## Target Customer
Chief Data Officer or SVP of Analytics at a commercial credit bureau. The commercial case is defensive as much as offensive: fintech lenders underwriting small businesses on transaction data are demonstrating that the thin file is workable, and the bureau's franchise depends on not being the last to notice.

## Impact If Built
Access to trade credit is the difference between a small retailer stocking a season and not, and thin-file businesses are currently penalized for the absence of data rather than assessed on it. Better discrimination in that segment extends terms to businesses that deserve them and withholds them from ones that do not — and it defends the bureau's position against underwriters who have found another way to see the same customers.
