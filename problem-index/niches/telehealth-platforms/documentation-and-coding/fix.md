# Fix: The Note Is Written Three Times

**Niche:** [[niches/telehealth-platforms/documentation-and-coding/profile|Documentation & Coding]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same information is typed into the intake by the patient, into the note by the clinician, and into the coding fields by someone else, because nothing carries forward.
**Tags:** #data-integration #workflow-orchestration #descriptive-statistics #evaluation-metrics #large-language-models #worker-facing #quick-win #automation
**Contested on:** Whether what the patient already typed will appear in the note without being retyped.

## The Problem

A patient completes a structured intake: symptoms, duration, severity, medications, allergies, history. Detailed, structured, and sitting in the platform's database.

The clinician opens the encounter, reads it, and then types much of it again into the note. Symptom description, duration, relevant negatives, medication list — re-entered as prose because the note template has fields that the intake did not populate.

Then the coding is derived, by the clinician or a coder, from the prose that was just written from the structured data that already existed.

The same information makes three journeys and is manually transcribed twice. In a nine-minute encounter this is a meaningful fraction of the total time.

## Why It's Still Broken

The intake and the note were built by different teams at different times for different purposes. The intake serves triage and routing; the note serves the legal record and billing; nobody connected them because neither team's requirements mentioned the other.

There is also a legitimate clinical concern that has been over-applied: a clinician should not attest to a history they did not take, and auto-populating a note from patient-entered data risks the note asserting things the clinician never verified. That is real, and the answer is to attribute the source — patient-reported, clinician-verified — not to retype it.

And the note templates are inherited from institutional practice, where there was no structured intake to draw from.

## What a Fix Looks Like

Carry the structured data forward with its provenance attached.

Pre-populate the note from the intake, with every pre-populated element visibly marked as patient-reported. The clinician confirms, amends or removes, and what they confirm becomes clinician-verified. This preserves the attestation properly and eliminates the transcription.

Redesign the note template around what is already structured. Fields the intake covers should not be free-text fields the clinician fills; they should be confirmations. The template should be designed for this setting rather than inherited from a clinic.

Derive the coding from the structured encounter rather than from the prose. The presentation, the decision, the complexity drivers and the time are all available as data, and coding from data is both more accurate and auditable. This also removes a downstream review step.

Keep the intake's own quality high, since everything now depends on it. Branching logic, clear questions, and validation — an intake that produces a good structured history is doing most of the documentation work.

Measure the time. Documentation minutes per encounter, before and after, by clinician and presentation. This is what justifies the work and what tells you whether the template redesign helped or just moved the effort.

And make the same structured record serve the other outputs — the patient summary, the primary care letter, the decision record — rather than generating each from the prose.

## Who Feels the Pain

Clinicians, for whom documentation is the largest non-clinical burden and a leading reason to leave, and who are retyping information that is on the screen in front of them. Patients, who answered the questions and are then asked them again. Coders and revenue cycle staff working from prose when structured data exists. And the platform, paying clinician time for transcription.

## Impact If Fixed

Documentation time falls substantially with no model and no new capability, purely by connecting two systems that already hold the data. The attestation stays clean because provenance is marked rather than hidden. And the structured record that results is what every other improvement in this industry — outcomes, prescribing analytics, write-back, continuity — needs and currently has to reconstruct from prose.
