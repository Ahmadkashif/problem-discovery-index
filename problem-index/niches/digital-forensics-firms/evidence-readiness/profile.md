# Pre-Incident Evidence Readiness

**Parent Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether an organisation can be told, before anything happens, which of its logging gaps will make the notification question unanswerable.

## Profile

**Market Size:** ~$400M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Very low — a retainer and a tabletop
**Target Buyer:** CISOs, general counsel, cyber insurers
**Automation Potential:** High — the gap assessment is largely mechanical

## What Makes This a Distinct Niche

This is the same question moved backwards in time. Not what does the surviving evidence support, but which evidence will survive, and which of the gaps will matter.

The assessment is tractable. A firm that has run thousands of investigations knows which evidence sources answer which questions, and an organisation's logging configuration is observable. Comparing the two produces a ranked list: if an intrusion of this shape occurs, these questions will be answerable, these will be bounded, and these will be unanswerable — and here is what to enable to change that.

That is a completely different business from its sibling. [[niches/digital-forensics-firms/evidence-bounded-inference/profile|🎯 Evidence-Bounded Inference]] is sold into an engagement already underway, to a client already in crisis and already paying, improving a deliverable already due. Readiness is sold to a CISO in a budget cycle, months or years before anything happens, as a remediation plan whose return appears only if an incident later occurs — which is the hardest sale in security and the reason this half is deferred.

The contest is over whether the gaps can be ranked by consequence rather than listed by best practice. A generic logging checklist exists everywhere and is ignored. A statement that this specific gap will make the notification decision unanswerable in the scenario most likely to happen to this organisation is a different artefact entirely.

## Current Tools & Gaps

Incident response retainers with an assessment component, usually a tabletop exercise and a readiness questionnaire. Logging best practice guidance from vendors and frameworks. Detection coverage assessments, which measure whether an attack would be detected rather than whether it could be investigated. SIEM and logging platform configuration reviews aimed at cost and coverage.

The gaps are specific. Assessments cover detection coverage and rarely investigative coverage, which are different questions — a control that blocks an attack leaves no record of what was attempted, and a detection that fires says nothing about what was accessed. Nothing ranks logging gaps by which investigative question they render unanswerable. Retention periods are assessed against policy rather than against the realistic dwell time of an intrusion. Cloud and SaaS audit logging, which is frequently off by default and expensive to enable, is inconsistently covered. And nothing connects the assessment to the notification decision, which is the consequence the organisation actually cares about.

## Problems

- [[niches/digital-forensics-firms/evidence-readiness/build|🔨 Build: The Gap That Will Cost You the Answer]]
- [[niches/digital-forensics-firms/evidence-readiness/buy|🛒 Buy: Detection Coverage Assessment, Pointed at Investigation]]
- [[niches/digital-forensics-firms/evidence-readiness/fix|🔧 Fix: Retention Is Set by Cost, Not by Dwell Time]]
