# The Integration Support Engineer

**Industry:** [[payment-processors|Payment Processors]]
**Type:** Worker Life Changing
**One-liner:** Support engineers debug other companies' checkout code from log fragments and a screenshot, answering the same twenty questions in a rotation that never ends.
**Tags:** #large-language-models #bert #k-nearest-neighbors #word-embeddings #evaluation-metrics #workflow-orchestration #worker-facing #automation

## The Problem
A merchant's engineer opens a ticket. The payment is failing. Attached is a screenshot of an error, occasionally a request ID, sometimes neither. The integration was written by a contractor who has left, against an SDK version two majors behind, in a framework the support engineer does not use.

The support engineer pulls the API logs for that merchant, finds the failing requests, and works out what is happening: a field omitted, an idempotency key reused, a webhook endpoint returning a non-200 and therefore being retried into a duplicate, a test-mode key in production, a three-domain-secure flow abandoned because the redirect was mishandled, a currency mismatch, a capture attempted after the authorisation expired.

Almost all of it is diagnosable from logs the processor already holds. The engineer does it by hand, per ticket.

The question distribution is extremely concentrated. A few dozen root causes account for the large majority of tickets, and the same explanation is written again, adapted to a different language and a different framework each time.

Escalation is the other half of the day. Anything that is genuinely a platform behaviour goes to an engineering team with its own priorities, and the support engineer becomes the relay between a frustrated merchant and a backlog.

## Why It Matters to the Worker
The work is skilled and framed as support. Diagnosing a broken payment integration from logs requires real understanding of the protocol, the SDK, the network rules and the merchant's stack, and the role is compensated and titled as a support function with a ticket-count target.

It is also relentlessly repetitive without being simple. The same twenty problems, each arriving in an unfamiliar codebase. There is no accumulation: the engineer who solves a webhook retry storm at hour three solves an identical one next week for a different merchant and writes the explanation again.

The emotional register is poor. The merchant is losing revenue while the ticket is open, and the person receiving that pressure has no control over the engineering backlog and often no authority to issue anything but an apology.

And the career path leads away from the expertise. The way out is a transfer to engineering, where the deep protocol and merchant-behaviour knowledge accumulated in support is treated as unrelated experience.

## What a Solution Looks Like
Diagnosis from logs before a human reads the ticket. The failing requests for this merchant in the relevant window, the specific deviation from the expected call sequence, and the matching known root cause, attached to the ticket automatically. The processor holds every request; the diagnosis is pattern matching against its own API traffic.

Answers drafted in the merchant's actual stack. The root cause is the same across languages; the fix is not. Generating the correction against the SDK version and framework the merchant is demonstrably using turns a paragraph of explanation into a diff.

Proactive detection. A merchant retrying an expired authorisation, accumulating webhook failures, or running a test key in production is visible in traffic before they open a ticket, and the best possible support interaction is the one that starts with the processor.

Integration health as a product surface. Merchants should be able to see their own error taxonomy and their deviation from the recommended call sequence without asking.

Knowledge that accumulates. Every resolved ticket is a labelled example of a log pattern mapped to a root cause and a fix; that corpus should improve the diagnosis rather than sit in a closed ticket.

## Impact If Solved
Integration support is one of the largest cost centres in a processor and is where merchant churn is often decided, since a merchant whose payments are broken for three days does not stay. Diagnosing from traffic the processor already holds, and detecting the common failures before the merchant does, converts a reactive queue into a proactive service and returns the engineers in it to work worth their skill.
