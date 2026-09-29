# Portfolio Cross-Promotion Allocation

**Industry:** [[game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A publisher's own games are its cheapest acquisition channel, allocation between them is decided by whoever needs installs this quarter, and nobody models what moving a player from one title to another actually costs.
**Tags:** #convex-optimization #causal-inference #markov-decision-processes #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
A publisher with several live titles can promote them to each other's players. The traffic is free in cash terms and is the highest-converting inventory the publisher has, because the audience already plays games from this publisher and frequently in an adjacent genre.

It is not free in reality. A player moved from one title to another may reduce their spending in the first, may split their time across both, or may leave the first entirely. The transfer therefore has a cost that depends on the player's value in the source title, their likely value in the destination, and whether the two are complements or substitutes — and essentially nobody models it.

Allocation is decided politically. The title that needs installs, or whose manager argues most effectively, receives the cross-promotion inventory, and the source title absorbs whatever the transfer costs. In publishers where each title has its own profit and loss, this creates an internal conflict that is resolved by negotiation rather than by evidence.

And the targeting is coarse. Cross-promotion is typically shown broadly rather than to the players most likely to benefit the portfolio, which is a decision about which specific player should see which specific promotion and is a well-formed problem nobody poses.

## What Already Exists
Mediation platforms support house ads and cross-promotion placements. Publishers maintain cross-promotion calendars and negotiate allocation internally. Some larger operators run cross-promotion as a managed channel with its own metrics. Player identity is usually resolvable across a publisher's own titles through platform accounts or a publisher account system. Segmentation tooling exists on both sides.

## The Customisation Gap
The missing object is a portfolio-level objective. The publisher wants total revenue across all titles over a long horizon, and the allocation is currently made against per-title install targets — which is the classic case of optimising components of a system separately and getting a worse whole.

The transfer cost is estimable and unestimated. Randomised or staggered cross-promotion exposure gives a clean read on what a promotion does to the source title's revenue as well as the destination's, and that net effect — per player segment, per title pair — is the number the allocation should be made against. Every publisher has the data and the ability to randomise.

Complement versus substitute is the interesting finding waiting to be made. Two titles in different genres played at different times of day may be genuine complements where cross-promotion adds portfolio revenue; two in the same genre may be substitutes where it merely moves it. Which pairs are which is measurable and is currently assumed.

And per-player targeting is the direct application. Which player should see which promotion, given their value in the source, their predicted value in the destination and the substitution risk, is a constrained allocation problem with all the inputs available.

## Impact If Solved
Cross-promotion is the cheapest acquisition a publisher has and is allocated by internal negotiation against per-title targets, which reliably produces portfolio outcomes nobody chose. Measuring the transfer's net effect per title pair and segment, and targeting per player against a portfolio objective, converts an internal argument into an optimisation — and the complement-versus-substitute finding alone would change which titles a publisher promotes to which audiences.
