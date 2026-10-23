# Every Inspector's Report Turned Into Tracked Deficiencies

**Niche:** [[niches/facilities-management-firms/statutory-inspection-compliance/profile|Statutory Inspection & Life-Safety Compliance]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dozens of inspection subcontractors each send a PDF in their own format, and the deficiencies in them become repairs only if someone reads every page.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to know, site by site, which code-required inspections are due, done and passed, and whoever closes each inspector's deficiency into a completed repair before the fire marshal, the insurer or the client's auditor asks takes the account.

## The Problem
A portfolio of a few hundred sites generates thousands of inspection reports a year across sprinkler, alarm, door, generator, elevator, boiler and backflow vendors. Each lists deficiencies in its own wording and severity scheme. A compliance coordinator reads them, re-keys the important ones into work orders and tracks the rest in a spreadsheet. Impairments, conditions that take a life-safety system partly out of service, are mixed in with housekeeping items.

## Why Nobody Has Built This
Inspection software is sold to the inspecting contractor, who has no reason to standardise output for the FM firm. CMMS vendors schedule the inspection but treat the report as an attachment. Reading free-form reports reliably was not practical until recently.

## What to Build
An ingestion layer that reads every vendor report, extracts each deficiency with location, system, code reference and severity class (impairment, critical, non-critical), and creates the repair work order with a due date driven by the severity class and the jurisdiction's rules. It keeps a portfolio frequency library mapped to each site's systems and adopted code edition, so missing inspections show up as gaps before the due date passes.

## Target Customer
Compliance and EHS managers at FM providers with multi-site portfolios, and client-side risk managers who need assurance across providers.

## Impact If Built
Coordinators stop re-keying, impairments surface the day they are found, and the portfolio's compliance status becomes a fact rather than a spreadsheet's opinion.
