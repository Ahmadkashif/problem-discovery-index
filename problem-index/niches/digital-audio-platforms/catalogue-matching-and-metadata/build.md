# Matching With More Than a Text Field

**Niche:** [[niches/digital-audio-platforms/catalogue-matching-and-metadata/profile|Catalogue Matching & Metadata]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform has the recording itself and matches it to an owner using the text somebody typed alongside it.
**Tags:** #contrastive-learning #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #compliance #k-nearest-neighbors #data-integration
**Contested on:** Every serious competitor in this niche is fighting to match a recording to a rights record cleanly enough that its money reaches an owner — and whoever resolves the unmatched pool releases a real sum to people who do not know it exists.

## The Problem
Matching runs on identifiers and metadata supplied by whoever delivered the recording. When an identifier is missing, wrong or inconsistent with a rights record, the match fails and the royalty accumulates unattributed. The platform has the audio itself, a complete listening record, the delivery chain, and every other version of the same recording and composition in its catalogue — none of which is used to resolve the match. The pool grows and the owners are not told.

## Why Nobody Has Built This
Matching was implemented as an identifier lookup because identifiers were supposed to solve this, so the failure case fell back to manual claims — a process designed around a key that is missing has no second method. The unmatched pool's eventual distribution does not disadvantage the platform. Audio-based matching was built for content identification rather than for rights resolution. And the owners cannot ask because they do not know.

## What to Build
Use every signal the platform has. Match on audio content as well as identifiers, which is the core and resolves the cases where metadata is wrong rather than merely absent. Use the platform's own catalogue as a reference, since the same recording or composition frequently exists elsewhere in it with a clean match. Use the delivery chain as evidence, because a distributor's other deliveries disambiguate a poorly labelled one. Express match confidence and route the uncertain to review rather than treating everything as matched or unmatched. Resolve the composition side as well as the recording, connecting to the wider rights problem. Report the unmatched pool's size and composition, which is the transparency that would create pressure to resolve it. Notify probable owners proactively rather than waiting for a claim, as the current arrangement requires the owner to know about money they have never been told about. Feed resolved matches back into the reference data, so the corpus improves. Detect the systematic delivery error rather than fixing instances, since one distributor's formatting problem produces thousands of failures. And report match rate as an operating metric, which nobody publishes and which would be a competitive claim.

## Target Customer
Rights operations leadership, artists and rights holders with unmatched money, distributors and societies, and music data vendors.

## Impact If Built
A process designed around a key that is missing has no second method, so failed matches fall to manual claims nobody makes. The audio, the catalogue and the delivery chain are all available as evidence and none of them is used.
