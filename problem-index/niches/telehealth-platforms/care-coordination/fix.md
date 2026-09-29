# Fix: The Prescription That Was Never Collected

**Niche:** [[niches/telehealth-platforms/care-coordination/profile|Care Coordination & Referral Closure]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The e-prescribing network reports whether a prescription was dispensed, and nobody looks, so the most common treatment failure is invisible.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #quick-win #automation #worker-facing
**Contested on:** Whether the platform will read the dispense notification it already receives.

## The Problem

A clinician prescribes. The prescription is transmitted to a pharmacy. A meaningful share of prescriptions are never collected — primary non-adherence is well documented and runs into the double digits for many drug classes, higher for expensive ones and for patients without coverage.

The e-prescribing network reports dispensing. The information is available, on an integration the platform already operates, and nobody consumes it. So a patient whose prescription cost $180 at the counter and who walked away without it is recorded as a successfully treated patient, and the platform's first indication that anything is wrong is a return visit a fortnight later, if there is one.

This is the most common treatment failure in the entire industry and it is invisible by omission.

## Why It's Still Broken

The e-prescribing integration was built to send, and the dispense notification is a different message on the same connection that nobody enabled. There is no product feature attached to it, so it was never prioritised.

Responsibility is also ambiguous once the prescription leaves. The prescriber's obligation is generally understood to end at transmission, the pharmacy's begins at receipt, and the gap between them belongs to nobody. A platform with no ongoing relationship with the patient has even less reason to claim it.

And the most common cause — cost at the counter — is one the platform feels unable to influence, which has made it feel like information without an action attached. It is not: a cheaper alternative, a coupon, a therapeutic substitution or a different pharmacy are all available responses.

## What a Fix Looks Like

Read the notification and act on the gap.

Enable dispense notifications on the e-prescribing integration and reconcile them against prescriptions written. This is a configuration and a job, and it produces the platform's first non-adherence number within a week.

Reach out when a prescription is not collected within a few days. A short message — we noticed you have not picked this up, is there a problem with cost or availability — resolves a substantial share, because the reason is usually specific and fixable. Cost, pharmacy stock, the patient went to a different pharmacy, or they changed their mind and should be talking to a clinician about that.

Prevent it at the point of prescribing where possible. Real-time benefit checking, available through the e-prescribing network, shows the patient's actual cost before the prescription is sent, and a clinician who can see that the first-line choice will cost $180 and an equivalent will cost $12 makes a different decision. This is the single most effective intervention and it is a feature many platforms have not turned on.

Track refills for chronic medications too, where the same signal shows a patient who stopped.

Report the rate by drug class, clinician and payer. It is a quality metric, it is a genuinely interesting clinical finding, and for a payer-contracted platform it is a number the payer wants and does not have.

And close the loop to the clinician, who currently has no idea that a share of their prescriptions are never taken.

## Who Feels the Pain

Patients who left without their medication and were counted as treated — disproportionately those without coverage or with high deductibles, for whom the counter price is the barrier. Clinicians, who do not know it happens and cannot account for it. Coordinators, who find out through a return visit. And the platform, whose outcome measurement is built on the assumption that prescribed means taken.

## Impact If Fixed

The most common treatment failure becomes visible, from a message the platform already receives on a connection it already pays for. Cost-driven abandonment gets caught within days and is usually resolvable. And real-time benefit checking at the point of prescribing prevents a large share of it from happening at all.
