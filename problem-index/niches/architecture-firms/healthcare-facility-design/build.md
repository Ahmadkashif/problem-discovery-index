# Room Data Sheets Checked Against FGI and State Rules

**Niche:** [[niches/architecture-firms/healthcare-facility-design/profile|Healthcare Facility Design]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A hospital has thousands of rooms, each with regulated minimums for area, clearance, gases, outlets and air changes, and conformance is checked by people comparing room data sheets to the Guidelines.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver clinical planning that passes FGI Guidelines-based state review (HCAI in California) on the first submission and matches the health system's operating model, and whoever holds that clinical and regulatory record wins the system's next project.

## The Problem
For every room type — exam room, ICU bed, procedure room, sterile processing — the FGI Guidelines and state amendments set minimum clear floor area, clearances around the bed, hand-washing stations, medical gas outlets, electrical receptacles and ventilation requirements. The architect's room data sheets and the model must meet them, the MEP engineers' design must match, and the state reviewer checks them. Discrepancies discovered in agency review cost a review round and sometimes a redesign.

## Why Nobody Has Built This
The rules are in prose and tables across the Guidelines, ASHRAE 170 for ventilation and state amendments, revised on multi-year cycles; translating them into machine-checkable rules is specialist work with a narrow market. Room data tools hold the data but not the regulation.

## What to Build
A rule library encoding FGI, ASHRAE 170 and major state amendments by room type, linked to the room data sheets and the Revit model, that checks every room continuously and produces a conformance report in the reviewer's terms. Each state review comment received is mapped back to the rule, so the library learns what reviewers actually enforce.

## Target Customer
Healthcare practice leaders and technical directors at firms with dedicated healthcare studios, and health system design and construction teams.

## Impact If Built
Fewer agency review rounds on hospital projects, where each round can hold a multi-hundred-million-dollar building, and less rework between architect and engineers.
