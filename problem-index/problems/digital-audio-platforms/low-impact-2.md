# Metadata Matching and Unattributed Royalties

**Industry:** [[digital-audio-platforms|Digital Audio Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A recording whose metadata does not match a rights record cleanly still gets played, and the money it earns sits in a pool nobody claims.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #graph-neural-networks #gradient-boosting #contrastive-learning #evaluation-metrics #compliance

## The Problem
Every stream generates two royalty obligations — one to the owners of the recording and one to the owners of the underlying composition — and paying them requires knowing who those parties are. That information arrives as metadata from distributors, labels and publishers, in inconsistent formats, with names spelled several ways, writers credited under aliases, contributors missing entirely, and identifiers absent or wrong.

When the match fails, the royalty cannot be paid and accumulates. The sums involved are substantial enough that the United States created a statutory body specifically to address the composition side of the problem, and the matching difficulty persists on both sides. Live and DJ recordings, samples, remixes, classical repertoire with many possible attributions, and non-Latin-script names are all systematically worse.

The people affected are least able to fix it. A songwriter who does not know their work is earning unattributed money has no way to discover it, and the claiming processes require knowing what to claim. Meanwhile the same recording exists in several catalogues with different identifiers, and reconciling them is manual work performed by rights operations analysts one dispute at a time.

## What Already Exists
Industry identifiers exist — ISRC for recordings, ISWC for compositions, IPI for parties — and coverage is incomplete and inconsistently applied. The Mechanical Licensing Collective in the US administers the unmatched pool and runs its own matching. Audio fingerprinting from Gracenote, ACRCloud and platform-internal systems identifies recordings by sound rather than by metadata. Publishers and collecting societies each run matching operations. Several industry-wide database initiatives have been attempted and have struggled with governance rather than technology.

## The Customisation Gap
Matching is an entity resolution problem across multiple noisy sources, and the industry runs it largely on exact identifier joins with manual fallback. The probabilistic version — resolving parties, works and recordings jointly using name similarity, co-credit structure, audio fingerprint, release context and temporal patterns — is standard practice in other domains and is applied here only patchily.

The joint structure is what is missing. A writer, a work and a recording are connected through a graph of collaborations, releases and publishers, and resolving them together is substantially more accurate than resolving each in isolation — an unknown credit on a recording is far more identifiable when the other four credits on it are known and the writer in question has worked with two of them before.

Audio fingerprinting is underused as a rights signal. It identifies the recording reliably even when metadata is absent, which anchors the recording side of the match and gives the composition side a strong prior through the recording's known prior releases.

And claimants need to be reachable. A matching system that produces high-confidence candidates should be able to notify the likely owner and let them confirm, rather than waiting for someone who does not know the money exists to discover and claim it. That is a straightforward outbound process and its absence is why unmatched pools persist for years.

## Impact If Solved
Unattributed royalties are money already earned by identifiable people who do not receive it, and the failure is a data quality problem rather than a dispute. Joint probabilistic resolution across parties, works and recordings, anchored by audio fingerprinting, closes a large share of the gap; proactive notification of likely owners closes more. Both are ordinary engineering applied to a problem the industry has treated as an administrative inevitability.
