# Review Where Failures Actually Are

**Niche:** [[niches/streaming-video-platforms/the-content-operations-reviewer/profile|The Content Operations Reviewer]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every asset is reviewed as though every asset were equally likely to be wrong.
**Tags:** #cnns #transformers #evaluation-metrics #confidence-intervals #automation #worker-facing #object-detection #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to stop a person watching every asset end to end against a specification — and whoever routes review by where failures actually occur turns an unbounded queue into a bounded one.

## The Problem
The reviewer watches the whole thing. Most of it is fine, because most of it comes from a competent supplier who produced a correct file. The defects concentrate: particular suppliers, particular languages, particular pipeline stages, particular kinds of content, particular positions in a file. None of that concentration is used to direct the review, so the reviewer spends their attention uniformly on a distribution that is anything but uniform, and the queue grows with the catalogue.

## Why Nobody Has Built This
Quality failures reach millions of viewers, so the process defaults to complete review — a failure mode that is public and embarrassing produces an inspection regime designed for certainty rather than for efficiency. Automated checks cover technical conformance and stop short of perceptual and linguistic quality. Failure data is not aggregated by source. And reviewer time is a cost centre nobody analyses.

## What to Build
Detect broadly and direct the human precisely. Detect perceptual and linguistic defects automatically — subtitle timing and reading speed, audio sync, dub mismatch, artwork conformance, missing chapters — which is the core and covers most of what is being watched for. Track failure rates by supplier, language, pipeline stage and content type, since the concentration is the basis for everything else. Route review by predicted risk rather than reviewing everything, which converts an unbounded queue into a bounded one. Present the reviewer with the segments most likely to contain a defect rather than the whole runtime, as that is where the hours are recovered. Catch defects earlier in the pipeline, because a defect found at the end has already had work built on it. Feed failure patterns back to suppliers, which is the only remedy that reduces volume at source. Measure reviewer consistency on seeded cases, since it is unknown and is the quality signal for the quality process. Use viewer signals as a post-publication detector, as subtitle toggles and abandonment report defects the process missed. Track the defects that reached viewers, which is the honest measure of the function. And report time per asset by content type, so the economics of the operation are visible.

## Target Customer
Content operations leadership, reviewers, suppliers and localisation vendors, and media quality control vendors.

## Impact If Built
A failure mode that is public and embarrassing produces an inspection regime designed for certainty rather than efficiency. Failure concentration by supplier, language and pipeline stage is the basis for routing review, and nobody tracks it.
