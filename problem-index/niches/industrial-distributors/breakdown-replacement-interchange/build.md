# A Graded Interchange Graph

**Niche:** [[niches/industrial-distributors/breakdown-replacement-interchange/profile|Breakdown Replacement & Interchange]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cross-reference tables say two parts are equivalent; nobody records whether the substitute actually fitted, lasted, and was accepted by the plant.
**Tags:** #tacit-knowledge-ml #graph-neural-networks #graph-theory #contrastive-learning #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to identify the exact replacement, or an interchange the plant will accept, from whatever arrives — a worn bearing, a nameplate photo, a superseded number — and put it in the maintenance technician's hand inside the downtime window, and whoever closes the most breakdown calls on the first identification takes the account.

## The Problem
When the exact part isn't in stock, the rep offers an interchange. Dimensional equivalence is the easy part; the hard part is whether the substitute's seal, clearance, cage material and load rating suit this machine, and whether this plant's maintenance manager will accept it. Veterans know; the system doesn't. Wrong interchanges come back as returns or, worse, as early failures nobody links to the substitution.

## Why Nobody Has Built This
Manufacturers publish cross-references for their own parts, with commercial reasons to be selective. Distributors hold the outcome data — returns, reorders, repeat failures — but never join it to the substitution decision, because the substitution is a conversation, not a record.

## What to Build
A graph of parts across brands, edges for dimensional and functional equivalence with their source, and weights learned from outcomes: substitution accepted, returned, reordered at normal interval, or failed early. Plant-level overrides sit on top ("site rejects shielded on washdown lines"). Reps see ranked interchanges with evidence and the plant's history, and every choice updates the graph.

## Target Customer
Inside sales and branch managers at BPT distributors handling breakdown calls; regional distributors competing against national chains' broader stock.

## Impact If Built
If graded interchanges let a branch close ~10–20% more breakdown calls from its own shelf instead of a next-day order (estimate), each avoided next-day wait spares the plant hours of downtime at ~$5,000–$50,000+ an hour (estimate), and identification skill stops depending on which veteran answers the phone.
