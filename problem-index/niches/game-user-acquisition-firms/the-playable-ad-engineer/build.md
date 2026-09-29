# Six Formats From One Source

**Niche:** [[niches/game-user-acquisition-firms/the-playable-ad-engineer/profile|The Playable Ad Engineer]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A complete game in five megabytes, six times, to a campaign deadline.
**Tags:** #worker-facing #workflow-orchestration #automation #optimization-fundamentals #evaluation-metrics #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to let one engineer build a complete small game to a five-megabyte budget in six network-specific formats on a campaign deadline — and whoever makes that tractable takes the account.

## The Problem
Building a playable ad means writing a small interactive game, fitting it inside a size budget that forces decisions on every asset, and then producing six variants for six networks with different packaging requirements, different APIs and different rules, most of which are documented inconsistently. The engineer does this per campaign, repeatedly, and every campaign's work is thrown away.

## Why Nobody Has Built This
The specialism is small and served by in-house teams and a few agencies. Network requirements change without notice, so tooling decays. The work is classified as creative production rather than as engineering. And each campaign's deadline prevents investment in the next one.

## What to Build
Build once, target many, and enforce the budget mechanically. Produce every network format from one source with packaging handled automatically, which is the core and removes the largest block of repeated work. Enforce the size budget continuously during development rather than discovering a breach at packaging, since late size problems force the worst compromises. Optimise assets automatically against the budget — compression, atlasing, audio, code size — which is mechanical and currently manual. Validate against each network's requirements before submission, as rejection late in a campaign is the costly failure. Maintain a shared component library of the mechanics that recur, because most playables are variations on a handful. Track each network's requirement changes centrally, which no individual engineer can keep up with. Instrument playables so their in-ad behaviour is measurable, which the creative team wants and rarely gets. Support rapid variant production for testing, since that is what the campaign actually needs. Keep a per-campaign record so the next one starts from the last. And make the size budget visible as a live number, which is the constraint that governs every decision.

## Target Customer
Playable ad teams and specialist agencies, mobile publishers, ad networks, and creative production tooling vendors.

## Impact If Built
A complete game in five megabytes, six times, per campaign, with every campaign's work discarded. One source targeting all formats with a continuously enforced budget is what makes the craft sustainable.
