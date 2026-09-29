# The Content Reviewer on the Submission Queue

**Industry:** [[stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Worker Life Changing
**One-liner:** Reviewers assess enormous volumes of submissions for technical quality, rights, similarity and policy compliance in seconds each, and every rejection is someone's work.
**Tags:** #cnns #object-detection #contrastive-learning #k-nearest-neighbors #transfer-learning #evaluation-metrics #worker-facing #compliance

## The Problem
The queue is submissions. Each needs a technical assessment — focus, noise, exposure, compression artefacts, chromatic aberration — a rights assessment, a similarity check against the existing catalogue and against the contributor's own batch, a keyword sanity check, and a policy check for prohibited content.

Volume is extreme. Contributors submit in batches of hundreds, the marketplace receives very large daily volumes, and review time per asset is measured in seconds.

Technical judgements are partly objective and partly stylistic. Grain can be a defect or an aesthetic choice. Soft focus can be a mistake or intentional. The reviewer decides, quickly, and contributors experience the outcome as arbitrary when two similar images are treated differently.

Similarity is a persistent irritant. A contributor submitting forty near-identical frames from one shoot expects them all accepted; the marketplace does not want forty near-duplicates in the catalogue; the reviewer picks.

Rejections carry a reason code from a short list that rarely matches the actual issue, so the contributor receives "technical quality" for an image rejected because the marketplace already has two thousand like it.

And the standards drift. What is accepted changes with the catalogue's composition and with demand, and reviewers absorb this informally.

## Why It Matters to the Worker
The volume and the pace are the defining features, and the task — sustained visual assessment of near-identical material — is one humans do poorly after the first hour.

The decisions affect real people's income and the reviewer knows it, while having seconds and a reason code list that cannot express what they actually saw.

The guidance is thin for the judgements that are hardest. Stylistic technical choices, similarity thresholds and borderline policy cases are where the disagreements are and where the documentation is weakest.

Contributor appeals are frequent and often justified, and the reviewer handling an appeal is defending a decision made in four seconds a month earlier.

And there is no feedback. A reviewer does not learn whether the assets they accepted went on to sell or whether the ones they rejected would have.

## What a Solution Looks Like
Automate the objective technical assessment entirely. Focus, noise, exposure, compression artefacts and aberration are measurable, and measuring them removes a substantial share of the decisions and makes them consistent, which is what contributors actually want.

Similarity clustering before review. Presenting a contributor's batch as clusters of near-duplicates, with the best of each pre-selected, turns forty decisions into one and is a direct application of embedding similarity.

Catalogue saturation as a visible input. Whether the marketplace already holds two thousand similar assets is computable and is the real reason for many rejections; showing it makes the decision honest and the reason code accurate.

Specific rejection reasons. A contributor told which region is soft, or that the catalogue holds many similar assets, or which logo needs removing, can act. A reason code cannot be acted on and generates the appeal.

Rights pre-checks with regions flagged, so the reviewer confirms rather than searches.

Outcome feedback. Whether accepted assets sold, and how rejected ones would have performed where that can be estimated, is the only route to calibrating a standard that currently drifts informally.

## Impact If Solved
This function decides which work enters the market, at a volume and pace that make careful assessment impossible, with reason codes that cannot explain the decision. Automating objective measures, clustering near-duplicates and making catalogue saturation visible reduce the decision count sharply and make the remaining judgements explainable to the person on the other side.
