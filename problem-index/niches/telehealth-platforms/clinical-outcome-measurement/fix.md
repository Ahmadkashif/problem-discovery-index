# Fix: The Return Visit Nobody Counts

**Niche:** [[niches/telehealth-platforms/clinical-outcome-measurement/profile|Clinical Outcome Measurement]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A patient coming back within two weeks for the same complaint is the clearest signal the platform has that something did not work, and it is counted as a second visit.
**Tags:** #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #worker-facing #automation
**Contested on:** Whether a repeat encounter will be read as a treatment failure rather than as revenue.

## The Problem

A patient has a virtual visit for a sore throat. Nine days later they have another virtual visit, on the same platform, for a sore throat.

In the platform's metrics that is two completed visits, two satisfaction surveys and two units of revenue. Nothing in any system connects the second to the first. The clinician seeing the second visit may be a different person who cannot see the first. And the most direct evidence the platform possesses that a clinical decision did not work is recorded as growth.

Return visits for the same complaint are computable today with a query over the existing encounter table. Nobody runs it.

## Why It's Still Broken

Because a repeat visit is revenue and there is no metric pointing the other way. In a business measured on visit volume, an encounter that generates another encounter is a good encounter, and the framing that would make it a bad one — treatment failure — does not exist anywhere in the reporting.

There are genuine complications. Matching a second encounter to a first requires the complaint to be identified consistently, which unstructured intake makes harder than it should be. Some returns are appropriate — the follow-up that was advised, the condition that was always going to need review — and distinguishing those from failures needs the clinician's plan to be recorded, which it frequently is not.

But the complications are modest and the signal is strong. A platform that computed return rates by presentation and clinician would learn a great deal in a week.

## What a Fix Looks Like

Count it, and make it a metric that points the right way.

Compute return rates by presentation. Same or related complaint within seven, fourteen and thirty days, per presentation, per clinician, per modality. Survival framing is better than a fixed window because the timing carries information — a return at three days means something different from one at twenty-five.

Separate advised from unadvised returns. When a clinician expects to see the patient again, record it as part of the plan at the first visit. Then a return that was planned is a plan working and one that was not is a signal. This is a field and a habit, and it makes the whole metric interpretable.

Show the second clinician the first visit. A patient returning for the same complaint should arrive with the prior encounter, the decision and the plan in front of whoever sees them. Its absence is both a clinical failure and the reason the return is invisible.

Give clinicians their own return rates, privately, case-mix aware, against the platform distribution. This is the single most useful feedback available to a clinician in this setting and it needs no external data at all.

Add the fill signal alongside it, since it comes from an integration the platform already has and answers the other obvious question — whether the treatment was ever started.

And put the return rate on the clinical dashboard next to visit volume, so the organisation has a number that moves in the opposite direction to throughput and someone is accountable for it.

## Who Feels the Pain

Patients who come back with the same problem to a clinician who cannot see that they have been here before. Clinicians, who never learn that a decision did not work and therefore cannot learn from it. And the platform, which is treating its clearest quality signal as a revenue line and will be asked about it by a payer sooner than it expects.

## Impact If Fixed

The platform acquires a resolution proxy from a query on data it already holds, at essentially zero cost. Clinicians see, for the first time, which of their decisions did not hold. And the metric set gains a number that points against throughput, which is what a clinical quality function needs in order to exist at all.
