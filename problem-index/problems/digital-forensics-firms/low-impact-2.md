# Attribution With Calibrated Confidence

**Industry:** [[digital-forensics-firms|Digital Forensics Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Attribution is asserted with confidence language nobody has calibrated, into a context where it affects insurance coverage, sanctions exposure and public statements.
**Tags:** #bayesian-inference #confidence-intervals #gradient-boosting #graph-neural-networks #k-nearest-neighbors #hypothesis-testing #evaluation-metrics #compliance

## The Problem
Incident reports identify the actor where they can: a named group, a ransomware affiliate programme, a broad category. The identification rests on tooling used, infrastructure, techniques, timing, targeting and sometimes language artefacts — a set of signals that are individually weak and collectively suggestive.

The consequences of that identification are substantial. Insurance coverage can turn on whether an act is attributed to a state actor, given how war and state-action exclusions are written and how they have been litigated. Sanctions compliance affects whether a ransom payment is lawful. Public statements about attribution shape regulatory and reputational outcomes.

The signals are also contestable by construction. Tooling is shared, sold and stolen; infrastructure is rented from the same providers; techniques are documented publicly and copied; and actors deliberately plant misleading indicators. A confident attribution from weak evidence is a real risk, and the field's convention of expressing confidence verbally — assessed with moderate confidence — is applied inconsistently and interpreted variably by the lawyers and insurers who read it.

And nobody knows the accuracy rate. Attributions are rarely confirmed, and when later evidence emerges it is not systematically compared against the original assessment.

## What Already Exists
Adversary frameworks and threat intelligence vendors maintain actor profiles with associated tooling, infrastructure and techniques. Malware analysis identifies families and sometimes builder-level artefacts. Infrastructure analysis links campaigns through hosting, certificates and registration patterns. Ransomware affiliate structures are reasonably well mapped. Government attribution statements occasionally provide external confirmation. Confidence expression conventions exist in the intelligence tradition and are widely borrowed.

## The Customisation Gap
Attribution should be a probabilistic inference over a signal set rather than a judgement expressed in words. Each signal has a likelihood ratio that is estimable from the corpus — how often this tool, this infrastructure pattern, this technique combination appears with this actor versus with others — and combining them with stated independence assumptions produces a posterior that can be reported as a number with a range.

Deliberate deception must be modelled rather than noted. Actors plant false indicators, and a framework that treats every signal as honest evidence is exploitable. Weighting signals by how easily they can be faked — infrastructure is cheap to mimic, certain build artefacts are not — is the difference between an analysis and a checklist.

Calibration against the confirmed cases is the missing discipline. Government attributions, arrests, leaks and subsequent research sometimes establish the truth, and comparing those against contemporaneous assessments would give the field an accuracy rate for its own confidence expressions, which nobody has.

And the consequence-aware framing matters. Where an attribution carries insurance or sanctions implications, the report should make explicit what the assessment does and does not support for that specific purpose, rather than offering a single verbal confidence that different readers will interpret differently.

## Impact If Solved
Attribution assessments feed decisions about coverage, payment legality and public statements, and they are expressed in confidence language that has never been calibrated. Likelihood-based inference with deception weighting, reported numerically with a range and calibrated against confirmed cases, would make attribution defensible for the purposes it is actually used for — and would let a firm say clearly when the evidence does not support the determination someone needs.
