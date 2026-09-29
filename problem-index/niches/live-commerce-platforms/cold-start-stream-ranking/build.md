# Four Minutes of Evidence

**Niche:** [[niches/live-commerce-platforms/cold-start-stream-ranking/profile|Cold-Start Stream Ranking]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every live stream is a cold-start item for its entire life, and the platforms rank them with follower counts and a recency boost.
**Tags:** #transformers #gradient-boosting #matrix-decompositions #confidence-intervals #evaluation-metrics #transfer-learning #bayesian-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rank a stream that has existed for four minutes against streams with hours of accumulated signal — and whoever gets the first minutes right decides which sellers survive.

## The Problem
At the moment a stream goes live the system must decide how much distribution to give it, and it knows almost nothing. In a catalogue this is a temporary embarrassment resolved within a day. Here it is the entire lifecycle: by the time enough behavioural signal exists to rank the stream confidently, the stream is over. The platforms respond with the only durable signal they have — how many followers the seller already has — which is a self-reinforcing loop that concentrates distribution on established hosts and starves the supply the marketplace needs.

## Why Nobody Has Built This
The infrastructure was built for items that accumulate signal and the cold-start path is an afterthought within it. The content of a live stream is the obvious prior and requires real-time audio-visual understanding at serving latency, which is expensive and until recently was not practical. Seller-level priors require a seller model nobody built because sellers were treated as content creators. And the follower heuristic performs acceptably on aggregate engagement, which is what is measured.

## What to Build
Rank from priors and update fast. Build a seller-level prior from their own history — conversion rate, retention curve, category, price band, reliability — which is the strongest available signal and is computable before the stream starts, and which is the piece a follower count crudely approximates. Use the announced inventory: what is being sold tonight is declared in advance and predicts who wants it far better than who follows the host. Read the opening minutes directly — what is on screen, what is being said, the energy and pace of the show — since audio-visual understanding at serving latency is now practical and this is the signal nobody uses. Update the estimate continuously from the first viewers' behaviour, treating each cohort as an experiment, which is how the four-minute estimate becomes a forty-minute one. Budget exploration against the stream's remaining life rather than against a fixed slot, since a stream ninety minutes in has no time left to earn back an exploration cost. Calibrate uncertainty explicitly, because the decision is how much distribution to risk and that is a decision under uncertainty rather than a point estimate. Transfer across a seller's streams, so the tenth show starts from the nine before it rather than from zero. And measure specifically on new and low-history sellers, since that is the cohort the system exists to serve and aggregate metrics hide it.

## Target Customer
Live commerce platforms, marketplaces with live formats, and the discovery teams whose cold-start path is a follower count.

## Impact If Built
Cold start is the permanent condition here rather than a transient state, and the follower heuristic is a self-reinforcing loop that starves new supply. Announced inventory and the opening minutes are both available before any behavioural signal exists and neither is used.
