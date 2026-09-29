# Ranking Explanation

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a freelancer whose placement moved can be told why, in terms specific enough to act on and stable enough to be worth acting on.

## Profile
**Market Size:** ~$1.46B — 40% of the ranking and allocation niche
**Share of Parent Industry:** ~10% of platform-intermediated gross services volume
**Digital Adoption:** Very low — every platform ranks algorithmically and none explains an individual placement
**Target Buyer:** Platform product and trust leadership; freelancer support organisations; worker advocacy groups and, increasingly, regulators
**Automation Potential:** High — the explanation is computable from the ranker's own scoring at the moment it ran

## What Makes This a Distinct Niche

The parent niche asks whether a ranking allocates work well. This half asks a narrower and much more uncomfortable question: can the platform tell an individual freelancer why they are where they are?

The distinguishing property is who the output is for. Every other piece of ranking work serves the platform's own quality objective. An explanation serves the person being ranked, and serves them specifically at the moment they are losing. It has to be per-account rather than per-model, it has to name factors the person can actually change, and it has to be truthful about the ones they cannot — that the category got more crowded, that a competitor lowered their rate, that the model was retrained.

It is also the half where the platform's interests and the freelancer's diverge most sharply, because an explanation that is specific enough to act on is specific enough to optimise against. That tension is not incidental to the niche; it is the niche.

## Current Tools & Gaps

Feature attribution methods are mature and cheap — Shapley-value attributions over a gradient-boosted ranker are a solved engineering problem, and the platform already computes the scores the attribution would run on. Nothing technical stands in the way.

What exists in production instead is a tier badge, a response-rate percentage and a help article. Some platforms surface a "profile completeness" score, which is an explanation of a thing that barely affects ranking, offered in place of an explanation of the things that do. The gap between what is computable and what is shipped is close to total, and it is a product decision rather than a capability limit.

## Problems
- [[niches/freelance-marketplaces/ranking-explanation/build|🔨 Build: Per-Account Placement Attribution]]
- [[niches/freelance-marketplaces/ranking-explanation/buy|🛒 Buy: Model Explainability Tooling Adapted to a Ranked Person]]
- [[niches/freelance-marketplaces/ranking-explanation/fix|🔧 Fix: The Help Article as the Answer to Every Ranking Question]]
