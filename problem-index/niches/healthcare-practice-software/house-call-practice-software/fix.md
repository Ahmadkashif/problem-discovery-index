# Place of Service Decided by a Dropdown

**Niche:** [[niches/healthcare-practice-software/house-call-practice-software/profile|House-Call & Mobile Practice Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Whether a visit is billed as a home, assisted living or skilled nursing encounter changes the code and the reimbursement, and it is recorded by a clinician selecting from a dropdown in a parked car, from memory, hours later.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #compliance #revenue-impact #automation #quick-win
**Contested on:** Every serious competitor selling to house-call and mobile practices is fighting to make a visit charted in a basement with no signal reconcile cleanly — right patient, right place of service, right time, no lost data — and whoever makes the offline round-trip trustworthy takes the account.

## The Problem
Place of service looks like a trivial field and is one of the most consequential ones in this segment. A patient who moved from their own home into an assisted living facility three months ago is still billed as a home visit because nobody updated the address, or is billed as a facility visit when the practice's documentation does not support it. The coding sets differ, the documentation requirements differ, and the error is systematic rather than random — it follows the patient's address record, so it repeats every visit until someone catches it. Practices discover it in an audit or in a bulk recoupment, at which point it covers a year of encounters.

## Why It's Still Broken
The address that decides place of service lives in the demographic record, which is updated by whoever last spoke to a family member, and there is no event in any EHR for "this patient has moved into a facility." The clinician standing in the building knows, and is given a dropdown rather than a question. Billing staff working from the chart cannot see the building. And the error is invisible at the claim level because a home visit code against a facility address is a perfectly well-formed claim that a payer will pay — until it does not.

## What a Fix Looks Like
Use what the device already knows and ask the clinician once. The visit's location is captured at the door, with consent, and compared against the patient's recorded address and against a facility registry; a mismatch prompts a single question to the clinician while they are standing in the building, which is the only moment the answer is easy and free. Facility status becomes a dated attribute of the patient with a history, not a field that gets overwritten, so a claim can be validated against where the patient lived on the date of service rather than where they live now. And the standing report is the cheap part: every claim in the last year whose place of service disagrees with the patient's facility status on that date, which any practice can compute today and almost none have.

## Who Feels the Pain
Billers reconstructing where a patient lived eight months ago; clinicians who answered a dropdown correctly and are told their coding was wrong; and practice owners facing a recoupment covering a year of visits.

## Impact If Fixed
The retrospective report typically surfaces a concentrated set of patients whose facility transition was never recorded, each representing a run of mis-coded visits — recoverable in one direction and a genuine liability in the other. Capturing location at the door removes the error class prospectively and takes three seconds of a clinician's time, and it is the rare compliance control that is faster than the thing it replaces.
