# Design & Proposal Generation

**Parent Industry:** [[industries/solar-installers|Solar Installers]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1-2B (embedded across all solar segments)
**Share of Parent Industry:** Cross-cutting function — every solar sale requires a system design and customer proposal
**Digital Adoption:** Medium-High — Aurora Solar dominates with 60%+ market share among US residential installers. Solargraf, OpenSolar, and EagleView compete. But even with Aurora, the design-to-proposal process takes 20-30 minutes per prospect.
**Target Buyer:** Solar sales rep, system designer, or sales manager seeking to increase proposal volume
**Automation Potential:** Very High — system design from satellite imagery is a mature CV problem, production modeling is computationally solved, and financial calculation is deterministic given rate inputs

## What Makes This a Distinct Niche
The design-to-proposal process is the bottleneck in solar sales. A solar company generates 50-200 leads per month through marketing and canvassing. Each lead that progresses past initial qualification requires a custom system design and financial proposal. The current Aurora workflow: import the address, generate a 3D roof model from satellite imagery (sometimes requiring manual adjustment), place panels considering shade, setbacks, and structural constraints, select equipment, run production simulation, input utility rate and incentive data, select financing options, and generate the customer-facing proposal. This takes 20-30 minutes per proposal for an experienced designer, requiring specialized training in Aurora's interface. Sales reps who can't design systems themselves depend on a design team, adding 24-48 hours of latency between the sales appointment and proposal delivery. This latency kills close rates — the customer's enthusiasm fades, they get competing proposals, or they lose interest.

## Current Tools & Gaps
Aurora Solar is the market leader — it handles roof modeling, shade analysis, panel placement, production simulation, and proposal generation. Solargraf competes with a faster (but less accurate) design workflow. OpenSolar offers a free tier with basic design capability. Instant Design tools (Aurora's Instant Design, SolarAPP+ data) attempt to auto-generate designs but produce results that experienced designers spend 10-15 minutes correcting. The 20-30 minute timeline has been stubbornly resistant to further automation because manual judgment is still required for panel placement optimization, structural assessment, and financial model configuration.

## Problems
- [[niches/solar-installers/design-proposal-generation/build|🔨 Build: One-Click Solar Proposal from Address]]
- [[niches/solar-installers/design-proposal-generation/buy|🛒 Buy: Aurora Instant Design Accuracy Enhancement]]
- [[niches/solar-installers/design-proposal-generation/fix|🔧 Fix: Proposal Accuracy — Projected Savings That Don't Materialize]]
