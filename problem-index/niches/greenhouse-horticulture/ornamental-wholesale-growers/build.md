# Growth-Stage Inventory Tracking with Bloom Date Prediction

**Niche:** [[niches/greenhouse-horticulture/ornamental-wholesale-growers/profile|Ornamental Wholesale Growers]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product tracks the growth stage of living crop lots in a greenhouse and predicts bloom dates using accumulated climate data — growers manage this entirely in their heads or on whiteboards, and when the head grower leaves, the knowledge walks out the door.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A wholesale ornamental grower managing 100+ crop lots across 10 greenhouse zones must know, at any moment, where each lot stands in its growth cycle and when it will be ready to ship. The head grower tracks this mentally: "Zone 3 poinsettias got their short-day treatment on September 15, they're showing first color, should be ready by November 18 if we keep nights at 62°F." This tracking depends on weekly physical walks through every zone, visual assessment of growth stage against the grower's internalized cultivar response curves, and mental adjustment for the accumulated light and temperature each lot has received. When the grower is out sick, on vacation, or retires, nobody else can make these assessments. The financial stakes are large: a 10-acre poinsettia crop worth $2M that blooms one week early or late loses $300K-$600K in value.

## Why Nobody Has Built This
Growth-stage tracking requires defining measurable phenological stages for dozens of crop species and hundreds of cultivars, then collecting training data that links accumulated growing conditions (temperature, light integral, photoperiod) to growth stage progression. This data does not exist in structured form — it lives in the grower's observations and is never recorded systematically. Building the prediction model requires multi-season data collection at partnering greenhouses, with growers recording weekly growth stage scores alongside climate computer data. No greenhouse technology company has invested in this data collection effort because each grower manages it adequately (in their head) until they do not.

## What to Build
A production management layer that: (1) registers crop lots with planting date, cultivar, zone assignment, and photoperiod treatment protocol, (2) captures weekly growth stage scores via a simple mobile interface (grower selects from 5-8 stage photos per crop type), (3) ingests climate data from the greenhouse's climate computer (accumulated temperature, DLI, photoperiod), and (4) predicts ship-readiness date using a gradient-boosted model trained on historical lot data. The system alerts when a lot is falling behind schedule (needs warmer temperatures or more light) or running ahead (needs growth regulation). After 2-3 seasons of data collection, the model provides predictions accurate to within 3-5 days.

## Target Customer
Head growers and operations managers at ornamental wholesale greenhouses with 5+ acres and 50+ active crop lots. Approximately 3,000-5,000 US operations at this scale. Price point: $300-$800/month.

## Impact If Built
Bloom timing accuracy improves from +/- 7-10 days (current manual tracking) to +/- 3-5 days, reducing crop timing losses by 30-50%. For a grower with $5M in annual flowering crop revenue, preventing 5% timing shrink saves $250K/year. Space utilization improves 5-10% when crop finish dates are predicted accurately enough to pre-schedule the next crop cycle.
