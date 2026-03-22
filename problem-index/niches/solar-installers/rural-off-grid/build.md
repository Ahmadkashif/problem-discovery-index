# Off-Grid System Sizing with Load Profiling

**Niche:** [[niches/solar-installers/rural-off-grid/profile|Rural & Off-Grid Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An off-grid design platform that guides load profiling, models worst-case seasonal production, sizes the solar array and battery bank for specified autonomy days, integrates generator backup sizing, and produces a complete off-grid system specification — replacing the manual spreadsheet calculations that experienced off-grid designers spend 4-8 hours on per project.
**Tags:** #time-series-forecasting #automation #data-integration #bayesian-inference #gradient-boosting

## The Problem
Off-grid system sizing requires balancing three variables: solar array size (determined by worst-month insolation and daily load), battery bank size (determined by autonomy requirement and depth-of-discharge limits), and generator backup (determined by gap between solar production and load during worst-case weather events). The designer must: (1) profile every load in the home or facility (appliances, lighting, HVAC, well pump, etc.) with wattage, duty cycle, and seasonal variation; (2) determine the design month — typically December or January, when insolation is lowest; (3) size the array to meet daily load in the design month; (4) size the battery bank for 2-5 autonomous days (the customer's specified comfort level with cloudy weather); and (5) size a backup generator for extended cloudy periods and winter shortfall. This calculation is done manually in Excel, with experienced off-grid designers spending 4-8 hours per project. The accuracy depends heavily on the load profile quality — if the customer underestimates their propane furnace blower run time or forgets to mention the chest freezer in the garage, the system will be undersized.

## Why Nobody Has Built This
The off-grid market is small relative to grid-tied (3% of installations) and the design complexity is higher. Aurora Solar and other design tools focused on the grid-tied market where the financial model (savings versus utility bill) drives the value proposition. Off-grid has no utility bill to offset — the value proposition is energy independence, which is harder to quantify in a sales proposal. Load profiling for off-grid is inherently difficult because it requires detailed appliance-by-appliance accounting that grid-tied design bypasses (for grid-tied, you just look at the utility bill).

## What to Build
An off-grid design platform with four modules. First, guided load profiling: the customer or installer selects appliances from a database of common off-grid loads (with typical wattages and duty cycles), adjusts for their specific usage patterns, and the system calculates daily and monthly energy consumption with seasonal variation. Second, solar array sizing: using the customer's location's worst-month insolation data (from NREL NSRDB), size the array to meet the daily load requirement with derating for temperature, soiling, and system losses. Third, battery bank sizing: calculate the required capacity for the specified autonomy period, accounting for depth-of-discharge limits, temperature derating, and the customer's chosen battery chemistry (lead-acid vs. lithium). Fourth, generator integration: size the backup generator for worst-case production shortfall and battery recharging time, and model the annual generator run hours and fuel consumption.

## Target Customer
Off-grid solar installers doing 10-50 off-grid systems per year, currently using Excel spreadsheets for design. Homesteaders and rural property owners who want to self-evaluate off-grid feasibility before engaging an installer.

## Impact If Built
Reduces off-grid design time from 4-8 hours to 30-60 minutes through guided load profiling and automated sizing calculations. Improves sizing accuracy by 15-25% through systematic load profiling that catches commonly omitted loads. Prevents undersized systems (customer runs out of power in winter) and oversized systems (customer overpays by $5K-15K for unnecessary capacity). Could be priced at $50-100/month for professional installers or $20-50 per design for occasional users.
