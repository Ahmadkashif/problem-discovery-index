# Nobody Measures Whether Routing Was Right

**Niche:** [[niches/procurement-spend-platforms/intake-and-orchestration/profile|Intake & Orchestration]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Requests are routed to reviews by a rules tree, a reviewer who receives something irrelevant closes it and moves on, and nobody counts how often that happens or which rule produced it.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #graph-theory #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in procurement intake is fighting to take a request from someone who does not know what procurement needs and route it correctly without a human help desk — and whoever routes most requests unassisted takes the account.

## The Problem
A security team receives a review request for a purchase that involves no systems, no data and no integration — a catering contract classified into a rule that routes anything above a threshold to security. They close it with a comment and receive another one next week. Across a year this consumes a substantial amount of a scarce reviewing team's time, and the rule producing it has never been examined because nobody counts the outcome of routing decisions. Meanwhile a purchase that genuinely warranted review was routed around because it fell below a threshold, and nobody counts that either.

## Why It's Still Broken
Routing rules are configured at implementation and grow by exception thereafter, with no telemetry on whether the routing was correct — which is the same unmeasured accumulation as the CRM routing tree, the claim edit library and the procurement approval chain. The reviewers who bear the false positives have no channel to report them as a routing problem rather than as an individual request, and the false negatives are invisible to everyone by definition.

## What a Fix Looks Like
Ask the reviewer and count the answer. Every review closes with a one-tap judgement: this needed my review, this did not, or this needed a different reviewer. That single field, aggregated, gives the false positive rate per rule within a month and identifies the rules generating the most wasted review capacity — which is usually a small number of blunt thresholds. False negatives are harder and are approachable through sampling: periodically route a random selection of requests that the rules excluded to a reviewer and ask the same question, which is the only way to estimate what the rules are missing and costs very little. Publish both rates. Prune the rules with the evidence attached, and replace threshold-based routing with the inference described in this sub-niche's build note, evaluated against the same measure. Report reviewer time consumed per rule, since that is the cost the rules impose and it currently falls on teams that have no say in the configuration.

## Who Feels the Pain
Security, legal and privacy reviewers spending time on requests that did not need them; requesters delayed by reviews that were never relevant; and the organisation, which is simultaneously over-reviewing the trivial and under-reviewing the consequential.

## Impact If Fixed
A one-tap judgement at review close produces the routing accuracy measure the category has never had, and the false positive concentration is typically severe enough that pruning a handful of rules returns meaningful capacity to scarce review functions. The sampled false-negative estimate is the uncomfortable half and is the only way to know whether the process is protecting anything.
