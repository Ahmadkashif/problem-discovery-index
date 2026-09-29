# The Match They Are Not Capturing

**Niche:** [[niches/robo-advisors/the-small-balance-client/profile|The Small-Balance Client]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The client is diligently contributing to a taxable account while leaving an employer match uncollected, and the platform can see both.
**Tags:** #quick-win #automation #evaluation-metrics #data-integration #revenue-impact #descriptive-statistics #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to deliver something worth having to a client whose fee revenue is a few dollars a year — and whoever makes that economically real owns the segment every competitor is quietly trying to grow out of.

## The Problem
A client contributes two hundred dollars a month to the platform. Their aggregated workplace plan shows a contribution rate below the employer match threshold. They are declining an immediate, guaranteed return in order to fund an account that charges them a fee. The platform can see the plan through aggregation, can see the contribution, and says nothing — because telling the client to send money somewhere else reduces the assets it manages.

## Why It's Still Broken
The advice scope was drawn around the platform's own accounts, so a recommendation pointing money elsewhere sits outside it by construction — and the commercial disincentive meant nobody challenged the boundary. Plan match details are not captured. The finding requires joining aggregation data to contribution behaviour, which no one owns. And nothing measures how often it occurs.

## What a Fix Looks Like
Detect it and say it. Ask the client their plan's match terms, which is the fix and is one question most clients can answer. Detect contributions to the platform alongside an unfilled match, since the join is straightforward once the terms are known. Tell the client plainly what the match is worth, because the number is large, immediate and almost always decisive. Report how many clients are in this position, which will be a larger figure than expected and is the argument for acting. Accept the short-term asset impact deliberately, as the retention and trust effect of giving obviously correct advice is the stronger position. Extend the same logic to high-interest debt, since it is the other case where contributing is plainly wrong. Re-check after job changes, because plan terms change and the client will not think to update. Make the recommendation act-on-able with a link and instructions, as the gap between knowing and doing is where this fails. Track how many clients act, which is both a product metric and a proof the advice lands. And say it once clearly rather than burying it in education content, because this is the single most valuable thing the platform can tell this client.

## Who Feels the Pain
Clients giving up guaranteed money; the segment the category was founded to serve; and platforms whose advice is constrained by where the assets sit.

## Impact If Fixed
The advice scope was drawn around the platform's own accounts by construction and the commercial disincentive kept anyone from challenging it. One question about match terms plus a join the platform can already make identifies the largest available gain for this segment.
