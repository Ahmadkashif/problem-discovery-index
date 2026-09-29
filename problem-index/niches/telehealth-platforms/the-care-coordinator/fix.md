# Fix: Everything Attempted Is Unrecorded

**Niche:** [[niches/telehealth-platforms/the-care-coordinator/profile|The Care Coordinator]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The specialist office was called twice and did not answer, the payer said to resubmit, the patient was left a voicemail — and none of it is written anywhere.
**Tags:** #workflow-orchestration #descriptive-statistics #evaluation-metrics #data-integration #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Whether contact attempts and their outcomes will be captured as records rather than kept in someone's head.

## The Problem

A coordinator spends a morning on a case: two calls to a specialist office that rang out, a payer line that said the authorisation needs a different code, a voicemail for the patient, and a fax that may or may not have arrived.

None of it is recorded, or it is recorded as a free-text line in a ticket that the next person will not read. Tomorrow, someone else picks up the case and starts again — calls the same office, waits on the same payer line, leaves a second voicemail. The patient, if they call in, is asked questions they answered last week.

Everything the coordinator learned — this office only answers before ten, this payer wants the form by fax not portal, this patient works nights — evaporates.

## Why It's Still Broken

Logging is work done under pressure with no immediate return to the person doing it, and the tooling does not make it nearly free. A coordinator who has just spent nine minutes on hold is not going to write a structured note about it.

The systems also do not have anywhere natural to put it. Calls happen on a phone, faxes in a fax system, portal work in a browser, and the task system is a fourth place. A note about a call has to be typed into a system that was not involved in the call.

And nobody measures the cost. Duplicated effort, repeated calls and lost context are invisible because they look like ordinary work.

## What a Fix Looks Like

Capture the attempts automatically and give them a home.

Route outbound calls through the platform so the call is logged against the patient and the open item automatically, with duration and outcome. Transcribe where lawful and disclosed, so the substance is captured without anyone typing. This single change captures most of the lost information.

Log fax transmissions and receipts against the case, with inbound faxes parsed and attached to the right patient and item. Fax is the channel most likely to fail silently and least likely to be recorded.

Make the outcome a two-tap entry, not a text box. Reached, no answer, left message, needs callback, resolved, needs different action — plus an optional note. Structured outcomes are what make the history usable and the reporting possible.

Capture the counterparty knowledge as a shared record rather than a personal one. A directory entry per specialist office, payer line and pharmacy: best times, preferred channel, known requirements, typical turnaround. Built up from the logged attempts and editable. This is the institutional memory the role most needs and most lacks.

Show the full history when a case is opened, prominently. A coordinator picking up a case should see every prior attempt in ten seconds.

And report on it: contact attempts per closed item, by counterparty and task type. This identifies the specialist offices and payer processes that consume disproportionate effort, which is the information that justifies an integration or a different approach.

## Who Feels the Pain

Coordinators, who repeat each other's work, absorb the frustration of a third unanswered call, and cannot hand over a case without a conversation. Patients, asked the same questions repeatedly and left waiting while effort is duplicated. And the platform, which is paying for the same call twice and cannot see it.

## Impact If Fixed

Effort stops being duplicated because the record of what was tried exists. The accumulated knowledge about counterparties becomes shared rather than personal, which is what lets the function grow past the coordinators who have been there longest. And the platform finds out which counterparties consume its coordinators' time, which is the first step toward not spending it.
