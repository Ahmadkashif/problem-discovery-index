# Build: Closed-Loop Referral and Order Tracking

**Niche:** [[niches/telehealth-platforms/care-coordination/profile|Care Coordination & Referral Closure]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Track every referral, order, authorisation and prescription to a confirmed outcome, with the open items ranked by clinical consequence.
**Tags:** #workflow-orchestration #data-integration #gradient-boosting #evaluation-metrics #confidence-intervals #survival-analysis #compliance #automation
**Contested on:** Whether closure can be confirmed for actions that complete in organisations the platform has no relationship with.

## The Problem

A virtual encounter produces actions the platform does not control. A referral to a dermatologist. A lab order. A prescription requiring prior authorisation. Each leaves the platform as a document or a message and enters a void.

Nothing confirms that the referral was booked, that the patient attended, that the lab was drawn, that the authorisation was approved, or that the medication was collected. The coordinator chases what they remember or what a patient calls about, and the rest is discovered when the patient returns, worse, having never seen the specialist because the practice never called them back.

Referral leakage and non-completion are well documented in healthcare generally and are worse here, where the referring party has no ongoing relationship with either the patient or the receiving provider.

## Why Nobody Has Built This

The actions complete outside the platform's systems, which has been read as meaning closure is unobservable. It is only partly true: prescription dispensing is reported on the e-prescribing network, lab results return through the ordering interface, authorisations have payer portal statuses, and referral attendance can be confirmed by the patient or, with exchange participation, by the receiving provider's record.

The deeper reason is accountability. The platform's obligation, as generally understood, ends when the referral is issued. Nobody is responsible for whether it completed, so nobody built the tracking, and the patient — the only party with a durable interest — has no tools at all.

And the work is unglamorous integration and workflow rather than anything novel, which loses every prioritisation argument.

## What to Build

An open-items ledger with automated closure and prioritised chasing.

**Make every post-encounter action a tracked object.** Referral, lab order, imaging, prescription, authorisation, follow-up appointment — each with a state, an owner, a due-by date and a clinical priority assigned at creation by the clinician. Today most of these are sentences in a note.

**Close what can be closed automatically.** Prescription dispensing from the e-prescribing network. Lab results returning through the ordering interface. Authorisation status from payer portals or integrations. Referral completion through exchange participation or the receiving provider's record where available. Each closure that happens without a human is a coordinator hour returned.

**Ask the patient for the rest.** A single message at the right interval — have you booked with the specialist yet, did you collect the prescription — closes a large share of the remainder and simultaneously prompts the action. One tap, well timed.

**Predict what will fall through.** Non-completion is predictable from the action type, the patient's history, the specialty, whether an authorisation is required, the wait time and prior behaviour. A model ranking open items by the probability of failure times the clinical consequence turns an unmanageable list into a chase queue, and this is what makes the whole thing operable at volume.

**Chase in priority order, automatically where possible.** Reminders to the patient, status queries to the payer, and escalation to a coordinator only for the items that need a human. The coordinator's day should be the residue, not the whole list.

**Measure closure rates.** By action type, specialty, payer and clinician. No platform can currently state what share of its referrals are completed, and it is both a quality metric and an argument to payers, for whom referral leakage is a direct cost.

## Target Customer

Platform operations leadership, where the case is coordinator productivity and clinical risk, and payer-contracted platforms, where closure rates are a quality and cost measure the payer cares about directly.

## Impact If Built

Actions that leave the platform stop disappearing. The coordinator works a ranked queue of things likely to fail rather than an undifferentiated list. And the platform can state its referral and order completion rates — a number the health system generally cannot produce and that payers will pay attention to.
