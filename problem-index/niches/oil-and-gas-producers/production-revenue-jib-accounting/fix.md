# Gas Statements That Arrive After Close

**Niche:** [[niches/oil-and-gas-producers/production-revenue-jib-accounting/profile|Production, Revenue & JIB Accounting]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Midstream gas and NGL statements arrive weeks after the month ends, so revenue is booked on estimates and corrected later through every owner's check.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to close each production month with every purchaser dollar booked to the right well and every owner and partner paid or billed correctly, and whoever leaves the fewest dollars in prior-period adjustments and unexplained suspense takes the account.

## The Problem
Gas processors settle after they know plant yields, NGL prices and fees, often a month or more after production. Operators accrue revenue on a rough estimate and true it up when the statement arrives, and owners see the difference as adjustments on later checks.

## Why It's Still Broken
The estimate is usually last month's realisation applied to this month's volume, because building a better one means modelling each contract's fees, keep-whole terms and NGL recoveries. Nobody owns that model.

## What a Fix Looks Like
Estimate each meter's settlement from the operator's own measured volumes and gas analyses, the contract's fee and percent-of-proceeds terms, and published NGL and gas prices. Track each processor's history of true-ups so the estimate improves monthly. Show the accountant the expected settlement with a range before close.

## Who Feels the Pain
Revenue accountants at close, controllers explaining variances, and owners puzzled by adjustments.

## Impact If Fixed
Bringing accrual error from ~5% to ~1% of gas and NGL revenue (estimate) shrinks the prior-period adjustments that later hit every owner's check by roughly four-fifths.
