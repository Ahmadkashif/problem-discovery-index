# Fix: Nobody Does the Complementary Controls

**Niche:** The Relying Customer
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every report lists the controls the customer must implement for the supplier's controls to work, and almost no customer implements any of them.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #worker-facing #workflow-orchestration #data-integration
**Contested on:** Whether the party the report exists for can extract anything from it beyond whether it is clean and current.

## The Problem

Every SOC 2 report contains a section listing complementary user entity controls. These are the things the customer must do for the supplier's controls to be effective — manage their own administrative accounts properly, configure the available security settings, review access they grant, monitor the logs the supplier provides, notify the supplier when a user leaves.

The auditor is required to list them because the supplier's control environment does not work without them. They are, in a real sense, the customer's half of the shared responsibility.

Almost nobody reads them. The report is scanned for the opinion, filed, and the section is not extracted. No owner is assigned. No control is implemented. And the customer relies on a supplier's controls whose effectiveness is explicitly conditional on actions the customer has not taken.

This is one of the clearest gaps in enterprise security practice. The supplier has done their part, has been audited on it, and has told the customer in writing exactly what the customer must do — and the customer files the document.

When something goes wrong in the shared boundary, the report is read carefully for the first time, and the section is found.

## Why It's Still Broken

**Nobody owns it on the customer side.** Vendor risk receives the report and does not implement controls. Security engineering implements controls and does not read vendor reports. The obligation falls between them.

**It is at the back of a long document.** The section is real, correctly placed by the standard, and read by nobody scanning a report for an opinion.

**Extraction is manual.** Pulling the list out of every supplier's report, for hundreds of suppliers, is work nobody has been assigned.

**The obligations are generic in wording.** Listed as principles rather than as specific configuration actions, which means translating them into work requires effort.

**The process measures assessment, not implementation.** Vendor risk is measured on suppliers assessed, and implementing complementary controls is not part of that.

**Nobody is asked about them.** Auditors do not ask the customer whether they implemented the controls their suppliers listed, and no framework requires it.

## What a Fix Looks Like

**Extract the section from every report received.** Even manually, for the critical suppliers, this is a few hours and produces a list nobody currently has.

**Assign an owner.** Each complementary control routed to whoever configures that system, as a ticket, like any other security work. This is the whole fix — the obligations are actionable and nothing routes them.

**Prioritise by supplier criticality.** Suppliers with access to the most sensitive data first. The list for all suppliers is long; the list for the top twenty is manageable and covers most of the exposure.

**Translate the generic wording into specific actions.** A stated obligation to review granted access becomes a specific quarterly review of a specific supplier's administrative accounts with a named reviewer.

**Track implementation and report it.** Complementary controls implemented, by supplier, reported alongside suppliers assessed. This is the metric that would make it happen.

**Ask suppliers to be specific.** A supplier listing generic principles could list the exact configuration settings and actions, and most would if asked — several already publish hardening guidance that is exactly this and is not connected to the report.

**Raise it with your own auditor.** An organisation's own attestation could reasonably cover whether it implements the complementary controls its suppliers require, which would create the forcing function that currently does not exist.

## Who Feels the Pain

The customer, relying on supplier controls whose effectiveness is explicitly conditional on actions they have not taken and were told about in writing.

The supplier, who did the work, was audited on it, disclosed the dependency clearly, and will nonetheless share the consequences when the shared boundary fails.

The vendor risk analyst, who received the information and had no mechanism to act on it.

And the security engineer, who would have implemented the controls if anyone had told them, and never saw the report.

## Impact If Fixed

Extracting the section and routing it to an owner is the entire fix, and the obligations are specific, actionable and already written down by somebody else.

Doing it for the top twenty suppliers covers most of the exposure and is a few hours of work, which makes this one of the highest-return security actions available to a vendor risk function.

And tracking implementation alongside suppliers assessed would convert an obligation that is currently listed everywhere and met nowhere into something the process actually produces.
