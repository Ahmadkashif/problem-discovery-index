# The Care Coordinator Between Systems That Do Not Talk

**Industry:** [[telehealth-platforms|Telehealth Platforms]]
**Type:** Worker Life Changing
**One-liner:** The referral was made, the specialist needs records, the pharmacy needs a prior authorisation, and a coordinator is on the phone reconstructing a patient's care from four systems that do not connect.
**Tags:** #large-language-models #bert #gradient-boosting #graph-neural-networks #evaluation-metrics #compliance #worker-facing #workflow-orchestration

## The Problem
Care coordination is what makes episodic virtual care into something continuous, and it is performed by people with a telephone and several browser tabs. A referral needs an appointment and records sent. A prescription needs a prior authorisation the payer requires. A test result needs chasing from a laboratory. A patient needs their next appointment scheduled with a clinician licensed in their state.

None of the systems connect. The platform's record, the payer's portal, the pharmacy's system, the laboratory's interface and the receiving practice's office are separate, and the coordinator is the integration layer. Prior authorisation in particular is a well-documented administrative burden across US healthcare, performed by phone and fax, with outcomes that arrive days later and frequently require appeal.

The work is interrupt-driven and clock-bound. A prior authorisation blocking a medication has a patient waiting. A referral that has not been scheduled means a condition is not being managed. The coordinator holds the list of things that have not happened yet and chases each one.

And the failure modes are invisible until they are serious: the referral nobody booked, the abnormal result nobody followed up, the prescription the patient never collected.

## Why It Matters to the Worker
This is a role that absorbs the consequences of an unintegrated health system, and the people in it carry patients' outcomes personally without clinical authority. A coordinator knows which patients are stuck and spends their day trying to unstick them against organisations with no obligation to respond quickly.

The administrative work is genuinely demoralising in the way that phone-and-fax processes in a digital era are, and the volume means the individual attention any given patient receives is limited by a queue.

The emotional weight is real too. The people who are stuck are frequently the ones least able to advocate for themselves, and the coordinator is often the only person in the system paying attention to whether their care actually progressed.

And the loop-closure failures — the unfollowed abnormal result, the unbooked referral — are the ones that produce harm and are attributed to whoever last touched the case, which is usually here.

## What a Solution Looks Like
Track the loops as system state. Every referral, order, authorisation and prescription is an open loop with an expected closure event, and a system that knows which loops are open, overdue and at risk is the single most valuable thing a coordination function could have. Most of this is workflow rather than intelligence.

Automate the authorisation preparation. Prior authorisation requires assembling clinical justification against a payer's published criteria, which is document assembly against a rule set, and drafting the submission with the supporting evidence attached removes the bulk of the work. Predicting which requests will be denied, and why, allows the case to be made properly the first time.

Retrieve and route records automatically. Requesting external records through exchange networks and sending visit summaries onward with consent is technically routine and is done manually or not at all.

Rank by risk rather than by queue. An overdue referral for a suspicious finding and one for a routine review are not the same, and prioritising by clinical consequence rather than by age is straightforward triage that is not currently applied.

And detect the silent failures. A result that arrived and was never acknowledged, a prescription never collected, a referral never scheduled — each is detectable and each is a loop that would otherwise close only when something goes wrong.

## Impact If Solved
Care coordination is where episodic virtual care either becomes continuous care or fails to, performed manually against systems that do not connect. Loop tracking with risk-based prioritisation catches the failures that currently surface as harm; authorisation automation addresses a well-documented administrative burden; and automated record routing fixes the fragmentation that makes coordination necessary in the first place.
