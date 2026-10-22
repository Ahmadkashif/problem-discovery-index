# SD-WAN Path Selection That Understands Orbits and Rain

**Niche:** [[niches/satellite-operators/enterprise-backhaul-capacity/profile|Enterprise, Backhaul & Government Data Capacity]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise SD-WAN already steers traffic across links by measured quality; pointed at GEO, MEO and LEO links it misreads latency, rain fade and handovers as failures.
**Tags:** #time-series-forecasting #markov-decision-processes #automation #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to sell guaranteed throughput across GEO, MEO and partner LEO capacity at a price per megabit that survives comparison with Starlink, and whoever can design, quote and prove a multi-orbit service level fastest takes the carrier or enterprise contract.

## The Problem
A multi-orbit site has two or three satellite links with very different behaviour: GEO with a round trip of ~600 ms (estimate) and rain fade, MEO with lower latency and periodic handovers, LEO with low latency, frequent handovers and shared-cell congestion. Applications need steering by type — voice on the low-latency link, bulk transfer on the cheaper one — and failover that doesn't flap.

## What Already Exists
Enterprise SD-WAN platforms (Cisco, Fortinet, VMware VeloCloud, Peplink) with application-aware path selection based on measured loss, latency and jitter.

## The Customization Gap
The adaptation needs: link models that expect GEO latency and don't treat it as degradation; rain-fade prediction from weather radar to steer before the link drops; awareness of scheduled MEO and LEO handovers; per-orbit cost so steering respects the customer's contract; and SLA measurement per path that the operator can report.

## Target Customer
Managed-services product managers at multi-orbit operators and their integrator partners.

## Impact If Solved
Applications ride the right orbit automatically, failovers stop flapping, and the multi-orbit promise holds up in the customer's own measurements.
