# First Response Time as the Wrong Target

**Niche:** [[niches/customer-support-platforms/messaging-async-support/profile|Messaging & Asynchronous Support]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Asynchronous support is managed to first response time, which is satisfied equally by a complete resolution and by a holding reply that asks for information, and the second is faster.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #survival-analysis #quick-win #worker-facing #automation
**Contested on:** Every serious competitor in asynchronous support is fighting to close an issue without the customer having to come back — and whoever raises first-contact resolution in a channel with no contact takes the account.

## The Problem
An organisation reports a median first response time of eleven minutes and treats it as a success. A substantial share of those responses are acknowledgements or requests for information that advance nothing, sent quickly because the timer is running. The customer's experience is an eleven-minute reply that does not help, followed by hours or days of further exchanges. Meanwhile an agent who spends twenty minutes composing a complete resolution is penalised by the metric. The organisation has instrumented the precise behaviour it does not want and reports it as a service level.

## Why It's Still Broken
First response time is easy to compute, was inherited from an era when acknowledgement genuinely was the deliverable, and appears in service level agreements that were written the same way. Replacing it requires measuring resolution, which requires deciding when an issue is resolved, which is harder and is contested — a conversation can be closed without being solved, which is the same measurement problem that appears throughout this industry. And the current number is flattering, which is a reliable reason for a metric to survive.

## What a Fix Looks Like
Measure what the customer experiences and keep the response timer for what it is actually good for. Time to resolution from the customer's first message, round trips per issue, and the share of first replies that materially advanced the issue rather than requesting information — the last of which is classifiable from the reply text and is the specific correction. Report first response time as an operational capacity measure rather than as a service quality one, which is what it is. Where a contractual service level specifies first response, add a resolution measure alongside it, since the contract's purpose was responsiveness and the letter of it has become a target that defeats the purpose. And show agents the round trip and resolution measures for their own work, since the current metric is what shapes the behaviour and agents will optimise for whatever is shown to them — which is an argument for changing what is shown rather than for exhorting them.

## Who Feels the Pain
Customers receiving fast replies that do not help; agents penalised for taking the time to solve something properly; and support leaders reporting a service level that measures speed of acknowledgement.

## Impact If Fixed
Classifying first replies as advancing or requesting is straightforward and immediately quantifies how much of the reported responsiveness is real. Changing what agents are shown is the mechanism that changes behaviour, and it is a reporting change rather than a systems project.
