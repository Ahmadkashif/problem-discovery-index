# The Engineer on Call for Six Transmitter Sites

**Industry:** [[broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Worker Life Changing
**One-liner:** A chief or contract engineer is the only person who can keep several stations' transmitters on the air and within their FCC parameters, and spends nights driving to mountaintop sites to diagnose alarms that a better read of the telemetry could have predicted or explained remotely.
**Tags:** #tacit-knowledge-ml #autoencoders #change-point-detection #time-series-forecasting #large-language-models #worker-facing #automation

## The Problem
Every licensed station must operate within its authorised power, frequency and, for AM directional stations, pattern parameters. It must keep its Emergency Alert System equipment working and its tower lights functioning, with outages reported to the FAA. The person responsible is a chief engineer who, at a radio cluster or a smaller TV station, may be the only engineer. Contract engineers often cover ~3–6 sites for several owners (estimate). Industry commentary describes an ageing workforce with few younger engineers behind it. One widely cited projection has 6,200 retirements against 5,100 hires needed over a decade.

The day is reactive. A remote-control system (Burk, Davicom or the transmitter maker's own monitoring) pages the engineer when reflected power rises, a power amplifier module faults or the site loses commercial power and the generator does not start. Many alarms are noise. Some are the first sign of a failure that will take the station off the air overnight. Telling the two apart depends on how this particular transmitter, line and antenna have behaved over years, and that knowledge lives in the engineer's head and a paper maintenance log at the site.

## Why It Matters to the Worker
The engineer carries the station's licence risk personally and is never off call. A 2 a.m. alarm means deciding from a phone whether to drive an hour to a snowbound site or wait until morning. Guessing wrong either way costs sleep or air time. Holidays depend on finding another engineer willing to cover. The work also includes the ATSC 3.0 transition planning the FCC opened in its October 2025 proposal, and moves of master control to group hubs. Both are layered on top of daily maintenance, with no added staff.

The engineers know their sites and equipment better than anyone. They cannot hand that knowledge to a successor or a backup in any form other than conversation and a binder, so they cannot step away from their stations without worry, and they cannot easily retire.

## What a Solution Looks Like
Telemetry from every site, pulled continuously from the remote-control systems into one place, with each transmitter's normal behaviour learned across seasons and loads. Alarms are ranked by how unusual they are for this unit and by the likely fault. A plain-language explanation draws on past incidents at the same site: "reflected power rose like this before the last line-pressure loss in February". A checklist for what to try remotely before driving out. The engineer's own diagnoses, captured in a sentence after each incident, become the training data that makes the next explanation better. When a backup covers, they inherit that site history.

## Impact If Solved
Fewer unnecessary site visits and fewer off-air hours, on the order of several nights a month back for an engineer covering six sites (estimate), and earlier fixes for failures that would otherwise take a station down. For the industry, it stretches a shrinking engineering workforce over more sites without stretching each engineer thinner. It also gives retiring engineers a way to leave their knowledge behind.
