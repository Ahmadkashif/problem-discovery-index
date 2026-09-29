# The Feed That Went Quiet

**Niche:** [[niches/dropshipping-suppliers/catalogue-and-stock-sync/profile|Catalogue & Stock Synchronisation]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** A supplier's feed stops updating and the platform keeps serving the last snapshot as though it were current, for eleven days, with no alarm anywhere.
**Tags:** #change-point-detection #data-integration #evaluation-metrics #workflow-orchestration #automation #quick-win #descriptive-statistics #compliance
**Contested on:** This niche is not terminal — knowing whether the item still exists and making the listing worth buying are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A supplier's endpoint starts returning the same file every time, or times out and the job retries silently, or returns a partial export after a change on their side. The platform has no concept of the feed being stale — it has the last good data and serves it. Merchants see stock levels that are eleven days old, advertise against them, and take orders. When the truth arrives, there is a backlog of orders for things that do not exist. Nothing failed loudly at any point: the job ran, returned data, and the data was old.

## Why It's Still Broken
Success is defined as the job completing rather than as the data being fresh, which is the framing error at the centre of it. A feed returning identical content looks identical to a feed with no changes, and nobody distinguishes them. Alerting is built around errors and this produces none. And the staleness is only discoverable downstream, where it appears as an oversell and is attributed to the supplier.

## What a Fix Looks Like
Measure freshness, not completion. Track last-changed rather than last-fetched per supplier and per product, which is the entire fix and immediately separates a quiet feed from a stable one — most platforms do not record this at all. Alert on a feed whose content has not moved beyond its historical pattern, since a catalogue that normally changes daily and has not changed in a week is broken regardless of what the job log says. Detect partial and truncated exports by comparing record counts and category coverage against the recent norm, which catches the silent supplier-side failure. Fail loudly on retry exhaustion instead of falling back to cached data quietly. Show merchants the age of the stock data on every listing, which turns an invisible risk into a decision they can make. Degrade automatically as data ages — stop recommending, then stop advertising, then stop accepting orders — rather than treating stale and fresh identically right up to the moment of failure. Use order rejections as an independent staleness signal, because they are the ground truth and arrive before anyone notices the feed. Report per-supplier freshness to the supplier, since many outages are on their side and unknown to them. And publish feed health as a platform metric, because a synchronisation product that does not measure its own freshness is not measuring the thing it sells.

## Who Feels the Pain
Merchants advertising against eleven-day-old stock; customers ordering items that have not existed for a week; and platforms whose integration is technically running and functionally dead.

## Impact If Fixed
Success is defined as job completion rather than data freshness, so a quiet feed and a stable one look identical. Tracking last-changed per supplier is the whole fix, and graduated degradation as data ages replaces a cliff nobody sees coming.
