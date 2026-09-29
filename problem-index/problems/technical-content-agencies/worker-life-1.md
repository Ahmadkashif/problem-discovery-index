# The Writer Chasing an Engineer for Review

**Industry:** [[technical-content-agencies|Technical Content Agencies]]
**Type:** Worker Life Changing
**One-liner:** A technical writer cannot ship until an engineer confirms the details are right, and the engineer has a sprint commitment that documentation review is not part of.
**Tags:** #large-language-models #bert #gradient-boosting #transformers #evaluation-metrics #worker-facing #workflow-orchestration #automation

## The Problem
Technical writing depends on subject matter access. To document a feature accurately a writer needs to understand it, which means reading the code and the design documents and then asking the person who built it the questions those did not answer — and then having that person check what was written.

Both requests compete with engineering priorities and lose. Review requests sit for days. A writer follows up, escalates to a manager, and gets a cursory approval that does not constitute a real check, or a detailed response two weeks after the release it was meant to accompany.

So writers develop workarounds: reading the code themselves, testing the feature to find the behaviour, inferring from pull requests and issue threads. That is genuinely part of the craft and it is also a writer doing engineering investigation because the engineer is unavailable, at a level of certainty below what a five-minute conversation would produce.

The release cadence makes it acute. Documentation is expected at launch, the feature stabilises days before launch, and the writer has the shortest possible window and the least engineering availability simultaneously.

And when documentation is wrong, the writer is accountable, regardless of whether the information was available.

## Why It Matters to the Worker
This is responsibility for accuracy without authority over the information supply. The writer's professional reputation rests on correctness they cannot independently verify, and the people who could verify it are measured on something else.

The structural position is low-status in a way that is felt daily. Documentation is treated as a downstream obligation rather than part of the product, writers are frequently outside the engineering organisation's planning process, and the request for twenty minutes of an engineer's time is received as an imposition. That is a recognised and long-standing complaint in the profession and it shapes who stays in it.

And the compressed window means the work is rushed at exactly the point where care matters most — a tutorial written in two days for a feature the writer could not fully test is where the drift problem originates.

## What a Solution Looks Like
Extract what can be extracted. Code, pull requests, design documents, issue threads, test cases and commit messages contain most of the factual substance of a feature, and assembling a grounded draft from them gives the writer a starting point and — more importantly — a specific list of what remains genuinely uncertain. Asking an engineer four precise questions is a request they will answer; asking them to review a page is one they will defer.

Make review targeted and cheap. An engineer should be asked to confirm the specific claims that could not be established from the source material, highlighted and individually confirmable, rather than to read a document. That converts a thirty-minute obligation into a three-minute one, which is the difference between a response and a backlog.

Verify the verifiable automatically. Code examples that compile and run, parameter names and types that match the current signatures, and configuration keys that exist are checkable in CI, and removing them from the human review scope leaves only the judgement.

Get documentation into the engineering workflow. Documentation tasks created automatically from feature work, with the writer's questions surfaced in the pull request where the engineer already is, addresses the access problem at its source rather than routing around it.

## Impact If Solved
Review latency and subject matter access are the binding constraints on documentation throughput and the main cause of documentation shipping late and thin. Grounded drafting with a precise uncertainty list, targeted claim-level review and automated verification of the mechanical facts address all three — and they change the writer's position from petitioner to reviewer, which is the status problem underneath.
