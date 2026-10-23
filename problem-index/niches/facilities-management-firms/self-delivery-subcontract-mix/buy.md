# Field Service Scheduling Pooled Across Clients

**Niche:** [[niches/facilities-management-firms/self-delivery-subcontract-mix/profile|Self-Delivery vs Subcontract Delivery Mix]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Field-service scheduling already optimises technician routes; IFM providers run it inside each account, which is exactly where density is lost.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to decide, service by service and region by region, whether its own technicians or a subcontractor will do the work more cheaply at the contracted SLA, and whoever builds enough self-delivery density to keep margin off the pass-through line takes the account.

## The Problem
A mobile technician serving one client's sites in a metro drives past other clients' sites that the same provider services through subcontractors. Scheduling is configured per account because SLAs, billing and CMMS instances are per account.

## What Already Exists
Field-service management and scheduling engines (Salesforce Field Service, ServiceMax, IFS and others) optimise routes, skills and time windows for a pool of technicians and a queue of jobs.

## The Customization Gap
IFM pooling needs: jobs drawn from several clients' CMMS instances with each client's own SLA clock and priority definitions; billing and timekeeping that split a technician's day across contracts correctly; contract rules on dedicated versus shared staff; subcontractor dispatch as a fallback inside the same optimiser, priced at each contract's pass-through terms; and reporting that proves to each client its SLA was met even though the technician was shared.

## Target Customer
Local and multi-client FM operations within the large providers, and regional FM firms whose model depends on metro density.

## Impact If Solved
Higher technician utilisation, fewer subcontracted callouts in metros where the provider already has people, and shared technicians who can be defended to each client.
