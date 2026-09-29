# The Report Cannot Tell a Searching Audit From a Permissive One

**Industry:** [[soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** High Impact
**One-liner:** The company being audited chooses and pays the auditor, the customer relying on the report cannot observe how searching the work was, and the deliverable is the same either way.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #hypothesis-testing #survival-analysis #evaluation-metrics #compliance #causal-inference

## The Problem
An attestation report exists so that a company's enterprise customers will accept it as evidence and proceed with a purchase. The company selects the auditor, negotiates the fee and the timeline, and receives a report. Its customers read the opinion and the exceptions, if any, and rarely anything else.

The purchaser's incentive is a clean report, quickly and cheaply. That is not corruption; it is the ordinary consequence of who pays. Auditors compete for that business, and the dimensions they can compete on are price, speed and — implicitly and never stated — how much friction the engagement generates.

The reader cannot observe any of it. Two reports, one from a firm that examined the full population and challenged the scope and one from a firm that accepted the client's description and tested the minimum, are formatted identically and carry the same opinion. There is no quality signal in the artefact, so the market cannot pay for quality, so rigour is a cost with no revenue attached.

The consequences appear at the edges. Companies with clean current attestations suffer breaches involving controls that were in scope, and when that happens nobody can say whether the audit was inadequate or the control failed after testing — because the report does not describe what was examined in enough detail to tell.

And the intermediaries who could demand more do not. Enterprise procurement checks that a report exists and that the opinion is unqualified. Insurers treat it as a control. Neither reads the testing detail, which means neither creates demand for it.

## Why It's Unsolved
The structure is the same one that has been studied in financial audit for decades — the party paying selects the assurer, the party relying cannot observe quality — and the mechanisms that partially address it there, peer review, oversight bodies, liability exposure and mandatory rotation, are weaker or absent in security attestation.

The deliverable format is the binding constraint. The standard reporting format does not require the auditor to characterise how searching the work was, and a firm that added that detail would be volunteering a comparison its competitors do not offer and its client did not ask for.

Observable quality signals are also genuinely hard to construct. Hours spent is a poor proxy; exception counts confound auditor rigour with client quality; and the outcome that would settle it — whether audited companies suffer fewer incidents — is rare, confounded and not collected.

And the client would object. A report describing the depth of testing invites its customers to ask why another supplier's report describes more, which is precisely the comparison the purchasing company does not want to enable.

## What a Solution Looks Like
Put testing depth in the report in a form a reader can evaluate. Population sizes, samples tested, whether testing was sample-based or full-population, which controls were tested how, what scope exclusions were accepted and why — presented as a structured appendix rather than buried in prose — would let two reports be compared for the first time. This requires nothing but a reporting convention and some willingness.

Build a quality signal from outcomes. Across a population of audited companies, whether an attestation was followed by an incident involving an in-scope control is observable where disclosure occurs, and relating that to auditor identity and testing characteristics is the analysis that would give the market a quality measure. It is confounded, it needs care, and even a crude version is more than exists.

Let the relying party specify the standard. Enterprise buyers could require a minimum testing depth rather than the existence of a report, and the first large buyer to do so would change what firms compete on — which shifts the demand side rather than hoping the supply side reforms itself.

Separate the report from the sales document. A version of the deliverable written for the relying party, with the testing detail and the limitations foregrounded, is a different artefact from the one the purchaser circulates, and the profession could define it.

## Impact If Solved
This report gates a large share of enterprise software procurement and carries no information about how searching the underlying work was, which means rigour is unpriced and competition runs on speed and cost. Structured testing-depth disclosure costs nothing but convention and would let the market distinguish; outcome-linked auditor quality signals would let it choose; and a relying-party standard would create the demand that the current structure cannot generate on its own.
