# Advertising and Organic Optimised Apart

**Niche:** [[niches/ecommerce-aggregators/marketplace-ranking-and-advertising/profile|Marketplace Ranking & Advertising]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Fix (Pain Point)
**One-liner:** Advertising is managed to a return target and organic ranking is somebody else's concern, and they are the same system — so cutting advertising to hit a margin target quietly destroys the rank that the margin depended on.
**Tags:** #causal-inference #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact #convex-optimization #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this sub-niche is fighting to hold organic position and advertising efficiency against sellers who watch one brand full-time — and whoever does that keeps the revenue, because ranking is the asset that was bought and it decays under inattention.

## The Problem
A portfolio needs margin, so advertising spend is cut to hit the target. Advertising-driven sales fall, which is expected. What was not modelled is that those sales contributed to the sales velocity the marketplace's ranking uses, so organic position slips over the following weeks, organic sales fall too, and the brand now needs more advertising than before to hold a worse position. The margin improvement reverses within a quarter and the ranking does not come back easily. The two systems are one system, they are managed by different targets, and the interaction is known anecdotally and modelled nowhere.

## Why It's Still Broken
Advertising return is measurable immediately and the organic consequence arrives weeks later, so the fast metric governs. The marketplace does not report the relationship and treats its algorithm as proprietary. Cutting advertising is the most available lever when a margin target is missed. And the reversal is attributed to market conditions because the causal chain spans weeks.

## What a Fix Looks Like
Model the loop and optimise against it. Estimate the relationship between advertising-driven sales, sales velocity and organic rank empirically from the portfolio's own history, which is achievable across dozens of brands and many listings where a single seller has too little data — this estimate is the fix and it turns an anecdote into a constraint. Optimise advertising against total contribution including the organic effect rather than against advertising return in isolation, which changes the answer materially in competitive categories. Treat the ranking position as an asset with a value and a decay rate, so cutting spend is priced as depleting an asset rather than as saving a cost. Report organic and paid sales together per listing with their trend, so a shift between them is visible. Test spend reductions on a subset before applying them across the portfolio, since the effect differs by category and the portfolio structure makes the test easy. Model the recovery cost, since regaining a lost position is more expensive than holding it and that asymmetry should govern the decision. Warn when a proposed cut would put a listing below a rank threshold where the decline accelerates. And set advertising targets at portfolio level over a horizon rather than per brand per month, since the monthly per-brand target is what forces the destructive cut.

## Who Feels the Pain
Operators whose margin improvement reverses with interest; brand managers blamed for a decline caused by a budget decision; and investors whose portfolio value declined through an interaction nobody modelled.

## Impact If Fixed
The two systems are one system managed by two targets, and the destructive interaction is known anecdotally and modelled nowhere. A portfolio can estimate the loop empirically where a single seller cannot, which turns an anecdote into a constraint on the budget decision.
