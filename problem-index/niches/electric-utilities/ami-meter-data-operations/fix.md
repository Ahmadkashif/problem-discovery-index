# The Estimated Bill Nobody Reviewed

**Niche:** [[niches/electric-utilities/ami-meter-data-operations/profile|AMI Meter Data Operations]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** A meter stops communicating, the system estimates for months, and the customer gets a large catch-up bill when the real read finally arrives.
**Tags:** #time-series-forecasting #exponential-smoothing #feature-engineering #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every exception in interval meter data into a correct bill and a correct grid model without a truck roll, and whoever resolves the most exceptions automatically, without a billing error reaching a customer, takes the account.

## The Problem
When an AMI meter drops off the network, the meter data system estimates consumption from history. If nobody chases the meter, estimation continues cycle after cycle. Catch-up bills after long estimation generate complaints, payment arrangements and commission scrutiny, and many states limit back-billing.

## Why It's Still Broken
Estimated reads pass validation by design, so they don't appear in exception queues, and communications failures are owned by a different team from billing.

## What a Fix Looks Like
Track consecutive estimated cycles per meter and escalate before the second bill. Compare estimates with neighbouring meters and weather to flag likely under-estimation. Notify the customer proactively when a bill is estimated, with the catch-up exposure.

## Who Feels the Pain
Customers hit with surprise bills; representatives handling the complaint; billing staff issuing corrections; regulators enforcing back-billing limits.

## Impact If Fixed
Catch-up bills after long estimation cut by ~50%–80% (estimate) by chasing non-communicating meters before the second estimated bill.
