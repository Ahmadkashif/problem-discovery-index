# The Roll-Off Dispatcher's Whiteboard

**Industry:** [[waste-haulers|Waste Haulers]]
**Type:** Worker Life Changing
**One-liner:** A roll-off dispatcher juggles phoned-in swap requests, a yard of boxes scattered across job sites and drivers stuck in landfill lines, all from memory and a whiteboard, and gets back a working day without constant interruption when orders and containers are tracked for them.
**Tags:** #large-language-models #time-series-forecasting #optimization-fundamentals #worker-facing #workflow-orchestration #automation

## The Problem
Roll-off work runs on short-notice orders from contractors: drop a 20-yard box at a new job, swap the 30 at the Elm Street site before the framers arrive, pull the 40 from the demolition when the excavator finishes. Most orders arrive by phone or text, many before 7 a.m. and many changed later the same day. The dispatcher matches them against a fleet of roll-off trucks, each doing perhaps five to ten hauls a day (estimate), and against an inventory of open-top boxes of five or six sizes, some in the yard, some at job sites, some damaged. Every haul includes a trip to a landfill or transfer station whose lines and hours vary, and some boxes come back overweight or full of material the landfill refuses.

The dispatcher's tools are a board, the billing system, a phone that never stops and memory. Which boxes have sat at a finished job for three weeks, earning nothing because nobody called to pull them? Which customer is on credit hold? Which street placement needs a city permit that expires Friday? Which driver can still make the landfill before it closes? The questions come all day, from drivers, customers, sales reps and the owner. When something goes wrong — a box dropped at the wrong address, a swap missed, a contractor's crew standing idle — the dispatcher takes the call.

## Why It Matters to the Worker
Dispatching is interruption work. A dispatcher may handle well over a hundred calls and texts a day (estimate), each breaking a plan built from memory, and the cost of forgetting one is an angry contractor and a driver sent across town twice. The job concentrates blame: drivers blame dispatch for bad sequencing, customers blame dispatch for late swaps, and the owner blames dispatch for idle boxes. Dispatchers at small and mid-sized haulers often also take customer service calls and enter billing, so the day never has a quiet hour.

The knowledge is also a trap. The best dispatchers carry the whole yard in their heads, which makes them hard to replace and hard to give a day off. When they leave, the company loses track of boxes and customers for weeks.

## What a Solution Looks Like
Orders taken from calls, texts and web forms into a structured queue, with the job-site address confirmed against the map and the customer's account and credit status checked. A live container map showing every box by size and condition, its days on site and when it last moved, with stale boxes flagged for a pull call. A suggested sequence for each truck that accounts for landfill hours and typical waits, which the dispatcher adjusts rather than builds from scratch. Rental days and overweight charges calculated from the box's actual dwell time and scale ticket, not from memory. Drivers update the job from the cab, so the dispatcher stops being the switchboard.

## Impact If Solved
Taking order entry and box tracking off the dispatcher's memory would give back ~2 hours a day per dispatcher (estimate), and flagging boxes idle at finished jobs typically lifts hauls per container by ~10% (estimate) — which for the dispatcher means fewer emergency drops when the yard runs empty.
