# Establishing What Was Accessed From Logs Nobody Kept

**Industry:** [[digital-forensics-firms|Digital Forensics Firms]]
**Type:** High Impact
**One-liner:** Regulatory notification, contractual obligations and public statements all turn on what the attacker accessed, and the evidence that would establish it was frequently never retained.
**Tags:** #bayesian-inference #confidence-intervals #probability-distributions #graph-neural-networks #hypothesis-testing #gradient-boosting #evaluation-metrics #compliance

## The Problem
When an intrusion is discovered, the decisive question is scope: which systems were reached, what data was accessed, and what left. Regulatory notification thresholds, contractual notification clauses, litigation posture and the organisation's public statements all depend on the answer, and there is a statutory clock running.

The evidence is usually incomplete. Logs have retention periods measured in days on the systems that matter. Endpoint monitoring covers some of the estate and is often installed during the response. Cloud audit logging captures what was configured to be captured, decided long before by someone with other priorities. Network flow records may exist in summary form. Attackers delete logs, and some tooling is designed to.

So the investigator reasons from what remains. Artefacts of execution, file system timestamps, memory where it was captured, authentication records, the attacker's own tooling and its known behaviour, and the pattern of what similar intrusions do. From that they construct an account — and the account is necessarily an inference, with parts that are established, parts that are probable and parts that are unknown.

The delivery of that account is where the problem sharpens. Clients, lawyers and insurers want a determination. A report that says access to this system could not be excluded is legally and operationally awkward, and there is pressure — rarely explicit, always present — toward a narrative that is cleaner than the evidence. The professional standard is to state limitations, and the commercial and legal context pushes the other way.

And the consequence of getting it wrong runs both directions. Over-scoping means notifying people whose data was not affected, with real cost and real alarm. Under-scoping means not notifying people whose data was, which is a regulatory and ethical failure discovered later if at all.

## Why It's Unsolved
The evidence gap is created before the incident by decisions nobody connected to this outcome. Log retention is set on cost grounds, monitoring coverage on deployment convenience, cloud audit configuration by default, and none of those decisions is made with the question "what will we be unable to establish if this system is compromised" in view.

Inference under missing evidence is genuinely hard and is currently done by expert judgement rather than by method. Experienced responders are good at it and cannot articulate the reasoning in a form that transfers, which is why the field's capability is concentrated in a small number of people.

Calibration is absent. Nobody knows how often an experienced responder's assessment of probable access turns out to be right, because the ground truth rarely emerges — and when it does, through later disclosure or litigation, it is not systematically fed back.

And the commercial structure discourages explicit uncertainty. A firm that reports wide bounds is harder to work with than one that reports a conclusion, insurers prefer definite scopes for reserving, and lawyers prefer statements that support a position. The pressure is diffuse and consistent.

## What a Solution Looks Like
Make the inference explicit and probabilistic. Given an evidence set, the set of systems and data the attacker could have reached is bounded, and the probability of access to each is estimable using the observed artefacts, the known behaviour of the tooling involved, and the firm's corpus of comparable intrusions. Reporting a bounded scope with per-system probabilities is more honest and more useful than a narrative, and it is defensible precisely because its limitations are stated.

Calibrate against the cases where truth emerged. Litigation, later disclosure, attacker leak sites and subsequent investigations sometimes reveal what actually happened, and systematically comparing those against the original assessments would give the field its first measure of its own accuracy.

State what the evidence cannot support, prominently. The most valuable line in a forensic report is frequently the one identifying what could not be established and why, and it currently appears in a limitations section that readers skip.

Move the work before the incident. A readiness assessment that tells an organisation which specific logging and monitoring gaps would make a future scope determination unanswerable — named systems, named data, named gap — is the highest-value product this industry could sell, and it converts a decision currently made on storage cost into one made on notification exposure.

## Impact If Solved
The scope determination governs notification obligations affecting millions of people, and it rests on expert inference from incomplete evidence, delivered under pressure toward certainty. Explicit probabilistic scoping with stated limitations, calibrated against the cases where truth emerged, would make the determination defensible rather than authoritative — and pre-incident readiness assessment addresses the gap at the only point where it can still be closed, which is before anything happens.
