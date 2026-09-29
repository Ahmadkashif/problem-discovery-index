# Underwriting Revenue Persistence

**Industry:** [[ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** High Impact
**One-liner:** Aggregators paid multiples on trailing earnings for brands whose performance rested on things that did not transfer with the sale, and the sector's contraction is the consequence of a prediction nobody made well.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #confidence-intervals #time-series-forecasting #hypothesis-testing #evaluation-metrics #revenue-impact

## The Problem
An aggregator buys a third-party marketplace brand for a multiple of its trailing twelve-month earnings. The thesis is that revenue continues and improves under professional management.

Frequently it declined instead, and the reasons are structural rather than incidental. The founding seller had a supplier relationship built over years that produced favourable terms and priority during shortages; the aggregator inherits a contract. The seller responded to reviews and customer messages within hours; a portfolio operator does not. Ranking momentum depended on a velocity of sales and reviews that a transition interrupts. The category had low competition when the trailing numbers were earned and three new entrants since. The product's demand was a pandemic artefact.

None of these appear in trailing earnings, which is what the price was set on.

Diligence looked at the marketplace's own reporting: sales history, advertising spend, inventory, review counts, returns. It did not have a way to distinguish a brand whose performance rested on transferable assets — a genuinely differentiated product, a defensible position — from one resting on the seller's own attention and relationships.

The sector wrote down a great deal of capital learning this, and the underwriting model that would have distinguished the two was buildable from data these firms were already collecting.

## Why It's Unsolved
The category grew too fast for the feedback loop. Acquisitions were made at pace with capital that had to be deployed, and the outcome of an acquisition is only visible eighteen months later — by which time hundreds more had been made on the same model.

Marketplace data is genuinely limited for this purpose. Seller Central reporting shows a seller their own performance and does not show competitive position, category dynamics, or how much of a ranking is defended by anything durable. The most important variables are outside the data room.

Transferability is the specific thing that was not modelled. Some drivers of performance move with the asset and some sit in the seller's head and relationships, and separating them requires diligence questions nobody was asking under time pressure in a competitive auction.

Selection effects made it worse. Sellers chose when to sell, and the rational moment is at peak performance — so the trailing twelve months systematically overstated the sustainable level, in a way that is well understood in other acquisition markets and was largely ignored here.

## What a Solution Looks Like
Post-acquisition outcomes as the training data. An aggregator with dozens of acquisitions has, for each, the pre-acquisition characteristics and the realised revenue trajectory afterwards — a directly supervised prediction problem that almost nobody built.

Transferability assessed explicitly. Which performance drivers depend on the seller personally is answerable through structured diligence — supplier concentration and contract terms, response time patterns, review velocity sources, ranking defensibility — and should be a scored dimension rather than a qualitative impression.

Competitive trajectory rather than a snapshot. Category entry rates, competitor listing growth and price trends over the trailing period tell you whether the earnings were achieved in an easy environment that has since changed, and this is observable from public marketplace data.

Peak detection. Whether trailing performance sits at an unusual high relative to the brand's own history is a straightforward time series question and directly adjusts the multiple.

Honest intervals on the projection. A revenue forecast with a range, and an explicit statement of what would have to be true for the low case, is what an investment committee needs and is not what a spreadsheet produced.

## Impact If Solved
The sector deployed billions on an underwriting model that did not predict the thing it was underwriting, and the correction destroyed a large share of that capital. Learning persistence from realised outcomes is a well-shaped supervised problem on data these firms already hold, and it is the difference between a durable roll-up strategy and a portfolio of decaying assets.
