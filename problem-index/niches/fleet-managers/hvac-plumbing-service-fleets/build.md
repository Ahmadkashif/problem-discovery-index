# Equipment-Aware Vehicle Assignment for Service Dispatch

**Niche:** [[niches/fleet-managers/hvac-plumbing-service-fleets/profile|HVAC/Plumbing Service Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No dispatch tool matches service calls to vehicles based on what equipment and parts are actually in each van — technicians arrive at jobs missing the tools they need.
**Tags:** #recommendation #tabular-ml #workflow-orchestration #automation #revenue-impact

## The Problem
An HVAC company dispatches a technician to install a mini-split system. The technician's usual van (with the vacuum pump, flare tools, and refrigerant recovery unit) is in the shop for maintenance, so dispatch assigns a backup van. The backup van doesn't have the vacuum pump. The technician arrives on-site, discovers the missing tool, and either drives 45 minutes to the shop to get it or reschedules the job — losing $300-$500 in revenue and damaging the customer relationship. This happens because dispatch sees vehicles as interchangeable, not as mobile workshops with specific equipment loadouts.

## Why Nobody Has Built This
Field service dispatch platforms (ServiceTitan, Housecall Pro) manage technician assignment based on skill and availability, not vehicle equipment. Fleet management platforms (Fleetio) track vehicles but don't know what's inside them. The equipment-to-vehicle-to-job matching requires bridging these three systems: what does the job require, what's in each vehicle, and which technician/vehicle combination is available and closest?

## What to Build
An equipment-aware dispatch layer that maintains a real-time inventory of tools and parts per vehicle, matches incoming service calls against equipment requirements by job type, and recommends vehicle-technician assignments that ensure the right tools arrive on-site. When a vehicle goes to the shop, the system flags which jobs it's ineligible for and suggests equipment transfers to backup vehicles. It also tracks when consumable parts (fittings, connectors, filters) need restocking per vehicle.

## Target Customer
Trades company owners with 10-50 service vehicles who experience 3-5 "wrong equipment" incidents per week, each costing $200-$500 in lost time and revenue.

## Impact If Built
Eliminates 80-90% of equipment-mismatch incidents, recovering $3,000-$10,000 per month in previously lost labor revenue. Reduces average job completion time by 15-20% by ensuring first-trip resolution.
