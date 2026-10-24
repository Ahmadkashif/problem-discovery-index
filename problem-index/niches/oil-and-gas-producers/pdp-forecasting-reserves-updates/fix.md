# The December Re-Forecast Crunch

**Niche:** [[niches/oil-and-gas-producers/pdp-forecasting-reserves-updates/profile|Producing-Well Forecasting & Reserves Updates]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Reserves teams re-forecast the whole producing base in the weeks before year-end, when the outside reserve engineers need the data, instead of keeping it current all year.
**Tags:** #time-series-forecasting #change-point-detection #evaluation-metrics #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to re-forecast every producing well as each month's volumes arrive, and whoever's proved-developed forecasts miss the following year's actual production by the least takes the account.

## The Problem
Year-end reserves and the spring borrowing-base redetermination both need updated forecasts for every well. Teams batch the work into the last quarter, pull data, refit, argue with the reserve auditor, and repeat in spring, with little time to investigate wells that changed.

## Why It's Still Broken
Forecasting is treated as a reporting event rather than a monthly process, and the tools make each refit a manual act.

## What a Fix Looks Like
Monthly automatic refits of every well with a short exception list: wells whose last three months broke their forecast band, wells with new nearby completions, and wells with downtime. Engineers clear exceptions monthly, and year-end becomes a review of a forecast that is already current.

## Who Feels the Pain
Reserves engineers working late in December, reserves managers facing the auditor, and finance teams waiting on borrowing-base numbers.

## Impact If Fixed
Spreading the work across the year can cut year-end reserves preparation from ~6–8 weeks to ~2–3 (estimate) and leaves time to investigate the wells whose forecasts matter most.
