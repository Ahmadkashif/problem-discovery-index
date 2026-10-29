# A Pricing Desk for One Store

**Niche:** [[niches/self-storage-operators/single-facility-independents/profile|Single-Facility Independent Owners]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A one-store owner competes with REITs that reprice every unit daily, using a weekly look at three competitors' websites and a flat annual increase.
**Tags:** #large-language-models #time-series-forecasting #bayesian-inference #survival-analysis #revenue-impact #ai-platform
**Contested on:** Every serious competitor in this niche is fighting to lift a one-store owner's rent roll without a revenue manager on staff, and whoever grows the owner's same-store rental income most over twelve months takes the account.

## The Problem
The independent owner sets web rates once a month, if that, and sends everyone the same increase, or none, every spring. In-place rents drift below street rates for long-tenured tenants while new tenants come in at promotions. The owner does not know what the store would earn under a REIT or a third-party manager, which is the number that decides whether to sell.

## Why Nobody Has Built This
Pricing vendors sell to portfolios, where one contract covers hundreds of stores. A single store cannot pay for a revenue manager or a model trained only on its own few hundred tenants. Facility software vendors serve independents but price simply.

## What to Build
A pricing desk delivered through the owner's existing software. A daily comp-set rate board is built from competitors' public rate pages. Web rates and promotions come from a vacancy forecast pooled across many similar small stores, with a Bayesian prior so a 300-unit store gets sensible estimates. A small ECRI optimiser sizes increases from tenure, gap to street rate and pooled move-out curves, with the state's notice rule built in. A twelve-month "what the store would earn" projection compares staying independent, hiring a third-party manager and selling.

## Target Customer
Owners of one to five stores; facility software platforms that want a premium tier for them.

## Impact If Built
If disciplined increases and daily web rates lift same-store rental income by ~3–5% (estimate) at a store collecting ~$500,000 a year, the owner earns ~$15,000–25,000 a year more. That is far more than the software costs, and it gives the owner the sell-or-hold comparison the REITs' buyers already make.
