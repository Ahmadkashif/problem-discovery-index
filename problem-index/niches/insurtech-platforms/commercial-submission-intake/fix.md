# Decline Reasons Nobody Records

**Niche:** [[niches/insurtech-platforms/commercial-submission-intake/profile|Commercial Submission Intake]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A carrier declines most of what it receives, records the decline as a status, and therefore cannot say what it is declining, why, or whether its appetite is costing it business it should be writing.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #bert #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in submission intake is fighting to turn a broker's email attachments into a structured, triaged submission and rank it by the probability it will be quoted and bound — and whoever raises quote-to-submission ratio most takes the account.

## The Problem
An underwriter declines a submission. The system records "declined" and possibly a free-text note. Across a year that is tens of thousands of declines with no structure — so nobody can say what proportion were outside appetite, priced by a competitor below what the carrier would offer, declined for missing information the broker could have supplied, or declined because no underwriter had capacity that week. Those are four completely different problems with four different responses, and the carrier's distribution strategy, appetite reviews and capacity planning all proceed without the decomposition.

## Why It's Still Broken
Recording a reason costs the underwriter time on a transaction that is, from their perspective, over. The taxonomy was never designed, so where a field exists it is free text or a list that does not fit. And there is an institutional discomfort: a carrier that measures declines by reason will discover it is declining business it wanted, which reflects on appetite, on capacity and on individual underwriters — all of which are easier not to measure.

## What a Fix Looks Like
Capture a structured reason at decline, in one tap, from a taxonomy designed for the purpose: outside appetite by class or hazard, outside appetite by size or geography, loss experience, price uncompetitive, information incomplete, capacity, broker relationship, or other with a note. Add the competitor and price where the broker tells the underwriter, which they frequently do and nobody records. Then produce the analysis nobody has: declines by reason, by class, by broker, by underwriter and over time. The appetite finding is usually the most valuable — a carrier discovering it declined several hundred submissions in a class it believes it writes has found a gap between its stated and its practised appetite. The price-uncompetitive analysis is the second, since it is the only systematic market feedback a carrier receives. And the labels are what make the triage model in the build note possible at all.

## Who Feels the Pain
Distribution leaders who cannot tell brokers what the carrier wants; underwriting leadership whose appetite exists on a document and not in practice; and brokers who keep sending submissions that keep being declined for reasons nobody has articulated.

## Impact If Fixed
A decline taxonomy costs a tap and produces the carrier's first honest picture of the business it turns away, which is by volume the majority of what it sees. It is also the labelling exercise that every subsequent capability in this niche depends on — triage, appetite management and broker management all need it and none of them can be built without it.
