# Routing Guide Decay Measured Rather Than Discovered

**Niche:** [[niches/freight-brokerage/freight-procurement-consultancies/profile|Freight Procurement & Bid Consultancies]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bid produces a routing guide that is optimal on the day it is awarded and degrades from then on as carriers reject tenders, and nobody measures the decay until the next bid.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #evaluation-metrics #causal-inference #confidence-intervals #optimization-fundamentals #feature-engineering #data-integration #revenue-impact

## The Problem
A freight bid awards lanes to carriers at contracted rates, and the value of the award depends entirely on whether carriers actually accept the tenders afterward. They frequently do not — the market moves, a carrier's network changes, an award was priced too thin — and the shipper falls through the routing guide to more expensive backups or into the spot market. That gap between contracted rate and realized cost is the whole economic outcome of the engagement, and it is examined at the next bid, twelve months later, by which point the money is gone. The consultancy delivered an optimization and never learns how the optimization performed.

## Why Nobody Has Built This
Tender acceptance data lives in the shipper's transportation system after the engagement has closed, and nothing in a bid engagement contemplates collecting it. The analysis is also confounded — a rejection can reflect a bad award, a market swing, or a shipper's own tender behaviour — so a naive comparison of contracted to realized cost misattributes. And the engagement model is project-shaped: the firm is paid to run a bid, not to monitor a routing guide.

## What to Build
Post-award monitoring as a standing extension of the engagement. Tender acceptance is tracked against the awarded guide, with rejections attributed between award quality, market movement, and shipper tender behaviour using the firm's cross-client view of the same lanes and periods — which is the analysis a single shipper cannot perform. Realized cost against contracted cost becomes the reported outcome of the engagement rather than a number nobody computes. Accumulated across clients and cycles, that produces what the firm has never had: an empirical model of which award structures actually hold, by lane type, carrier profile, and market condition — so the next bid is designed against evidence rather than against the assumption that awarded means accepted. And decay monitoring is a recurring service in a business that is currently annual and lumpy.

## Target Customer
Practice leaders at freight procurement consultancies running 30-150 analysts, and the transportation leaders at shippers who discover their routing guide has failed when the freight bill arrives.

## Impact If Built
Turns a one-off optimization into a measured outcome and a recurring relationship. The award-durability model is also strictly proprietary — buildable only by a party that runs many bids and can see the same lanes across many shippers — and it directly improves the product the firm already sells.
