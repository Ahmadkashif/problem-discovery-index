# Transient Fault Triage Before the Aircraft Lands

**Niche:** [[niches/aircraft-mro-shops/fbo-line-maintenance/profile|FBO Line Maintenance & Transient AOG Support]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A crew radios or texts ahead that a fault message is showing, and the FBO mechanic finds out what it means only when the aircraft is on the ramp and the parts suppliers are closed.
**Tags:** #large-language-models #k-nearest-neighbors #bert #worker-facing #workflow-orchestration #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to return a transient aircraft to service the same night it arrives with a fault, and whoever diagnoses, sources the part and signs it off before the crew's departure time takes the account.

## The Problem
Transient faults are the FBO shop's highest-margin and most stressful work. The crew reports a message; the mechanic, who may see this type a few times a year, starts troubleshooting on arrival, discovers the likely part, and then begins calling for it. Hours are lost that could have been spent before landing: identifying the probable causes, the tooling and the parts, and asking the operator's maintenance controller to approve.

## Why Nobody Has Built This
Troubleshooting knowledge sits with OEM help desks and in the heads of mechanics who know a type. FBO shops see many types infrequently, so none builds deep history alone. Fault-isolation tools exist for some business jets through OEM programmes, but not as a pre-arrival workflow for the shop that receives the aircraft.

## What to Build
A pre-arrival triage service. The crew or operator submits the fault message and symptoms; the system matches them against the fault isolation manual, prior fixes on the same type pooled across the chain's locations, and public Service Difficulty Reports on related parts. It returns ranked likely causes, required tools and parts with stock locations, and a draft work authorisation for the operator to approve before landing. The mechanic who meets the aircraft starts with a plan, and records what actually fixed it, which feeds the next case.

## Target Customer
Directors of maintenance at FBO chains with repair stations (Signature, Atlantic, Million Air and regional chains) and their operator customers' maintenance controllers.

## Impact If Built
If triage brings same-night return to service from ~50% to ~70% of transient faults (estimate), a chain handling ~5,000 transient faults a year keeps ~1,000 more aircraft on schedule and earns the labour and parts margin on them, plus the fuel and handling the crew would otherwise buy elsewhere.
