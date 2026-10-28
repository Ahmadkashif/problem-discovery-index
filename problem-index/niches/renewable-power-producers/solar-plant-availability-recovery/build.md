# Lost Megawatt-Hours Ranked by Repair

**Niche:** [[niches/renewable-power-producers/solar-plant-availability-recovery/profile|Solar Plant Availability & Underperformance Recovery]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Solar monitoring shows which inverters are down, but no system turns every fault, stuck tracker and drone finding into one repair list ranked by the megawatt-hours each fix would recover.
**Tags:** #gaussian-processes #cnns #semantic-segmentation #feature-engineering #time-series-forecasting #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to find and fix the inverters, trackers and strings that drag a plant below its expected output, and whoever has the smallest energy-based availability loss across a fleet takes the account.

## The Problem
O&M crews work from alarms and calendars. A dead inverter gets a truck roll; a tracker row stuck flat each morning, a string with a blown fuse or a block losing 3% to soiling can run for months because nobody has priced it against the other work.

## Why Nobody Has Built This
Expected output at inverter and string level needs a per-block irradiance and shading model, tracker data come from a separate vendor, and drone thermography arrives as an annual report rather than a data feed. Monitoring vendors stop at detection; O&M contractors are paid per visit.

## What to Build
A per-block expected-output model (irradiance, temperature, tracker angle, shading) compared with inverter, combiner and tracker telemetry; drone thermal and RGB imagery segmented into defect classes with locations; every loss converted into megawatt-hours per week; and a weekly repair list ordered by energy recovered per crew hour, with the result checked after each fix.

## Target Customer
Directors of solar operations at IPPs with 2 GW or more of utility-scale solar.

## Impact If Built
Raising energy-based availability from ~97.5% to ~98.5% (estimate) on 2 GW of solar producing ~4,000 GWh a year recovers ~40 GWh, ~$1.8M a year at $45/MWh.
