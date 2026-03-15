# Dynamic Route Reoptimization During Delivery

**Industry:** [[last-mile-delivery|Last-Mile Delivery]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic route optimization tools plan the day's stops before departure but don't reoptimize the remaining route in real time as stop completion times deviate from plan, traffic conditions change, and failed deliveries require rerouting decisions.
**Tags:** #tabular-ml #time-series-forecasting #workflow-orchestration #automation

## The Problem

A 40-stop route optimized at 7am is increasingly suboptimal by noon. Some stops took longer than planned (access difficulty, recipient interaction), others were faster. Traffic evolved differently than predicted. Three failed deliveries have been returned to pending. The driver is running behind schedule — but are they behind by 30 minutes across the whole day or are the remaining stops realistically completeable? The static morning plan can't answer this.

Route optimization tools (Route4Me, OptimoRoute) provide static plans. Real-time reoptimization of the remaining sequence given current position, remaining stops, and elapsed time is a continuous problem that existing tools handle poorly for dynamic operations.

## What Already Exists

Google Maps and Waze provide real-time traffic routing. Route4Me and Circuit have some real-time update capabilities. None integrate current driver position, remaining stop time estimates, and dynamic traffic into a continuously-updated "will I finish the route?" prediction.

## The Customisation Gap

A real-time reoptimization tool needs: (1) integration with driver GPS position from telematics; (2) updated stop-time estimates based on current-day performance (if the driver is averaging 5 minutes/stop vs. the planned 4 minutes, reproject the remaining route); (3) ETA for each remaining stop updated in real time for customer notification; (4) identification of stops that will exceed the delivery commitment window (so the dispatcher can notify customers before the window passes, not after). The real-time position + adaptive time estimate model is the gap.

## Impact If Solved

Improves day-end customer satisfaction by providing accurate ETAs (not morning estimates that become 3+ hours wrong by midday). Enables dispatcher to proactively reschedule stops that can't be reached within commitment windows. Reduces failed delivery attempts from time-window misses.
