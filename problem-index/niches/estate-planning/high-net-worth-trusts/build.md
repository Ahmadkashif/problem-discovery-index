# Estate Tax Scenario Modeling Engine

**Niche:** [[niches/estate-planning/high-net-worth-trusts/profile|High-Net-Worth Trusts]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** HNW estate attorneys stop building one-off Excel spreadsheets for every client and instead model trust structures against current and projected tax law in minutes, showing clients exactly how much each strategy saves.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact

## The Problem
When a client with a $20M estate asks "should I do a GRAT, a dynasty trust, or an ILIT?", the attorney must model each structure's tax implications under current law, projected law changes (2026 sunset), state-specific rules, and the client's specific asset mix and family structure. This modeling happens in custom Excel spreadsheets that each attorney builds independently. A single scenario analysis takes 3-8 hours. With the 2026 sunset affecting every HNW client, firms are overwhelmed — some are turning away clients because they can't model fast enough. The tacit knowledge problem is severe: experienced HNW attorneys develop intuition for which trust structures work best for specific client profiles, but this judgment lives in individual attorneys' heads and retires when they do.

## Why Nobody Has Built This
Estate tax modeling requires encoding federal estate tax rules, state estate/inheritance tax rules (which vary dramatically — some states have $1M exemptions while the federal is $13M), generation-skipping transfer tax rules, gift tax rules, and the interaction effects between them. The combinatorial complexity is high: a single client might need a GRAT funded with appreciating assets plus an ILIT funded with annual exclusion gifts plus a charitable remainder trust for income-producing real estate, and each structure's tax outcome depends on the others. No software vendor has built the comprehensive rule engine because the market (HNW estate attorneys at boutique firms) is small and the domain expertise required to build it correctly is rare.

## What to Build
A scenario modeling platform where the attorney inputs: client assets (type, value, location, growth rate), family structure (spouse, children, grandchildren, ages), existing estate plan structures, and state of residence. The system models 3-5 trust structure combinations and produces side-by-side comparisons showing: total estate tax liability, generation-skipping tax exposure, income tax implications of each structure, annual gift tax exclusion utilization, and net transfer to beneficiaries under current law and post-sunset projections. An ML layer trained on anonymized planning outcomes from participating firms learns which structures experienced attorneys recommend for similar client profiles, surfacing the tacit knowledge of experienced planners as "recommended strategies" for newer attorneys.

## Target Customer
HNW estate planning attorneys at boutique firms (2-10 attorneys) who currently spend 3-8 hours per client building Excel-based tax models and are facing a surge in plan reviews driven by the 2026 estate tax sunset.

## Impact If Built
Reduces per-client tax modeling time from 3-8 hours to 30-60 minutes. Enables firms to handle the 2026 sunset review surge without turning away clients. Captures retiring attorneys' planning intuition as training data, preserving institutional knowledge that currently walks out the door.
