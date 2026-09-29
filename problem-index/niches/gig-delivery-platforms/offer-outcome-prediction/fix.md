# Fix: Nobody Measures How Wrong the Estimates Are

**Niche:** [[niches/gig-delivery-platforms/offer-outcome-prediction/profile|Offer Outcome Prediction]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every offer's estimate is checkable against what happened within the hour, and no platform reports how often its own estimates are materially wrong.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #change-point-detection #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will publish the accuracy of a number it asks people to make decisions on.

## The Problem

A courier accepts an offer on a stated time and amount. Within the hour the platform knows exactly what both turned out to be. That comparison — estimated versus realised, per offer — is the most direct quality measure available for the single most important number the platform produces, and it is computed by nobody.

Not internally in any systematic way, and certainly not externally. There is no published figure for what fraction of offers run over their estimate, by how much, in which markets, at which merchants. Independent estimates of courier net hourly earnings vary wildly between studies, which is itself the symptom: the only party who can compute it precisely is the one that does not.

## Why It's Still Broken

Because the number would be bad and there is no obligation to produce it. An estimate optimised for acceptance is an estimate biased short, and publishing the bias would document it. There is no regulator currently demanding it in most jurisdictions and no competitive pressure, since nobody publishes and so nobody can be compared.

Internally the measurement falls between teams. The estimate is produced by the pay model or ETA team, the outcome is recorded by the delivery tracking system, and the accuracy of courier-facing estimates is not in anyone's metric set — the ETA team is measured on customer-facing accuracy, which is a different interval.

And there is a quiet reason: measuring it well means measuring it by merchant, by market and by courier cohort, and those breakdowns raise questions about who bears the error. A finding that estimates are systematically worse in low-income delivery zones, or at certain merchant chains, creates an obligation to act.

## What a Fix Looks Like

Compute the calibration. It is a join between two tables the platform already writes.

Per offer: estimated time against realised engaged time, estimated pay against realised pay including any post-delivery tip change. Aggregate into a distribution rather than a mean — the share of offers running over by 25%, 50%, 100% is what matters, because the tail is where the harm concentrates. Break it down by market, merchant, hour, order type and courier tenure. This is descriptive statistics with no modelling at all and it is the entire first deliverable.

Monitor for drift. Estimate accuracy degrades when merchant behaviour changes, when a market's supply-demand balance shifts, or when a model ships. Change-point detection on calibration by market catches all three and is cheap.

Show the courier their own record. Per delivery, estimated versus realised, and weekly aggregate. A courier can then learn which offer types run long in their market, which is knowledge they currently acquire expensively and cannot transfer. It also converts a general grievance into a specific one, which is more useful to everyone.

Show merchants theirs. A merchant whose wait distribution runs fifteen minutes above the market's is imposing a cost on couriers and on the platform's delivery promise, and most do not know it. This is the mechanism by which merchant lateness actually improves, and it needs no courier-facing disclosure about the merchant at all.

Publish the market-level figure. A platform that reports estimate accuracy and realised net earnings per engaged hour by market, before a statute requires it, sets the terms of the comparison rather than receiving them. Several jurisdictions are already legislating exactly this, and the compliance systems built for them demonstrate the computation is entirely feasible.

## Who Feels the Pain

Couriers, who make thousands of decisions a year on a number whose accuracy nobody has established. Researchers and regulators, who cannot compute what gig couriers earn and produce widely varying figures that then get argued about instead of the underlying conditions. And the platform, which has no internal quality signal on its most consequential worker-facing output and therefore cannot tell whether it is getting better or worse.

## Impact If Fixed

The estimate acquires an accuracy figure, which is the precondition for improving it and currently does not exist. Systematic optimism becomes visible and therefore fixable. And the long-running public argument about what gig couriers actually earn becomes answerable with data from the only party who has it — on terms the platform sets rather than terms a statute imposes.
