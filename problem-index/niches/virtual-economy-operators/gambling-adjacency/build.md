# Owning the Infrastructure Question

**Niche:** [[niches/virtual-economy-operators/gambling-adjacency/profile|Gambling Adjacency]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The sites are third parties and the items, the trading rails and the audience are not.
**Tags:** #compliance #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to hold a defensible position on third-party sites that accept its items as stakes, when the items, the trading infrastructure and the audience are all the operator's — and whoever builds that position takes the account.

## The Problem
An ecosystem of third-party sites accepts game items as stakes for wagering. It has drawn litigation and regulatory action, and its participants have repeatedly included minors. The operator's stated position is that these sites are unauthorised and that it prohibits them in its terms. Meanwhile the items are issued by the operator, the trades that fund the wagering settle on the operator's infrastructure, the operator can see them, and the audience came from its game.

## Why Nobody Has Built This
Acting implies responsibility, and the current position depends on not having it. The trade volume is real revenue. Detection is straightforward but acting on it means restricting trades. And the legal position in most jurisdictions remains untested, which makes inaction defensible in the short term.

## What to Build
Measure it first, then decide deliberately rather than by default. Identify accounts trading with known gambling operators and quantify the volume, which is the core — an operator that has never measured this has chosen not to know, and the measurement is the decision point. Maintain and update the set of known destinations, which is public information the community tracks openly. Detect the characteristic trade patterns rather than relying only on a list, since sites rotate accounts. Apply controls proportionate to a chosen position — trade holds, restrictions, warnings, or nothing — but choose deliberately and write it down. Identify likely minor accounts specifically, as that is the sharpest element of the exposure and is partly inferable from existing signals. Measure the harm indicators available in the operator's own data: rapid inventory liquidation, repeated one-sided transfers to known destinations, account behaviour consistent with chasing. Provide a route for parents and players to restrict trading on an account, which costs almost nothing and is plainly right. Prepare a regulatory position with counsel in the jurisdictions that have acted, ahead of being asked. Publish what the operator does and does not do, since the current silence is itself a position. And accept that a chosen position with controls is more defensible than a disclaimer, which is the strategic argument the technical work supports.

## Target Customer
Virtual economy operators, legal and policy leadership, regulators and consumer protection bodies, and trust and safety vendors.

## Impact If Built
An operator that has never measured this has chosen not to know, and the measurement is itself the decision point. Quantifying the volume and identifying likely minors converts a disclaimer into a position that can be defended.
