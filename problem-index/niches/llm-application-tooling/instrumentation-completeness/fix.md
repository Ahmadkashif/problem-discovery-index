# The User's Reaction in a Different System

**Niche:** [[niches/llm-application-tooling/instrumentation-completeness/profile|Instrumentation Completeness]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** The application records what it said and the product analytics records what the user did next, and nothing joins them — which discards the only free quality label the application produces.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #causal-inference #confidence-intervals #automation #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to make the trace contain the thing you need at the moment you need it — and whoever does that takes the account, because a trace missing the decisive context is indistinguishable from no trace at all.

## The Problem
A user receives a generated answer, rewords the question and asks again, then abandons the session. That sequence is a clear quality signal: the answer did not work. It is recorded in the product analytics platform as three events with a session identifier. The response itself is in the tracing platform with a trace identifier. Nothing connects them. The team pays for a judge to grade sampled outputs while the users are grading every single one for free in a system nobody has joined to the first.

## Why It's Still Broken
The two systems are bought by different teams for different purposes and neither vendor treats the join as their problem. The correlation identifier is not propagated to the front end. Product analytics is organised around funnels rather than around individual responses. And nobody has framed retries and abandonment as quality labels, so the value of the join is not obvious until it is stated.

## What a Fix Looks Like
Join the response to what happened next. Propagate a correlation identifier from the response into the front end and back onto the reaction events, which is a small engineering change and unlocks everything else here. Define the reaction signals that indicate quality — rewording and retry, edit before use, copy, escalation to a human, abandonment, an explicit rating — and treat them as labels rather than as product metrics. Report quality by these signals per input cluster, per prompt version and per model, which gives the team a continuous quality measure on their entire traffic rather than on a graded sample. Use the signals as the regression suite's labels, which makes the suite reflect real user outcomes rather than a rubric somebody wrote. Calibrate the implicit signals against explicit ratings on a sample, so their meaning is known rather than assumed. Surface the worst-reacted responses for review, which is the highest-value queue an applied AI engineer can have and does not currently exist. Feed them into failure clustering, since a cluster of badly-received responses is a defect with a free label attached. And report coverage of the join, since a partially propagated identifier silently biases everything built on it.

## Who Feels the Pain
Teams paying to grade a sample while users grade everything for free; applied AI engineers with no queue of genuinely bad responses to work from; and users rewording a question three times into a system that records their frustration nowhere useful.

## Impact If Fixed
Users label every response for free and nothing joins that to the response. Propagating a correlation identifier into the front end is a small change that converts retries, edits and abandonment into a continuous quality measure over all traffic.
