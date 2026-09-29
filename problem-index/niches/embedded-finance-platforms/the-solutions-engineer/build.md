# Extracting What They Know

**Niche:** [[niches/embedded-finance-platforms/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The knowledge that makes a regulated product launch succeed lives in a handful of people's heads and is transmitted one call at a time.
**Tags:** #tacit-knowledge-ml #large-language-models #workflow-orchestration #automation #worker-facing #sets-and-logic #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to get the regulated-product knowledge a solutions engineer carries in their head into a form a first-time developer team can use without them — and whoever extracts it turns the category's scarcest people into leverage instead of a bottleneck.

## The Problem
A developer team building their first financial product does not know that the account structure they have designed will not support the dispute flow, that the fee they intend to charge needs a disclosure the bank will want to see, that the identity verification step they treated as a formality determines what the programme can do later, or that the reconciliation they have not thought about is the thing that will wake them at night. The solutions engineer knows all of it and tells them, on calls, over months, one team at a time.

## Why Nobody Has Built This
The knowledge is tacit — held as judgement about what usually goes wrong — and nobody attempted to extract it because it never looked like a documentable thing. It is also bank-specific and partly commercially sensitive, which discourages writing it down. Solutions engineering is staffed as a cost of sale rather than treated as a product surface. And the calls happen, so the pressure to systematise never arrives.

## What to Build
Extract the tacit knowledge and deliver it at the decision point. Mine the existing corpus — implementation Slack channels, call notes, support tickets, past review findings — for the recurring guidance, which is the core and is a large, real body of evidence that every platform already has and none has read as a whole. Identify the decisions that are expensive to change later and surface them at the start, since the value is almost entirely in timing rather than in content. Attach guidance to the API surface where the decision is actually made, because documentation read in advance is documentation not read. Encode the bank-specific constraints alongside the general ones, which is the part that only exists in people's heads. Warn on the design that usually fails review, since the same mistakes recur across teams. Tell a developer what they have not considered, because the hardest part of a first regulated build is the unknown unknowns and no documentation format addresses them. Keep the solutions engineer in the loop for the genuinely novel, so the extraction raises the floor rather than replacing the role. Capture new guidance as it is given, which makes the corpus self-maintaining instead of a one-time project. Version guidance against bank policy change, since stale advice here is actively harmful. And measure questions asked and launch failures avoided, which is how the leverage shows up.

## Target Customer
Platform solutions and developer experience leadership, first-time fintech builders, and developer platform vendors for whom regulated-build guidance is uncharted.

## Impact If Built
The knowledge is tacit and nobody tried to extract it because it never looked documentable. The implementation channels, call notes and review findings are a substantial corpus, and mining them is the first time the category's scarcest expertise becomes reusable.
