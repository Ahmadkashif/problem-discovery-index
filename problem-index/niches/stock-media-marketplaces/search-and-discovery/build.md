# Ranking on What Buyers Licensed

**Niche:** [[niches/stock-media-marketplaces/search-and-discovery/profile|Search & Discovery]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The ranking decides which contributors earn and it is optimised on clicks rather than on whether the buyer's brief was satisfied.
**Tags:** #contrastive-learning #matrix-decompositions #evaluation-metrics #confidence-intervals #causal-inference #gradient-boosting #revenue-impact #transformers
**Contested on:** Every serious competitor in this niche is fighting to return the asset a buyer actually wanted from a library of hundreds of millions — and whoever ranks on what buyers licensed rather than on what they clicked decides which contributors earn anything.

## The Problem
A buyer arrives with a brief: an image of a particular kind of person doing a particular thing in a particular style, usable commercially, in the right orientation. They type a few words. The ranking returns results optimised to be clicked, which favours the striking, the familiar and the already-popular, and the buyer scrolls, refines, and often settles. Meanwhile the asset that would have satisfied the brief exactly may be unfindable because its contributor keyworded it badly, and it earns nothing.

## Why Nobody Has Built This
Click and download signals are abundant and satisfaction is not, so the objective followed the available data — a ranking optimised on the plentiful signal will drift from the outcome that matters. The brief behind a query is mostly unstated. Subscription licensing weakened the purchase signal, since a download costs the buyer nothing marginal. And the contributor-side consequence of ranking is not anyone's metric.

## What to Build
Optimise for the satisfied brief. Define the outcome as an asset that was licensed and used rather than clicked, which is the core and requires the signals that indicate genuine selection rather than browsing. Model the brief behind the query, since a few words stand in for a specification and the refinement sequence reveals it. Use the full search session rather than the single query, as the sequence of refinements is the richest statement of intent available. Handle the subscription problem explicitly, because a costless download is a weak preference signal and the ranking is currently trained on it. Rank on satisfaction rather than popularity, which is what gives a well-matched new asset a chance against a familiar one. Solve the cold start for new contributors, since an asset with no history cannot compete and the resulting concentration is self-reinforcing. Suppress near-duplicates in results, as they crowd out variety and waste the buyer's attention. Use the abandoned and zero-result searches as demand evidence, which connects to the commissioning work. Measure the contributor-side distribution of exposure, because the ranking is an income allocation mechanism and is unexamined as one. And evaluate with real buyer briefs rather than click-through, since the current evaluation measures the thing being optimised rather than the thing that matters.

## Target Customer
Product and search leadership, buyers with specific briefs, contributors whose work is unfindable, and search technology vendors serving media libraries.

## Impact If Built
A ranking optimised on the plentiful signal drifts from the outcome that matters, and clicks are plentiful. Modelling the brief behind the query and ranking on satisfied selection changes who earns in a library where the ranking is the economy.
