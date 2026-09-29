# Matching Viewers to Streams in Real Time

**Industry:** [[live-commerce-platforms|Live Commerce Platforms]]
**Type:** High Impact
**One-liner:** A stream exists for two hours with no history, its value depends on what is happening in it this minute, and recommendation systems built for persistent catalogues have nothing to work with.
**Tags:** #contrastive-learning #transformers #cnns #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #revenue-impact

## The Problem
A live shopping stream is a perishable, mutating object. It starts, runs for a couple of hours, and ends. During that time what it is changes continuously — the host moves from one item to the next, holds an auction, answers questions, shows something unexpected.

Matching a viewer to it must happen now. A viewer opening the app wants something worth watching in this moment, and the platform has seconds to decide from among thousands of concurrent streams.

The standard machinery does not fit. Collaborative filtering needs items with interaction history and a stream has none until it is over, at which point it no longer exists. Content-based matching needs a description, and the stream's description is a title the host typed before starting, which does not reflect what is being shown at minute forty. Behavioural signals accumulate over a stream's life, which means the cold start lasts precisely as long as the window in which it could help.

The cost is asymmetric and immediate. A stream with no viewers does not sell, and a seller who does not sell does not return — so a poor match destroys supply, not just a transaction. Small sellers are hit hardest and they are the supply the platform most needs.

## Why It's Unsolved
Every stream is a permanent cold start. There is no accumulated interaction history to draw on, ever, because the object ceases to exist.

The content signal that would substitute must be extracted from live video and audio in real time — what is being shown, what the host is saying about it, what is happening in chat — which is a demanding pipeline with a latency budget measured in seconds.

Host identity helps and only partly. A returning host's audience is somewhat predictable and their catalogue changes stream to stream, so historical performance transfers imperfectly.

Viewer intent is ambiguous in a way it is not in search. Someone opening a live shopping app may want to buy a specific thing, browse a category, or be entertained, and the same person wants different things at different times. Optimising for watch time — which is what the inherited short-form video machinery does — is not the same as optimising for purchase, and the two diverge.

And the exploration cost is high. Testing whether a viewer likes an unfamiliar stream costs part of a session, and sessions are short.

## What a Solution Looks Like
Real-time stream understanding as the foundation. Continuously extracting what is currently being shown and discussed — product category, brand, price point, format such as auction or demonstration, energy and pace — turns an undescribed stream into a live feature vector, which is the input everything else needs.

Matching on current state rather than on stream identity. A viewer should be matched to a stream because of what is happening in it now, and the match should be re-evaluated as the stream moves on, which also creates a natural re-entry recommendation.

Intent inference within the session. Whether this viewer is shopping for something specific or browsing is inferable from their first few interactions, and it should change what is surfaced.

Supply-side objectives made explicit. Purely engagement-optimised ranking starves new and small sellers, which destroys the supply the marketplace depends on — so the ranking objective should include seller outcomes deliberately rather than discovering the consequence later.

Sell-through prediction to guide exploration. Estimating which streams will convert well lets the platform spend its limited exploration budget where it is likeliest to pay, for both the viewer and the seller.

## Impact If Solved
Discovery determines whether a stream sells, and whether a seller returns, which makes it the mechanism that grows or shrinks supply. Real-time content understanding is the missing input that would let matching work on what a stream actually is at this moment rather than on a title typed before it started.
