# The Cull Nobody Logs

**Niche:** [[niches/grocery-stores/fresh-perishables-ordering-markdown/profile|Fresh Perishables Ordering & Markdown]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Fix (Pain Point)
**One-liner:** Fresh product thrown away is booked as a monthly inventory adjustment, so the single best label for over-ordering never reaches any forecasting model.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #quick-win #worker-facing #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to cut fresh-department shrink without emptying the shelves". But that contest splits in two. Ordering vendors win before the truck arrives, by cutting the most shrink at an unchanged in-stock rate. Markdown, surplus and dynamic-pricing vendors win after the product is aging, on margin recovered per lot. The buyers, data and winners differ. Decomposed into contested sub-niches below.

## The Problem
When a produce clerk pulls a case of soft peppers, it goes in a bin and then a dumpster. At many stores no scan is made. Shrink appears later as the gap between book inventory and the physical count, with no item, day or reason attached.

## Why It's Still Broken
Logging takes time the department does not have at 6 a.m., the scale and the handheld are in different places, and nothing the clerk sees changes when they do log. Store managers are measured on the total, not on its causes.

## What a Fix Looks Like
Put cull logging on the scale: scan or tap the item, the weight is captured, and the clerk picks one of five reasons. A daily screen shows the department what it threw away yesterday against what the forecast said it would sell. The log feeds the order engine as an over-order signal the next morning.

## Who Feels the Pain
Department managers asked to cut shrink they cannot see by item; replenishment teams tuning forecasts without the over-order label; and food-bank programmes that cannot plan pickups without knowing what is pulled.

## Impact If Fixed
Item-level cull logs at ~15 seconds per entry, ~40 entries per department per day, cost ~10 minutes a day (estimate) and give the forecast its missing label. If that cuts fresh shrink by a tenth at a store with ~$6M of fresh sales and 6% shrink, it is worth ~$36,000 a store a year (estimate).
