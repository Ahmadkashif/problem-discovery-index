# A Hundred Thousand Decisions a Day

**Niche:** [[niches/digital-audio-platforms/catalogue-intake-at-scale/profile|Catalogue Intake at Scale]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Everything that determines what the catalogue is happens at intake, at a volume that rules out anyone looking.
**Tags:** #contrastive-learning #cnns #evaluation-metrics #confidence-intervals #graph-theory #automation #compliance #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to ingest well over a hundred thousand tracks a day without letting the bad ones through or losing the good ones — and whoever does it well controls what the catalogue actually is.

## The Problem
Intake decides what exists on the platform: whether a release is classified correctly, whether its metadata supports discovery, whether it is a duplicate of something already there, whether it impersonates another artist, whether it is infringing, and whether it is functional noise uploaded to harvest royalties. Each decision is made automatically at enormous volume, with a thin review layer, and the consequences fall on listeners, on rights holders and on the royalty pool.

## Why Nobody Has Built This
Intake was engineered for throughput because the volume demanded it, so quality checks are the ones that can run cheaply at scale — a pipeline built to accept a hundred thousand items a day optimises acceptance rather than assessment. The pool structure means low-quality uploads cost other artists rather than the platform. Classification quality is not measured against discovery. And rejection falls on artists with no route to appeal.

## What to Build
Assess at intake rather than merely accept. Detect duplicates and near-duplicates against the whole catalogue, which is the core and addresses both a discovery problem and a royalty-harvesting one. Detect impersonation by name and audio similarity, since it is the highest-consequence intake failure and is largely a matching problem. Classify genre, mood and attributes automatically and measure the classification against discovery outcomes, because metadata quality determines whether a release can be found and is currently unmeasured. Detect functional and generated audio uploaded at scale to harvest royalties, as it draws from a fixed pool and is a transfer from other artists. Validate rights and identifiers at intake rather than discovering the problem in royalty matching. Give a rejected release a specific reason and a route to appeal, since a legitimate artist blocked by an automated check has no recourse. Route the uncertain to review rather than deciding automatically in both directions. Report what intake accepted and rejected by category, which is the honest description of what the catalogue is becoming. Feed intake decisions back into distributor quality scoring, because problems concentrate at source. And measure intake's effect on the catalogue rather than its throughput, which is the metric the function should have.

## Target Customer
Catalogue engineering and trust leadership, artists rejected or impersonated, rights holders whose pool is drawn from, and content identification vendors.

## Impact If Built
A pipeline built to accept a hundred thousand items a day optimises acceptance rather than assessment. Duplicate, impersonation and functional-audio detection at intake addresses discovery, integrity and the royalty pool at the same point.
