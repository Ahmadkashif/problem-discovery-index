# The Hours Forecast Nobody Owns

**Niche:** [[niches/self-insured-benefit-pools/hw-fund-cost-projection/profile|Health & Welfare Fund Cost Projection & Bargaining Allocation]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Fix (Pain Point)
**One-liner:** A health fund's income is contribution rate times hours, and the hours line in the projection is usually last year's hours with a guess attached.
**Tags:** #time-series-forecasting #exponential-smoothing #change-point-detection #feature-engineering #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to project a health fund's cost per hour worked across a three-to-five-year bargaining agreement, and whoever's projection keeps the fund's reserve inside the trustees' target band without a mid-contract benefit cut or emergency reallocation takes the account.

## The Problem
Cost per hour is a ratio. When hours fall in a construction slowdown, contributions fall at once while claims for covered members and their families continue, partly paid from hour banks. Projections assume an hours level, often flat or trended, and the trustees find out it was wrong from the monthly remittance totals.

## Why It's Still Broken
Nobody owns the hours number. The actuary takes it from the fund office, the fund office takes it from last year, and the union's dispatch data and the contractors' backlogs, which say most about next year's hours, are never connected to the fund's model.

## What a Fix Looks Like
An hours forecast built from the fund's own remittances by employer and craft, joined to union hiring-hall dispatch counts, regional building permits and contractor backlog where the bargaining parties share it, with change-point alerts when hours break trend. The forecast feeds the cost projection with its own uncertainty band.

## Who Feels the Pain
Fund administrators explaining a reserve drop; trustees who must cut benefits or reopen allocations mid-contract; members who lose coverage when hour banks run dry.

## Impact If Fixed
An early, owned hours forecast gives trustees months of warning before reserves fall, which is the difference between an orderly allocation change at bargaining and an emergency one.
