# Bid/No-Bid Decision Waste

**Niche:** [[niches/general-contractors/estimating-bidding/profile|Estimating & Bidding Operations]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** GCs stop wasting 40-80 hours estimating projects they have no realistic chance of winning — because a scoring model predicts bid competitiveness before the full estimation investment.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact

## The Problem
A typical GC bids on 50-200 projects per year and wins 10-20%. Each bid requires 40-80 hours of estimator time for takeoff, pricing, and proposal preparation. That means 80-90% of estimation effort produces no revenue. Some of these losses are inevitable — competitive bidding means someone has to lose. But many are avoidable: the GC bid a project type they don't win (hospitals when their strength is office), in a geographic area where they have no subcontractor relationships, against an incumbent with a relationship advantage, or at a price point outside their competitive range. Experienced estimators and business development managers intuitively avoid some of these poor-fit bids, but the firm still chases too many opportunities because the cost of saying "no" (missing a potential win) feels higher than the cost of estimating (which is treated as overhead rather than a direct cost).

## Why It's Still Broken
No tool helps GCs analyze their historical win/loss patterns to identify which project characteristics predict competitive advantage. The data exists — every GC knows which bids they won and lost, the project type, size, owner, architect, and competing bidders — but it sits in CRM notes, bid log spreadsheets, and the business development manager's memory. Nobody has structured this data into a model that answers: "Given our win rate for this project type, size, location, and owner, what's our probability of winning this bid?" Construction CRMs (Cosential, Unanet) track bid history but don't analyze patterns. Generic CRM tools (Salesforce) can theoretically model win probability but require extensive customization for construction bidding dynamics (where the relationship web of owner/architect/CM/competing GCs determines outcomes as much as price).

## What a Fix Looks Like
A bid scoring tool that uses the GC's historical bid data to predict win probability for each new opportunity. Inputs: project type, size, location, owner, architect, construction manager (if CM-at-risk), known competitors, and whether the GC has prior work with the owner/architect. The model identifies patterns: "We win 35% of office TI bids under $2M but only 8% of hospital bids over $5M" or "We win 52% of bids where we've worked with the architect before vs. 12% with new architects." Each new opportunity gets a win probability score with the key factors driving it. The estimating team uses this to prioritize: full estimation effort on high-probability bids, abbreviated estimates on medium-probability bids, and a quick decline on low-probability bids. Over time, the model improves as new bid outcomes are logged.

## Who Feels the Pain
Estimators who spend 60+ hours per week on takeoffs during bid season, knowing that 80% of their work will be wasted. GC owners who see $200K-$500K in annual estimating labor costs producing diminishing returns because the team is spread too thin across too many bids, reducing quality on every estimate.

## Impact If Fixed
Redirecting estimation effort from low-probability to high-probability bids can improve win rates by 20-40% without increasing estimation capacity. For a GC spending $300K annually on estimating labor, reducing wasted bids by 30% recovers $90K in direct cost and allows deeper, more competitive estimates on the remaining opportunities. More importantly, it reduces estimator burnout during bid season by eliminating futile work.
