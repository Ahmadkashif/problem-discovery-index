# Predicting Batch Failure Before the Sample Reaches the Lab

**Niche:** [[niches/greenhouse-horticulture/cannabis-compliance-testing-labs/profile|Cannabis Compliance Testing Laboratories]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The lab knows which growing operations produce failing batches and only ever says so one batch at a time, after the crop is already harvested.
**Tags:** #logistic-regression #gradient-boosting #binary-classification #anomaly-detection #evaluation-metrics #revenue-impact

## The Problem
A failed compliance panel destroys a harvest. Pesticide residue, aspergillus, or a heavy metal result above the action limit means the batch cannot be sold and in most jurisdictions must be remediated or destroyed — tens to hundreds of thousands of dollars, discovered weeks after the plants came down and months after the decision that caused it.

The laboratory has run panels for the same cultivators for years. It knows which operations fail and how often, which cultivars carry microbial load, which failures cluster in particular months, and which growers' results drift before they break. All of that sits in the LIMS as individual certificates. No one has ever asked the corpus a question.

The lab reports a result. It does not report a pattern, and it has never told a cultivator that the last four batches trended toward an action limit that the fifth will cross.

## Why Nobody Has Built This
The lab is paid per sample and regulated as an impartial testing body, so the culture is deliberately transactional: analyze, report, do not interpret. Interpretation looks like advising a client whose product you also certify, and in a sector where lab-shopping and result inflation are a live regulatory concern, labs are cautious about anything that resembles helping a customer pass.

That caution is misapplied to prediction. Telling a cultivator their microbial results have drifted for four consecutive batches is not helping them pass a test; it is telling them their facility has a problem, before the harvest that gets destroyed. The distinction is defensible and nobody has bothered to draw it.

The other reason is the software. Cannabis LIMS platforms are built for regulatory reporting — sample in, state system out — and offer essentially no analysis over the lab's own accumulated results.

## What to Build
A predictive layer over the lab's result history that scores an incoming batch's failure risk and flags drift in a cultivator's results before it crosses a limit.

Three pieces. **Drift detection** on each cultivator-analyte series: microbial and residue results move before they fail, and a run of rising values under the limit is the signal. **A failure risk model** using cultivator, cultivar, growing method, room, season, and the operation's own result history — trained on the outcome, which is unambiguous and already labelled in every record the lab holds. **Root-cause clustering** across the client base: when a pesticide appears in unrelated cultivators' samples in the same month, it came from a shared input, and only the lab can see that because only the lab tests all of them.

The clean part of this problem is the label. Pass or fail against a numeric action limit — no adjudication, no ambiguity, no waiting to find out. Every historical sample is a training row.

## Target Customer
Laboratory director or owner-operator at a multi-state or high-volume single-state licensed lab. The commercial pitch is retention: testing is priced near commodity and cultivators switch on price, and a lab that warns a client before a destroyed harvest is not competing on price.

## Impact If Built
For the cultivator, a harvest saved is the difference between a profitable quarter and a loss. For the lab, it converts a per-sample commodity into a subscription relationship, and does it using data the lab already owns and currently uses once each.

Sector-wide, the same analysis run across a lab's whole book is the only genuine contamination surveillance that exists in cannabis — better than any regulator has, because the regulator sees pass/fail flags and the lab sees the numbers.
