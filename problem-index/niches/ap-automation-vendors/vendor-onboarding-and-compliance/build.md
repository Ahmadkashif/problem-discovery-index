# Onboard Once, Reuse Everywhere

**Niche:** [[niches/ap-automation-vendors/vendor-onboarding-and-compliance/profile|Vendor Onboarding & Compliance]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A supplier sends the same tax form and insurance certificate to two hundred customers, and every one stores it separately and lets it expire.
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #graph-theory #confidence-intervals #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to onboard a supplier once, verify them properly, and never ask them for the same document again — and whoever does it across a network collects the evidence every buyer currently gathers separately.

## The Problem
The same supplier is onboarded hundreds of times a year across the platform's customer base. Each buyer requests the same tax documentation, the same banking details, the same insurance evidence, the same screening. Each stores its own copy, tracks its own expiry badly, and re-requests annually. The supplier's finance team spends real time on forms that differ only cosmetically. The platform sits in the middle of all of it and treats each onboarding as a separate customer workflow.

## Why Nobody Has Built This
Onboarding was built per customer because the product is sold per customer, so the network was never the unit of design — and a feature scoped to one tenant cannot see the duplication across tenants. Buyers assume compliance evidence must be collected by them directly. Suppliers are not the paying party and their time does not enter anyone's calculation. And no standard exists for what a reusable supplier credential would contain.

## What to Build
Make the evidence a reusable asset. Let a supplier maintain one verified profile that many buyers can draw on, which is the core and eliminates the duplication at its source. Verify each element once, properly, rather than collecting it many times superficially, since a single well-verified tax identifier or bank account is worth more than two hundred unchecked copies. Track expiry centrally and ask the supplier once before it lapses, because expiry management is the failure mode and a single reminder serves every buyer. Screen continuously rather than at onboarding, as sanctions and watchlist status changes and a one-time check ages immediately. Let buyers add their own requirements on top of the shared base, since policies genuinely differ and the base covers most of it. Validate documents on receipt rather than storing images, which is where the current process quietly fails. Make the supplier's experience the design centre, because their cooperation is what makes the network work and nobody has ever considered them the user. Feed verified identity and banking into payment verification, which is where the compliance value compounds. Establish the legal basis for sharing evidence between buyers, as that is the binding constraint and is solvable. And measure onboarding time and document freshness, which no buyer currently knows for their own file.

## Target Customer
Vendor operations and compliance leadership, suppliers filling in the same forms repeatedly, procurement teams, and supplier network and verification vendors.

## Impact If Built
Onboarding was scoped per tenant because the product is sold per tenant, so the duplication across the network is invisible from inside it. One verified supplier profile serving many buyers removes the work and produces better evidence than any single collection.
