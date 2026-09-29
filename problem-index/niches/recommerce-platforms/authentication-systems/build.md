# A Capability the Opponent Studies

**Niche:** [[niches/recommerce-platforms/authentication-systems/profile|Authentication Systems]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Authentication combines trained expertise, reference databases and increasingly imaging, and every platform still makes the final call as a human judgement under time pressure with asymmetric consequences on both sides.
**Tags:** #cnns #object-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #contrastive-learning #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to distinguish genuine from counterfeit against opponents who study exactly what is being checked — and whoever does that holds the category, because a single publicised false accept destroys the trust the whole platform rests on.

## The Problem
An authenticator checks a set of features they were trained on. Counterfeiters buy authenticated genuine examples, study which features are examined — frequently from the platform's own published educational content — and reproduce them accurately. The checks that worked two years ago now pass a good counterfeit. The authenticator's training was fixed at a point in time, the reference database contains genuine examples rather than the counterfeits that are actually circulating, and nothing systematically tracks which checks still discriminate. The capability degrades continuously against an opponent that improves continuously, and the platform finds out when a fake is publicised.

## Why Nobody Has Built This
The adversarial dynamic is understood by authenticators and is not reflected in how the capability is managed, which treats training and reference data as assets rather than as depreciating ones. Counterfeit examples are the scarce and valuable training data and most platforms return or destroy them rather than retaining them systematically. Sharing reference data between platforms would help everybody and helps competitors. And the degradation is invisible until a failure.

## What to Build
Manage the capability as a depreciating adversarial asset. Retain every confirmed counterfeit with full imaging and a record of which features gave it away, since counterfeits are the scarcer class and the record of how the current generation fails is the most valuable asset in this niche and most platforms discard it. Track which checks still discriminate, by measuring how often each feature separates confirmed genuine from confirmed fake, and retire the ones that have stopped — this is the measurement that makes the adversarial dynamic manageable. Rotate and diversify the checks so that the published and inferable ones are not the only ones in use, and keep some deliberately unpublished. Use imaging to detect what a human cannot rather than to confirm what they can, since the marginal value is in the features outside human perception — material structure, stitching regularity at magnification, spectral properties — and that is where the opponent has the least room to adapt. Train models on the image corpus, which is large and labelled by the authenticators' own decisions, and use them as a second opinion rather than as a decision. Measure both error directions, which the fix note develops. Build a shared counterfeit intelligence function across platforms where the competitive logic permits, since the opponent is shared. And stop publishing the check list in educational content, which is a marketing decision with a direct operational cost.

## Target Customer
Authentication operations in luxury, sneaker and collectible categories, the platforms whose trust rests on them, and the brands whose goods are being counterfeited.

## Impact If Built
The capability depreciates against an opponent that studies it, and it is managed as a fixed asset. Retaining confirmed counterfeits with the features that exposed them is the most valuable data in the niche and is routinely discarded, and measuring which checks still discriminate makes the degradation visible before a failure does.
