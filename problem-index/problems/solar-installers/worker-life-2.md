# System Performance Anomaly Detection and Proactive Customer Communication

**Industry:** [[solar-installers|Solar Installers]]
**Type:** Worker Life Changing
**One-liner:** Solar installers whose monitoring platforms (SolarEdge, Enphase) show hundreds of installed systems but have no automated alert system for underperforming systems — meaning customers notice the underperformance months before the installer does — get proactive anomaly alerts and auto-drafted customer communication before the customer calls to complain.
**Tags:** #isolation-forest #anomaly-detection #time-series-forecasting #signal-processing #worker-facing

## The Problem

After installation, solar systems are monitored by inverter platforms (SolarEdge monitoring, Enphase Enlighten). These platforms display production data and generate alerts for complete system failures but don't detect gradual underperformance — a partially shaded string producing 30% below expected output, a single inverter with a communication fault dropping offline intermittently, or seasonal production below modeled expectations that might indicate a faulty string fuse.

Customers who see their electricity bills higher than expected after installing solar become angry before calling the installer — they've been watching it for 2-3 months while the problem went undetected. Proactive outreach from the installer ("We noticed your system produced 15% below expected last month — we'd like to schedule a check") converts a potential complaint call into a loyalty moment.

## Why It Matters to the Worker

Customer service reps at solar companies spend significant time on inbound calls from customers who have noticed underperformance. These calls are reactive and often come with months of compounding customer frustration. Proactive detection and outreach before the customer calls converts the interaction from damage control to customer care.

## What a Solution Looks Like

A monitoring overlay on SolarEdge/Enphase data: for each installed system, compare monthly production against the original Aurora Solar production estimate (adjusted for actual weather conditions using NREL weather data). Flag systems producing > 10% below weather-adjusted expectations for two consecutive months. Auto-draft a customer communication: "We've noticed your system's production was lower than expected last month — this might indicate a panel, string, or inverter issue. We'll schedule a review at no charge." Route to the service scheduler. Customer receives a proactive call before they've had time to become upset.

## Impact If Solved

Reduces reactive complaint calls. Identifies hardware warranty issues earlier — catching them in the manufacturer warranty window vs. after. Turns system monitoring into a proactive customer retention and upsell channel (e.g., customers with marginal shade situations can be offered microinverter upgrades when production data demonstrates the benefit).
