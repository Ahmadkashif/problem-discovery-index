# A Reference Architecture Written From Opinion

**Niche:** [[niches/headless-commerce-vendors/composition-pattern-intelligence/profile|Composition Pattern Intelligence]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The reference architecture every implementation starts from was drawn by an architect from experience and has never been checked against how the implementations that followed it actually performed.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #graph-theory #compliance #quick-win #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to turn hundreds of implementations into an empirical account of which compositions work — and whoever does that advises better than anybody, because every architect in the category is currently designing from anecdote.

## The Problem
The vendor's reference architecture is a diagram showing which services sit where and how they connect. It was produced three years ago by a respected architect, reflects the service landscape at that time, is the starting point for most implementations, and has never been evaluated. Implementations that followed it and implementations that departed from it have both been delivered, with outcomes the vendor can observe, and nobody has compared them. The single most influential artefact in the category's delivery practice is an untested opinion carrying the authority of an official document.

## Why It's Still Broken
A reference architecture is a marketing and enablement artefact produced by the field organisation, and evaluating it is nobody's role. Comparing outcomes requires the characterisation work nobody has done. Finding that the reference is wrong in places would be awkward for its author and for the vendor. And it has the authority of officialness, which discourages the question.

## What a Fix Looks Like
Evaluate the reference and version it. Compare outcomes between implementations that followed the reference and those that departed from it, which uses data the vendor holds and is the evaluation that has never been run — it will show that parts hold and parts do not, which is the useful finding. Version the reference with a date and a review cycle, since the service landscape changes and an undated diagram implies a timelessness it does not have. Mark each element with its evidential basis — measured, inferred, or a judgement — which is an honesty that costs nothing and tells an architect how much weight to give each part. Publish the departures that worked, since a departure with a better outcome is a finding and is currently treated as a deviation. Provide variants for the recurring retailer shapes rather than one architecture, since a single-market single-brand retailer and a twelve-market group need different compositions and are given the same diagram. Record which implementations followed which version, so the evaluation can continue. Update it when a finding contradicts it, visibly, which is what turns a document into a maintained asset. And let architects contribute findings back, since they are the people who discover what the reference got wrong.

## Who Feels the Pain
Architects starting from an untested diagram; retailers whose implementations inherited its errors; and vendors whose most influential artefact is unexamined.

## Impact If Fixed
The most influential artefact in the category's delivery practice is an untested opinion with official authority. Comparing outcomes between implementations that followed it and those that departed uses data the vendor holds and will show which parts hold, which is the useful finding either way.
