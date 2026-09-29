# Ranking on the Outcome Instead of the Click

**Niche:** [[niches/lending-marketplaces/borrower-routing/profile|Borrower Routing]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model that decides which lender a borrower sees is trained on whether they clicked, which is several steps removed from whether anything good happened.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals #matrix-decompositions #revenue-impact #hypothesis-testing #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to send each borrower to the lender who will actually approve them on the best terms — and the contest splits cleanly enough that it is not terminal.

## The Problem
Ranking is optimised against click-through weighted by bid. A borrower clicks based on a rate table entry and a brand they recognise, neither of which predicts whether that lender will approve them. The result is a system that maximises the handoff and is indifferent to the decline that follows. Lenders respond by complaining about lead quality, the marketplace responds with volume, and the borrower is the only party who pays in credit inquiries and wasted time.

## Why Nobody Has Built This
The click is the signal that returns, so the model was built around it — and once an objective is instrumented, everything optimises to it regardless of what it measures. Outcome data is contractually absent from most lender relationships. Revenue is earned at the handoff, which removes the commercial pressure. And nobody has defined what a good routing outcome even is, which means there is no target to move toward.

## What to Build
Change the objective and the feedback. Define the routing outcome explicitly — approved, on terms the borrower accepted, on a loan that performed — which is the core and is a definitional step the category has never taken. Predict approval probability and offered terms per lender per borrower, which is the inference half and is tractable even with partial data. Change what comes back by making the decision a condition of participation, which is the commercial half and is where the leverage actually is. Model selection bias explicitly, since outcomes are observed only for the borrowers who were routed and the naive model will be badly wrong. Rank on expected borrower outcome with bid as a component rather than as the objective, because the marketplace can still be paid while optimising for something real. Use the cross-lender view as a substitute signal where outcomes are missing, since a borrower who reappears shopping the next week probably did not get funded. Measure routing quality as a reported metric, as a function with no quality measure will drift to whatever is measured instead. Run routing experiments, because the counterfactual — what would have happened at a different lender — is only obtainable deliberately. Report approval rate per lender per profile back to lenders, which is the argument that makes them supply data. And align the revenue model with funded outcomes where possible, since the incentive is the root cause.

## Target Customer
Data and product leadership, lenders paying for leads that decline, borrowers routed to lenders who will not approve them, and marketplace technology vendors ranking on clicks.

## Impact If Built
Once the click was instrumented as the objective, everything optimised to it regardless of what it measures. Defining the routing outcome and predicting approval is the half the marketplace can do alone; changing what lenders return is the half that changes the category.
