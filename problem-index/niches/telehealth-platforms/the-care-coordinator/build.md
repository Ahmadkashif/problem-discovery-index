# Build: One Patient View and an Automated Residue

**Niche:** [[niches/telehealth-platforms/the-care-coordinator/profile|The Care Coordinator]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consolidate the four systems into one patient view, automate the retrieval and status chasing, and leave the coordinator the conversations that actually need a person.
**Tags:** #workflow-orchestration #data-integration #large-language-models #evaluation-metrics #gradient-boosting #confidence-intervals #worker-facing #automation
**Contested on:** Whether the manual cross-organisation work can be automated when the counterparties are phone lines and fax machines.

## The Problem

A coordinator's work is retrieval and transcription across systems that were never meant to meet. Look up the patient in the clinical record. Log into the payer portal and re-enter their details to check an authorisation. Call the specialist office and read out the referral. Fax the records. Call the pharmacy. Update the spreadsheet. Repeat, forty times a day.

Almost none of it requires clinical judgement or even much judgement at all. It requires persistence, a telephone and the ability to hold a great deal of state. The genuinely valuable part of the role — talking to a confused patient, persuading a specialist office to fit someone in, working out why an authorisation keeps being denied — is squeezed into whatever is left.

## Why Nobody Has Built This

Coordination is a cost centre and the automation is unglamorous integration against counterparties who are not cooperating. Payer portals have no APIs for most plans. Specialist offices communicate by phone and fax. There is no elegant technical solution, only a lot of specific, fiddly work.

The role is also invisible to the product organisation. Coordinators are operations staff; the product team builds for clinicians and patients; and a tool for the people holding the middle together has no natural owner.

And the case for it has never been made numerically, because nobody has measured where a coordinator's time goes.

## What to Build

A coordinator workbench that consolidates, automates the mechanical and ranks the rest.

**One patient view.** Clinical record, open actions with their states, prior contact attempts with outcomes, payer and coverage details, pharmacy, and the communication history with every party. The coordinator should never need a second tab for the common case, and today they need four.

**Automate the portal work.** Authorisation status checks, eligibility verification and claim status across payer portals — increasingly available through clearinghouse APIs and automation vendors, and where not, through robotic automation against the portals themselves. This is the largest single consumer of coordinator time and the most automatable.

**Handle the phone and fax counterparties.** Automated outbound for status checks where the counterparty accepts it, inbound fax parsing into structured records, and transcription of calls into the contact log. The fax layer specifically is worth building: a large share of inbound documents arrive that way and are currently read and retyped.

**Rank the queue by consequence.** Which open items are most likely to fail and matter most clinically. A coordinator working a ranked list instead of a chronological one is the difference between covering the important things and covering the recent ones.

**Record every attempt.** Who was called, when, what happened, what was promised. This is the institutional memory the role currently keeps in one person's head, and it is why a handover loses everything.

**Draft the communications.** Referral letters, records requests, authorisation appeals and patient messages generated from the record for review rather than composed. Much of the writing is templated with patient specifics inserted, which is exactly the task to automate.

**Measure where the time goes.** Time by activity, by payer, by specialty, by task type. Nobody has this, and it is what identifies which integration to build next.

## Target Customer

Platform operations leadership, where the case is coordinator productivity at a function that scales linearly with visit volume and is therefore a growing cost. Payer-contracted platforms have the additional argument that coordination quality shows up in closure rates the payer is measuring.

## Impact If Built

The coordinator stops being a human integration layer between four systems and starts doing the part of the job that requires a person. The mechanical work — portal checks, status chasing, document handling, drafting — moves to automation. And the record of what was attempted stops living in one person's memory.
