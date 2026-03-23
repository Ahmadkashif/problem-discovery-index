# Replace-vs-Repair Decision Engine with Lifecycle Cost Modeling

**Niche:** [[niches/fleet-managers/aging-fleet-lifecycle/profile|Aging Fleet Lifecycle Management]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool models the projected maintenance cost of keeping a specific vehicle versus the total cost of replacing it — fleet managers make $30K-$60K replacement decisions on gut feel.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #automation

## The Problem
A fleet manager has a 2017 Ford Transit with 185,000 miles. It needed $4,200 in repairs last year and is currently worth $12,000 wholesale. Should they spend $6,000 on the transmission repair it needs now, or sell it for $12,000 and buy a replacement for $45,000? The answer depends on: projected maintenance costs for the next 12-24 months (which accelerate non-linearly), projected depreciation (how much value it loses per month/mile), opportunity cost of capital ($45K for a new vehicle versus deploying that cash elsewhere), and operational risk (what's the probability of a breakdown that strands a driver?). This multi-variable financial decision is currently made based on the fleet manager's experience and a mental model of "when vehicles become too expensive to keep."

## Why Nobody Has Built This
The model requires vehicle-specific maintenance cost curves — how much does a 2017 Transit cost to maintain at 200K vs. 250K miles? This data exists across thousands of fleet records but has never been aggregated into predictive models by make/model/mileage. Each fleet's operating conditions (climate, duty cycle, driver behavior) modify the curve. Building accurate projections requires both historical fleet data and vehicle-specific engineering knowledge about failure patterns at high mileage.

## What to Build
A lifecycle decision engine that takes a vehicle's complete maintenance history, current mileage, current market value, and projected annual usage, then models: (1) expected maintenance cost for the next 12/24/36 months based on similar vehicles, (2) expected depreciation trajectory, (3) probability of major system failure (engine, transmission, differential) based on mileage and history, and (4) total cost of keeping vs. replacing. The output is a clear recommendation: "Keep this vehicle — projected 12-month maintenance ($3,200) is below replacement cost threshold" or "Replace this vehicle — projected 12-month maintenance ($8,500) plus breakdown risk exceeds replacement net cost."

## Target Customer
Fleet managers with 20+ vehicles averaging 8+ years or 150K+ miles who make 5-15 replace-vs-repair decisions per year.

## Impact If Built
Optimizes vehicle lifecycle timing, reducing total fleet cost by 8-15% through better replacement decisions. Prevents $10K-$25K mistakes per vehicle (keeping a vehicle too long or replacing it too early). For a 50-vehicle fleet, this translates to $50K-$150K in annual savings.
