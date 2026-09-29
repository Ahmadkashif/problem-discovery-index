# Delivered With No Confidence Attached

**Niche:** [[niches/web-data-extraction-firms/extraction-correctness/profile|Extraction Correctness]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every extracted record arrives looking equally trustworthy, whether it came from a stable page with a clean parse or a restructured one where the extractor guessed.
**Tags:** #confidence-intervals #evaluation-metrics #descriptive-statistics #hypothesis-testing #probability-distributions #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to detect when an extraction is returning plausible wrong values rather than no values — and whoever does that takes the account, because silent corruption is the failure customers cannot defend against.

## The Problem
A delivery contains two million records. Some came from pages the extractor has parsed identically for two years. Some came from pages that changed last week, where a model-based extractor made a judgement call between two candidate elements. Some came from pages that partially failed to render. The customer receives one file in which every record looks the same. They cannot filter to the reliable subset, cannot weight by confidence, and cannot exclude the questionable records from a training corpus or a pricing decision. The information distinguishing them existed at extraction time and was discarded on the way out.

## Why It's Still Broken
Confidence is not part of the delivery format, and adding a column is a schema change across every customer integration. Publishing per-record confidence advertises that some records are unreliable, which reads as a weakness rather than as the honesty it is. Model-based extractors produce a usable signal and it is thrown away because the interface was designed for selector-based extraction that either worked or did not. And customers do not ask for what they have never been offered.

## What a Fix Looks Like
Carry the confidence through to delivery. Emit a per-record and per-field confidence derived from what the extractor already knows — whether the selector matched exactly, whether the model had competing candidates, whether the page structure matched the expected template, whether validation checks passed — which is assembled from existing signals and is the whole fix. Let customers filter and weight by it, since a training corpus and a pricing feed want different thresholds and one delivery can serve both. Flag records extracted after a detected page change until they are verified, which is where the risk concentrates. Report the extraction method per record, so a customer knows whether a value came from a stable selector or a model's judgement. Calibrate the confidence against verified samples, because an uncalibrated score is worse than none and calibration is straightforward once sampling verification exists. Report field-level rather than only record-level confidence, since one field is usually the broken one and discarding the whole record loses good data. Deliver a per-batch quality summary with the batch, which is a small artefact that changes how a customer treats the data. And make it opt-in on the existing schema so no integration breaks.

## Who Feels the Pain
Customers unable to distinguish reliable records from guesses; teams whose models trained on a corpus containing a fraction of silently wrong values; and the firms whose careful extraction is indistinguishable from careless extraction at delivery.

## Impact If Fixed
The signal distinguishing a clean parse from a guess exists at extraction time and is discarded at delivery. Per-field confidence, calibrated against verified samples, lets one delivery serve a training corpus and a pricing feed at different thresholds.
