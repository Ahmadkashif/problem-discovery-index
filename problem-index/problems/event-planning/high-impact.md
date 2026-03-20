# Event Budget Estimation and Scope Management

**Industry:** [[event-planning|Event Planning]]
**Type:** High Impact
**One-liner:** Planners quote within 5% on the first consultation instead of discovering the budget gap three months into planning — because the model reads the real scope behind the client's vision.
**Tags:** #gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #revenue-impact

## The Problem
When a client describes their event vision — "rustic chic barn wedding, 200 guests, craft cocktails, live band, autumn theme" — an experienced planner mentally prices every implied element: the barn venue costs $8K-$15K, craft cocktails for 200 means $35-$50/person ($7K-$10K), a live band runs $3K-$8K, autumn floral is premium ($6K-$10K), and they haven't mentioned lighting, rentals, stationery, transportation, or day-of coordination. The real budget is $60K-$90K, but the client says "$40K." An experienced planner manages this gap immediately, resetting expectations or adjusting scope. A new planner takes the client at their word, plans to $40K, and spends three months discovering that nothing in the vision fits the budget — destroying the relationship and the planner's margin.

## Why It's Unsolved
The translation from "vision language" to "budget reality" requires deep market knowledge (what things actually cost in this specific market), client-reading skill (distinguishing must-haves from nice-to-haves), and pattern matching across hundreds of past events. These costs vary dramatically by region, season, guest count, and venue type. No database maps "rustic chic barn wedding" to a reliable cost range because the definition of "rustic chic" varies by client. The experienced planner has calibrated their internal model through years of final invoices — knowledge that's tacit and market-specific.

## What a Solution Looks Like
A budgeting tool that takes event parameters (type, guest count, style descriptors, venue category, season, market/city) and generates a detailed budget estimate by category with ranges (optimistic/expected/premium). The model learns from actual event costs, calibrated to specific markets. During consultation, the planner inputs the client's vision and immediately sees: "This event typically costs $75K-$95K in the Austin market. At your $40K budget, here's what's feasible: [adjusted scope]." Scope-to-budget tradeoff visualization lets the planner walk the client through decisions in real-time.

## Impact If Solved
Eliminates the #1 cause of planner-client conflict (budget-vision mismatch). Enables new planners to quote with confidence on day one instead of after two years of expensive learning. Reduces scope-creep-driven margin erosion by establishing realistic budgets upfront. Increases client satisfaction by setting expectations early rather than disappointing late.
