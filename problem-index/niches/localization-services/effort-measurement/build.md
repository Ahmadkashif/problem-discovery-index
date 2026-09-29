# Capturing What the Work Took

**Niche:** [[niches/localization-services/effort-measurement/profile|Effort Measurement]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The environment sees every keystroke and reports a word count.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #automation #confidence-intervals #workflow-orchestration #worker-facing #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to capture what post-editing a segment actually takes, from an environment that records everything and reports nothing — and whoever captures it takes the account.

## The Problem
Translation happens inside a tool that observes everything: which segment was opened, how long it was worked on, how much was changed, whether it was returned to, how the machine suggestion was used. None of it is captured as effort data. The only measure that leaves the environment is a word count and a match band, which describe the input rather than the work, and every commercial and operational decision is made on those.

## Why Nobody Has Built This
Translation environments were built to produce translations rather than to measure production. Measuring linguists' work raises legitimate consent and surveillance concerns that nobody has addressed properly. The party with the tooling benefits from the current measure. And nobody has asked.

## What to Build
Capture the work, with the linguists' agreement, and use it for everything. Capture per-segment effort — active time, edit distance, revision count, returns to the segment — which is the core and turns an unexamined assumption into a measured quantity. Handle consent and privacy properly, with linguists owning their own data and aggregate use agreed, since a measurement regime imposed on a freelance workforce will be resisted and should be. Relate effort to machine output characteristics, which tells an agency which engines and content types are actually cheap. Aggregate by content type, language pair and engine, as the variation across those is what makes a flat discount wrong. Use it for scoping and scheduling, which is immediate operational value independent of any rate question. Feed it into engine selection, since a cheaper engine that costs more to edit is a false economy nobody can currently detect. Give linguists their own data back, which is both fair and the thing that makes participation acceptable. Report distributions rather than averages, because the tail is the disputed part. Separate measurement from evaluation explicitly, so it is not used to rank individuals. And publish the methodology, since the credibility of the whole exercise rests on it.

## Target Customer
Language service providers, translation technology vendors, translator associations, and enterprise localization teams.

## Impact If Built
The environment observes everything and exports a word count, which describes the input rather than the work. Per-segment effort capture, consented and aggregated, turns the industry's central assumption into a measurement.
