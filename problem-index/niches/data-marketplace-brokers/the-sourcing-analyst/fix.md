# The Evaluation Nobody Wrote Down

**Niche:** [[niches/data-marketplace-brokers/the-sourcing-analyst/profile|The Sourcing Analyst]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** A provider is evaluated and rejected for a specific reason, the reason is never recorded, and eighteen months later another analyst repeats the entire evaluation and reaches the same conclusion.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #worker-facing #automation #quick-win #compliance #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to give the analyst a reusable evaluation harness instead of a quarter spent rebuilding one — and whoever does that takes the account, because the same comparison is being constructed from scratch in every firm in the market.

## The Problem
An analyst evaluates eleven providers for a category, shortlists two, and buys one. The other nine were rejected for specific, durable reasons — this one covers only urban areas, that one's key field is sparse outside two states, another's refresh is quarterly despite the listing. None of that is recorded anywhere except the analyst's working notebook, which is deleted when they change laptops. Eighteen months later a colleague in another team evaluates the same category and repeats all eleven evaluations. The firm has paid twice for the same knowledge and will pay again.

## Why It's Still Broken
The output of an evaluation is a purchase decision, and once made, the supporting work looks like scaffolding. There is no system designed to hold it, so it lands in a notebook or a slide deck. Rejection reasons feel like negative information with no future use, which is exactly backwards. And the analyst who would benefit is a future colleague rather than the person doing the work.

## What a Fix Looks Like
Record the rejection as carefully as the purchase. Capture a structured rejection reason for every candidate — coverage gap, field sparsity, freshness, price, provenance, licence terms — at the moment of the decision, which is one field and is the entire precondition for reuse. Keep the full evaluation output, not just the conclusion, since a future analyst with different requirements may find the rejected provider suitable and the measurements are what tells them. Timestamp it and re-check on reuse, because a provider's coverage may have improved and a stale rejection should prompt a quick re-measurement rather than a permanent exclusion. Surface prior evaluations automatically when a provider is next considered, so the knowledge arrives without anyone having to remember it exists. Report rejection reasons in aggregate, which tells the firm what the market is systematically failing to supply and feeds the unmet-demand signal. Share the reason with the provider where appropriate, since a provider told their coverage failed can fix it and currently receives silence. Track how often a prior evaluation saved a repeat, which is what demonstrates the value. And make capture part of the harness rather than a separate discipline, because anything separate will not happen.

## Who Feels the Pain
Analysts repeating colleagues' work; firms paying repeatedly for the same conclusion; and providers rejected for fixable reasons nobody ever told them.

## Impact If Fixed
One structured field at the moment of decision is the entire precondition for reuse, and keeping the measurements rather than just the verdict is what lets a future analyst with different requirements benefit. Aggregate rejection reasons double as the market's unmet-demand signal.
