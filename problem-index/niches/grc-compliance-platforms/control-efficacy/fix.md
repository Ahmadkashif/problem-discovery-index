# Fix: All Hundred Controls Are Equally Important

**Niche:** Control Efficacy Measurement
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A framework presents its controls as a flat list, organisations implement them in whatever order the platform surfaces them, and nobody can say which ones carry the protection.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #hypothesis-testing #revenue-impact #descriptive-statistics
**Contested on:** Whether the relationship between implementing a framework's controls and actually suffering fewer incidents has ever been measured, by anyone.

## The Problem

A framework hands an organisation a hundred-odd controls with no ranking. The platform surfaces them as a checklist with a completion percentage. The organisation works through them in the order the dashboard presents, or the order that is easiest, or the order the auditor asks about.

The implicit claim is that they matter roughly equally, because nothing says otherwise. That claim is almost certainly false. In any comparable domain the distribution of protective effect across a list of interventions is highly skewed — a few carry most of it and a tail carries very little.

The cost of the flat list is misallocation. A company with limited engineering capacity spends the same effort on a control that would have prevented a real incident and one that produces a document. Both turn green, both count the same toward the percentage, and the percentage is what the certificate reflects.

It also distorts what gets built. Platforms optimise for controls they can verify through an integration, which correlates with what is easy to observe rather than what is protective. A framework requirement that resists automated verification gets less attention, regardless of its importance.

Everyone in this chain suspects the list is not flat. Nobody can say which controls are which, so everybody proceeds as though it is.

## Why It's Still Broken

**No evidence exists to rank with.** The honest reason. Ranking requires outcome data nobody has assembled, and in its absence a flat list is the only defensible presentation.

**Ranking creates liability.** A framework body or a platform that declares some controls less important has taken a position that will be quoted after an incident involving a deprioritised control. The safe move is to assert that all are required.

**Auditors assess conformance, not importance.** An audit checks whether controls are implemented as specified. Importance is outside its scope by design, so the assessment apparatus reinforces the flat treatment.

**Completion percentage is the product's headline.** Platforms report readiness as a fraction, which structurally treats all controls as equal weight. A weighted score would be more useful and harder to explain, and would require the weights to exist.

**Frameworks accrete.** Controls are added over revisions and almost never removed, because removal requires demonstrating irrelevance. The list grows and the average importance per item falls.

**Nobody with the data has a reason.** The platforms could at minimum rank by how often each control fails, how long it takes to remediate and how often it regresses — none of which is efficacy, all of which is informative, and none of which is published.

## What a Fix Looks Like

**Grade the evidence honestly, now.** Label each control by the strength of evidence behind it: demonstrated in published research, supported by incident analysis, expert consensus only. Most will be consensus and saying so is the finding. This requires no new data, only the willingness to state what is known — which is exactly what clinical guidelines did.

**Publish what the platforms already know.** Failure rates, remediation times, regression rates and exception frequencies per control, across the customer base. This is not efficacy and it is genuinely useful — a control that everyone fails and nobody remediates is telling you something, and the data is sitting in every platform.

**Rank by expert-elicited effect in the interim.** Structured elicitation from experienced practitioners, with disagreement reported, produces a defensible provisional ranking and identifies exactly where the experts disagree — which is where the research should go. Medicine did this before it had trials.

**Let organisations weight by their own threat model.** An organisation handling payments faces different risks from one handling health records. Platforms could support customer-specific weighting and instead present a uniform checklist.

**Stop reporting completion as a flat percentage.** A weighted readiness score, even with provisional weights, would direct effort better than a count. The current number rewards finishing the easy controls.

**Separate the certificate from the guidance.** Certification may reasonably require all controls. Guidance about where to spend effort first is a different artefact and could be honest about importance without changing what the certificate demands.

## Who Feels the Pain

The organisation with limited engineering capacity, spreading it evenly across a list where the returns are almost certainly not even.

The engineer implementing a control they can see is ceremonial, told it is required, with no mechanism to raise that — which is a meaningful contributor to the compliance-is-theatre attitude that makes the whole programme harder.

The enterprise buyer, treating a certificate as a security signal of unknown and unmeasured strength.

And the field itself, which cannot improve its frameworks because it has no way to tell which parts of them are working.

## Impact If Fixed

Evidence grading is available immediately, costs nothing but candour, and would tell every practitioner which of their hundred obligations rest on more than plausibility.

Publishing platform-held failure and remediation statistics per control is a small disclosure decision that would give the field its first population-scale data about how controls behave in practice.

And customer-specific weighting would let organisations direct effort by their own risk rather than by a checklist order, which is the difference between a compliance programme that improves security and one that produces a certificate.
