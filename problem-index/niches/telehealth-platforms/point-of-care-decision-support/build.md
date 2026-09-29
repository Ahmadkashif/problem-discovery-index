# Build: A Pre-Visit Clinical Brief from Retrieved History

**Niche:** [[niches/telehealth-platforms/point-of-care-decision-support/profile|Point-of-Care Decision Support]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Retrieve the patient's actual medication, problem and visit history before the encounter and present it as a one-screen brief with the decision-relevant facts surfaced.
**Tags:** #large-language-models #data-integration #evaluation-metrics #confidence-intervals #compliance #bayesian-inference #worker-facing #automation
**Contested on:** Whether external clinical history can be retrieved and condensed reliably enough to be trusted in a twelve-minute encounter.

## The Problem

The clinician's information disadvantage in virtual care is treated as intrinsic to the modality. Much of it is not. A substantial share of what an in-person clinician would have — current medications, chronic conditions, recent encounters, relevant labs — exists in retrievable systems: pharmacy fill data through the e-prescribing network, clinical summaries through health information exchanges and interoperability frameworks, prior visits on this platform, and payer claims where the platform has a payer contract.

None of it is in front of the clinician when they open the encounter. They have a form the patient completed, which for medications means whatever the patient could recall and spell, and which for chronic conditions is systematically incomplete.

The physical examination cannot be recovered. The record largely can, and conflating the two has meant nobody tried.

## Why Nobody Has Built This

Interoperability integration is unglamorous, slow and politically awkward — each network has its own onboarding, participation requirements and data-use terms, and the payoff is invisible in any product metric. It competes for engineering attention against features that increase visit volume and loses.

There is also a presentation problem that has sunk attempts: retrieving a patient's full clinical summary produces pages of documents, and a clinician with twelve minutes cannot read them. Retrieval without condensation makes the encounter slower, which is why clinicians who have had access to raw HIE data in this setting mostly stopped using it.

And some platforms have been ambivalent about knowing more. A complete history occasionally reveals that the visit should not be handled virtually, which is a completed visit lost.

## What to Build

A retrieval and condensation layer producing a brief, ready before the encounter opens.

**Retrieve from every available source.** Pharmacy fill history through the e-prescribing network — this alone is the highest-value single source and is frequently already accessible. Clinical summaries through the interoperability frameworks. Prior encounters on this platform. Payer claims where a contract exists. PDMP where relevant and permitted. Run retrieval asynchronously at booking so the data is ready before the clinician opens the encounter.

**Condense into a brief, not a chart.** One screen: active medications with fill dates and adherence gaps, chronic conditions, allergies, recent encounters with dates and reasons, relevant results, and prior visits for this complaint. Generated with a model and every item traceable to its source, so the clinician can expand any line to the original document. The condensation is the product — retrieval without it makes the encounter worse.

**Surface the decision-relevant facts explicitly.** Not the whole picture but the two or three things that bear on this decision: an interaction with what is being considered, a recent prescription for the same complaint from another provider, a condition that contraindicates the obvious treatment, a pattern of repeat visits for the same symptom. This is where the clinical value concentrates.

**Reconcile against what the patient said.** Where the fill history and the patient's stated medication list differ — which is most of the time — show the difference rather than replacing one with the other. The discrepancy is itself clinically informative and the patient may be right.

**Flag escalation features.** Presentation characteristics that should prompt in-person assessment, drawn from the licensed guideline content and tuned to this platform's scope. Surfaced early, before the clinician has committed to a course.

**Measure whether it helps.** Time to decision, prescribing changes, escalation rates and adverse events, with and without the brief. This is measurable and is what turns an integration project into a funded programme.

## Target Customer

Platform clinical informatics and medical leadership, where the case is care quality and risk reduction, and payer-contracted platforms, where clinical data exchange is frequently already contemplated in the contract and simply not implemented.

## Impact If Built

The clinician starts the encounter knowing what the patient is actually taking and what they have actually been treated for, which is the largest single information gap in virtual care and is substantially closable. Decisions improve where the retrieved history contradicts the questionnaire, which is often. And the platform's clinical model becomes defensible on the basis that its clinicians had the record.
