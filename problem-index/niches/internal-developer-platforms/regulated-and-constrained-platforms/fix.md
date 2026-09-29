# The Approval That Nobody Can Evaluate

**Niche:** [[niches/internal-developer-platforms/regulated-and-constrained-platforms/profile|Regulated & Constrained Platforms]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A change advisory board approves deployments it cannot assess, which adds days of latency and no assurance, and everyone involved knows it.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give a regulated or air-gapped organisation a platform that produces the control evidence as a by-product of shipping — and whoever does that takes those estates, because the compliance burden is where their engineering time actually goes.

## The Problem
A deployment requires approval from a board that meets twice a week. The board reviews forty changes per meeting, each described in a ticket, and approves nearly all of them — because the members cannot evaluate a code change from a summary and declining without cause is not defensible. The control adds three days of average latency, produces an approval record, and provides no assurance that anybody has assessed anything. Its existence is justified by a regulatory requirement that says changes must be authorised, which this satisfies in form and not in substance.

## Why It's Still Broken
The board was established when deployments were rare and consequential and has not been revisited as they became frequent and small. The regulation requires authorisation and is silent about mechanism, so the conservative reading — a human committee — persists because nobody has built the evidence for an alternative. The approval rate is not measured, so the theatre is not demonstrated. And proposing to remove a control is professionally risky in a way that keeping an ineffective one is not.

## What a Fix Looks Like
Replace the gate with enforcement and evidence, and make the case with data. Measure the board first: approval rate, rejection reasons, latency added, and whether any incident was prevented by a rejection — which is the evidence that the control is not doing what it is credited with and is straightforward to compute from the existing record. Classify changes by risk and route accordingly, since the majority are routine and a small minority genuinely warrant review, and treating them identically is what makes the review meaningless. Automate the assessable controls — segregation of duties, test evidence, artefact provenance, environment conformance — so the assurance is real and continuous rather than periodic and nominal. Reserve human review for the changes where judgement adds something, with the reviewer given the information to exercise it. Produce evidence that is stronger than an approval record, since the argument with the auditor is won by showing better assurance rather than less of it. Pilot on a limited scope with the evidence retained, which is how these changes are actually accepted. And track the outcome, since a demonstrated improvement in both latency and assurance is what generalises the change.

## Who Feels the Pain
Engineering teams waiting days for an approval that assesses nothing; board members approving changes they cannot evaluate; and organisations carrying a control that provides latency instead of assurance.

## Impact If Fixed
Measuring the board's approval rate and prevented incidents is a query over the existing record and usually establishes that the control is nominal. Risk-based routing plus automated enforcement provides more assurance and less latency, which is the argument that wins with an auditor.
