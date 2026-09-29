# Scores Are Published Without Ever Being Validated

**Niche:** [[niches/charter-bus-operators/driver-risk-data-providers/profile|Commercial Driver Risk Data Providers]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Insurers price on the score and employers act on it, and the firm publishing it runs no standing validation — so a scoring model that has drifted out of calibration would look exactly the same as one that has not.
**Tags:** #evaluation-metrics #cross-validation #change-point-detection #confidence-intervals #hypothesis-testing #logistic-regression #gradient-boosting #compliance #data-integration #causal-inference

## The Problem
The score is used to set premiums, to decide whether a driver stays on a carrier's roster, and to determine whether a charter operator is acceptable to a school district. It is produced continuously and evaluated almost never. There is no standing measurement of whether a driver scored in a given band actually experiences crashes at the rate the band implies, no monitoring for drift as populations and enforcement practices change, and no subgroup analysis of whether calibration holds across regions, carrier types, and driver populations. When something goes wrong — enforcement practice shifts in a large state, a data feed degrades, a mapping breaks — the score changes and nobody can distinguish that from a real change in risk.

## Why It's Still Broken
Validation requires outcome data the firm has not systematically assembled, for the same reasons that block empirical weighting: crash records arrive from different sources with different identifiers and lags. The commercial structure also removes the pressure — clients buy the score as an input and rarely have the data or the appetite to validate it independently, so nobody is asking. And the incentive is uncomfortable in the familiar way: standing validation creates a record of periods when the score was miscalibrated, which is a documented liability in a product used for employment and pricing decisions. The result is that a consequential predictive product operates with less measurement discipline than an internal marketing model would.

## What a Fix Looks Like
A standing validation function, run as a permanent process rather than as a periodic project. Predicted risk is compared to realized outcomes continuously, at the band level, with calibration reported rather than only discrimination — because an insurer needs the stated probability to be the actual probability, not merely for the ordering to be right. Monitoring covers subgroups explicitly: geography, carrier type, driver tenure, and the demographic dimensions that fairness scrutiny concerns itself with, reported whether or not the results are comfortable. Drift detection distinguishes genuine population change from data pipeline failure, which is the practical failure mode and currently indistinguishable from signal. And validation results are versioned alongside the model, so a score challenged three years later can be explained in terms of what was known and measured at the time — which is the record the firm most needs and least has.

## Who Feels the Pain
Insurers pricing on an unvalidated input; carriers and drivers whose livelihoods turn on a score nobody checks; the compliance function facing employment-decision scrutiny with no calibration evidence; and the firm, whose entire product is a claim about prediction supported by no measurement.

## Impact If Fixed
Converts an assertion into evidence in a market that competes on trust between vendors selling similar raw data. It also front-runs the regulatory direction — scoring products used in employment and insurance decisions are moving toward validation and fairness reporting expectations everywhere, and the firm that has the record already is in a different position from the one assembling it under inquiry.
