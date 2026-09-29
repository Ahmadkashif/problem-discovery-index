# A Capacity Purchase and an Avoidance Purchase

**Niche:** [[niches/vector-search-vendors/vector-index-infrastructure/profile|Vector Index Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same index is sold to platform teams buying capacity at billion scale and to developers trying to avoid running a second system, and almost nothing that decides either purchase is shared.
**Tags:** #k-nearest-neighbors #graph-theory #evaluation-metrics #data-integration #norms-and-inner-products #automation #dimensionality-reduction #workflow-orchestration
**Contested on:** Not terminal — the contest differs by whether the buyer is acquiring capacity or avoiding a system, and the decomposition is recorded in the profile.

## The Problem
A vendor pitches the same product to a platform team with eight hundred million vectors and to a startup with a hundred and forty thousand. The first asks about memory per vector at a given recall, replica behaviour under a hot shard, and what the bill looks like at two billion. The second asks whether this is really better than the extension already in their Postgres, and how much of their week it will cost to operate. Winning the first requires a cost structure; winning the second requires being obviously worth a new dependency, which for most small corpora it is not. The product answers both with a feature list.

## Why Nobody Has Built This
The single product is the efficient thing to build and the positioning follows the engineering rather than the market. The small end looks like a funnel into the large end, which makes abandoning it uncomfortable even when the commoditisation has already happened. And the large end's requirements — cost per vector, predictable tail latency — are unglamorous engineering that competes for roadmap against features that demo well.

## What to Build
Build the substrate that both genuinely need and let the go-to-market diverge. The honest common layer is the measurement and operational surface neither side gets: an explicit recall-latency-cost frontier for the customer's own corpus rather than a benchmark's, so a buyer can choose an operating point knowingly instead of accepting a default. Make index parameters self-tuning against a stated target — hold this recall at the lowest cost, or this latency at the highest recall — since the parameters are currently set by copying an example and the mapping from parameters to outcome is exactly what the vendor knows and the customer does not. Report memory, storage and compute per vector transparently, because the buyer is doing this arithmetic anyway and doing it badly. Support graceful migration in both directions, including out, since a vendor confident in their economics should make leaving easy and the ones that do not are telling the buyer something. Make the operational surface — backup, restore, replica, failover, upgrade — as good as a mature database's, which is the part that determines whether the second buyer ever trusts a second system. Publish behaviour under adversarial conditions: hot shards, skewed queries, mutation bursts. And be explicit about which buyer the product serves, since the small end is genuinely commoditising and pretending otherwise wastes everyone's time.

## Target Customer
Platform teams and application developers on either side of the split, and the vendors deciding which business to be in.

## Impact If Built
The shared layer that both buyers need — a corpus-specific recall-latency-cost frontier and self-tuning against a stated target — is the part nobody ships, because the vendor knows the parameter-to-outcome mapping and leaves the customer to guess it.
