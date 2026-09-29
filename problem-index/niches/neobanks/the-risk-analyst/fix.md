# Measured on Cases Closed

**Niche:** [[niches/neobanks/the-risk-analyst/profile|The Risk Analyst]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The analyst's performance metric is cases per hour, the decisions determine whether people can reach their wages, and nobody measures whether the decisions are right.
**Tags:** #evaluation-metrics #worker-facing #hypothesis-testing #confidence-intervals #compliance #quick-win #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give the analyst the evidence and the time to decide correctly rather than a screenshot and a throughput target — and whoever does that changes who gets access to their own wages.

## The Problem
The analyst is reviewed on volume. Two analysts with identical queues can close the same number of cases while making systematically different decisions — one restoring access readily, one rarely — and the performance system cannot distinguish them. The institution is running a decision process whose output varies substantially by who happens to pick up the case, has no measure of that variation, and rewards speed. When the throughput target tightens, decisions get faster and the direction they get faster in is whichever is quicker to justify, which is usually the restrictive one.

## Why It's Still Broken
Throughput is measurable immediately and accuracy requires an outcome join nobody has built — the available metric became the management system, which is the same substitution pattern running through this whole cluster. The outcomes exist in the ledger and belong to a different team. Measuring accuracy would reveal variation nobody currently has to account for. And the analyst has no way to argue for more time on a case.

## What a Fix Looks Like
Measure the decision, not the minute. Join decisions to outcomes in the institution's own ledger, which is the fix, is entirely feasible, and produces a per-analyst accuracy measure where none exists. Report both error directions per analyst, since one who never restores access and one who always does are both wrong and only one of them looks careful. Run calibration exercises on the same cases, which measures agreement directly and is the fastest way to see how much the outcome depends on the reviewer. Balance throughput and accuracy in the performance measure explicitly, rather than measuring one and hoping for the other. Give analysts feedback on their own decisions, which is how judgement improves and which they currently never receive. Route difficult cases to reviewers who are better at them, since the variation is real and can be used rather than only corrected. Investigate disagreement as information about the case type rather than as a reviewer failure, which is where the process improvements come from. Protect the time for the consequential cases explicitly, so a hard case is not decided at queue speed. Report the restoration rate over time, since a drift toward restriction under queue pressure is exactly what a volume metric produces and nobody watches for it. And publish quality alongside volume in the operations review, because whichever number is reported is the one the team optimises.

## Who Feels the Pain
Members whose access depends on which analyst picked up their case; analysts rewarded for speed on decisions that deserve care; and institutions whose freeze rate drifts with their queue.

## Impact If Fixed
The available metric became the management system, and it rewards speed on decisions about people's wages. Joining decisions to ledger outcomes produces a per-analyst accuracy measure, and calibration on shared cases shows immediately how much the outcome depends on who reviewed it.
