# Battery Storage Integration

**Parent Industry:** [[industries/solar-installers|Solar Installers]]
**Category:** Low Digitized

## Profile
**Market Size:** $2-3B
**Share of Parent Industry:** ~10% and growing rapidly
**Digital Adoption:** Low-Medium — battery sizing tools from manufacturers (Tesla, Enphase, Generac) are product-specific and don't compare across brands. TOU arbitrage and dispatch optimization are not modeled in any standard solar design tool.
**Target Buyer:** Solar installer adding battery storage to their portfolio, or storage-focused installer
**Automation Potential:** High — battery sizing is a mathematical optimization problem, dispatch scheduling is a control systems problem, and warranty compliance monitoring is a rules-based automation opportunity

## What Makes This a Distinct Niche
Battery storage transforms solar from a production asset into a dispatchable energy asset. With a battery, solar energy produced during midday can be stored and used during evening peak hours when utility rates are highest (TOU arbitrage), discharged during demand peaks to reduce demand charges, or reserved for backup power during grid outages. The value proposition depends entirely on the specific utility rate structure and the homeowner's priorities — a customer on a TOU rate gets maximum value from daily arbitrage, while a customer in a hurricane zone prioritizes backup capacity. Battery sizing and dispatch optimization require modeling that most solar installers don't have the tools or training to perform. The common approach is oversimplified: "Add a Powerwall for backup" without analyzing whether the customer's TOU rate differential justifies the $12K-15K investment on economic grounds.

## Current Tools & Gaps
Tesla's design tool sizes Powerwalls for backup duration but doesn't model TOU arbitrage economics. Enphase's configuration tool sizes IQ Battery systems for self-consumption but doesn't optimize dispatch for specific rate structures. Aurora Solar added basic battery sizing but doesn't model optimal dispatch. No tool compares battery options across manufacturers (Tesla vs. Enphase vs. Generac vs. Franklin) on the customer's specific rate structure and load profile.

## Problems
- [[niches/solar-installers/battery-storage-integration/build|🔨 Build: Battery Sizing and Dispatch Optimizer for TOU Arbitrage]]
- [[niches/solar-installers/battery-storage-integration/buy|🛒 Buy: Manufacturer Sizing Tools Unified Across Brands]]
- [[niches/solar-installers/battery-storage-integration/fix|🔧 Fix: Battery Warranty Compliance Monitoring]]
