# Multifamily-Specific Energy Audit and Modeling Platform

**Niche:** [[niches/energy-auditors/multifamily-retrofit-auditors/profile|Multifamily Retrofit Auditors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No energy modeling tool handles the unique structure of multifamily buildings — residential units with individual conditions plus shared mechanical systems and common areas.
**Tags:** #workflow-orchestration #data-integration #automation #revenue-impact

## The Problem
A 100-unit apartment building has: a central boiler serving all units, individual window AC units in each apartment, common area lighting in hallways and lobbies, a parking garage ventilation system, 5-8 distinct unit floor plan types with different orientations and envelope exposure, and utility billing that may be master-metered (owner pays all) or individually metered (tenants pay electric, owner pays gas). An auditor must model this building holistically — but residential tools (TREAT) can model one unit at a time and cannot represent central systems, while commercial tools (eQUEST) model the building as a single entity and cannot represent unit-level variation. The auditor ends up running 3-4 partial models and manually combining results, a process that takes 20-40 hours per building and produces inconsistent results.

## Why Nobody Has Built This
Multifamily energy modeling requires combining residential-style unit modeling (individual envelopes, occupant behavior, in-unit equipment) with commercial-style central system modeling (boilers, cooling towers, distribution losses, common area loads) and a financial analysis layer that handles split-incentive economics. This combined model is technically complex and the market (multifamily audit firms) is too small for major software vendors to prioritize. The DOE has funded prototype tools (BETTER, Building Energy Asset Score) but none have achieved production-grade modeling for multifamily-specific use cases.

## What to Build
An energy modeling platform designed for multifamily buildings that: models individual unit types with envelope, orientation, and in-unit equipment variations; represents central mechanical systems with distribution losses; handles common area loads separately; combines unit-level and building-level results into whole-building energy projections; and performs split-incentive financial analysis showing which improvements benefit the owner (central systems, common areas) versus tenants (in-unit equipment), with options for utility billing restructuring (RUBS, sub-metering) that align incentives.

## Target Customer
Energy audit firms specializing in multifamily buildings (typically 50-500 unit properties), housing authorities auditing public housing portfolios, and ESCOs pursuing multifamily performance contracts.

## Impact If Built
Reduces per-building audit time from 30-50 hours to 15-25 hours by eliminating multi-model reconciliation, produces more accurate savings projections by modeling unit-level and building-level interactions simultaneously, and enables auditors to address the split-incentive barrier with data-driven financial analysis.
