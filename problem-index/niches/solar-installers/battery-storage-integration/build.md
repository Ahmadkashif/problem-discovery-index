# Battery Sizing and Dispatch Optimizer for TOU Arbitrage

**Niche:** [[niches/solar-installers/battery-storage-integration/profile|Battery Storage Integration]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A battery sizing and dispatch optimization engine that takes the customer's utility rate structure, load profile, and solar production curve, and determines the optimal battery size, chemistry, and dispatch strategy to maximize economic return — answering the question "does a battery make financial sense for this specific customer?" with engineering precision rather than sales assumptions.
**Tags:** #reinforcement-learning #time-series-forecasting #revenue-impact #data-integration #automation #gradient-boosting

## The Problem
Battery storage is the fastest-growing segment of residential solar, but most battery sales are driven by backup power desire (emotional) rather than economic analysis (rational). A Tesla Powerwall 3 costs $12K-15K installed. On a utility with a $0.04/kWh TOU differential (off-peak $0.08, on-peak $0.12), the daily arbitrage value of a 13.5 kWh battery is approximately $0.54 — producing an economic payback of 60+ years, making the investment purely a backup power play. On a utility with a $0.25/kWh TOU differential (California TOU rates), the same battery produces $3.38/day in arbitrage, yielding a 10-12 year payback — a marginal but defensible economic case. Solar installers don't have the tools to make this analysis, so they sell batteries based on backup marketing regardless of economics. Customers who later realize the battery doesn't pay for itself through rate savings feel misled.

## Why Nobody Has Built This
Optimal battery dispatch is a complex optimization: the battery must decide in real-time whether to charge (from solar or grid), discharge (to load or grid), or idle — and the optimal decision depends on current solar production, current load, current and future electricity prices (TOU period transitions), and battery state of charge. Modeling this for a proposal requires simulating 8,760 hours of dispatch decisions using the customer's actual load profile and the utility's complete rate structure. The reinforcement learning approach (train a dispatch agent that maximizes economic value) is technically sound but requires rate-specific training for each of the 3,000+ US rate schedules.

## What to Build
A battery economics platform with two modes. First, proposal mode: input the customer's utility rate, monthly consumption, solar system size, and backup priority. The optimizer simulates a full year of optimal dispatch and outputs: the economically optimal battery size (which may be zero on some rate structures), the expected annual savings from TOU arbitrage and demand charge reduction, the backup capacity in hours at various load levels, and the total payback period including the ITC credit. The output is a customer-facing comparison chart: "Battery A: 10 kWh, $10K, 12-year payback, 8 hours backup" vs. "Battery B: 13.5 kWh, $14K, 14-year payback, 12 hours backup" vs. "No battery: $0, backup via generator." Second, operational mode: for installed systems, a dispatch controller that sends charging/discharging commands to the battery based on real-time TOU rates, solar production, and load — maximizing the economic value of the installed battery rather than using the manufacturer's default dispatch algorithm.

## Target Customer
Solar installers adding battery storage to 20-50% of installations, wanting to make data-driven sizing and economic recommendations. Battery-focused installers doing 100+ storage installations per year. Homeowners in high-TOU-differential markets (California, Hawaii, Arizona, Connecticut) where battery economics are marginal to positive.

## Impact If Built
Increases customer confidence in battery purchases by providing transparent economic analysis. Prevents uneconomic battery sales that damage installer reputation when customers realize payback is 30+ years. Optimizes dispatch for installed systems, increasing actual battery economic value by 15-30% versus default manufacturer dispatch. Could be priced at $5-10 per proposal plus $5-10/month per monitored system.
