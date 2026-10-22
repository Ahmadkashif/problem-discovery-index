# One Record per Structure

**Niche:** [[niches/outdoor-advertising-companies/site-leases-and-entitlements/profile|Site Leases & Entitlements]]
**Industry:** [[industries/outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A billboard location is a lease, two permits, a structure and a revenue stream held in four systems, and its risk can only be seen when they are joined.
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #workflow-orchestration #compliance
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep every permitted location in the portfolio, but that splits into two contests with different counterparties and different winners: against landowners and lease aggregators over rent and tenure, and against cities and state DOTs over the right to keep, convert or relocate a structure. Decomposed into contested sub-niches below.

## The Problem
When a structure is at risk (a lease expiring, a permit lapsing, a highway project approaching, a landlord selling), each department sees its own piece. Real estate has the lease, operations the structure, sales the revenue, legal the permit file. The value at risk, and which risk matters most, appears only when someone pulls all four together, usually too late.

## Why Nobody Has Built This
The records grew up separately over decades of acquisitions; each acquired plant brought its own lease files and numbering. Lease extraction from scans was too expensive until language models.

## What to Build
A structure-centred data model and ingestion pipeline: lease terms extracted from documents and amendments, permits matched to state and local registries, structure attributes and condition from operations, revenue by face from billing. On top of it sit a site-value estimate and a risk register that ranks every location by value times probability of loss, routed to the right team. This is the foundation both contested sub-niches need.

## Target Customer
VPs of real estate at operators with thousands of structures, especially those integrating acquired plants.

## Impact If Built
The portfolio is managed by value at risk instead of by whichever file landed on someone's desk, and losses through paperwork become rare.
