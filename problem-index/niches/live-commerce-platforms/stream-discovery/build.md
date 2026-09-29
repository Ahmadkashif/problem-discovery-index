# Two Hours and No History

**Niche:** [[niches/live-commerce-platforms/stream-discovery/profile|Stream Discovery]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A stream exists for two hours with no history, its value depends on what is happening in it this minute, and recommendation systems built for persistent catalogues have nothing to work with.
**Tags:** #transformers #matrix-decompositions #gradient-boosting #evaluation-metrics #revenue-impact #confidence-intervals #time-series-forecasting #automation
**Contested on:** This niche is not terminal — the fight over cold-start ranking and the fight over the ranking objective are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Recommendation as practised assumes the thing being recommended persists. A product accumulates views, purchases and reviews; a video accumulates watch time; both can be scored from their own history. A live stream has none of that. It appears, it is relevant for a hundred and twenty minutes, and its relevance changes minute by minute as the host moves from one item to the next. A viewer who would have bought is shown it forty minutes after the item they wanted sold out. The entire apparatus of collaborative signal, built over two decades, is unavailable at exactly the moment it is needed.

## Why Nobody Has Built This
The platforms arrived at live commerce through short-form video and brought that stack with them, where the item is permanent and the objective is watch time — both assumptions are wrong here and neither is visible as an assumption from inside the system. Building for a two-hour item means abandoning most of what the existing infrastructure does well. And the seller-side cost of a bad match is invisible in engagement metrics, which is what the system is judged on.

## What to Build
Treat the stream as a perishable item with a within-session state. Score a stream from priors rather than from its own history — the seller's record, the category, the announced inventory, the opening minutes — which is the only signal available at the moment it matters and is the cold-start sub-niche's contest. Model relevance as changing within the stream, since what the host is showing now is the unit of relevance and a stream-level score is the wrong granularity in a way nothing else in commerce is. Use the live signal directly: what is on screen, what is being said, what is selling in the last ninety seconds, which is available in real time and unused. Rank for purchase intent rather than for watch time, which is the second sub-niche's contest and is a different system rather than a reweighting. Account for the deadline explicitly — a match that arrives after the item sold is worth nothing, so latency is part of the objective rather than an engineering constraint. Balance the seller side deliberately, because a new seller with an empty room does not return and the marketplace's supply depends on it. Re-entry matters as much as entry: pulling a viewer back when the stream reaches an item they want is a mechanic no persistent-catalogue system has needed. And evaluate on purchase and on seller retention, not on session length.

## Target Customer
Live commerce platforms, the marketplaces adding live formats, and the discovery teams whose inherited stack does not fit the problem.

## Impact If Built
The whole apparatus of collaborative signal is unavailable at the moment it is needed, because the item lives two hours. Relevance changing within the stream makes stream-level scoring the wrong granularity, and the deadline makes latency part of the objective rather than an engineering detail.
