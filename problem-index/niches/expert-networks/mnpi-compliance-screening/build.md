# Every Call Reviewed, Not a Sample

**Niche:** [[niches/expert-networks/mnpi-compliance-screening/profile|MNPI & Compliance Screening]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A chaperone listens to some calls and a reviewer reads some transcripts, and the evidence a fund has that its calls were clean is a sample and a signature.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to give a fund's chief compliance officer full-population evidence that no expert call carried material non-public information, in a form an examiner accepts — and whoever does that cheaply enough to run on every call becomes the network a regulated fund can approve.

## The Problem
Real-time chaperoning is expensive and is applied to a fraction of calls, often chosen by client policy rather than by risk. Post-call review is applied to library transcripts and some recorded calls. The rest rely on the expert's attestation.

## Why Nobody Has Built This
Positives are rare, the cost of a miss is large, and nobody wanted to own a model whose failure would be a regulatory event. Recording every call also raises expert and client consent questions.

## What to Build
Passage-level MNPI-risk classification on every recorded call, conditioned on the expert's employment record relative to the companies discussed, with real-time alerts to a chaperone and a post-call evidence pack. Report recall with confidence intervals against reviewer-confirmed cases, and route uncertain passages to humans.

## Target Customer
Chief compliance officers at expert networks; compliance heads at hedge funds that require recorded calls.

## Impact If Built
Full-population review replaces a sampling defence with evidence, and lowers per-call compliance cost at the same time.
