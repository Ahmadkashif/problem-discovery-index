# Why Is This Number Lower

**Niche:** [[niches/music-distribution-platforms/the-artist-support-agent/profile|The Artist Support Agent]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The most common question in the queue has a computable answer and is answered with a paragraph about how streaming works.
**Tags:** #worker-facing #quick-win #descriptive-statistics #automation #evaluation-metrics #data-integration #confidence-intervals #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to let an agent answer a royalty question with an actual answer rather than a description of a process — and whoever gives them visibility into the accounting changes what support can be.

## The Problem
Payments vary month to month for identifiable reasons: fewer streams, a rate change, a statement arriving in a different period, a correction, a currency movement, a deduction. The artist asks why. The agent sends an explanation of how per-stream rates vary. The artist, whose rent depends on the number, is not satisfied and replies. The exchange repeats across thousands of tickets a month, and the actual cause of each was a computable difference between two statements.

## Why It's Still Broken
The knowledge base answers the general question because the specific answer requires data the agent cannot reach, so the generic reply became the standard response — a support function equipped only with general information will give general answers forever. Nobody decomposed the variance. The repetition is absorbed as ticket volume. And the artist's dissatisfaction is treated as inherent to the subject.

## What a Fix Looks Like
Decompose the change automatically. Compute the period-over-period difference by service, territory, track and cause, which is the fix and is arithmetic on data the distributor already holds. Present the top contributors to the change, since one or two usually account for most of it. Distinguish a volume change from a rate change, as they mean completely different things to an artist and are conflated in every generic explanation. Flag corrections and late statements explicitly, because those are the most confusing and the easiest to explain once identified. Show the artist this decomposition in their own account, which prevents most tickets from being opened. Give the agent the same view, so the ones that are opened are answered in one reply. Report the ticket volume by question type, which will confirm how concentrated this is. Explain deductions and currency separately, since they are systematically misunderstood. Set expectations about normal variation in the statement itself, as an artist who knows the range is not alarmed by it. And measure repeat contacts on the same question, which is the honest measure of whether the answer worked.

## Who Feels the Pain
Agents sending the same generic explanation daily; artists whose income question is answered with a lecture; support leadership carrying avoidable volume; and distributors whose most frequent interaction with artists is an unsatisfying one.

## Impact If Fixed
A support function equipped only with general information will give general answers forever. Decomposing the period-over-period change is arithmetic on existing data and turns the most common ticket in the queue into a self-service answer.
