# Matching on Title and Artist Name

**Niche:** [[niches/music-distribution-platforms/recording-to-composition-matching/profile|Recording-to-Composition Matching]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The match fails because the uploader wrote the title with a bracket and the registry has it without one.
**Tags:** #quick-win #word-embeddings #evaluation-metrics #automation #data-integration #confidence-intervals #descriptive-statistics #bert
**Contested on:** Every serious competitor in this niche is fighting to determine which composition a recording embodies and who wrote it, across corpora with different identifiers and no shared key — and whoever matches most accurately at scale controls where the composition money goes.

## The Problem
A substantial share of match failures are trivial: a featured artist in the title, a bracketed version descriptor, an accented character, a remix suffix, a writer's name with an initial instead of a middle name, a title in one language and the registry entry in another. Each is individually obvious to a person and defeats an exact-match lookup. They account for a large amount of unmatched money and are fixable without any audio analysis at all.

## Why It's Still Broken
The lookup was implemented as an exact match because exact matching is unambiguous, so every formatting difference became a failure — a join designed for certainty fails silently on variation rather than resolving it. Normalisation rules exist informally in people's heads. Nobody reports match failure by cause. And each individual failure is small.

## What a Fix Looks Like
Normalise and fuzzy-match the obvious cases. Normalise titles and names before matching — brackets, features, versions, punctuation, accents, transliteration — which is the fix and will resolve a large share of failures immediately. Report match failures by cause, since the distribution will be dominated by a handful of formatting patterns and that list is the work queue. Fuzzy-match with a confidence threshold rather than requiring exact equality, because near-identical is almost always identical here. Match on writer name variations, as the same person's name is recorded several ways across registries. Use duration and release date as corroborating evidence, which disambiguates most of the remaining near-matches. Handle the featured artist convention explicitly, since it is the single most common title variation. Surface the near-misses for human confirmation rather than discarding them, as a person resolves them in seconds. Standardise what the distributor submits, so the same failure does not recur on the next release. Measure the match rate before and after, which will demonstrate the value clearly. And feed confirmed matches back so the normalisation improves.

## Who Feels the Pain
Writers unmatched over a bracket; artists whose registration looked complete; rights teams working claims that should never have existed; and an industry whose unmatched pool is partly a formatting problem.

## Impact If Fixed
A join designed for certainty fails silently on variation rather than resolving it, so formatting differences became unmatched money. Normalisation plus fuzzy matching resolves a large share of failures with no audio analysis at all.
