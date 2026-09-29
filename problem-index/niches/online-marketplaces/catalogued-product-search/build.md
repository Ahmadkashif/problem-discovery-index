# Ranking for the Click Rather Than the Outcome

**Niche:** [[niches/online-marketplaces/catalogued-product-search/profile|Catalogued Product Search]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Offers are ranked to maximise the chance of a purchase and not the chance of a satisfied buyer, which puts the cheapest risky offer above the slightly dearer reliable one.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #survival-analysis #revenue-impact #hypothesis-testing #cross-validation
**Contested on:** Every serious competitor in this sub-niche is fighting to put the offer a buyer will actually be happy with at the top for an item they already named — and whoever does that takes the transaction, because the same item is one tab away on another marketplace.

## The Problem
A buyer searches for a specific camera model. The top offer is the cheapest, from a seller with a thin history, described as excellent condition, shipping from far away. It converts well, because price ranks first in a buyer's attention. A third of these purchases end in a return, a dispute or a disappointed buyer who never comes back, and the marketplace counts the conversion in its ranking metrics and the churn in a separate report. The signal needed to rank for satisfaction rather than for purchase — return rates, dispute rates, repeat purchase, review sentiment by seller and condition claim — is all held and is not in the objective.

## Why Nobody Has Built This
Conversion is immediate and satisfaction arrives weeks later, so the fast signal wins the optimisation. Ranking teams are measured on conversion and revenue per search. Downranking cheap offers looks like harming buyers in the moment and raising take-rate-weighted revenue, which invites suspicion. And the buyer who quietly stops returning is not attributed to a ranking decision made six months earlier.

## What to Build
Rank for the outcome. Predict post-purchase satisfaction per offer — return probability, dispute probability, review sentiment, repeat purchase — from the seller's history, the condition claim, the price relative to the item's distribution and the shipping profile, which is a well-posed problem with abundant delayed labels and is the core of the build. Put predicted satisfaction in the ranking objective alongside conversion, with the weighting stated, so the trade is a deliberate decision rather than an artefact of which signal arrives first. Rank on total cost including shipping, taxes and expected return cost, since a buyer compares totals and a ranking on item price alone is systematically misleading. Report the satisfaction consequences of ranking changes, which requires waiting for the delayed labels and is the discipline that makes this real. Measure sponsored placement's effect on buyer outcomes and disclose it, since paid position that degrades satisfaction is a long-run cost the sponsorship revenue does not cover. Show the risk to the buyer rather than hiding it, since a buyer told that this offer is cheaper with a higher return rate can choose, and that transparency is a better product than a silent downrank. Correct product matching errors, which put the wrong offers under an item and are a large and mechanical source of disappointment. And measure repeat purchase as the ranking team's north star, because it is the only metric that captures both halves.

## Target Customer
Marketplace ranking teams, the operators whose buyer retention depends on this, and the reliable sellers currently outranked by cheaper risk.

## Impact If Built
Conversion arrives in seconds and satisfaction in weeks, so the fast signal wins an optimisation nobody decided to make. Predicting satisfaction from delayed labels the platform already holds, and ranking on total cost, are what align the objective with the business.
