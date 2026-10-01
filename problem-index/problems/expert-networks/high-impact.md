# The Screener Passes the Wrong Expert

**Industry:** [[expert-networks|Expert Networks]]
**Type:** High Impact
**One-liner:** The judgement that separates a profile that sounds right from an expert who actually made the decision is held by a few senior project managers, is never recorded, and is re-learned by every new associate from the client's complaints.
**Tags:** #tacit-knowledge-ml #gradient-boosting #large-language-models #k-nearest-neighbors #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A client request arrives as a paragraph: a former category manager at a US grocery chain who negotiated private-label dairy contracts between 2021 and 2023. An associate searches the network's database and LinkedIn, messages dozens of candidates, and sends each respondent a screener of three to five questions the client approved. Candidates who answer plausibly are forwarded as profiles with their screener responses. The client picks some, the call happens, and on a meaningful share of calls the expert turns out to have been adjacent to the decision rather than in it — they sat in the category but another team owned the contract, or their title meant something different at that company.

Senior project managers are visibly better at this. They read "Director, Strategic Sourcing" at a particular retailer and know that function sits in a shared-services centre that never touched private label. They notice that a screener answer is fluent but generic in the way people answer when they are guessing. They know which former employers of a company produce candid experts and which produce people still bound by restrictive separation agreements. None of that is written down; it shows up only as a higher client rating on their projects.

## Why It's Unsolved
The data collection problem is that the expert judgement happens in a few seconds of reading a profile and is never captured — the associate's decision to forward or drop a candidate leaves a CRM status, not a reason. Reconstructing it means recording the expert reviewer while they triage real candidates and asking them to say why, which slows down a business that sells next-morning turnaround.

The labelling problem is that the outcome is noisy and partly unobserved. A low client rating may reflect the client's bad question, an unprepared analyst, or a good expert who could not discuss the topic for confidentiality reasons; the experts who were never forwarded produce no outcome at all, so the label set covers only candidates who passed the screen. Senior reviewers do not agree with each other, and do not agree with themselves on the same profile a month apart, which is exactly the inter-rater signal the model needs to be calibrated against.

The deployment problem is speed and trust. An associate with a 24-hour turnaround and a call-volume target will ignore any ranking that takes longer than reading the profile, and will stop trusting it after two confident recommendations that the client rejects. The model has to be faster than the expert's glance, show its reason in the associate's vocabulary, and stay advisory.

## What a Solution Looks Like
Build the outcome record first: for every call, the client request, the candidate profile and screener answers as forwarded, the client's selection, the call rating and any dispute or refund, rebooking of the same expert, and — where the client consents — a transcript-derived measure of how much of the call addressed the stated question. Then capture senior reviewers' judgement deliberately on a sample: profile triage with a one-line reason, run as a calibration exercise across reviewers.

Train a fit model on request–profile–screener triples against call outcomes, with propensity correction for which candidates were forwarded, and use nearest-neighbour retrieval to show the associate the most similar prior expert from the same employer and role with their call record. Flag screener answers that are fluent but non-specific, a pattern language models can detect against answers from experts who later rated well.

## Impact If Solved
A refunded or disputed call costs the network the fee and a little of the client's patience; an undisputed bad call costs the client an hour and costs the network its next request. Raising the share of calls where the expert actually made the decision is the single variable that decides which network a research team calls first, and it turns the senior project manager's instinct from a retention risk into a shared asset.
