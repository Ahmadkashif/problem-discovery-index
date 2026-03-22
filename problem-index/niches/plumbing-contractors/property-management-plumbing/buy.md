# Yardi/AppFolio Plugin for Plumbing Equipment Tracking and Compliance

**Niche:** [[niches/plumbing-contractors/property-management-plumbing/profile|Property Management Plumbing]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Property management software tracks work orders but doesn't know what plumbing equipment is installed in each unit — a plugin that adds equipment registry, age tracking, and compliance calendaring transforms a reactive work order system into a proactive asset management tool.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #quick-win

## The Problem
Yardi and AppFolio are the dominant property management platforms, but both treat maintenance as a work order flow: tenant reports problem → work order created → vendor assigned → work completed → invoice processed. There's no concept of equipment-level tracking. The system knows "Unit 302 had a plumbing work order on 3/15/2024" but doesn't know "Unit 302 has a 2015 Rheem 50-gallon gas water heater approaching end of life." This means: no age-based replacement planning, no warranty tracking (property managers miss manufacturer warranty claims because they don't know installation dates), no compliance calendaring (backflow preventer testing due dates, water heater earthquake strap requirements, Legionella testing in some jurisdictions), and no equipment-level cost tracking (what has Unit 302's water heater cost in total — purchase, installation, maintenance, and repairs — over its lifetime?).

## What Already Exists
Yardi's Equipment module and AppFolio's maintenance tracking handle HVAC equipment with serial numbers and service histories, but the implementation is HVAC-centric — designed for tracking furnaces and air conditioners, not plumbing assets. Both platforms have API access for third-party integrations. Facility management platforms (UpKeep, Fiix) handle equipment lifecycle management but are designed for manufacturing and commercial facilities, not multi-family residential.

## The Customization Gap
A plumbing-specific plugin for Yardi or AppFolio needs: (1) a plumbing equipment registry with pre-built asset types (water heater, backflow preventer, shut-off valve, sump pump, garbage disposal, water softener, expansion tank) and manufacturer/model lookup, (2) age-based replacement alerts with configurable lifecycle durations per asset type adjusted for water quality and usage, (3) compliance calendar integration — auto-generating annual backflow testing work orders, earthquake strap inspections, and jurisdiction-specific plumbing compliance tasks, (4) warranty tracking with manufacturer warranty claim deadlines and documentation requirements, (5) equipment-level cost tracking that aggregates all work orders, parts, and contractor invoices associated with a specific asset. Built as a Yardi Marketplace or AppFolio Stack app, priced per property ($2-5/unit/month) so the price scales with portfolio size.

## Target Customer
Property management companies managing 100-500+ units on Yardi or AppFolio, spending $100K-500K/year on plumbing maintenance, currently managing equipment tracking in spreadsheets or not at all, losing money to emergency replacements that could have been planned and missing warranty claims on prematurely failed equipment.

## Impact If Solved
Captures $2,000-5,000/year per 100 units in recovered warranty claims on prematurely failed equipment. Reduces emergency plumbing incidents by 30-50% through age-based proactive replacement, saving $20K-60K/year for a 200-unit portfolio. Eliminates backflow testing compliance violations ($500-2,000 per missed test per jurisdiction) by auto-generating testing work orders 30 days before due dates.
