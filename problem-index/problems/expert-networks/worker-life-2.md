# The Analyst With Thirty Calls and No Synthesis

**Industry:** [[expert-networks|Expert Networks]]
**Type:** Worker Life Changing
**One-liner:** A buy-side or diligence analyst runs dozens of expert calls in a sprint, ends up with dozens of transcripts and notes that disagree with each other, and reconciles them by rereading everything the night before the investment committee.
**Tags:** #large-language-models #transformers #word-embeddings #k-means-clustering #evaluation-metrics #worker-facing #workflow-orchestration

## The Problem
A private equity associate in a two-week diligence sprint, or a hedge fund analyst building a thesis on a company, books fifteen to forty calls across several networks: former employees, customers, competitors, distributors. Each call produces a transcript or the analyst's own notes. The same questions are asked in slightly different words; the answers disagree; some experts are clearly more informed than others; some statements are opinions and some are specific claims with numbers attached.

The analyst also searches transcript libraries for prior calls on the same company, adding dozens more documents written for different questions at different times.

The synthesis — what do customers actually think of the product, how do former employees describe the sales cycle, where do the experts disagree — is assembled by hand into a memo or a slide, by an analyst who is also building the model.

## Why It Matters to the Worker
This is the least-supported step in a research workflow and the one closest to the decision. The analyst carries the reconciliation in their head across late nights, rereads transcripts to find the quote they half-remember, and has no way to show their senior colleague how many experts supported a claim versus how many contradicted it.

They also cannot easily weight the sources. The former VP who left four years ago and the current customer who uses the product daily are presented as equals in a pile of transcripts.

## What a Solution Looks Like
A workspace that reads every call transcript and library document in a project, extracts the specific claims made, groups them by question, and shows agreement and disagreement with the source — expert role, tenure, recency, relationship to the company — beside each claim. Every statement in the synthesis is linked to the transcript lines that support it, so the memo can be checked rather than trusted.

Gaps are surfaced while there is still time to book another call: no customer in the mid-market segment has been spoken to; nobody has addressed the pricing change.

## Impact If Solved
Expert calls are among the most expensive primary-research inputs a research team buys, and their value is realised only in the synthesis. Making the synthesis traceable and incremental gives the analyst back the nights before the committee and gives the committee a memo whose evidence is visible.
