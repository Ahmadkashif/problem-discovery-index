# Build: One Capture, Many Outputs

**Niche:** [[niches/telehealth-platforms/documentation-and-coding/profile|Documentation & Coding]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Capture the encounter once and generate the clinical note, the code, the patient summary, the primary care letter and the structured decision record from it.
**Tags:** #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #data-integration #worker-facing #automation
**Contested on:** Whether one capture can produce every downstream artefact at a quality each audience will accept.

## The Problem

A virtual encounter currently produces one artefact — a clinical note — at a cost of roughly as much clinician time as the encounter itself. That note is used for billing and stored, and everything else that should exist is either written separately or does not exist at all.

The patient gets no summary, or a generic one. The primary care provider gets nothing. The next clinician on this platform gets a note written in shorthand for the author's own reference. The outcome measurement programme has no structured decision record. The coding is derived by the clinician or a coder from prose that was written for a different purpose.

Every one of those artefacts is derivable from the same encounter. The information is captured once and exploited once.

## Why Nobody Has Built This

Documentation has been treated as a single deliverable — the note — because in institutional medicine the note serves most purposes for a reader who shares the context. In virtual care the readers are more varied and share less, and nobody has re-examined the assumption.

The generative capability to do this arrived recently and has been applied to the obvious target, which is reducing the time to write the note. Reusing the capture for other outputs is a product idea rather than a technical one and has not been the first thing anyone built.

And the downstream consumers do not exist yet at most platforms — there is no write-back, no patient summary, no decision record — so there has been nothing to generate them for.

## What to Build

A single capture with an artefact-generation layer over it.

**Capture properly.** The encounter audio with speaker separation, plus the structured intake, plus the clinician's actions in the system. For asynchronous encounters, the questionnaire and the clinician's reasoning. This is the raw material and it is the only thing that has to happen during the encounter.

**Generate the clinical note first**, since it is what clinicians need and what justifies the deployment. Structured, in the platform's format, with the clinician reviewing and editing rather than composing. Review must be fast or nothing is saved.

**Then generate the rest from the same capture.** A patient-facing summary in plain language, with what was found, what to do and when to seek further care — which patients value highly and almost never receive. A primary care letter suited to an external reader who does not share the context. A structured decision record with the presentation, differential, decision and reasoning as fields, which is what outcome measurement and prescribing analytics need and which nobody types by hand. And the coding suggestion, derived from the encounter rather than from the note.

**Make the clinician review once.** The review step covers the clinical note, and the derived artefacts are generated from the approved note plus the capture. Asking a clinician to review five documents defeats the purpose entirely.

**Measure quality per artefact.** Note accuracy against clinician edits, coding accuracy against auditor review, patient summary comprehension, and decision record completeness. Each has a different audience and a different failure mode, and a single quality number hides all of it.

**Handle the compliance posture explicitly.** Recording consent, retention, the clinician's attestation that the note is theirs, and the audit trail showing what was generated versus edited. The note is a legal record and the provenance matters.

## Target Customer

Platform clinical operations, where the case is clinician time — the most expensive input in the business — and clinician retention, since documentation burden is a leading reason clinicians leave. The derived artefacts then make the continuity, outcome and coordination work possible at no additional capture cost.

## Impact If Built

Documentation stops consuming as much clinician time as the consultation. The patient gets a summary, the primary care provider gets a letter, and the outcome programme gets a structured record — all from a capture that was happening anyway. And the single largest source of clinician burnout in this setting is substantially reduced.
