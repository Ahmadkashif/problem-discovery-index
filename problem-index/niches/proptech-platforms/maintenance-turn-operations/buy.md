# Condition-Based Maintenance Applied to the Unit

**Niche:** [[niches/proptech-platforms/maintenance-turn-operations/profile|Maintenance & Turn Operations]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Condition-based and reliability-centred maintenance are settled industrial disciplines, and rental housing runs preventive maintenance off a calendar that treats a six-year-old water heater and a sixteen-year-old one identically.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #hypothesis-testing #automation #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
Preventive maintenance in rental housing is a schedule: filters quarterly, inspections annually, water heater flush on a cycle. Meanwhile the operator holds every repair ever performed on every component in every unit, which is a complete failure history across tens of thousands of instances of the same components in the same conditions. A water heater in its fourteenth year in a hard-water submarket with two prior repairs is a different risk from a four-year-old one, and both receive the same calendar treatment — so money is spent on units that did not need it and emergency calls come from units that did.

## What Already Exists
Reliability-centred maintenance, failure-mode analysis and condition-based scheduling are mature industrial disciplines with a large literature and standard methods. Survival analysis tooling is commodity. Component failure data for building systems exists in manufacturer and industry sources. Smart-home and leak sensors are cheap, increasingly installed for other reasons, and produce a genuine condition signal. Everything needed is available.

## The Customization Gap
The adaptation is to a housing portfolio's data and its economics. It requires: (1) building component-level failure models from the operator's own repair history rather than from manufacturer expectations, which means inferring component identity and age from repair records where no asset register exists — the same equipment-record problem that appears in field service; (2) modelling the consequence rather than only the failure, since a failed water heater in a ground-floor unit and one above three occupied apartments are different events and the expected cost, not the probability, should drive the schedule; (3) turnover as an intervention point, because the cheapest moment to replace anything is when a unit is vacant and no current product connects component risk to the turn calendar; (4) incorporating sensor signal where it exists without requiring it, since coverage will be partial for years; and (5) expressing the output as a replacement and inspection plan with a budget, which is how capital planning in this industry actually happens.

## Target Customer
Multifamily and single-family operators with large portfolios and ageing assets, and the platform vendors whose preventive maintenance modules are calendars.

## Impact If Solved
Shifting preventive spend from a calendar to a risk-weighted plan reduces emergency calls, which are the most expensive and most resident-damaging maintenance events, while cutting unnecessary scheduled work. Tying component replacement to the turn calendar is the single largest cost saving available and requires only that two existing systems be connected.
