# Everything Is the Wrong Size

**Niche:** [[niches/game-asset-marketplaces/multi-source-coherence/profile|Multi-Source Asset Coherence]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The door is twice the height of the character, the pivot is in the middle of the mesh, and this is the ninth asset today.
**Tags:** #quick-win #automation #workflow-orchestration #worker-facing #evaluation-metrics #data-integration #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to make assets from fifteen creators with fifteen conventions look like one game, and whoever automates that work takes the account.

## The Problem
The first minutes with any purchased asset are the same: it imports at the wrong scale because the creator authored in different units, its pivot is in the centre rather than at the base, its forward axis points the wrong way, and its materials came in with the wrong shading model. Every one of these is corrected by hand, on every asset, by someone whose skills are being spent on unit conversion.

## Why It's Still Broken
The conventions are not recorded anywhere — an asset that does not state its units, pivot or axis convention forces the importer to infer them every time, and nobody has ever been required to state them. Import settings handle format, not convention. Each creator's choices are reasonable in isolation. And the correction is quick enough individually to never become anyone's project.

## What a Fix Looks Like
Infer the conventions and correct them on import. Detect the authored unit scale from the geometry and correct to the project standard automatically, which is the fix and handles the commonest case outright. Place pivots by rule — base centre for props, hinge for doors — rather than accepting whatever arrived. Detect and correct the forward axis, which is mechanical and currently manual. Map materials to the project's shading model on import rather than after. Apply the project's naming and folder convention automatically. Report what was changed so the artist can check rather than trust blindly. Build a per-creator convention profile, since a creator's conventions are consistent and learning them once serves every future purchase. Run a batch pass over assets already in the project, which usually finds a backlog. Flag anything that cannot be inferred confidently instead of guessing. And make it the default import path rather than a tool someone has to remember.

## Who Feels the Pain
Technical artists spending skilled hours on unit conversion; studios paying for integration they did not budget; art leads with inconsistent scenes; and the schedule that absorbs it invisibly.

## Impact If Fixed
An asset that does not state its units, pivot or axis convention forces the importer to infer them every time, and nobody has ever been required to state them. Inferring and correcting on import turns the first ten minutes of every asset into nothing.
