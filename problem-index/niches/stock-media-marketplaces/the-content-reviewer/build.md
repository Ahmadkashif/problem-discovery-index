# Separating the Mechanical From the Judgement

**Niche:** [[niches/stock-media-marketplaces/the-content-reviewer/profile|The Content Reviewer]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Four different kinds of assessment happen in the same three seconds and only one of them needs a person.
**Tags:** #cnns #object-detection #contrastive-learning #worker-facing #evaluation-metrics #confidence-intervals #automation #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to let a reviewer assess technical quality, rights, similarity and policy in seconds without every rejection being an unexplained loss to someone — and whoever supports that decision improves both the catalogue and the relationship it depends on.

## The Problem
The reviewer checks focus, noise, exposure and artefacts; whether releases are present and adequate; whether the asset duplicates something already in the catalogue or in the same submission; whether it breaches policy; and whether it is commercially viable. The first is measurable, the second and third are largely computable, the fourth is rule-based and the fifth is judgement. They are all done at once, by eye, at a pace set by the queue, and the contributor receives a single code.

## Why Nobody Has Built This
Review was defined as one step because it happens at one moment, so the distinct assessments were never separated — a process named for when it occurs rather than for what it does resists decomposition. Automated quality checks were added as a pre-filter and the reviewer still looks at everything. Contributor-facing explanation was scoped to a reason code. And reviewer accuracy is unmeasured.

## What to Build
Decompose the review and give the judgement its time. Assess technical quality automatically and completely, which is the core and removes a large share of what the reviewer looks for. Detect near-duplicates against both the catalogue and the same submission, since similarity assessment by eye is unreliable at volume and computable at scale. Check rights detection and release matching automatically, connecting to the clearance work. Route only the commercial and aesthetic judgement to a person, which is the part they are there for and currently the part with the least time. Present the automated findings alongside the asset so the reviewer confirms rather than searches. Rank the queue so the marginal cases get attention and the clear ones do not. Give the contributor a specific reason with an example, because a code teaches nothing and a specific finding improves the next submission. Measure reviewer consistency on duplicated assets, since it is unknown and is the only available quality signal. Track rejected assets that were resubmitted and accepted, as that is direct evidence about rejection accuracy. Provide an appeal that works, because a contributor's work being rejected wrongly with no recourse is the relationship-defining event. And report review outcomes by reason, which will show which categories are automatable and which are inconsistent.

## Target Customer
Review operations leadership, reviewers, contributors receiving rejections, and content moderation platform vendors.

## Impact If Built
A process named for when it occurs rather than for what it does resists decomposition, so four assessments share three seconds. Automating the technical, similarity and rights checks gives the commercial judgement the attention it is the only one that needs.
