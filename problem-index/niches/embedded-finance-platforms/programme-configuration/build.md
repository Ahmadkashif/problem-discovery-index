# The Twenty Archetypes

**Niche:** [[niches/embedded-finance-platforms/programme-configuration/profile|Programme Configuration]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nearly every new programme is a variation on one of about twenty shapes, and each is configured from primitives as though it were the first of its kind.
**Tags:** #workflow-orchestration #automation #optimization-fundamentals #sets-and-logic #compliance #k-means-clustering #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn the twenty programme archetypes that keep getting rebuilt by hand into configurable starting points that carry their bank-specific constraints with them — and whoever does it takes launch time from months to days.

## The Problem
A company wants to give its drivers instant payouts with a spending card. Another wants teen accounts with parental controls. Another wants a business expense product with receipt capture. These are not novel financial products — the platform has built each of them ten times — and each one starts from account primitives, card primitives, limit primitives and a compliance ruleset assembled from scratch. The decisions that matter were made before, by someone who has since left, and the record of them is a configuration in production that nobody reads as a template.

## Why Nobody Has Built This
The platform sells primitives and flexibility, so archetypes felt like a constraint on the product rather than an accelerant — the composability was the pitch, and packaging it looked like giving it up. Bank constraints differ per sponsor, which makes a portable archetype harder than it looks. Implementation revenue rewards duration. And nobody mined the existing programmes to discover what the archetypes actually are.

## What to Build
Derive the archetypes and make them portable. Cluster the live programmes by their configuration to discover the real archetypes empirically rather than assuming them, which is the core and is computable today from what every platform already holds. Express each archetype as a parameterised configuration with its decisions explicit, since the value is in the decisions rather than in the settings. Model each sponsor bank's constraints formally so an archetype can be instantiated against a specific bank and validated, which is what makes the library portable and is the hardest and most valuable part. Validate at configuration time rather than at bank review, because discovering an incompatibility months later is the single largest source of launch delay. Carry the compliance ruleset with the archetype, since the monitoring calibration is part of the product shape and is currently set separately or not at all. Record why each archetype's decisions were made, so the template teaches rather than just copies. Diff a proposed programme against its archetype, which makes the genuinely novel parts visible and focuses review on them. Version the archetypes as regulation and bank policy change, because a library that ages silently is worse than none. Surface which archetype a new request most resembles, so the conversation starts from a shape. And measure launch time by archetype, which is the number the business cares about.

## Target Customer
Platform implementation and product leadership, fintech programme teams launching their first product, and sponsor banks whose review queues are full of incompatible proposals.

## Impact If Built
Composability was the pitch, so packaging it looked like giving up the product. Clustering live programmes reveals the archetypes empirically, and binding them to a formal model of each bank's constraints is what turns months into days.
