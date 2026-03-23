# Labor Scheduling for Harvest and Crop Maintenance

**Niche:** [[niches/greenhouse-horticulture/controlled-environment-vegetable/profile|Controlled-Environment Vegetable Production]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** CEA vegetable operations schedule harvest crews based on the head grower's visual estimate of fruit readiness — a subjective assessment that routinely results in 15-25% over- or under-staffing because actual harvest volume varies unpredictably from the estimate.
**Tags:** #gradient-boosting #regression #tabular-ml #worker-facing #automation

## The Problem
A 20-acre greenhouse tomato operation employs 40-80 harvest workers, with daily labor needs varying by 30-50% depending on the volume of ripe fruit. The head grower walks the greenhouse 1-2 days before harvest and estimates the next day's yield by visually scanning truss ripeness across rows and zones. This estimate determines how many workers are called in. Under-estimating means ripe fruit is left on the vine (overripe tomatoes lose 1-2 quality grades, dropping $0.50-$1.50/lb in value), and over-estimating means workers are paid for idle time ($15-$20/hour). The estimation error compounds across the week because unharvested fruit from Day 1 adds to Day 2's volume unpredictably.

## Why It's Still Broken
Fruit ripening rate depends on accumulated temperature, light, and crop load in ways that interact non-linearly. The grower's visual estimate integrates these factors intuitively but inconsistently. Climate computer data logs the environmental conditions driving ripening but no model connects these inputs to daily harvestable volume. Computer vision for fruit counting and color staging exists in research (e.g., using overhead cameras to count red vs. green fruit), but no commercial greenhouse has deployed it as a harvest forecasting tool. The labor scheduling problem is further complicated by worker transportation logistics (many workers are bused from centralized housing) and minimum shift requirements.

## What a Fix Looks Like
A harvest forecasting model that predicts daily harvestable volume (in lbs/sq meter) for each zone, 2-3 days ahead. The model ingests: accumulated temperature and light data from the climate computer, recent harvest volumes by zone (from scanner/scale data at the pack line), and fruit count/color data from periodic camera captures or worker-reported estimates. Output: recommended crew size per day with confidence intervals, plus zone-level harvest priorities. Integrates with the crew scheduling system to generate worker call-in lists 24-48 hours in advance.

## Who Feels the Pain
Head growers who spend 4-6 hours per week on harvest estimation walks and still mis-forecast by 15-25%. Harvest workers who face unpredictable schedules — called in early for big harvest days, sent home mid-shift when volume is lighter than expected. Pack line managers who must adjust processing capacity to match actual (not forecasted) harvest volume.

## Impact If Fixed
Labor scheduling accuracy improves from +/- 20% to +/- 8%, reducing overtime costs and idle labor by $50K-$150K annually on a 20-acre facility. Overripe fruit loss reduced by 30-40% through timely harvest, recovering $100K-$300K in quality-grade value. Worker satisfaction improves with more predictable schedules, reducing turnover in an industry where harvest worker turnover exceeds 40% annually.
