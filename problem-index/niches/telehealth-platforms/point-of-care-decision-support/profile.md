# Point-of-Care Decision Support

**Parent Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether the clinician has, at the moment of deciding, the history and the evidence the decision requires.

## Profile
**Market Size:** ~$4.86B — 60% of the prescribing and decision-making niche
**Share of Parent Industry:** ~16% of US virtual care delivery
**Digital Adoption:** Low — interaction alerts exist, actual history retrieval mostly does not
**Target Buyer:** Platform clinical informatics; clinicians themselves
**Automation Potential:** Very high — retrieval and surfacing are both solved problems elsewhere

## What Makes This a Distinct Niche

This is the half pointed at helping the person doing the work. A clinician opens an encounter with a questionnaire the patient filled in and whatever the patient remembers about their own medications. The things that would make the decision better — the actual medication list from pharmacy fill records, the problem list from a health information exchange, recent labs, prior visits on this platform for the same complaint, the guideline for this presentation, the features that should prompt escalation to in-person care — are retrievable and mostly not retrieved.

The distinguishing property is that nobody opposes it. The clinician wants it, the medical director wants it, the platform's interests align — better information produces better care, fewer adverse events, fewer escalations and a defensible clinical model. It is an engineering and integration problem with a clear internal sponsor.

It is also immediately useful with no measurement programme behind it. Putting a patient's real medication history in front of a prescriber improves the decision whether or not anyone ever measures the outcome.

## Current Tools & Gaps

E-prescribing networks with interaction and formulary checking, PDMP integration where mandated, licensed clinical reference content, and intake questionnaires with branching logic. Some platforms integrate with health information exchanges; most do not.

The gaps are retrieval and presentation. Pharmacy fill history is available through the e-prescribing network and is frequently unused. HIE and interoperability connections exist and require integration work nobody has prioritised. And what is surfaced is presented as EHR-style alerts designed for an institutional workflow rather than as a pre-visit brief suited to a twelve-minute encounter.

## Problems
- [[niches/telehealth-platforms/point-of-care-decision-support/build|🔨 Build: A Pre-Visit Clinical Brief from Retrieved History]]
- [[niches/telehealth-platforms/point-of-care-decision-support/buy|🛒 Buy: Interoperability and CDS Products Adapted to Episodic Virtual Care]]
- [[niches/telehealth-platforms/point-of-care-decision-support/fix|🔧 Fix: The Medication List Is Whatever the Patient Remembered]]
