# Build: Resolution Measurement from Internal and Linked Data

**Niche:** [[niches/telehealth-platforms/clinical-outcome-measurement/profile|Clinical Outcome Measurement]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure whether the problem resolved, using return visits, prescription fills, follow-up responses and linked downstream data, per presentation and per clinician.
**Tags:** #survival-analysis #bayesian-inference #causal-inference #confidence-intervals #evaluation-metrics #gradient-boosting #compliance #data-integration
**Contested on:** Whether resolution can be established from signals that are all partial and mostly indirect.

## The Problem

A platform completes twenty thousand visits a month and knows nothing about what followed any of them. The patient closed the video window and left the measurement boundary.

Every signal that would establish resolution is partial and several are available. A patient who returns within two weeks for the same complaint probably did not get better. A prescription never collected from the pharmacy did not work because it was never taken. A patient who appears in an emergency department eight days after a reassurance was reassured wrongly. A follow-up message answered "still the same" is a direct answer.

None of these is definitive alone and together they are considerably better than nothing, which is the current state.

## Why Nobody Has Built This

The measurement crosses boundaries the platform does not currently cross. Emergency department presentations require claims or health information exchange linkage; fills require the medication history feed; both need agreements and integration work with no product feature attached.

There is also a selection issue that has deterred serious attempts: patients who improve have no reason to come back, so absence of a return visit conflates resolution with abandonment, switching to another provider, and giving up. Handling that properly requires a follow-up mechanism and honest treatment of non-response.

And the result is commercially double-edged. A platform that measures resolution well will find presentations it handles poorly, which is valuable internally and awkward externally, and the incentive to start has been weak while payers were buying on access.

## What to Build

A resolution model that combines every available signal with explicit uncertainty.

**Use the internal signals first, because they are free.** Return visit for the same complaint within a window — a survival framing, since time to return is informative. Escalation to a different modality. Message volume after the visit. Cancellation of a scheduled follow-up. These require no external data and are computable today from the platform's own database.

**Add the fill signal.** Whether the prescription was dispensed, and whether a chronic medication was refilled on schedule, through the e-prescribing network. Primary non-adherence — the prescription never collected — is common, is highly informative, and is invisible to every platform that does not query it.

**Link downstream where you can.** Emergency department and urgent care presentations after a virtual visit are the outcome that matters most for a reassurance decision, and they are obtainable through payer claims where a contract exists or through health information exchange participation. The subset of the population where this is available becomes the anchor for calibrating the internal signals against real outcomes.

**Ask the patient, briefly and well.** A single message at the right interval — is this better, the same, or worse — answered in one tap. Response rates are far higher for one question than for a satisfaction survey, and for many conditions a validated symptom scale takes ninety seconds and gives a far better measure. Treat non-response as informative and model it rather than discarding it.

**Report by presentation before by clinician.** The platform-level resolution rate per presentation is the number that matters most, is far more robust, and creates no individual jeopardy. Clinician-level attribution needs case mix adjustment and heavy shrinkage and should come second.

**Close the loop to the clinician.** A clinician who can see, for their own decisions, what share resolved and what share returned is getting the feedback the entire virtual workforce lacks — and it is the strongest argument for building any of this.

## Target Customer

Payer- and employer-contracted platforms, where outcome reporting is moving into contracts and where claims linkage is contractually available. This segment funds the measurement, and the direct-to-consumer business inherits it.

## Impact If Built

The platform learns which presentations it actually resolves and which it merely closes, which is the foundation for deciding what it should be treating at all. Clinicians get feedback on their decisions. And the industry acquires an outcome argument to make to payers, in a market that is moving from buying access to buying results.
