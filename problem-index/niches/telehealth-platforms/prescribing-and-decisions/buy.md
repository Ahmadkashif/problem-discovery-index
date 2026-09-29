# Buy: Clinical Decision Support Adapted to a Short Virtual Encounter

**Niche:** [[niches/telehealth-platforms/prescribing-and-decisions/profile|Prescribing & Clinical Decision-Making]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical decision support is a mature category built for an EHR with a full patient record and a clinician who can examine the patient; virtual care has neither.
**Tags:** #large-language-models #bayesian-inference #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #worker-facing
**Contested on:** Whether decision support designed around a longitudinal record can help a clinician who has a questionnaire and twelve minutes.

## The Problem

Clinical decision support has decades of development behind it. Drug interaction checking, allergy alerts, dosing calculators, guideline content, order sets and diagnostic reference tools are all embedded in every major EHR and available from specialist vendors, with real evidence behind several of them.

They assume the context of institutional care: a longitudinal record with problem list, medications and results; a clinician who has examined the patient; and an encounter with enough time to engage with an alert. A virtual visit has a questionnaire, a video window, a patient whose history is elsewhere, and a schedule that does not accommodate a four-click advisory.

## What Already Exists

UpToDate, the EHR-embedded CDS modules, First Databank and Medi-Span interaction databases, guideline content from professional bodies, e-prescribing with formulary and PDMP integration, and a growing set of ambient and generative clinical tools. The content and the interaction-checking infrastructure are strong and should be licensed rather than rebuilt.

## The Customization Gap

**The record is absent and has to be assembled.** Interaction checking against a medication list is only as good as the list, and here the list is what the patient remembered to type. Retrieving actual medication history from pharmacy networks and health information exchanges before the visit — which is technically available — is the highest-value adaptation and is not what the CDS vendor provides.

**Alert design has to account for a twelve-minute encounter.** Alert fatigue is a documented failure of institutional CDS and is worse here, where the time budget is smaller and the clinician is working a queue. Ruthless suppression, with only high-severity and high-specificity alerts surfacing, is a tuning exercise the vendor defaults do not do.

**The differential is narrower and the danger is the atypical presentation.** Virtual care handles a defined set of presentations well and the clinical risk concentrates in the ones that look ordinary and are not. Support tuned to flag the features that should prompt escalation to in-person care is a different emphasis from general diagnostic reference, and it is where the clinical value is.

**Regulatory constraints are specific and jurisdictional.** Controlled substance prescribing rules for remote encounters differ by state and have been repeatedly extended rather than settled federally; some presentations require an in-person examination in some jurisdictions. Encoding that as a live constraint at the point of prescribing, rather than as a policy document, is platform work no CDS vendor covers.

**Asynchronous encounters have no moment of decision to interrupt.** A meaningful share of virtual care is questionnaire-based with no live interaction. Decision support that assumes an open chart during a conversation has nowhere to appear, and the support has to be restructured around a review queue instead.

## Target Customer

Platform clinical informatics teams licensing CDS content and finding it assumes a chart they do not have. Also the CDS vendors, for whom virtual care is a large and growing deployment context their institutional products fit poorly.

## Impact If Solved

The licensed interaction databases, guideline content and reference tools get used, and the record retrieval, alert suppression, escalation-focused tuning, jurisdictional constraints and asynchronous surfaces get built. Concretely: a clinician starts the encounter with the patient's actual medication history rather than the one they typed from memory.
