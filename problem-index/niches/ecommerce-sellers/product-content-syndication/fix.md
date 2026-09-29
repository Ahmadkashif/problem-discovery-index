# Retailer Specs Are Tribal Knowledge Held by Account Teams

**Niche:** [[niches/ecommerce-sellers/product-content-syndication/profile|Product Content & Syndication Operations]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Fix (Pain Point)
**One-liner:** What a retailer actually requires is known by the two people who work that account, and when they leave the provider relearns it through a season of rejections.
**Tags:** #tacit-knowledge-ml #bert #transformers #word-embeddings #evaluation-metrics #descriptive-statistics #k-means-clustering #data-integration #worker-facing #workflow-orchestration

## The Problem
Retailer relationships are staffed by small teams who accumulate, over years, the knowledge that makes submissions succeed: which fields this retailer really enforces, which contact resolves a stuck item, what the undocumented image requirements are, how the seasonal onboarding window actually behaves. None of it is written down in a form anyone else can use — the published specification is in a document, and everything that matters is not. The provider's ability to serve a retailer is therefore concentrated in individuals, which shows up as a quality cliff when someone leaves, as inconsistency between accounts, and as an inability to onboard a new retailer quickly because there is no template for what knowledge needs assembling.

## Why It's Still Broken
Account teams are measured on their own retailers' throughput, so time spent documenting for others' benefit is unrewarded. Retailer knowledge also changes continuously, which makes any static document stale fast enough to discourage maintaining it. And the knowledge is genuinely fragmented across specifications, rejection experience, relationship history, and workaround technique, so there has never been an obvious container for it.

## What a Fix Looks Like
A structured retailer profile maintained as a by-product of operations rather than as documentation. It holds the published specification alongside the observed enforcement model derived from submission outcomes, the undocumented requirements as discrete recorded facts with the evidence that established them, the operational calendar, and the escalation paths — each item versioned with when it was last confirmed, so staleness is visible rather than assumed away. Contributions come from resolving work: when an analyst diagnoses a rejection cause that is not in the profile, capturing it is one step in the workflow they are already performing. Across retailers the profiles become comparable, which surfaces something no one can see today — the common patterns beneath what looks like hundreds of unique specifications, which is what makes onboarding the next retailer cheap instead of expensive.

## Who Feels the Pain
Analysts inheriting accounts with no institutional knowledge; clients whose launches slip when an experienced account person leaves; the operations leader who cannot staff flexibly because knowledge is account-bound; and the growth plan, since onboarding a new retailer currently costs a season of learning.

## Impact If Fixed
Converts the provider's real expertise from personal to institutional, which is what allows flexible staffing and fast retailer onboarding. It also makes the enforcement model and the mapping layer possible, since both depend on knowing what a retailer actually requires — which today only two people know.
