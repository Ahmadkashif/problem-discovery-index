# Which Forty Seconds

**Niche:** [[niches/ugc-video-platforms/decision-explanation/profile|Decision Explanation]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model knows exactly where in the video it found the problem and the notification does not contain it.
**Tags:** #large-language-models #cnns #transformers #evaluation-metrics #confidence-intervals #semantic-segmentation #compliance #object-detection
**Contested on:** Every serious competitor in this niche is fighting to make a classifier state which passage of a video triggered its decision and how confident it was — and whoever does it turns an unaccountable determination into one a person can act on.

## The Problem
Enforcement classifiers operate over segments, frames, transcripts and audio. Internally they produce localised signals — this segment, this phrase, this image, with this score. The decision is aggregated into a binary action and a policy label, and everything that would let a person understand or contest it is discarded at the point of notification. The capability gap between what the system computes and what it communicates is entirely on the communication side.

## Why Nobody Has Built This
Explanation was never a requirement of the classifier's design, so its outputs are built for a decision rather than for a rationale — a model optimised to produce an action has no obligation to carry the reasons forward. Surfacing detail raises adversarial and legal concerns that have gone unchallenged. Engineering effort follows enforcement accuracy rather than explicability. And nobody measured whether explanation would reduce repeat violations.

## What to Build
Carry the reasons forward and calibrate them. Localise the triggering evidence — timestamp, region, phrase, element — which is the core and is present internally in almost every architecture used here. Produce a calibrated confidence rather than a threshold crossing, so a marginal decision can be treated as marginal. Generate a human-readable rationale from the localised evidence, which is precisely what the platforms' own language models are good at. Distinguish which model or rule fired, since an enforcement driven by a keyword and one driven by a visual classifier warrant different responses. Calibrate disclosure by policy category, because the adversarial argument is strong in some categories and weak in most. Test whether explanations reduce repeat violations, as that is the empirical answer to the objection and nobody has measured it. Provide the same explanation to the reviewer, which improves review quality and is currently also absent. Retain the explanation with the decision record for later review. Measure explanation accuracy, since a wrong explanation is worse than none and would be seized on. And ship it to the creator, because everything above is worthless if it stops at an internal tool.

## Target Customer
Trust and safety engineering leadership, creators, appeal reviewers, and regulators requiring reasoned decisions.

## Impact If Built
A model optimised to produce an action has no obligation to carry the reasons forward, though it computes them. Localising the triggering evidence and generating a rationale from it is within the capability already deployed.
