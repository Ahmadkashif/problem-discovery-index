# The Merchant Risk and Dispute Handler

**Industry:** [[bnpl-providers|BNPL Providers]]
**Type:** Worker Life Changing
**One-liner:** One team arbitrates between consumers who say the goods never arrived and merchants who say they did, on evidence neither side supplies, several hundred times a week.
**Tags:** #bert #large-language-models #k-nearest-neighbors #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing #workflow-orchestration

## The Problem
The case is a consumer saying the item never arrived, or arrived broken, or was not what was described, or that they returned it three weeks ago and are still being debited. On the other side is a merchant with a tracking number and a policy.

The handler has the consumer's message, the order record, whatever the merchant has supplied, and the provider's own data about this merchant and this consumer. They decide who bears the loss: refund the consumer and claw back from the merchant, decline the claim, or absorb it.

Evidence is the problem. Tracking says delivered; the consumer says it was not. The merchant's return policy says fourteen days; the consumer says they posted it on day twelve and has no receipt. The item description is a paragraph of marketing copy and the dispute turns on whether the product matched it.

The merchant relationship complicates every decision. Large merchants are commercially important and have account managers who take an interest in claw-back rates. The handler making a decision against a major merchant knows this.

Volume is high, the amounts are small, and the same merchants generate the same disputes repeatedly — which is the most useful fact available and the least systematically used.

## Why It Matters to the Worker
The role requires judgement, is staffed as processing, and is graded on throughput and on a quality sample that reviews decisions against a rubric written for the clear cases. The hard cases — where both parties are plausible and the evidence is thin — are the majority of the work and the rubric does not reach them.

Handlers absorb both sides' frustration. The consumer believes the provider is defending a merchant; the merchant believes the provider is siding with a customer against them. Both are speaking to the same person.

The commercial pressure is real and unspoken. Nobody instructs a handler to favour a large merchant, and everybody understands the account structure. Working inside an unstated constraint is corrosive in a way that an explicit policy would not be.

And the pattern knowledge does not accumulate anywhere. A handler who recognises that a particular merchant's non-delivery claims spike whenever it uses a specific carrier has learned something valuable about the merchant book, and has a free-text notes field to put it in.

## What a Solution Looks Like
Claim classification and evidence assembly before the case opens. What the consumer is actually claiming, extracted from their message; the tracking record, delivery scan, merchant policy, return window and prior interactions gathered into one view; the specific evidentiary gap named.

Merchant-level pattern surfacing. Claim rates by merchant, by category, by carrier and by time, with anomalies flagged. When a merchant's non-delivery claims triple in a fortnight, that is a merchant problem rather than several hundred consumer problems, and identifying it once prevents the rest.

Consumer-side pattern detection handled carefully. Repeat claimants exist and a small number are abusing the process, and the signals that identify them also identify people who genuinely receive a lot of bad parcels. This should raise a review threshold, never auto-deny, and the distinction deserves to be explicit rather than folded into a score.

Precedent retrieval. Similar prior cases with their decisions and what happened after — did the merchant contest, did the consumer complain, did the decision hold — turns an isolated judgement into a consistent one.

Decision consistency monitoring, including by merchant size. If outcomes on identical fact patterns differ systematically with merchant importance, the organisation should know that number rather than leave it to individual conscience.

## Impact If Solved
Dispute handling is where the provider's two customers collide, and it is currently resolved case by case by people with incomplete evidence and unstated pressure. Assembling evidence automatically, surfacing merchant-level patterns and retrieving precedent makes the decisions faster, more consistent and defensible to both sides — and measuring consistency makes the uncomfortable part of the job visible enough to fix.
