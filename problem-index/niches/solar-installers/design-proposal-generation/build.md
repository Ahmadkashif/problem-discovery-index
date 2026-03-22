# One-Click Solar Proposal from Address

**Niche:** [[niches/solar-installers/design-proposal-generation/profile|Design & Proposal Generation]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that takes only a street address and utility bill (or annual consumption estimate) and produces a complete solar proposal in under 60 seconds — auto-detecting the roof, designing the system, modeling production, calculating financials, and generating a customer-facing document — eliminating the 20-30 minute design process that limits solar sales volume.
**Tags:** #semantic-segmentation #automation #revenue-impact #quick-win #cnns #gradient-boosting

## The Problem
Solar companies are constrained by proposal throughput. A company generating 150 leads per month needs 150 custom proposals. At 20-30 minutes per proposal, a full-time designer produces 16-24 proposals per day — the company needs a full-time designer just for proposal generation. For sales models that involve door-to-door canvassing or instant online quotes, the 20-30 minute timeline is completely incompatible with the sales moment. A homeowner on their doorstep will not wait 20 minutes for a proposal; an online shopper expects an instant quote. Aurora's Instant Design feature attempts to solve this but produces designs that require significant manual correction (incorrect roof segmentation, panels on skylights or dormers, setback violations) in 40-60% of cases, making it unreliable for customer-facing output without human review.

## Why Nobody Has Built This
Reliable one-click proposals require solving several problems at very high accuracy: (1) roof segmentation from satellite imagery — identifying every roof plane with correct azimuth, tilt, and area, including complex roofs with dormers, hip intersections, and varying heights (requires 95%+ accuracy to be useful without manual correction); (2) obstruction detection — identifying skylights, chimneys, vents, HVAC equipment, and satellite dishes that panels cannot cover; (3) structural assessment — determining whether the roof can support panels based on age and construction type (a judgment currently made by the designer from visual assessment); (4) optimal panel placement — maximizing production while respecting setback requirements that vary by jurisdiction and fire code; and (5) financial modeling with accurate rate data — requiring up-to-date utility rate schedules for the customer's specific address.

## What to Build
An end-to-end proposal automation pipeline: input an address and annual kWh consumption. The system: (1) retrieves high-resolution satellite/aerial imagery and generates a 3D roof model using CV-based segmentation with sub-degree accuracy on azimuth and tilt; (2) detects obstructions and exclusion zones from imagery; (3) applies jurisdiction-specific setback rules and fire code requirements; (4) places panels to maximize production within the buildable area, using the customer's consumption as the system size target; (5) runs a full production simulation using TMY weather data, shade analysis from 3D surroundings, and module-level performance modeling; (6) retrieves the customer's utility rate from a rate database and calculates 25-year savings; (7) applies available incentives (ITC, state, local, utility); (8) generates a customer-facing proposal PDF or interactive web page — all in under 60 seconds. Designs that exceed a confidence threshold are delivered instantly; designs below the threshold are flagged for human review.

## Target Customer
Solar companies doing 200+ proposals per month that want to scale sales without scaling design staff. Door-to-door and online-first solar sales organizations that need instant proposals. Aurora Solar or competitors seeking to achieve truly instant, accurate design.

## Impact If Built
Reduces per-proposal cost from $15-25 (20-30 minutes of designer time) to under $1 (compute cost). Enables instant on-site proposals for door-to-door sales, increasing close rates by 30-50% versus next-day proposal delivery. Eliminates the design team bottleneck that limits solar sales scaling. Worth $200M+ in addressable market value across the US solar installation industry.
