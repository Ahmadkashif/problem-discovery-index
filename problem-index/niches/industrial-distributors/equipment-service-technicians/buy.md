# Field Service Software Built Around the Machine's Serial Number

**Niche:** [[niches/industrial-distributors/equipment-service-technicians/profile|Equipment Service Technicians at Pump, Compressor & Lift-Truck Dealers]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic field-service platforms schedule technicians well; industrial equipment service also needs the machine's serial, OEM parts tree and contract terms on the job.
**Tags:** #large-language-models #k-nearest-neighbors #data-integration #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to fix a down pump, compressor or lift truck on the first visit, and whoever sends the technician with the right diagnosis and the right parts already on the truck takes the account.

## The Problem
Technicians arrive with a work order that names the customer and the complaint but not the machine's configuration, service history or which parts the contract covers. They phone the branch for parts lookups by serial number and photograph nameplates to send back.

## What Already Exists
Enterprise field-service platforms (Salesforce Field Service, Microsoft Dynamics 365 Field Service and others), residential-trade platforms, dealer management systems and OEM parts portals.

## The Customization Gap
An industrial layer: the machine record keyed by serial number with its configuration and parts tree from OEM data; service and planned-maintenance contract terms (what's covered, response times); hour-meter and telematics readings where available; and truck stock checked against the likely parts list before dispatch.

## Target Customer
Service managers and dispatchers at equipment distributors running generic or ERP-bundled service tools.

## Impact If Solved
If the machine record cuts ~3–5 calls a day from each technician to the branch (estimate) and catches ~2–5% of labour and parts currently billed to the wrong contract (estimate), the dealer gains technician time and margin on fixed-price maintenance agreements.
