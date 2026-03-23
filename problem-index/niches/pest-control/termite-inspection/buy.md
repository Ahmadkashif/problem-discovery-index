# WDO Report Platform with Treatment Integration

**Niche:** [[niches/pest-control/termite-inspection/profile|Termite Inspection & Treatment]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Home inspection platforms generate WDO reports but don't connect findings to treatment proposals, chemical selection, or warranty contracts.
**Tags:** #workflow-orchestration #data-integration #automation

## The Problem
Termite inspection generates a WDO report (state-mandated form for real estate transactions), but the report is a dead end — it documents findings but doesn't feed into treatment planning. When the inspector finds active termites, the company must separately create a treatment proposal (chemical type, application method, warranty terms, price) by hand, often re-entering the same property information. The treatment proposal must reference the inspection findings, but there's no structured data flow between the two documents.

## What Already Exists
HomeGauge, Spectora, and Palm-Tech handle home/WDO inspection reports. PestPac and ServSuite handle pest treatment operations and customer management. The inspection report lives in one system, the treatment proposal in another, and the warranty contract in a third (or in a filing cabinet). No platform spans the full lifecycle: inspection → treatment proposal → contract → treatment delivery → warranty tracking.

## The Customization Gap
The platform needs to flow inspection findings directly into treatment proposal templates: identified pest species maps to recommended treatment protocol, affected area maps to treatment zone diagram, and construction type maps to application method (slab injection vs. soil trench vs. bait station). The treatment proposal should auto-generate pricing from a configurable rate card, and accepted proposals should create work orders and warranty contracts automatically.

## Target Customer
Termite companies doing 30+ inspections per month that currently re-key inspection data into treatment proposals, losing 20-30 minutes per proposal.

## Impact If Solved
Saves 10-15 hours per month in administrative re-work, reduces proposal turnaround from 24-48 hours to same-day (critical in competitive real estate transaction timelines), and ensures treatment protocols match inspection findings without manual translation errors.
