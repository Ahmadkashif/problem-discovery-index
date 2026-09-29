# Matching With the Recording Itself

**Niche:** [[niches/music-distribution-platforms/recording-to-composition-matching/profile|Recording-to-Composition Matching]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The strongest evidence about which song a recording is comes from listening to it, and the matching is done on text fields.
**Tags:** #contrastive-learning #transformers #graph-theory #evaluation-metrics #confidence-intervals #bert #k-nearest-neighbors #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to determine which composition a recording embodies and who wrote it, across corpora with different identifiers and no shared key — and whoever matches most accurately at scale controls where the composition money goes.

## The Problem
Matching is attempted on metadata: title, artist, duration, sometimes a writer name spelled inconsistently. That fails for cover versions, live recordings, remixes, translated titles, featured artist variations, and every case where the uploader typed something different from the registry. The recording itself contains far better evidence — the melody, the lyrics, the structure — and it is not used, so a problem with an abundant signal is solved with the sparsest available one.

## Why Nobody Has Built This
Matching was implemented as a database lookup against registries, so audio was never part of the pipeline — a process designed to join two text records has no place to put an acoustic signal. Fingerprinting has been used for recording identification rather than for composition matching. The distributor's own corpus of correctly matched works was never framed as training data. And the benefit accrues to the payee rather than to the matcher.

## What to Build
Use the audio, the lyrics and the corpus. Match on acoustic and lyrical similarity as well as metadata, which is the core and handles the cover, the live take and the remix that text matching cannot. Train on the distributor's own corpus of recordings with verified compositions, writers and splits, since that is the largest labelled set for this problem anywhere and it is sitting unused. Resolve writer and party identity across registries, as the same person appears under several spellings and identifiers and that is a large share of the failure. Express match confidence, because a wrong match pays the wrong writer and is harder to reverse than a non-match. Handle the many-to-many structure properly, since a recording may embody more than one composition and a composition has many recordings. Detect the interpolation and the sample, which are common, valuable and routinely unclaimed. Return the match to the registries rather than holding it, as the industry-level fix requires the corpus to converge. Prioritise by unmatched money, so effort follows value. Flag the contested composition for adjudication rather than matching it, because two claimants is a different problem. And publish match accuracy, since a matching claim nobody can evaluate is worth little.

## Target Customer
Data and rights leadership, collecting and licensing organisations, publishers and writers, and music recognition vendors focused on recordings.

## Impact If Built
A process designed to join two text records has no place to put an acoustic signal, so the best evidence is unused. The distributor's corpus of verified recording-to-composition links is the largest labelled dataset for this problem in existence.
