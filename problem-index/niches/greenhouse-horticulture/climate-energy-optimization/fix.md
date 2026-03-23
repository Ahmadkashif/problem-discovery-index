# Night Energy Waste from Conservative Heating Setpoints

**Niche:** [[niches/greenhouse-horticulture/climate-energy-optimization/profile|Climate & Energy Optimization]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** Growers set nighttime heating setpoints 3-5°F higher than the crop actually requires because the cost of a cold event (crop damage worth $50K-$500K) far outweighs the cost of over-heating ($50-$200/night) — but this risk-averse default wastes 15-25% of total heating energy across the winter season.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact #automation

## The Problem
Nighttime heating is the single largest energy cost in greenhouse operations — 60-70% of annual heating expenditure occurs between 10 PM and 6 AM during the heating season (October-April in northern regions). The head grower sets night temperature setpoints based on the crop's minimum temperature tolerance plus a safety margin. The safety margin exists because: (1) greenhouse temperature can drop faster than the heating system responds during cold snaps, (2) perimeter zones lose heat faster than interior zones, creating cold pockets, and (3) the consequence of a cold event (crop damage or loss) is catastrophic relative to the cost of extra heating. So the grower over-heats by 3-5°F every night as insurance. On a 5-acre greenhouse spending $400K/year on heating, this conservative buffer costs $60K-$100K annually.

## Why It's Still Broken
The grower is making a rational decision under uncertainty: the downside risk of under-heating ($50K-$500K crop damage) dwarfs the cost of over-heating ($50-$200/night). But the uncertainty is reducible — with better weather forecasting, better thermal modeling of the specific greenhouse structure, and better understanding of each crop's actual cold tolerance (which varies by growth stage, health status, and acclimation history). Current climate computers apply the same static setpoints regardless of whether the overnight low is 25°F (dangerous) or 40°F (no heating needed at all). A predictive system that knows "tonight's low is 32°F, your greenhouse holds heat for 3 hours at this outside temperature, the crop in Zone 4 tolerates 58°F for up to 4 hours — safe to lower setpoint from 65°F to 60°F" would save energy on the 80% of winter nights that are not actually dangerous.

## What a Fix Looks Like
A night setpoint advisory system that runs each evening at 6 PM. It ingests: (1) the hourly overnight weather forecast (temperature, wind speed, cloud cover), (2) the greenhouse's thermal response model (learned from historical data: how fast does inside temperature drop when outside temperature falls, by zone?), (3) crop-specific minimum temperature thresholds by zone and growth stage, and (4) heating system response characteristics (how quickly can the system recover if temperature drops below target?). Output: recommended night setpoints per zone with a risk assessment ("Zone 3: recommend 60°F instead of 65°F, estimated energy savings $85, risk level: low — outside temperature will not drop below 30°F and recovery time is 12 minutes if forecast is wrong by 5°F").

## Who Feels the Pain
Head growers who know they are over-heating but cannot quantify the risk of reducing setpoints on any given night. Facility managers who see the heating bills and know there is waste but cannot identify which nights and which zones. Ownership that watches competitors in milder climates operate at lower energy costs.

## Impact If Fixed
Night heating energy reduced by 15-25% through dynamic setpoint management, saving $40K-$100K annually on a 5-acre greenhouse. Crop risk does not increase — the system only recommends reductions on nights where the safety margin is unnecessarily large. Grower confidence increases over time as the system's predictions prove reliable, enabling progressively tighter setpoints. Across a 5-month heating season, this represents 100+ nights of measurable savings.
