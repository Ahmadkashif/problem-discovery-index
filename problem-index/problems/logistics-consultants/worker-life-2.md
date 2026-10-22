# The Facility Designer Redrawing Every Scenario

**Industry:** [[logistics-consultants|Logistics Consultants]]
**Type:** Worker Life Changing
**One-liner:** A distribution centre designer spends days on site measuring and observing, then evenings in a hotel redrawing the layout in CAD for every change in volume, automation option or building the client decides to look at.
**Tags:** #k-means-clustering #graph-theory #monte-carlo-methods #optimization-fundamentals #worker-facing #automation #workflow-orchestration

## The Problem
A facility design engagement — a new distribution centre, an expansion, or an automation retrofit — begins on site. The designer walks the building, measures clear heights, column spacing and dock positions, photographs the racking and conveyor, watches picking and replenishment through a shift, and pulls the order history to build a profile: lines per order, cube per line, SKU velocity, how often SKUs are ordered together. Back at the hotel the profile becomes a slotting plan and a block layout in AutoCAD, and the layout becomes a material-handling equipment list and a labour model.

Then the scenarios multiply. The client wants to see the layout at today's volume and at five-year growth; with a goods-to-person system and without; in this building and in a candidate building with a different column grid; with and without a mezzanine. Each is a redraw, and each redraw changes the slotting, the travel distances, the equipment count and the labour model. When marketing revises the growth forecast, every scenario is redrawn again. The designer carries the reasoning — why the fast movers sit there, why the pick module is two levels, not three — in their head, because the drawings show the outcome, not the logic.

## Why It Matters to the Worker
The designer's judgement — how product should flow through a building, what an order profile implies for the pick method — is the scarce skill, and most of their week goes on drafting and re-drafting rather than on that judgement. Travel is heavy: site visits, vendor meetings, construction checks. The evenings in hotels are spent on CAD revisions that a client request at 4 p.m. made necessary.

There is also exposure. A layout that cannot reach its projected throughput at go-live is a visible, expensive failure, and it is the designer's name on it, even when the cause was a growth forecast that changed three times.

## What a Solution Looks Like
A layout assistant that takes the order profile and the building drawing and generates candidate block layouts and slotting plans for each scenario, with travel distance and throughput estimated by simulating last year's orders through each candidate; re-generates every scenario automatically when a forecast or building input changes; and records the design rules the designer applies ("fast movers within 60 feet of pack-out", "no replenishment across the pick aisle in peak"), so the logic travels with the drawing. The designer edits and approves; the drafting becomes a review.

## Impact If Solved
If each scenario redraw falls from one or two days to a couple of hours (estimate), a designer can show a client twice the options in the same engagement, and most of the late-night CAD sessions disappear from a job whose real value is in the first walk through the building.
