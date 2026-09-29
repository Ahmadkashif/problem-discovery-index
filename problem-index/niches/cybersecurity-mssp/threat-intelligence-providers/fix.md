# Attribution Reasoning Lives in the Analyst Who Made the Call

**Niche:** [[niches/cybersecurity-mssp/threat-intelligence-providers/profile|Threat Intelligence Providers]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Fix (Pain Point)
**One-liner:** Linking infrastructure or a campaign to a named actor is the most consequential judgment the firm makes, and the chain of evidence behind it is retained as a conclusion in a published report.
**Tags:** #graph-neural-networks #graph-theory #bert #transformers #large-language-models #evaluation-metrics #word-embeddings #tacit-knowledge-ml #data-integration #worker-facing

## The Problem
Attribution decisions accumulate into the actor profiles that are the product's spine. Each one rests on a chain — infrastructure overlap, tooling similarity, operational tradecraft, timing, targeting pattern — weighed by an analyst who decides it is enough. The chain is described in the published report to the extent it can be without exposing collection, and it is not retained as a structured record. Two consequences follow. When new evidence contradicts an earlier link, nobody can identify which downstream assessments depended on it, so a revised attribution does not propagate and profiles accumulate contradictions. And when the analyst who built an actor profile leaves, the profile becomes a set of assertions their successor cannot interrogate — so it is neither revised nor confidently defended, and attribution quality degrades in a way nobody can see.

## Why It's Still Broken
Attribution reasoning is sensitive: it reveals collection capability, so there is a genuine and correct instinct to publish conclusions rather than chains. That instinct has been applied to internal records too, where it does not apply. The knowledge graph systems in use are also built to hold entities and relationships rather than the evidence and inference behind them, so there is nowhere for a chain to live. And attribution is treated as the highest expression of analyst craft, which has made systematic capture feel like a diminishment of the analyst rather than a preservation of their work.

## What a Fix Looks Like
Attribution as a structured internal record with the evidence chain retained: which observations supported the link, how each was weighted, what alternative explanations were considered and rejected, the analyst's confidence, and the standing trigger — what evidence would overturn it. Access-controlled so that collection-sensitive detail stays internal while the conclusion publishes as it does today. Once chains exist, revision propagates: contradicting one observation surfaces every assessment that leaned on it, which is impossible now. Consistency between analysts on comparable evidence becomes measurable. New analysts inherit reasoning rather than assertions. And the accumulated chains make the firm's own attribution methodology inspectable, which matters increasingly as attribution claims are challenged publicly and occasionally in legal proceedings.

## Who Feels the Pain
Analysts inheriting profiles they cannot interrogate and therefore do not revise; intelligence leadership with no way to measure attribution consistency or to propagate a revision; clients acting on actor attributions whose basis they cannot see; and the firm, whose most reputationally exposed output is defended by the recollection of whoever made the call.

## Impact If Fixed
Preserves the firm's most valuable and most personal expertise as an institutional asset, and makes the actor profiles — its central intellectual property — revisable rather than merely accumulative. It is also the precondition for scoring assessments, since a claim cannot be evaluated until the reasoning behind it is recorded.
