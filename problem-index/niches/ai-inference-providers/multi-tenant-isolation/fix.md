# Nobody Says What Is Actually Shared

**Niche:** [[niches/ai-inference-providers/multi-tenant-isolation/profile|Multi-Tenant Isolation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Customers do not know whether their requests run on dedicated or shared accelerators, what the isolation actually guarantees, or that a neighbour can move their latency — and no provider publishes it.
**Tags:** #compliance #evaluation-metrics #descriptive-statistics #confidence-intervals #worker-facing #quick-win #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to share an accelerator between tenants without one of them being able to affect another's latency — and whoever does that takes the account, because sharing is the only route to acceptable utilisation and the hardware was not built for it.

## The Problem
A team builds a product on an inference endpoint and plans capacity against the latency they measured. They do not know their requests share an accelerator with other tenants, that memory bandwidth is unpartitioned, or that a neighbour's batch job can add hundreds of milliseconds to their tail. Nothing in the documentation says so. When it happens they investigate their own code, their own prompt lengths and their own concurrency, and find nothing, because the cause is a customer they have never heard of. The information that would have saved the week is a paragraph the provider has chosen not to write.

## Why It's Still Broken
Disclosing shared tenancy and its consequences reads as a weakness, particularly against competitors who disclose nothing. There is no industry norm, so unilateral honesty is punished. Regulated customers who would ask are a minority. And the provider's own view of interference is anecdotal, so writing a precise statement would require measuring something they currently do not.

## What a Fix Looks Like
Write the paragraph, then back it with a tier. Publish the tenancy model per product tier — what is shared, what is partitioned, what is guaranteed — which costs nothing, is the minimum honest disclosure, and is the fix a customer most immediately benefits from. Offer a dedicated tier at a stated price, so the disclosure comes with a remedy rather than only a caveat. State the isolation guarantee in terms a customer can plan against: this tier's tail latency is bounded under co-tenancy, this one is not. Report co-tenancy interference in the customer's own metrics, so a latency excursion caused by a neighbour is visible as such rather than attributed to their code. Give customers a way to ask what happened during an excursion and get a real answer. Include tenancy in the compliance documentation, since regulated buyers have to know and are currently told nothing. Publish achieved service levels per tier rather than a single fleet number. And push for a disclosure norm across the industry, since the reason nobody discloses is that the first mover looks worse, and that is exactly the coordination problem a norm solves.

## Who Feels the Pain
Product teams debugging their own code for a neighbour's behaviour; regulated customers unable to document what they are running on; and providers whose genuinely better isolation is unrewarded because nobody discloses anything.

## Impact If Fixed
The paragraph costs nothing to write and would save customers weeks of misdirected investigation. Reporting co-tenancy interference in the customer's own metrics turns an invisible cause into a visible one, and a priced dedicated tier turns the disclosure into a choice.
