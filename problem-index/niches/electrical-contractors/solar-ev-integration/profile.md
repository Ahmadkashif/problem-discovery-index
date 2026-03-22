# Solar & EV Integration

**Parent Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Category:** Low Digitized

## Profile
**Market Size:** $20-25B
**Share of Parent Industry:** ~10%
**Digital Adoption:** Low-Medium — solar design tools (Aurora Solar, Helioscope) handle the PV array side but don't address the electrician's scope: panel integration, load calculations, and NEC Article 690/625 compliance. Most EV charger installations are quoted from experience with no design tools.
**Target Buyer:** Electrician or EC owner adding solar and EV charger installation to their existing service offerings
**Automation Potential:** High — system design involves deterministic NEC calculations, utility interconnection is a document-processing bottleneck, and load calculations for panel capacity are structured problems

## What Makes This a Distinct Niche
Solar and EV integration is the fastest-growing segment of electrical contracting, driven by the Inflation Reduction Act (30% ITC), state-level EV mandates, and homeowner demand. The work sits at the intersection of traditional electrical contracting (panel upgrades, circuit installation, NEC compliance) and new technology (inverters, battery storage systems, EV charging stations, smart panels like Span). For electricians, the challenge is that solar, EV, and battery storage each introduce new NEC code sections (Article 690 for PV, Article 625 for EV, Article 706 for energy storage) that didn't exist or were minimally relevant five years ago. A residential solar + EV + storage project requires calculating whether the existing panel can handle the new loads (NEC 220 load calculation), determining if the "120% rule" (NEC 705.12) allows backfeed into the existing panel or if an upgrade is needed, sizing conductors for the PV system per NEC 690, and sizing the EV circuit per NEC 625. Each of these calculations is manual and must account for the interaction between all three systems.

## Current Tools & Gaps
Aurora Solar and Helioscope design the PV array (panel placement, string sizing, shade analysis) and generate permit documents — but they stop at the inverter output. The electrical work from inverter to panel (disconnect sizing, conductor sizing, panel integration, load calculations) is the electrician's scope and has no design tool. EV charger manufacturers (ChargePoint, Tesla, Emporia) provide installation guides but not site-specific electrical design. Smart panel companies (Span, Lumin) handle load management but don't help with the initial design decision of whether the existing panel has capacity. Utility interconnection applications vary by utility and are submitted manually — each utility has different forms, requirements, and timelines.

## Problems
- [[niches/electrical-contractors/solar-ev-integration/build|🔨 Build: Solar/EV/Storage Electrical Design Calculator]]
- [[niches/electrical-contractors/solar-ev-integration/buy|🛒 Buy: Utility Interconnection Application Automation]]
- [[niches/electrical-contractors/solar-ev-integration/fix|🔧 Fix: NEC Code Complexity for New Entrants]]
