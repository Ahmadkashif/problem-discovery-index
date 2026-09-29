# Fourteen Paths to the Same Impression

**Niche:** [[niches/programmatic-ad-platforms/supply-path-and-inventory-quality/profile|Supply Path & Inventory Quality]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every buyer needs to know which of the fourteen paths to the same impression is real and which sites exist only to carry ads, and the tools that answer it score the open web generically rather than the buyer's own spend.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #descriptive-statistics #revenue-impact #confidence-intervals #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer which of the fourteen paths to the same impression is real and which sites exist only to carry advertisements — using that buyer's own spend rather than a generic score.

## The Problem
The same impression is offered to a buyer through fourteen routes: direct from the publisher's exchange, through three resellers, through a wrapper, through an intermediary reselling another intermediary. Each path has different fees, different latency, different fill and different legitimacy. The buyer bids on several simultaneously, sometimes against themselves, and has no view of which path delivered what. Their verification vendor tells them the site scored well in general. It does not tell them that eight percent of their own delivery last month went through a path that resells inventory of unclear origin, because it is not looking at their spend.

## Why Nobody Has Built This
Verification vendors sell a scored index of the web because it scales across customers, and a per-buyer analysis does not have the same economics — this is why the generic product exists and why it answers the wrong question. Path data is fragmented across the buyer's own logs, the exchanges and the supply-side platforms, and nobody joins it. Intermediaries have no interest in making their layer visible. And the buy side lacks the analytical capacity to do it themselves.

## What to Build
Analyse the buyer's own supply graph. Reconstruct every path the buyer's spend actually travelled, joining bid logs, exchange identifiers, seller declarations and delivery records, which is the foundation and is the thing no generic product can do. Compute path-level economics — the cost, the fees, the latency, the win rate and the outcome delivered per route to the same inventory — which immediately identifies the paths that should simply be switched off. Detect self-competition, where the buyer bids against themselves across routes and raises their own clearing price, which is common, expensive and invisible without a path view. Classify inventory by what it is rather than by a generic score, since made-for-advertising properties have identifiable structural signatures in traffic, layout, content velocity and monetisation density. Score against the buyer's own outcomes, because a site that performs for one advertiser and not another is the normal case and a universal score cannot represent it. Trace resold and rebrokered inventory through the chain, which is where origin becomes unclear and where the losses concentrate. Push conclusions into bidding as automatic path exclusions rather than into a report, since a quarterly finding changes nothing. Monitor continuously, as paths and intermediaries change weekly. Quantify recovered spend, which is the argument that funds the function. And give the buyer an auditable record, because these findings become commercial conversations with intermediaries and need evidence.

## Target Customer
Large advertisers and agency trading desks, demand-side platforms differentiating on supply quality, and the verification vendors whose generic product answers a different question.

## Impact If Built
A generic web score cannot say that eight percent of this buyer's delivery went through an opaque reseller. Reconstructing the buyer's own supply graph with path-level economics identifies routes to switch off immediately and exposes self-competition that raises their own clearing price.
