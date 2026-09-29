# Case Management and Determination Reuse

**Niche:** [[niches/software-supply-chain-security/security-engineer-triage/profile|The Security Engineer]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Claims adjudication, medical coding and legal review all built systems that reuse a prior determination on an identical case, and security triage re-derives every one from scratch.
**Tags:** #bert #k-nearest-neighbors #k-means-clustering #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #compliance
**Contested on:** Every serious competitor that takes this seriously is fighting to stop an application security engineer establishing that findings do not apply, one at a time, in a queue the scanner regenerates nightly — and whoever does that takes the function, because that is currently the job.

## The Problem
Any domain with a high volume of expert determinations over similar cases builds the same machinery: recognise that this case resembles one already decided, surface the prior decision and its reasoning, and let the expert confirm rather than re-derive. Claims adjudication, medical coding and document review all work this way. Security triage, which has an unusually high proportion of genuinely identical cases because the components are literally the same software, re-derives each one.

## What Already Exists
Case-based reasoning systems with a long history; similarity search over structured and textual cases; adjudication platforms with precedent surfacing; active learning to direct expert attention where it is most informative; and the portable exploitability exchange formats designed specifically to express and share these determinations.

## The Customization Gap
The adaptation is to determinations whose validity depends on code that changes. It requires: (1) a case representation keyed on component, version range, usage pattern and configuration rather than on the finding, since that is what determines whether a prior determination transfers — and is the modelling decision the whole reuse depends on; (2) invalidation conditions recorded with the determination, so the system knows what would make it no longer hold and can resurface it when that changes, which is what distinguishes safe reuse from blanket suppression; (3) confidence and provenance on every proposal, since the engineer is accepting somebody else's reasoning and must be able to inspect it; (4) cross-organisation sharing through the exchange formats, because the same open-source component is assessed independently by thousands of teams and the determinations are largely identical and entirely shareable — which is a public good nobody is coordinating; and (5) audit retention, since a security determination that a finding does not apply is a decision somebody will eventually review.

## Target Customer
Vulnerability management vendors, application security functions, and the exchange format communities whose standards exist precisely for this and are thinly supported.

## Impact If Solved
The determination reuse pattern is standard wherever expert volume is high, and this domain has an unusually high proportion of identical cases. Recorded invalidation conditions are what make reuse safe, and cross-organisation sharing addresses work that is currently duplicated thousands of times over identical components.
