# The Taxonomy That Stops at a List

**Niche:** [[niches/ai-red-teaming-firms/domain-harm-taxonomies/profile|Domain Harm Taxonomies]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** An engagement produces a carefully constructed list of domain-specific harms and then tests against the generic technique catalogue anyway, because nothing connects a harm to a probe.
**Tags:** #evaluation-metrics #automation #compliance #descriptive-statistics #graph-theory #hypothesis-testing #quick-win #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to enumerate what actually goes wrong in one regulated deployment rather than what goes wrong in general — and whoever does that takes the account, because the generic list is the part the client already has.

## The Problem
Week one of an engagement produces a good domain harm taxonomy: eleven ways a clinical assistant could cause harm, articulated with a clinician, specific and correct. Weeks two to four run the standard technique catalogue, because that is what the tooling supports, and the report maps findings back onto the taxonomy afterwards where they happen to fit. Four of the eleven harms were never tested for, because no probe exists that targets them and writing one was not in the plan. The taxonomy appears in the report as scoping and functioned as decoration.

## Why It's Still Broken
Probes are organised by technique because that is how the attack literature is organised, and harms are organised by outcome, and nothing maps between them. Writing a probe for a specific domain harm requires understanding both the harm and the system, which is the expensive combination. The after-the-fact mapping looks like coverage in a report. And no coverage measure exists that would reveal the gap.

## What a Fix Looks Like
Connect the taxonomy to the testing. Require every harm in the taxonomy to have at least one probe targeting it, and report coverage per harm rather than per technique, which is the fix and it immediately exposes the harms nobody tested for. Generate candidate probes from a harm description, which is now tractable and turns a day of probe writing into an hour of review. Maintain a probe library indexed by harm as well as by technique, so a sector's accumulated probes are reusable across clients — this is the asset that makes domain testing affordable at the second engagement. Report the harms for which no adequate probe exists as an explicit finding, since an untestable harm is important information and currently disappears. Have the domain practitioner review the probes, since they can tell immediately whether a probe targets the harm they described. Report per-harm effort and outcome, so a reader can see which harms were examined hard. Include non-adversarial probes, because many domain harms arise from ordinary use rather than from induced failure and a technique-driven catalogue contains none. And map each harm's coverage to the regulatory obligation it implicates, which is the artefact the client's compliance function needs and which nothing currently produces.

## Who Feels the Pain
Clients whose sector-specific risks were enumerated and not tested; domain practitioners whose careful articulation was decorative; and the firms whose reports claim a coverage their method did not deliver.

## Impact If Fixed
Requiring a probe per harm and reporting coverage per harm rather than per technique immediately exposes the untested ones. A probe library indexed by harm is what makes the second engagement in a sector affordable, and untestable harms become a reported finding rather than a silent gap.
