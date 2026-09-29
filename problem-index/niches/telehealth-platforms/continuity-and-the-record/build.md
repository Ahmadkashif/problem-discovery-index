# Build: A Longitudinal Thread and a Write-Back to Primary Care

**Niche:** [[niches/telehealth-platforms/continuity-and-the-record/profile|Continuity & the Fragmented Record]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Build a patient thread the clinician actually sees at the start of every encounter, and send the encounter back to the patient's primary care provider automatically.
**Tags:** #large-language-models #data-integration #compliance #evaluation-metrics #confidence-intervals #workflow-orchestration #worker-facing #automation
**Contested on:** Whether a platform will send its encounter record to a provider it has no relationship with.

## The Problem

Virtual care is episodic by construction and fragmenting by omission. The episodic part is inherent; the fragmenting part is a choice.

Within the platform, a patient's third visit for the same recurring problem is handled by a clinician who sees an intake form. The two previous encounters, with their decisions and outcomes, exist in the database and are not on the screen. The clinician re-derives, re-prescribes, and the pattern that should have prompted a referral six weeks ago goes unnoticed because nobody has seen all three.

Outward, the encounter ends and the patient's actual doctor never learns it happened. A prescription was written, a diagnosis was considered, a reassurance was given — and the person responsible for the patient's overall care has no idea. The next time that patient sees them, the record has a hole in it.

## Why Nobody Has Built This

The internal thread is a product priority that has always lost to booking and matching. Prior encounters are technically accessible, which lets everyone believe the problem is solved, and clinicians under throughput pressure do not navigate to them.

The write-back is more interesting. It requires knowing who the patient's primary care provider is, which platforms rarely ask, and sending a clinical document to an organisation the platform has no contract with — which the interoperability frameworks now make technically routine and which carries a faint commercial disincentive: a platform that routes its encounters back into primary care is reinforcing a relationship it is in some sense competing with.

And nobody is accountable for the patient's record as a whole, which is exactly the condition that produces fragmentation.

## What to Build

A thread inside and a pipe outward.

**Construct the patient thread and put it in front of the clinician by default.** Every prior encounter on the platform with its date, presentation, decision, prescription and outcome signal, condensed into a short summary at the top of the encounter view, not behind a tab. Where there are many, generate a narrative summary with the important items surfaced — recurring presentations, escalating symptoms, repeat prescriptions of the same class, a decision that did not hold.

**Detect the patterns the thread reveals.** Three visits for the same complaint in two months. Escalating doses. Repeated presentations shortly after a prescription. Each of these is a flag that this patient needs something other than another episodic visit, and each is computable over the thread. This is where continuity turns into clinical value rather than a nicer screen.

**Ask who their doctor is and capture it properly.** At registration, with the practice identified against a provider directory rather than as free text. Without this the write-back has nowhere to go, and it is a single field most platforms omit.

**Send the encounter back.** A clinical summary to the patient's primary care provider after every encounter, via the interoperability frameworks or direct secure messaging, with the patient's consent captured clearly at registration. This is the same integration used for retrieval, run in the other direction, and it is the single most valuable thing a telehealth platform could do for the health system it operates in.

**Offer continuity where the condition needs it.** A named clinician for chronic and behavioural health, with the same patient returning to the same person. This works, it is what patients want, and it is operationally harder — but the thread makes it possible to identify which patients need it rather than offering it to everyone or nobody.

**Give the patient their own record.** Encounters, decisions, prescriptions, exportable. Patients are the one party with a durable interest in their own continuity and the one nobody equips.

## Target Customer

Platform clinical and product leadership, and payer contracts, where care coordination and record exchange are increasingly contractual expectations. Primary care organisations are a natural partner rather than a customer: they want the write-back badly and receive nothing.

## Impact If Built

The clinician sees the patient's history on this platform without navigating for it, and the patterns that indicate episodic care is no longer appropriate become visible. And the patient's own doctor finds out what happened — which is the difference between virtual care supplementing the health system and quietly fragmenting it.
