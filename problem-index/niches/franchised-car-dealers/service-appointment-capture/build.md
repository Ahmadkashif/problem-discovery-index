# Booking Against Real Technician Capacity

**Niche:** [[niches/franchised-car-dealers/service-appointment-capture/profile|Service Appointment Capture]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Schedulers book time slots, not the technician hours and skills a job needs, so the drive overbooks Monday and the agent's "booked" appointment becomes a two-day wait.
**Tags:** #large-language-models #time-series-forecasting #gradient-boosting #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn every inbound service call, text and web request into a kept appointment in the dealer's own scheduler, and whoever books the highest share of inbound service contacts into kept appointments takes the account.

## The Problem
An agent or BDC rep books "Tuesday 8 a.m." for a customer describing a transmission shudder. The scheduler has the slot; it doesn't know that only one technician is certified for that diagnosis and he is booked solid, so the car sits. J.D. Power's 2025 study still found appointment waits longer than in 2018–2022 (search summary).

## Why Nobody Has Built This
Technician skills, certifications and flagged-hour capacity live in the DMS and the foreman's head; scheduler vendors sell slot grids, and voice-agent vendors sell conversations.

## What to Build
A capacity layer that maps the caller's concern to likely op codes and labour time, forecasts each technician's available hours by skill, and offers only appointments the shop can complete, with loaner and parts checks, written back to the DMS scheduler by the agent.

## Target Customer
Fixed ops directors at high-volume stores with mixed technician skill levels and EV or diagnostic specialists.

## Impact If Built
Fewer cars waiting for a qualified technician, fewer reschedules and a higher kept-appointment rate; a store booking ~1,500 appointments a month (estimate) that avoids ~5% reschedules saves ~75 frustrated customers a month.
