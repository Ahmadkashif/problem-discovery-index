# Closed-Loop Chemical Dosing Optimization

**Niche:** [[niches/oil-gas-field-services/production-chemical-services/profile|Production Chemical Services]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system automatically adjusts chemical treatment dosing based on real-time water quality measurements, replacing the current practice of fixed-rate dosing adjusted quarterly by lab results.
**Tags:** #gaussian-process #bayesian-network #reinforcement-learning #regression #tabular-ml #revenue-impact

## The Problem
Chemical injection pumps at wellsites run at a fixed rate set during the last pumper visit — typically 2-5 gallons per day of corrosion inhibitor, regardless of actual well conditions. But well conditions change continuously: water cut increases (raising corrosion risk), bacterial populations fluctuate seasonally, scale deposition varies with temperature and pressure, and chemical effectiveness degrades as well fluids change. A well being treated at 3 gallons/day of corrosion inhibitor may actually need 5 gallons/day in summer (higher bacterial activity) and only 1.5 gallons/day in winter. The fixed-rate approach either over-treats (wasting $1,000-$5,000/well/year) or under-treats (causing $20,000-$100,000 in corrosion-related equipment failures).

## Why Nobody Has Built This
Closed-loop chemical optimization requires two capabilities that do not exist at most wellsites: (1) real-time water quality measurement (pH, conductivity, ORP, iron concentration, bacterial counts) deployed at the wellhead rather than sampled quarterly, and (2) remotely adjustable chemical injection pumps that can receive dosing commands from a control system. The first requires sensor hardware deployment and maintenance in harsh environments. The second requires upgrading from simple mechanical injection pumps to electronically controlled pumps connected to SCADA — a $2,000-$5,000 investment per well that operators have not made because no optimization software exists to justify the upgrade.

## What to Build
A closed-loop dosing system that: deploys water quality sensors (pH, conductivity, ORP, and optionally corrosion probes) at the wellhead or separation facility, ingests real-time readings alongside SCADA production data (flow rate, water cut, temperature, pressure), runs a Bayesian optimization model that predicts optimal chemical dose for current conditions, and adjusts the electronic injection pump rate automatically (with operator-set bounds and override capability). The model learns well-specific response curves — how corrosion rate and scale deposition respond to changes in chemical dose, water chemistry, and operating conditions — and converges on the minimum effective dose.

## Target Customer
Oil and gas operators spending $500K+/year on production chemicals across 50+ wells who suspect 20-40% of that spend is wasted on over-treatment.

## Impact If Built
Reduces chemical costs by 15-30% ($75K-$300K/year for a 100-well operator) while simultaneously reducing chemical-related equipment failures by 20-40% through more responsive dosing. Environmental benefit: reduces total chemical volume injected into produced water systems.
