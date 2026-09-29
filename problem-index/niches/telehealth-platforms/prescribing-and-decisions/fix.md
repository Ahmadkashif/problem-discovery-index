# Fix: The Decision That Needs More Time Than the Schedule Allows

**Niche:** [[niches/telehealth-platforms/prescribing-and-decisions/profile|Prescribing & Clinical Decision-Making]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Visits per hour is the metric, the patient is a questionnaire and a video window, and the decision that would take longer is the one the schedule does not allow.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing #quick-win #compliance
**Contested on:** Whether a clinician can take the extra ten minutes a presentation needs without it costing them.

## The Problem

A clinician on a throughput target has a patient whose presentation is not straightforward. The right action is to spend longer — ask more questions, pursue the differential, look at the history, arrange a follow-up, or decide this needs in-person care. Every one of those costs time the schedule has allocated to the next patient.

The alternative, which is quicker and produces a satisfied patient, is to treat the presenting complaint as presented. Prescribe the thing, close the visit, move on. It is not negligent and it is frequently not right, and the system's incentives point at it every single time.

Clinicians describe this as the defining pressure of the work. It is not a training problem or a quality problem; it is a scheduling problem, and it is produced deliberately by a business model with thin per-visit economics.

## Why It's Still Broken

Because visits per hour is the unit economics of the business, and any change to it is a direct margin change. The measurement that would justify the change — that longer visits for complex presentations produce better outcomes and fewer escalations — has never been made, because outcomes are not measured.

The schedule is also uniform when the work is not. Every visit gets the same slot regardless of presentation, though the variance in what a presentation requires is enormous and substantially predictable from the intake questionnaire before the visit starts.

And the clinician has no mechanism to flag that a case needs more. Running over is absorbed personally, shows up in their metrics as slower throughput, and is not recorded as a clinical judgement.

## What a Fix Looks Like

Let the schedule respond to what the visit actually requires.

**Predict complexity before the visit from the intake.** Presentation, symptom duration, comorbidities, medication list, age, and prior visit history all predict how long an encounter will take, and the platform has every one of them from the questionnaire. A complexity score assigned at booking, allocating a longer slot where indicated, is a straightforward prediction problem with abundant labels from historical visit durations.

**Make running over legitimate.** A clinician should be able to mark a visit as extended for clinical reasons, with the reason recorded, and have it excluded from throughput metrics. This is a metric definition and a button. Without it, every clinician who does the right thing pays for it, and they know it.

**Give an explicit escalation route.** "This needs in-person care" or "this needs longer than I have" should be a supported action with a defined path — a same-day longer slot, a referral pathway, a specialist consult — rather than an abandonment of the visit. Where the only options are prescribe or nothing, prescribing wins.

**Measure the relationship.** Visit duration against return visits, escalations and downstream contacts, by presentation. If short visits for complex presentations generate more returns, the throughput target is costing money as well as care quality, and that is the argument that changes it. Nobody has computed it.

**Report what clinicians say.** Clinicians know which presentations the schedule does not accommodate and are rarely asked. A structured channel for that, reviewed by the medical director, is cheap and surfaces the problem cases faster than any model.

## Who Feels the Pain

Clinicians, who face the same conflict dozens of times a day between the schedule and their judgement, and who carry the professional risk of the decision either way. Patients whose presentation was not straightforward and who were treated as though it was. And the platform, which is generating downstream escalations and regulatory exposure from a scheduling parameter it has never evaluated against anything clinical.

## Impact If Fixed

The schedule starts reflecting what a presentation requires rather than an average, using a prediction the platform can make before the visit. Taking the clinically necessary extra ten minutes stops costing the clinician. And the platform finds out whether its throughput target is actually cheaper once the returns and escalations are counted — which is a question nobody has asked.
