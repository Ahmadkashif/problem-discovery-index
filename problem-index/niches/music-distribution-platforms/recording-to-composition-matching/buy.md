# Entity Resolution and Content Fingerprinting

**Niche:** [[niches/music-distribution-platforms/recording-to-composition-matching/profile|Recording-to-Composition Matching]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Audio fingerprinting identifies recordings extremely well and was never pointed at the composition underneath them.
**Tags:** #contrastive-learning #transformers #evaluation-metrics #confidence-intervals #graph-theory #k-nearest-neighbors #data-integration #bert
**Contested on:** Every serious competitor in this niche is fighting to determine which composition a recording embodies and who wrote it, across corpora with different identifiers and no shared key — and whoever matches most accurately at scale controls where the composition money goes.

## The Problem
Audio fingerprinting is a mature, deployed technology that identifies a specific recording from a few seconds of audio with very high accuracy, and it underpins content identification across several large platforms. It answers "which recording is this". The industry's expensive question is "which composition is this recording of", which requires recognising the same song performed differently — a related but genuinely harder problem that the deployed technology was not built for.

## What Already Exists
Acoustic fingerprinting for exact recording identification; cover song detection research; melodic and harmonic similarity methods; lyric matching; and entity resolution frameworks for party and work records.

## The Customization Gap
The adaptation is from exact recording identity to compositional identity. It requires: (1) recognising the same composition across different performances, keys, tempos, arrangements and languages, which exact fingerprinting is explicitly designed not to do — this is the substantive technical gap; (2) lyric evidence alongside audio, since a translated or instrumental version breaks one signal and not the other; (3) a many-to-many structure with splits, where fingerprinting returns a single identity; (4) a financial consequence for a wrong match, which raises the confidence bar above content identification's; and (5) registries as the target rather than a content database, so the output must be a claim rather than an identification.

## Target Customer
Rights and data leadership, collecting organisations, publishers, and audio recognition vendors focused on recordings.

## Impact If Solved
Fingerprinting answers which recording this is and the industry needs to know which song it is of. Recognising a composition across performances is the harder problem, and the corpora needed to train it exist inside the distributors.
