# Audit Evidence as a By-Product of Work Orders

**Niche:** [[niches/aircraft-mro-shops/small-part-145-repair-stations/profile|Small Part 145 Repair Stations]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A small repair station's quality manager spends the week before every FAA visit or customer audit pulling work orders, training files and calibration certificates to prove the shop did what its manual says.
**Tags:** #large-language-models #transformers #compliance #workflow-orchestration #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a small repair station's certificate and its customers' approvals with a one-person quality department, and whoever leaves the fewest findings per FAA and customer audit takes the account.

## The Problem
The FAA inspector, an airline's supplier auditor, or a Coordinating Agency for Supplier Evaluation auditor asks for samples. Show the incoming inspection on this part, the qualification of the technician who signed this release, the calibration of the torque wrench used, the current revision of the component maintenance manual on the day. The quality manager assembles this by hand from several binders and systems. Findings come from gaps in the evidence more often than from bad work.

## Why Nobody Has Built This
Quality software for aviation was built for airline MROs with quality departments, and manufacturing QMS for AS9100 plants. Small stations are a fragmented market of thousands of firms with thin budgets. Nobody has tied the evidence to the work order itself, where it is created.

## What to Build
A layer over the station's work orders that maps each manual procedure (145.211's list: incoming inspection, preliminary and hidden-damage inspection, technical data currency, final inspection and return to service, calibration, corrective action) to the evidence each job should produce, captures it as the job runs, and flags missing items before release. For an audit, it produces sample packs on request and pre-fills customer questionnaires from the manual and the evidence history.

## Target Customer
Accountable and quality managers at component, avionics, propeller and small airframe repair stations with roughly 5–50 staff.

## Impact If Built
Cutting audit preparation from ~40–80 hours per audit to ~8 (estimate), across ~6–15 customer and FAA audits a year, returns several hundred hours to a quality manager who is often also an inspector, and it cuts findings that put customer approvals at risk.
