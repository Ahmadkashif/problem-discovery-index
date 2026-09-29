# Verification Instead of a Checkbox

**Niche:** [[niches/game-asset-marketplaces/asset-provenance/profile|Asset Provenance]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform's entire provenance apparatus is a checkbox the uploader ticks.
**Tags:** #contrastive-learning #autoencoders #compliance #evaluation-metrics #confidence-intervals #data-integration #automation #dimensionality-reduction
**Contested on:** Every serious competitor in this niche is fighting to establish that a listing is what the seller says it is, when verification currently rests on the creator ticking a box — and whoever can establish it takes the account.

## The Problem
A marketplace's defence against stolen, resold and undisclosed-derivative assets is a disclosure form and a reactive takedown process. Rights holders discover infringement themselves, report it, and wait. Generative tooling made the question harder: a listing may be original, may be a model output, may be a model output derived from someone else's work, and the file alone does not always distinguish them. The platform's liability grows while its verification capability does not.

## Why Nobody Has Built This
Verification costs money and reduces listings, both of which hurt in the short term. The generative question is genuinely unsettled legally, so platforms prefer not to establish facts they would then have to act on. Similarity detection across a large multi-format corpus is real engineering. And the reactive regime has been adequate so far.

## What to Build
Detect what is detectable and govern what is not. Run similarity detection across the full catalogue at upload, which is the core and catches the resold, rescaled and repackaged listings that make up most of the volume. Build representations that survive the transformations sellers actually apply — rescaling, retopology, recolouring, format conversion — since exact matching catches almost nothing. Require substantive attestation rather than a checkbox, with consequences attached, as a declaration with no consequence is not evidence. Record a chain of custody for derived and generated assets, which is what a buyer with legal exposure needs and cannot get. Surface the provenance position to buyers rather than keeping it internal, because commercial studios increasingly will not buy without it. Give rights holders a proactive matching service instead of requiring them to police the catalogue. Handle the generative case explicitly rather than by omission, since silence is itself a position and a deteriorating one. Score sellers on provenance history, which concentrates review where it belongs. Retain the evidence for each decision, as takedown disputes turn on it. And publish the policy and its enforcement rate, which is what makes the regime credible to both sides.

## Target Customer
Asset marketplaces and storefronts, rights holders and creators, commercial studios with legal exposure, and content identification vendors.

## Impact If Built
A declaration with no consequence attached is not evidence, and it is the entire apparatus today. Similarity detection robust to real transformations, plus a substantive attestation regime, replaces a checkbox with a position.
