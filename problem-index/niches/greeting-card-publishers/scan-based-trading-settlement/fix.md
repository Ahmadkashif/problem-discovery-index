# One UPC Rung Up for Every Card

**Niche:** [[niches/greeting-card-publishers/scan-based-trading-settlement/profile|Scan-Based Trading Settlement & Shrink]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** A cashier who rings every card at one price with a single UPC makes one design look like a bestseller and a hundred look like shrink, and the publisher pays for both.
**Tags:** #change-point-detection #descriptive-statistics #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche (deduction-recovery and reconciliation vendors, EDI analytics providers and publishers' own settlement teams) is fighting to pin each store's missing cards under scan-based trading to a cause the retailer will accept in settlement, and whoever recovers the most disputed shrink per store takes the publisher's settlement work.

## The Problem
When a card's barcode will not scan, or the line is long, a cashier keys a convenient UPC or a department code. Under scan-based trading, if the keyed code is one of the publisher's own cards, that design is paid for at its price while the real design never registers as sold; if it is a department code, the sale is not attributed to the publisher at all. Either way the card actually sold later appears as shrink. Replenishment then sends more of the "bestseller" and none of the real sellers.

## Why It's Still Broken
Substitution is visible only as an unusual pattern across one UPC in one store, which no department-level report shows. Publishers reconcile monthly in aggregate, long after the pattern started.

## What a Fix Looks Like
Daily checks on scan feeds for UPCs whose sales jump far beyond their pocket capacity or their history in that store, matched to rising apparent shrink across other pockets, with an alert to the account team and the merchandiser, who can confirm at the next visit and ask the store to fix the scanning practice.

## Who Feels the Pain
Settlement teams; replenishment planners misled by false bestsellers; merchandisers blamed for "shrink" that is a till habit.

## Impact If Fixed
Recovered revenue, accurate replenishment and fewer disputed settlements, from a simple rule run every day.
