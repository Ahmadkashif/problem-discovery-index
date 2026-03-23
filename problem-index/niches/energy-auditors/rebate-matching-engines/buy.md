# Real-Time Program Rule Database

**Niche:** [[niches/energy-auditors/rebate-matching-engines/profile|Rebate & Incentive Matching Engines]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** DSIRE catalogs incentive programs but is a static reference database — auditors need a real-time, machine-readable rules engine that can evaluate specific building conditions against current program criteria.
**Tags:** #automation #data-integration #compliance #quick-win

## The Problem
DSIRE (the standard incentive reference) lists programs with descriptions, eligible technologies, and contact information — but the information is narrative text, not structured rules that a matching engine can evaluate. An auditor reading DSIRE's entry for a utility rebate sees: "Residential customers of [utility] may be eligible for rebates on qualifying ENERGY STAR heat pump water heaters installed by a licensed contractor. Rebate amount: $500-$800 depending on first-hour rating." This requires the auditor to: determine if the recommended equipment is ENERGY STAR certified, look up its first-hour rating, check if the contractor is licensed in the relevant state, and calculate the specific rebate amount. Each of these checks is manual, and the DSIRE entry may be 3-6 months out of date.

## What Already Exists
DSIRE provides the most comprehensive US incentive database with 2,500+ programs. EnergyStar.gov maintains a qualified product list. IRS provides tax credit guidance. Individual utility websites list current rebate programs. Rewiring America's Savings Calculator estimates IRA incentives by income level. None of these are structured as machine-readable rule sets that can be evaluated programmatically against specific building and measure parameters.

## The Customization Gap
The incentive matching challenge requires converting narrative program descriptions into structured evaluation rules: IF (utility_territory = "PG&E" AND measure_type = "heat_pump_water_heater" AND energy_star_certified = TRUE AND first_hour_rating >= 67) THEN rebate = $800. This rule structuring must be done for 2,000+ programs and updated continuously as programs change. The database must also handle income-qualified tiers (IRA provides higher incentives for households under 150% area median income), stacking rules (some incentives cannot be combined with others), and sunset dates.

## Target Customer
Incentive matching engine developers seeking the structured data backbone for their product, and large audit firms building internal incentive tracking systems for their auditors.

## Impact If Solved
Enables automated incentive matching that eliminates 1-2 hours of manual research per project, ensures incentive information is current within 30 days of program changes (versus the current 3-6 month lag), and provides the foundation for audit-integrated tools that transform incentive identification from a research task to an automatic output.
