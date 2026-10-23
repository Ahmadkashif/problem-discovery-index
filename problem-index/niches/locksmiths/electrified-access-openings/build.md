# A Function and Wiring Check Before the Door Is Hung

**Niche:** [[niches/locksmiths/electrified-access-openings/profile|Electrified Hardware & Access-Ready Openings]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Many electrified-door commissioning failures are visible on paper before installation, a fail-secure lock on a stair door or a strike with no power transfer, but nobody checks the hardware schedule against the access point schedule door by door.
**Tags:** #large-language-models #transformers #graph-theory #compliance #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to deliver electrified locks, strikes and exit devices that work with the client's access-control system and still release for egress and fire alarm the day the door is commissioned, and whoever passes commissioning without a return visit takes the account.

## The Problem
On a new building or a retrofit, the door-hardware schedule (one document) lists each opening's hardware set. The access-control point schedule (another document, from another trade) lists which doors get readers, how they lock and what releases them. The two are drawn by different people at different times. Mismatches surface on site: an electrified lock with no power transfer hinge, a fail-secure strike on a door that must release on fire alarm, a request-to-exit device that the exit device's own switch duplicates. Each one means reordering hardware and a return visit, often after the inspector has failed the door.

## Why Nobody Has Built This
The two schedules belong to two trades and two software worlds: hardware consultants and distributors on one side, integrators on the other. Neither side's tools read the other's output, and the documents are PDFs with inconsistent naming.

## What to Build
A checker that extracts both schedules from PDFs and spreadsheets and links them by opening number. It models each opening as a small graph (credential, controller, power, lock, release inputs, fire-alarm interface) and tests it against rules: fail mode against egress and fire requirements, power path present, monitoring devices present and not duplicated, and voltage and current within the power supply's capacity. It produces a door-by-door conflict list before ordering and a commissioning checklist per door after installation.

## Target Customer
Commercial locksmith and door-hardware firms subcontracting electrified hardware on integrator and general-contractor projects; integrators who want fewer return trips.

## Impact If Built
Conflicts are caught at submittal rather than at the inspection, saving a reorder and a site visit per affected door. On a project with dozens of electrified openings that can decide whether the hardware scope makes money (estimate).
