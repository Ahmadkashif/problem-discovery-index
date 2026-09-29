# Integration Support and the Blame Boundary

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Worker Life Changing
**One-liner:** Integration support engineers stop spending every ticket establishing whose fault it is, because the request and response are both on record and the answer is determinable in seconds.
**Tags:** #bert #word-embeddings #gradient-boosting #k-means-clustering #change-point-detection #evaluation-metrics #automation #worker-facing

## The Problem
A consumer reports that the API is broken. The support engineer's first task is almost never diagnosis; it is determining which side the fault is on.

Usually it is the consumer's. A malformed request, a misunderstanding of a parameter, an authentication token that expired, pagination handled incorrectly, a retry storm they created themselves, an assumption about ordering the API never promised. Sometimes it is genuinely the provider's. Occasionally it is a third party in between.

Establishing which takes a conversation. The engineer asks for the request, the timestamp, the correlation identifier, the error response — and the consumer supplies a screenshot and an approximate time. Then the engineer searches logs, finds the request, and works out what happened.

The interaction is faintly adversarial from the start because both parties suspect the other, and the engineer is in the position of telling a customer they made a mistake, repeatedly, all day.

Meanwhile the gateway logged both the request and the response, with a correlation identifier, at the moment it happened.

## Why It Matters to the Worker
Integration support requires real technical depth — protocol behaviour, authentication flows, the API's semantics, common client library pitfalls — and most of the day is spent on evidence gathering rather than on applying any of it.

The blame dynamic is the corrosive part. Being right is not satisfying when being right means telling a developer their code is wrong, and doing it fifteen times a day makes the role adversarial by construction. Engineers describe developing a defensive tone that they dislike in themselves.

There is also a systemic frustration. The same misunderstandings recur endlessly — the same parameter misread, the same pagination mistake, the same auth flow error — and each is handled as an individual ticket rather than as evidence that the documentation or the API design is misleading.

## What a Solution Looks Like
Self-service diagnosis before the ticket. A consumer should be able to look up their own request by identifier and see what was sent, what was returned and what was wrong with it, in their own portal. That resolves the majority of cases without a conversation and removes the blame dynamic entirely, because the consumer discovers the answer themselves.

Automatic fault attribution when a ticket does arrive, from the logged request and response — malformed input, expired credential, rate limit, provider error — so the engineer starts from the answer rather than from a search.

Error pattern clustering, so that recurring consumer mistakes are visible as design and documentation findings rather than as a stream of tickets. A parameter that a hundred consumers misuse is a naming problem.

Proactive detection of a consumer whose error rate has jumped, since the provider sees the failure before the consumer's on-call does and telling them first inverts the entire relationship.

## Impact If Solved
Integration support is dominated by evidence gathering to settle a blame question the gateway logs already answer. Self-service request inspection removes most of the volume and all of the adversarial framing, and error clustering turns recurring tickets into the design fixes that would prevent them.
