# PPA Settlement, Curtailment Claims & Certificate Delivery

**Parent Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to settle each contract month without a dispute, and whoever has the smallest share of invoiced settlement value disputed or restated takes the account.

## Profile
**Market Size:** ~$250M a year of settlement staff time, ETRM licences, shadow-settlement services and registry administration (estimate)
**Share of Parent Industry:** ~0.7% of wind and solar energy revenue (estimate)
**Digital Adoption:** Medium — inputs are electronic (ISO statements, meter data, registry records) but each contract is calculated in its own spreadsheet
**Target Buyer:** Director of Commercial Operations or settlements manager at an IPP
**Automation Potential:** Very high — the calculation is rule-based once each contract's terms are encoded

## What Makes This a Distinct Niche
Most new wind and solar is sold under physical or virtual PPAs and hedges with negotiated clauses on settlement point, negative prices, curtailment and certificate delivery. Every month, every contract settles; every ISO resettlement reopens it. Curtailment is growing (CAISO set a monthly record of 919 GWh in March 2025), and the curtailment clause decides who pays for it. The contest is one measure, the share of invoiced value disputed or restated, and the competitors are ETRM vendors (Allegro, ION), shadow-settlement and revenue analytics firms (REsurety, named from recall), offtake platforms such as LevelTen, outsourced settlement services and in-house teams. Certificate tracking runs through M-RETS, PJM-GATS, WREGIS and the other registries; registry administration as an insight pocket is logged at [[niches/solar-installers/rec-incentive-administration/profile|🔍 Renewable Certificate & Incentive Administration]].

## Current Tools & Gaps
ETRM systems configured for trading desks, ISO settlement statement parsers, Excel workbooks per contract, and registry web portals. Gaps: contract clauses are re-implemented by hand per workbook, curtailment intervals are not classified the way each contract defines them, and certificate transfers are reconciled to contracts manually.

## Problems
- [[niches/renewable-power-producers/ppa-settlement-rec-delivery/build|🔨 Build: Contracts Compiled Into Settlement Rules]]
- [[niches/renewable-power-producers/ppa-settlement-rec-delivery/buy|🛒 Buy: Trading-Desk ETRM for a Two-Person Commercial Team]]
- [[niches/renewable-power-producers/ppa-settlement-rec-delivery/fix|🔧 Fix: Certificates Transferred Late or to the Wrong Account]]
