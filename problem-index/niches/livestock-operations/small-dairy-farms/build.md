# Affordable Activity-Based Heat Detection for Small Herds

**Niche:** [[niches/livestock-operations/small-dairy-farms/profile|Small Dairy Farms]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No heat detection system exists at the $5-8/cow/year price point that a 100-cow dairy can justify — current systems cost $15-25/cow in hardware plus $5,000-15,000 in infrastructure, creating a minimum herd size of 300+ cows to break even.
**Tags:** #lstm #anomaly-detection #signal-processing #tacit-knowledge-ml #revenue-impact

## The Problem
On a 100-cow dairy, a missed heat (estrus) event extends the calving interval by 21 days, costing $250-400 in lost milk production and additional feed. Visual heat detection — watching for mounting behavior, restlessness, and mucus discharge — requires checking the herd 3-4 times daily for 20-30 minutes each time. Even experienced farmers achieve only 50-60% detection rates because standing heat lasts just 8-12 hours and often occurs at night. The cumulative cost of missed heats on a 100-cow herd at 55% detection rate is $15,000-$25,000/year in extended days open.

## Why Nobody Has Built This
Existing activity monitoring systems (collar or leg-mounted accelerometers) require a base station receiver network, herd management computer, and dealer installation — creating a $10,000-$20,000 fixed cost that only amortizes over large herds. A small-herd-viable system requires a completely different architecture: low-cost sensors ($5-10/unit at scale using MEMS accelerometers and BLE), smartphone-based data collection (farmer walks through the barn with phone acting as receiver), and cloud-based analytics that eliminate the on-farm computer requirement. No precision dairy company has targeted this market because per-farm revenue is too small to justify their enterprise sales model.

## What to Build
A BLE-enabled leg band ($8-10/cow) paired with a smartphone app that collects activity data during twice-daily milking (when cows pass within BLE range). An LSTM model trained on activity patterns from large-herd reference data identifies heat events from the 12-hour activity profile between milkings. The farmer receives a push notification: "Cow #47 is likely in heat — inseminate within 8 hours." No base station, no herd computer, no dealer installation.

## Target Customer
Dairy farmers with 50-200 milking cows who currently rely on visual heat detection or tail paint/chalk methods. Approximately 20,000 US dairy operations at this scale. Price point: $8-12/cow/year subscription including hardware amortization.

## Impact If Built
Heat detection rate increases from 55% to 85%, reducing average days open from 140 to 105 days. At $3/day cost of an open cow, this saves $105/cow/year on a 100-cow herd — $10,500 annually, against a system cost of $800-$1,200/year. The 3-year economic impact exceeds $25,000 per farm.
