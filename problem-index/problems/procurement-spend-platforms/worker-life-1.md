# Analyst Intake Request Triage

**Industry:** [[procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Worker Life Changing
**One-liner:** Procurement analysts stop being a help desk for people who do not know what procurement needs from them, because intake asks the right questions and routes itself.
**Tags:** #large-language-models #bert #word-embeddings #gradient-boosting #evaluation-metrics #workflow-orchestration #automation #worker-facing

## The Problem
Somebody in the business wants to buy something. They message procurement — in Slack, by email, occasionally in the actual intake form — with a sentence: "we need to get this tool, can you help." What procurement needs in order to act is considerably more: what is being bought, from whom, for how much, under what term, whether a contract exists, whether the supplier is onboarded, whether security review applies, whether it touches personal data, whether legal must review the paper, whether it is in budget, and who approves it.

An analyst extracts all of that by conversation. Several messages back and forth, per request, dozens of requests in flight, most from people who have never bought anything before and do not know the process exists.

The intake queue is therefore a help desk, and the analyst's day is triage: work out what this is, work out who needs to look at it, chase the requester for the missing information, chase the reviewers, and tell an impatient stakeholder why it is taking three weeks.

The rise of intake and orchestration tools as a distinct product category is the market's admission that this, rather than the purchase order, was the real friction.

## Why It Matters to the Worker
Procurement analysts are hired for commercial judgement — evaluating suppliers, structuring deals, understanding a category — and the intake queue displaces it entirely. The role becomes coordination, and coordination of people who did not want to talk to procurement in the first place.

The relationship dynamic is corrosive. The analyst is experienced as an obstacle by the requester and as a bottleneck by leadership, while the delay is usually caused by reviewers in security, legal or finance whom the analyst cannot compel. They own the cycle time metric and none of the levers.

And it is repetitive at exactly the level that grates: the same clarifying questions, hundreds of times, because the person asking has no way to know what was needed.

## What a Solution Looks Like
Intake as a conversation that asks the right questions rather than a form nobody completes. From a single sentence and an attached quote, the system should determine what is being bought, classify it, check whether the supplier is known and under contract, and then ask only what it genuinely cannot infer.

Routing determined from the request rather than from a decision tree the requester navigates. Whether security review, privacy review, legal review or a specific approval threshold applies is derivable from the classification, the amount, the data involved and the supplier's status.

Duplicate detection is the highest-value single check: a large share of requests are for tools the company already owns under an existing agreement, and nothing currently notices.

Reviewer chasing automated, with escalation on predicted rather than elapsed lateness, and status visible to the requester so the analyst stops being the status API.

## Impact If Solved
Intake cycle time is what the business experiences as procurement, and it is currently produced by an analyst conducting the same conversation repeatedly. Removing the extraction and routing work returns the analyst to commercial judgement and removes the adversarial dynamic that makes the function unpopular.
