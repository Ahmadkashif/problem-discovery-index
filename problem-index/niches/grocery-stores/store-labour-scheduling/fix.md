# Labour Standards Set in a Different Decade

**Niche:** [[niches/grocery-stores/store-labour-scheduling/profile|Store Labour Scheduling & Workload Forecasting]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Fix (Pain Point)
**One-liner:** The minutes allowed per case stocked or per item scanned were set by time studies years ago, before self-checkout, online picking and new fixtures changed the work.
**Tags:** #linear-regression #feature-engineering #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to match each store's scheduled hours to its 15-minute workload of customers, trucks and online orders, and whoever delivers the fewest understaffed intervals at the same payroll takes the account.

## The Problem
Every scheduling engine turns forecast volume into hours using labour standards: seconds per item at a register, minutes per case stocked, minutes per online order picked. Many chains' standards come from engineering studies done years ago. Self-checkout, new shelving, case-ready meat and in-store picking have changed the work since, so the forecast is right and the hours are still wrong.

## Why It's Still Broken
Re-studying standards means sending industrial engineers to stores with stopwatches. The handheld scan streams that already time much of this work are not used to update standards. Standards are also contested with unions, so changing them is slow.

## What a Fix Looks Like
Estimate task times continuously from existing scan and transaction streams: register throughput, stocking scans per case, picker scan intervals. Compare them with the standards, and flag standards that differ by more than a set margin for a focused study rather than a full re-study.

## Who Feels the Pain
Department managers scheduled against hours that do not cover the work; associates blamed for missing productivity targets set for an old process; and labour teams defending standards nobody has checked.

## Impact If Fixed
Correcting standards that are ~10% off on the largest three tasks moves ~5% of a store's hours to where the work is (estimate), ~200 hours a week at a large store.
