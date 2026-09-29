# Fix: The Medication List Is Whatever the Patient Remembered

**Niche:** [[niches/telehealth-platforms/point-of-care-decision-support/profile|Point-of-Care Decision Support]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Interaction checking runs against a medication list the patient typed from memory, and the actual fill history is one query away on a network the platform already uses.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #compliance #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Whether the platform will pull the medication history it already has access to.

## The Problem

Every safety check in a virtual encounter — drug interactions, duplicate therapy, contraindications — runs against the medication list in the platform's record. That list came from a form the patient filled in, in which they wrote down the drugs they could remember, with the spellings and doses they could recall, omitting the ones they take intermittently and the ones prescribed by a specialist they saw once.

The actual list exists. Pharmacy fill history is available through the same e-prescribing network the platform uses to send prescriptions, is standard functionality, and shows what was actually dispensed and when. Many platforms do not query it, or query it and do not surface it prominently, so the safety checks run against the patient's memory.

This is not a subtle gap. It is the difference between checking an interaction against reality and checking it against a recollection.

## Why It's Still Broken

It was never anyone's task. E-prescribing was implemented to send prescriptions, which is what the product requires; medication history is a different call in the same integration and delivers no visible product feature, so it was not enabled.

Where it is enabled, the presentation frequently defeats it. A raw fill list of thirty entries over two years, unsorted and unreconciled, is not usable in a twelve-minute encounter, so clinicians stop opening it. Retrieval without condensation is close to useless, which has led some platforms to conclude the data is not valuable.

And consent handling adds friction that nobody has smoothed. Medication history access requires patient consent in most configurations, and asking for it clumsily at the wrong moment reduces uptake substantially.

## What a Fix Looks Like

Query it, reconcile it, and show the difference.

Turn on medication history in the e-prescribing integration and retrieve at booking rather than during the encounter, so it is present when the clinician opens the chart. This is a configuration and an integration call, not a project.

Ask for consent well. At signup, in plain language, explaining that it lets the clinician see what medications have actually been dispensed so they can check for interactions. Framed that way, consent rates are high; buried in a terms checkbox, they are not.

Reconcile automatically against what the patient stated and present the difference. Active medications with recent fills, medications the patient listed with no corresponding fill, and fills the patient did not mention. Each of the three is clinically meaningful and the third is where the interaction risk lives.

Show adherence gaps, which fall out of the same data. A prescription filled once six months ago and never refilled tells the clinician something important about a chronic condition, and it is visible in the fill dates.

Run the safety checks against the reconciled list rather than the stated one, and say which list was used.

Keep it to one screen with everything else collapsed behind it. The failure mode of this feature everywhere it has been tried is volume, and the fix is aggressive condensation with expansion available.

## Who Feels the Pain

Patients, whose interaction checks run against an incomplete list — most acutely those on multiple medications from multiple prescribers, who are exactly the population where interactions matter. Clinicians, who know the list is unreliable and have no better one. And the platform, whose safety apparatus is built on a foundation it could replace with a query on a network it already pays for.

## Impact If Fixed

Safety checking runs against dispensed reality rather than patient recall, which is the single cheapest clinical quality improvement available in this industry. The reconciliation surfaces discrepancies that are themselves clinically useful. And adherence becomes visible, which for chronic conditions is frequently the most important thing in the encounter.
