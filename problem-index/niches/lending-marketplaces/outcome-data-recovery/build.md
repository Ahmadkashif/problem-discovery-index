# Data as a Condition of Participation

**Niche:** [[niches/lending-marketplaces/outcome-data-recovery/profile|Outcome Data Recovery]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision exists, the marketplace does not receive it, and no contract has ever required it.
**Tags:** #data-integration #workflow-orchestration #compliance #evaluation-metrics #revenue-impact #automation #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make returning the decision a condition of participating in the marketplace — and whoever changes that term first gets the feedback loop the whole category has been operating without.

## The Problem
Every complaint in the category traces to one missing field. Lenders complain about lead quality, which the marketplace cannot improve without knowing who was approved. Borrowers are routed badly, which cannot be fixed without the same data. Partner managers negotiate without evidence. The data is a few bytes per application sitting in the lender's loan origination system, and in most relationships nobody asked for it, because the contracts were written when the marketplace's product was a directory.

## Why Nobody Has Built This
The contracts predate the marketplaces' ambition to be a matching engine, so they simply do not contemplate outcome data — and renegotiating a live revenue relationship over a data field is a risk nobody with a quarterly number wants to take. Lenders see disclosure as giving away underwriting. No marketplace has offered enough in return to make it attractive. And the cost of not having it has never been quantified for either side.

## What to Build
Design the exchange so the lender wants to participate. Quantify what the missing data costs the lender — the wasted underwriting on unqualified applicants, the leads bought and declined — which is the core, because the argument must be made in the lender's interest rather than the marketplace's. Offer better-matched volume in exchange, since that is the only currency lenders care about and it is exactly what the data enables. Ask for the minimum field set — decision, reason band, terms offered, acceptance — rather than everything, because a small ask is negotiable and a large one is not. Tier participation on data contribution, so ranking preference is earned rather than only bought, which is the structural change. Protect the lender's criteria by taking aggregated or banded responses rather than raw rules, which removes the proprietary objection almost entirely. Build the pipeline to be trivially easy to send to, since integration effort is the excuse that ends most of these conversations. Start with the lenders who already send funding notifications, as they have the integration and the commercial alignment. Prove the value on a pilot and publish the result to the rest, because evidence from a peer is the most persuasive asset available. Consider an industry exchange where no single marketplace has leverage, as the collective-action framing may be the only workable one. And handle the fair lending and privacy implications explicitly, since decision data about applicants is sensitive and mishandling it would end the effort.

## Target Customer
Commercial and partner leadership, lender partnership teams, industry bodies who could convene an exchange, and data exchange vendors with no presence here.

## Impact If Built
The contracts predate the ambition and nobody renegotiates a live revenue relationship over a data field. Making the exchange valuable to the lender — better-matched volume for a banded decision — is the move that turns a refusal into a trade.
