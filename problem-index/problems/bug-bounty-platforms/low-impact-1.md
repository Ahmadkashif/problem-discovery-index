# Triage Volume and Duplicate Detection

**Industry:** [[bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Most submissions to a public programme are duplicates, out of scope, scanner output or non-issues, and every one must be read by someone qualified to tell the difference.
**Tags:** #bert #transformers #contrastive-learning #gradient-boosting #k-nearest-neighbors #dbscan #evaluation-metrics #automation

## The Problem
A public bounty programme receives submissions continuously, and the large majority are not actionable. Duplicates of known issues, findings outside the declared scope, raw scanner output submitted without validation, misunderstandings of intended behaviour, and low-quality reports that may or may not describe something real.

Each must be assessed by a person with enough security knowledge to distinguish a genuine finding from a plausible-looking one, which is an expensive person. Triage is therefore the dominant operating cost of a bounty programme and the main reason organisations restrict to private programmes, cap participation or do not run one at all.

Duplicate detection is the specific difficulty. Two researchers describing the same underlying vulnerability will write completely different reports — different endpoints, different payloads, different framing — and matching them requires understanding what the underlying issue is rather than comparing text. Getting it wrong in either direction is costly: a missed duplicate pays twice, and a wrongly-called duplicate denies a researcher payment for original work, which is the most damaging thing a programme can do to its reputation.

Report quality varies enormously and correlates with researcher experience, which means the signal for prioritising the queue exists and is barely used.

## What Already Exists
Platforms provide submission workflows with basic keyword search for duplicates and manual assessment. Managed triage is offered as a service by the major platforms. Researcher reputation scores exist and inform prioritisation loosely. Scope definitions and automated scope checking catch the simplest out-of-scope submissions. Some programmes use submission templates to improve report structure. Scanner output detection is largely by eye.

## The Customisation Gap
Duplicate detection needs to operate on the underlying vulnerability rather than on report text. Representing a finding by its technical substance — the affected component, the weakness class, the mechanism, the reachability path — supports matching across entirely different write-ups, which keyword search cannot do. The platform holds the largest corpus of such pairs in existence, including confirmed duplicate decisions, which is the label set.

Prioritisation is the second gap. Expected validity is predictable from report structure, researcher history in this technology area, evidence quality and specificity, and using that to order the queue rather than processing chronologically would materially change triage economics — while requiring that nothing is dropped, only ordered, since a low-prior report from an unknown researcher is occasionally the most important one.

Scanner output detection is cheap and unbuilt. Reports that are unvalidated tool output have recognisable signatures, and separating them at intake with a request for validation rather than a rejection handles a large share of volume without alienating people.

And the routing should match expertise. A submission about a specific technology should reach a triager who knows it, and platform triage teams have skill profiles that are not used for assignment.

## Impact If Solved
Triage cost determines whether an organisation can run an open programme at all, which determines how much of the researcher population ever gets to look at their systems. Substance-based duplicate detection, validity-ordered queues and intake-stage scanner filtering would change the economics directly — and better duplicate accuracy addresses the single most damaging failure mode for researcher trust.
