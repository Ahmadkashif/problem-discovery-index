# Provenance and Licence Verification

**Industry:** [[game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Marketplaces have always had stolen and resold assets, generative tooling has made originality harder to establish, and verification rests on the creator ticking a box.
**Tags:** #contrastive-learning #autoencoders #cnns #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #compliance #graph-neural-networks

## The Problem
Asset marketplaces have a long-standing resale problem: work taken from another marketplace, from a game, from a free repository or from an artist's portfolio, relisted under a new name. Detection is largely reactive, driven by the original creator noticing and filing a complaint, and the same asset frequently reappears under another account.

Generative tooling added a second and harder question. Listings may be generated, partly generated, or generated and then hand-finished, and the platforms have adopted disclosure requirements that depend on creators declaring accurately. Beyond disclosure sits the unresolved question of what a generator was trained on, which is the subject of active litigation and which no marketplace can verify.

Licence compliance is the third strand. Assets incorporate other assets — a model using a purchased texture, a plugin bundling a library, an audio pack containing a sampled instrument — and whether the incorporated component's licence permits resale is checked essentially never. Buyers inherit that risk and discover it, if at all, when someone else does.

The consequence for a studio is real. Shipping a game containing an asset the seller did not have the right to sell is a legal exposure the studio carries, and the marketplace's terms generally place it there.

## What Already Exists
Marketplaces run manual review of submissions with varying rigour, and takedown processes for complaints. Reverse image search catches some straightforward theft. Perceptual hashing is used in adjacent media industries and is applied here only patchily. Generative disclosure policies have been introduced across the category and are declaration-based. Licence terms are standardised per marketplace. Some studios run their own provenance diligence on purchased assets, which is a manual and expensive process.

## The Customisation Gap
Similarity detection at asset level rather than image level is the gap. Geometry, material structure, texture content and audio waveform all support fingerprinting that is robust to the transformations a reseller applies — retopology, retexturing, rescaling, format conversion, pitch shifting — and that is a substantially different and harder problem than reverse image search on a thumbnail. The marketplace holds every file in the catalogue, which makes it the only party able to check a submission against the whole corpus.

Cross-marketplace checking is the extension that would matter most, and it requires cooperation between competitors on a shared fingerprint index — which is how other content industries eventually addressed the same problem.

Bundled component detection is the unglamorous piece with real legal consequence. Identifying that a submitted asset contains a texture, library or sample from a known source, and flagging whether that source's licence permits redistribution, is a matching problem against public and licensed corpora.

And generative provenance needs honesty about its limits. Detection of generated content is unreliable and becoming more so, and a marketplace that claims to verify it will be wrong in both directions — wrongly accusing creators and wrongly clearing listings. The defensible position is strong disclosure requirements, verifiable process evidence where creators can supply it, and clear statements to buyers about what has and has not been established.

## Impact If Solved
Provenance failures transfer legal risk to studios who cannot assess it and income to resellers from the creators they copied. Asset-level fingerprinting against the catalogue catches the resale problem the category has tolerated for a decade; bundled component detection addresses a licence exposure nobody currently checks; and being honest about the limits of generative detection is worth more than a claim that will not survive contact with either creators or courts.
