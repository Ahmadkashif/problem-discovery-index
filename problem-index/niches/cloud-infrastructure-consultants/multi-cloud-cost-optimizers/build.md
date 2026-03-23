# Cross-Provider Commitment Optimizer

**Niche:** [[niches/cloud-infrastructure-consultants/multi-cloud-cost-optimizers/profile|Multi-Cloud Cost Optimizers]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can jointly optimize Reserved Instance, Savings Plan, and Committed Use Discount purchases across AWS, Azure, and GCP to minimize total cloud spend.
**Tags:** #reinforcement-learning #time-series-forecasting #tabular-ml #revenue-impact #automation

## The Problem
Enterprises running multi-cloud spend $2M-$50M/year across providers. Each provider offers commitment devices (AWS RIs/SPs, Azure RIs, GCP CUDs) with different term lengths, flexibility rules, and discount structures. Consultants currently optimize each provider independently, missing cross-provider arbitrage — e.g., shifting a workload from on-demand Azure to committed AWS may yield better savings than committing on Azure. The combinatorial complexity of joint optimization across 3 providers with 10+ instance families each is beyond spreadsheet modeling.

## Why Nobody Has Built This
Each provider's pricing APIs are structured differently, discount rules change quarterly, and the interaction effects between commitment devices are non-linear. Building a cross-provider model requires normalizing heterogeneous pricing schemas and forecasting workload demand per provider simultaneously — a problem that falls between what FinOps tools do (single-provider analysis) and what management consultants do (strategic vendor negotiation).

## What to Build
A portfolio optimization engine that ingests usage data from all three major cloud providers, forecasts demand by instance family over 1-3 year horizons, and recommends a joint commitment purchase strategy that minimizes total cost of ownership. The system models commitment flexibility (convertible vs. standard RIs), break-even timelines, and workload mobility between providers.

## Target Customer
FinOps consultants advising enterprises with $5M+/year multi-cloud spend. Typical engagement saves 20-35% — the tool takes a percentage of incremental savings.

## Impact If Built
Unlocks an additional 8-15% savings beyond single-provider optimization for multi-cloud enterprises, worth $400K-$7.5M annually per client.
