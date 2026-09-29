# Scope Determination

**Parent Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Category:** High Market Share
**Contested on:** Whether "what did the attacker access" is answered with calibrated bounds from the evidence that exists, or with a narrative that reads as more certain than the evidence supports.

## Profile

**Market Size:** ~$1.00B
**Share of Parent Industry:** ~20%
**Digital Adoption:** Very low — expert judgement under a clock
**Target Buyer:** General counsel, insurers, regulators, boards
**Automation Potential:** High for the inference, none for the accountability

## What Makes This a Distinct Niche

Every consequential decision in a breach turns on one question: what did the attacker actually access. Regulatory notification thresholds, contractual notification obligations, litigation exposure, insurance coverage and the public statement all follow from the answer.

The answer is frequently unavailable. The logs that would show which files were read were not retained. The endpoint that was compromised was not monitored. The cloud audit trail was never enabled. Database query logging was off because of its performance cost. So the responder can establish that the attacker had access to a system, and cannot establish what they did with it.

What the client's counsel wants is a number: how many records, whose, from where. What the evidence supports is a bound: access existed for this window, to these systems, containing this much data, with no evidence of exfiltration and no evidence against it.

The gap between those two is where this industry's hardest professional judgement lives. Report the bound honestly and the client must notify conservatively at enormous cost. Report a narrower scope and the firm is making a claim the evidence does not carry, which will be examined if it turns out to be wrong.

### Contested sub-niches

- [[niches/digital-forensics-firms/evidence-bounded-inference/profile|🎯 Evidence-Bounded Inference]]
- [[niches/digital-forensics-firms/evidence-readiness/profile|🎯 Pre-Incident Evidence Readiness]]

## Current Tools & Gaps

Forensic suites for host and disk examination. Log analysis platforms. Data discovery tooling for establishing what was in an affected store. Notification decision frameworks from counsel. Insurer and regulator expectations, which vary and are largely uncodified.

The gaps are fundamental. Nothing states what a given evidence set can and cannot establish, so the limitation is communicated in prose and is routinely lost as the finding travels upward. Bounds are not calibrated — a firm saying it found no evidence of exfiltration has no basis for saying how often that conclusion has been wrong given comparable evidence. The data-at-risk question is answered by inventory rather than by access, so scope is frequently stated as everything in the affected system. And no firm can tell a prospective client, before an incident, which of their logging gaps would make this question unanswerable.

## Problems

- [[niches/digital-forensics-firms/scope-determination/build|🔨 Build: Bounds, Not Narrative]]
- [[niches/digital-forensics-firms/scope-determination/buy|🛒 Buy: Evidence Standards From Forensic Science]]
- [[niches/digital-forensics-firms/scope-determination/fix|🔧 Fix: No Evidence of Access Is Not Evidence of No Access]]
