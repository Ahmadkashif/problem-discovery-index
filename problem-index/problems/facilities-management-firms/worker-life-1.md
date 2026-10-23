# The Technician Whose Route Is Rebuilt Every Hour

**Industry:** [[facilities-management-firms|Facilities Management Firms]]
**Type:** Worker Life Changing
**One-liner:** A mobile multi-craft technician covering a region of unstaffed sites gets back a plannable day and unbroken nights when dispatch stops tearing up the route for every new call and an alarm is checked remotely before anyone gets in the van.
**Tags:** #worker-facing #optimization-fundamentals #dynamic-programming #time-series-forecasting #change-point-detection #workflow-orchestration #automation

## The Problem
On a retail, bank-branch or light-industrial portfolio, the FM firm does not staff each building. One technician covers ten or fifteen sites spread across a metro area. The day starts with a planned list: two PMs, a lighting repair, a generator run. Then a priority call lands, and dispatch sends the technician forty minutes across town. An hour later another lands, back near where the day started. Each new call rebuilds the route around the SLA clock of whatever arrived last. The planned work slides to tomorrow and becomes overdue, the PM-completion KPI suffers, and the technician spends more of the shift driving than working.

On-call weeks add the night. The building automation system raises an alarm (high space temperature, a freezer warning, a low-pressure alert on a boiler), the service desk sees a priority call, and the on-call technician is woken and sent. Many of these alarms turn out to be nothing: a sensor drifting, a setpoint someone changed, a unit that recovered on its own ten minutes after alarming. The technician drives an hour each way to confirm it, then starts the next day's route on four hours of sleep.

## Why It Matters to the Worker
The technician cannot plan a day, a school pickup or a lunch break, because the route belongs to whichever call came in last. Overdue PMs and missed response times are logged against their name even when dispatch caused them. Repeated false-alarm callouts are the most resented part of the job: lost sleep and lost family time for problems that a look at the trend data would have dismissed. Fatigue on the road is also a safety risk the employer rarely counts.

## What a Solution Looks Like
Dispatch that plans the day as a whole rather than one call at a time. It groups work by geography and skill, slots true emergencies in where they cost the least disruption, and moves a non-urgent call to the technician already nearby, or to the next morning when the contract's priority definition allows it. The technician sees an honest route with realistic times and a protected block for planned work. For alarms, a remote check runs before the callout: the system reads the asset's recent trend, recognises sensor faults, transient excursions and self-recovery, and either clears the alarm with a note for the morning or escalates it with the evidence attached. On-call rotations are balanced on actual callouts, not just on the calendar.

## Impact If Solved
Less windshield time and more completed planned work each shift, and a large share of night callouts handled without a trip (estimate: a third or more of after-hours alarm dispatches avoided on portfolios with BAS access). A technician on call can expect to sleep through most nights, which is the difference between a job people stay in and one they leave.
