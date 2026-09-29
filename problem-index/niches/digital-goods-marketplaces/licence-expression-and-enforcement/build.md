# Terms Nothing in the System Can Read

**Niche:** [[niches/digital-goods-marketplaces/licence-expression-and-enforcement/profile|Licence Expression & Enforcement]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every purchase carries licence terms in prose, no part of the delivery path knows what they say, and neither the buyer who wants to comply nor the creator whose terms were exceeded can establish what was permitted.
**Tags:** #compliance #workflow-orchestration #automation #large-language-models #evaluation-metrics #data-integration #revenue-impact #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make a licence something the delivery path can read and check rather than prose in an agreement — and whoever does that lets compliance happen by default instead of by goodwill.

## The Problem
A studio buys nine assets for a client project over eighteen months. Three were personal-use, four commercial, one commercial with a circulation cap, one from a creator whose terms changed after purchase. The project ships. Nobody in the studio can say which asset had which terms, because the terms were prose in nine separate agreements that nobody kept and nothing in any tool records. When a creator later objects, neither side can establish what was permitted — the buyer cannot prove compliance and the creator cannot prove breach. The entire licensing layer, which is what is actually being sold, exists only as text nobody reads.

## Why Nobody Has Built This
Licences are drafted by lawyers as prose and the category never translated them into anything else. Machine-readable licensing requires a standard vocabulary that no marketplace can establish alone, which is a coordination problem rather than a technical one. Enforcement at point of use means reaching into the buyer's tools, which no platform has attempted. And ambiguity favours the platform, which avoids adjudicating.

## What to Build
Make the licence a structured, portable, checkable object. Define an enumerated grant vocabulary — use context, distribution scale, modification rights, redistribution, sublicensing, duration, territory, attribution — which covers the overwhelming majority of real terms and is the prerequisite for everything else in this niche. Attach the structured grant to the entitlement and to the delivered files, so the terms travel with the asset instead of living in an email. Embed a durable identifier in the file itself, which is what lets an asset found later be traced to a licence and is the mechanism underneath both compliance and enforcement. Express the terms to the buyer as a few plain statements rather than as an agreement, since a buyer who cannot state their obligations in one sentence will not meet them. Check use at the point it happens through tool integrations, which is where compliance either occurs or does not and is the step nobody has built. Offer the upgrade at the moment of the exceeding use, because most breaches are scope changes on a live project and a buyer told at the right moment will usually pay — this is the revenue argument that funds the whole thing. Keep a durable compliance record both parties can rely on, which is what turns a dispute into a lookup. Handle term changes with proper grandfathering, since creators do change terms and current practice leaves buyers exposed retroactively. Support team and organisation entitlements, because the individual-purchase model does not match how studios actually work and is a major source of inadvertent breach. And standardise across marketplaces, since buyers assemble projects from several and a single-platform vocabulary solves a third of the problem.

## Target Customer
Digital goods marketplaces, the studios and agencies assembling projects from many sources, and creators whose terms are unenforceable in practice.

## Impact If Built
What is actually being sold is a licence, and it exists only as prose nobody reads or retains. A structured grant vocabulary attached to the entitlement and embedded in the file turns compliance into a lookup and makes the scope-change upgrade a revenue event rather than a dispute.
