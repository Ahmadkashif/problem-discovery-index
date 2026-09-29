# Build: A Report Reader's Instrument

**Niche:** The Relying Customer
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Extract scope, exclusions, carve-outs, exceptions, testing depth and complementary user controls from every report automatically, compare across suppliers and across time, and route what the customer must act on.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #compliance #data-integration #automation
**Contested on:** Whether the party the report exists for can extract anything from it beyond whether it is clean and current.

## The Problem

A vendor risk analyst receives a SOC 2 report. They have perhaps twenty minutes and three hundred more reports this year.

They check the period, the type, the auditor and the opinion. They scan for exceptions. They file it and record the supplier as assessed.

Everything else stays in the document. The scope boundary that excludes a subsidiary. The two carved-out subservice organisations. The eleven complementary user entity controls that the customer themselves must implement for the supplier's controls to function — which are in the report because the auditor is required to list them and which almost nobody acts on. The exception in change management that was remediated in month nine. The fact that this year's scope is narrower than last year's.

Each of those is material to the decision the analyst is making and none of them is extracted.

The documents are structured enough to extract from. They follow a standard format with predictable sections. Scope is in the system description. Carve-outs are disclosed. Complementary user entity controls are in a defined section. Exceptions are tabulated. Pulling all of it into structured data is an ordinary extraction problem over a corpus with a consistent shape.

## Why Nobody Has Built This

**The reader is not the buyer of anything.** The report is commissioned by the supplier. The vendor risk platform market sells workflow rather than analysis. Nobody sells to the reading problem.

**Reports are PDFs with no structured export.** Extraction is necessary because the format is a document, and that is a decision made by the standard rather than by any vendor.

**The volume makes deep review look impossible.** Analysts have adapted to a binary check, so the aspiration to extract more feels unrealistic — until it is automated.

**Complementary user entity controls are an unclaimed obligation.** Nobody owns them on the customer side, so surfacing them creates work with no owner.

**Vendor risk platforms treat the report as evidence, not as content.** The artefact's existence satisfies the process, so the platform's job is storing it.

**The suppliers have no reason to help.** Structured export would make comparison easier, which is against the interest of suppliers with weaker reports.

## What to Build

**Extract the report into structured data.** Scope statement and exclusions, carve-outs with what they cover, trust services criteria, control matrix, exceptions with descriptions and management responses, complementary user entity controls, auditor, period and testing detail where stated.

**Present a one-page summary per report.** What is in scope, what is excluded, what is carved out, what exceptions were found, and what the customer must do. Twenty minutes becomes two.

**Route the complementary user entity controls.** These are obligations on the customer, listed in the report, that make the supplier's controls work. Extracting them and routing them to an owner is the highest-value output, because they are currently listed and ignored everywhere.

**Compare across suppliers.** Which suppliers have narrower scope, more exceptions, or carve out the functions that matter most. This is the comparison a vendor risk function cannot currently make.

**Track the same supplier over time.** Scope narrowing, new exceptions, auditor changes, period changes. A supplier whose scope shrank is a signal and is currently invisible.

**Flag what the report does not cover.** Where a supplier's report excludes a system that processes the customer's data, that is the finding, and it requires knowing both the exclusion and the data flow.

**Prioritise review by what matters.** Suppliers with broad access and narrow scope should reach an analyst; suppliers with narrow access and broad scope need less. This is the allocation the volume makes necessary.

## Target Customer

Enterprise vendor risk functions at large buyers, who process these at volume, and for whom the extraction converts an unread document into a usable input.

Vendor risk platform vendors, for whom report content extraction is an obvious feature adjacent to the storage they already provide.

Security and procurement leadership, who authorise supplier relationships on the basis of an artefact nobody in their organisation has actually read.

## Impact If Built

The report becomes readable at the volume its reader operates at, which is the practical difference between an artefact that informs a decision and one that documents that a step occurred.

Routing the complementary user entity controls is the highest-value single output, because those are obligations on the customer that are listed in every report and acted on in almost none.

And tracking scope across periods would catch a supplier's boundary narrowing, which is a meaningful signal that no current process would ever detect.
