# Price Protection Claimed on Inventory Nobody Counted

**Niche:** [[niches/consumer-goods-wholesalers/consumer-electronics-appliance-wholesale/profile|Consumer Electronics, Appliance & Housewares Wholesale]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Fix (Pain Point)
**One-liner:** When a brand cuts its price, the distributor is owed credit on every unit on hand and in transit, but only if it counts them by the effective date and claims inside the window.
**Tags:** #large-language-models #feature-engineering #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to have the exact model a dealer or regional retailer just sold sitting in a nearby warehouse when the order lands, and whoever fills the highest share of dealer order lines from stock takes the account.

## The Problem
Brand price drops arrive as emails or portal notices with an effective date. The distributor must count units on hand, in transit and sometimes at dealers on that date, file the claim in the brand's format within a short window, and pass protection to dealers who bought recently. Alliance Entertainment's 10-K describes the same mechanism: protection limited to "a designated period of time".

## Why It's Still Broken
Notices are unstructured, inventory snapshots are not kept by date, and the claim is one more task for a buyer at the end of a month. Missed claims make distributors wary of deep stock, which costs fill.

## What a Fix Looks Like
Read each price-change notice into a structured record, snapshot inventory and in-transit units at the effective date automatically, draft the claim in the brand's format, and track credits against claims.

## Who Feels the Pain
Buyers and controllers at distributors, and dealers waiting for pass-through credits.

## Impact If Fixed
Capturing protection on every eligible unit could recover ~0.2–0.5% of sales a year (estimate), about $1–2.5M on $500M, and makes deeper stocking safe.
