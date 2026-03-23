# Cross-System Lot Traceability Gaps

**Niche:** [[niches/medical-device-mfg/class-ii-implantable-devices/profile|Class II Implantable Device Manufacturers]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Lot traceability — the ability to trace a finished implant back to every raw material, component, process step, and sterilization cycle — breaks at system boundaries, causing 15-25% of FDA 483 observations at implant manufacturers.
**Tags:** #data-integration #compliance #automation

## The Problem
FDA requires that implantable device manufacturers can trace any finished device to its component lots, manufacturing process records, and sterilization records. In practice, this traceability chain breaks at system boundaries: ERP tracks component lots by purchase order, MES tracks production by work order, sterilization monitoring tracks by load number, and the QMS tracks by DHR lot number. When these systems use different identifiers or when manual data entry introduces errors at handoff points, the traceability chain has gaps. Quality engineers spend 5-10 hours per week manually reconciling traceability discrepancies, and during FDA inspections, inability to demonstrate full traceability within a reasonable timeframe triggers 483 observations.

## Why It's Still Broken
Each system (ERP, MES, sterilization monitoring, QMS) was purchased independently, often from different vendors, at different times. Integration was not a purchase criterion because traceability was handled manually by quality technicians who knew which lot number in System A corresponded to which work order in System B. As these technicians retire or leave, the institutional knowledge of how to navigate the traceability chain across systems is lost. Custom integration projects are expensive ($200-500K) and brittle — any system upgrade breaks the integrations.

## What a Fix Looks Like
A lightweight middleware layer that maintains a master lot genealogy — a graph linking every identifier (PO lot, work order, production lot, sterilization load, DHR number) across systems. It ingests data from ERP, MES, sterilization monitoring, and QMS via API, flat file, or database connector, automatically detects identifier mismatches, and alerts quality technicians to reconcile discrepancies in real time rather than discovering them during DHR assembly or FDA inspection. The genealogy graph can answer the question "show me everything associated with this implant serial number" in seconds.

## Who Feels the Pain
Quality technicians who spend hours chasing lot numbers across systems, quality engineers who must demonstrate traceability during FDA inspections, and quality directors who receive 483 observations for traceability failures that were preventable.

## Impact If Fixed
Traceability query time drops from 30-60 minutes to under 1 minute. 483 observations related to traceability gaps decrease by 60-80%. DHR assembly prerequisite work (lot reconciliation) drops from hours to minutes per lot.
