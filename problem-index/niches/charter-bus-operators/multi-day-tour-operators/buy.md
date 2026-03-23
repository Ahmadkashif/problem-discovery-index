# Multi-Day Driver HOS Compliance Planner

**Niche:** [[niches/charter-bus-operators/multi-day-tour-operators/profile|Multi-Day Tour Operators]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ELD systems track HOS in real time but cannot plan forward across a multi-day tour itinerary to predict where compliance conflicts will occur before the trip starts.
**Tags:** #compliance #automation #time-series-forecasting #tabular-ml

## The Problem
FMCSA Hours of Service rules (10-hour driving limit, 14-hour on-duty window, 34-hour restart requirement) are straightforward for single-day charters but become complex puzzles on multi-day tours. A 5-day tour with 6-8 hours of driving per day might seem compliant, but factor in the 14-hour on-duty window (which includes loading, fueling, escorting passengers), early morning departures that compress the restart window, and timezone changes that shift the clock — and the driver can hit an HOS violation on Day 4 that forces a mandatory 34-hour restart, stranding 50 passengers for a full day. Currently, operators discover these conflicts during the trip when the ELD alerts, not during planning when the itinerary could be adjusted.

## What Already Exists
ELD providers (Samsara, KeepTruckin/Motive, Geotab) track HOS in real time and alert when violations are imminent. Fleet management platforms calculate remaining drive time for the current day. Route planning tools (Google Maps, PC*MILER) estimate driving times per segment. None of these project HOS compliance across a multi-day itinerary to identify problems before departure.

## The Customization Gap
Multi-day tour HOS planning requires: forward simulation of the entire trip itinerary against FMCSA rules (driving time + on-duty time + required rest periods), accounting for variable activity durations at each stop (a 2-hour attraction visit counts as on-duty time), identifying the specific day and hour where a violation will occur, and recommending schedule adjustments (extend a rest stop, swap drivers, adjust departure time) to prevent it. The tool must handle the 34-hour restart rule across multi-day sequences and account for the sleeper berth exception when team drivers are used.

## Target Customer
Tour operators and dispatchers planning multi-day charter trips who currently rely on manual HOS calculations or discover compliance issues mid-trip.

## Impact If Solved
Eliminates mid-trip HOS violations (currently occurring on 10-15% of multi-day charters, each resulting in $1,000-$16,000 fines and stranded passengers), and reduces planning time for HOS verification from 2-3 hours per trip to under 15 minutes.
