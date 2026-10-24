# The Pumper's Route

**Industry:** [[oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Worker Life Changing
**One-liner:** A pumper drives the same loop of ~30 to 60 wells every day (estimate), gauging tanks and writing numbers on a form, and decides by memory which well is in trouble; a route that showed the exceptions first would give back hours of driving and the blame for the well they didn't reach.
**Tags:** #gradient-boosting #change-point-detection #time-series-forecasting #feature-engineering #worker-facing #automation #quick-win

## The Problem
The pumper, or lease operator, is the operator's eyes on its wells. Each morning they drive a route, often 100 to 200 miles of lease road (estimate), and stop at every well and tank battery. At each stop they gauge oil and water tanks with a tape or read the level gauge, read gas meters and chart recorders, check the pumping unit, the separator, the heater-treater and the chemical pump, and look for leaks, stuck valves and tripped motors. They write the readings on a gauge sheet or tap them into a phone app, fill out run tickets when a truck hauls oil, and call the foreman when something is down.

Larger operators have SCADA on newer pads, but the pumper still visits, and on older and smaller wells the gauge sheet is the production record. The route is fixed by habit, not by need: the well that has been fine for six months gets the same stop as the one whose fluid level has been dropping for a week. When a well goes down at the far end of the loop, it can sit off production until tomorrow's visit. Many pumpers are contractors paid per well per month, so a longer route earns more but leaves less time per well.

## Why It Matters to the Worker
The job is long, solitary and judged on things the pumper cannot see coming. A pumper who misses a failing pump or an overflowing tank is the one blamed for the lost barrels or the spill, even if the warning sign was a slow trend across a week of handwritten numbers. The paperwork happens at the end of the day or in the truck, and the gauge sheet gets re-keyed by someone in the office, who calls back with questions.

Experienced pumpers carry a mental model of every well: this one always runs low after a rain, that separator dumps late in cold weather, this tank reading is off because the gauge board sticks. New pumpers have none of it, and the well-by-well knowledge leaves when the experienced pumper retires.

## What a Solution Looks Like
A phone app that the pumper already uses for readings ranks the day's stops. It learns each well's normal pattern from past gauge readings, SCADA where present, run tickets and downtime notes, and flags the wells whose recent numbers break that pattern, with the reason in plain words: "oil down 30% for three days, water up, check the pump". The pumper still visits what the operator requires, but in exception order, and readings are captured once, by voice or photo of the gauge, with the office copy filled in automatically.

## Impact If Solved
If exception-first routing gets a down well back on production a day sooner on even a few wells a month, a route of 50 wells making ~10 BOE/d each (estimate) recovers hundreds of barrels a year. The pumper saves the end-of-day re-keying, roughly 30–60 minutes a day (estimate). The stripper-well version of this burden, with paper production reports, is described under [[oil-gas-field-services|Oil & Gas Field Services]].
