# Multi-Department Fleet Dashboard with Budget Allocation Tracking

**Niche:** [[niches/fleet-managers/municipal-vehicle-fleets/profile|Municipal Vehicle Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No fleet management tool allocates vehicle costs (fuel, maintenance, depreciation) back to individual city departments for internal billing — the fleet superintendent can't show the police chief how much their fleet actually costs.
**Tags:** #data-integration #automation #workflow-orchestration #revenue-impact

## The Problem
A city fleet of 200 vehicles serves 8 departments (police, fire, public works, parks, water, administration, inspections, transit). The fleet superintendent manages all vehicles centrally but each department has its own budget for fleet costs. Currently, fuel costs are allocated by department fuel card, but maintenance costs are tracked as a lump sum in the fleet budget — no one knows that the police department consumed 55% of the maintenance budget because high-idle cruisers destroy engines and transmissions. Without per-department cost visibility, budget requests are based on historical allocation rather than actual consumption, and the departments destroying vehicles fastest get subsidized by departments that maintain theirs carefully.

## Why Nobody Has Built This
Commercial fleet management tools assume a single entity owns and operates the fleet for a single purpose. Municipal internal billing requires cost allocation by department, vehicle class, and budget line item — concepts that don't exist in commercial fleet software. Government accounting standards (GASB) require specific depreciation and capitalization rules for fleet assets that commercial tools don't implement.

## What to Build
A municipal fleet cost allocation layer that tracks all vehicle costs (fuel, maintenance, parts, depreciation, insurance) by vehicle and department, produces monthly internal billing reports per department, and generates annual budget-request data showing each department's true fleet cost with trend analysis. It should support GASB-compliant asset depreciation and produce reports formatted for city council budget presentations.

## Target Customer
City and county fleet superintendents managing 50-500 vehicles across 5+ departments who currently cannot tell department heads what their fleet costs.

## Impact If Built
Enables data-driven fleet budgeting that reduces total fleet costs by 10-15% through accountability — departments that see their costs invest in driver training and vehicle care. Saves 20-30 hours per month of manual cost tracking and report preparation during budget season.
