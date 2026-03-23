# Real-Time Motor Club SLA Risk Dashboard

**Niche:** [[niches/towing-companies/motor-club-rotation-fleets/profile|Motor Club Rotation Fleets]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool shows a dispatcher which active motor club calls are about to miss SLA — they find out after the fact when the monthly scorecard arrives.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
A dispatcher juggles 8 active calls: 3 from AAA (30-minute ETA requirement), 2 from Agero (45-minute window), 1 police dispatch (immediate), and 2 private calls. Each motor club call has a different SLA clock ticking. The dispatcher mentally tracks which calls are closest to SLA breach, but when the phone rings with a new call, they lose track. A single SLA breach contributes to a performance score that, once it drops below threshold, results in rotation suspension — which can take months to reinstate. Experienced dispatchers intuitively prioritize based on SLA risk; new dispatchers handle calls in order received, which is suboptimal.

## Why Nobody Has Built This
Motor club portals are inbound-only — they push calls to the towing company but don't provide a real-time API for SLA clock status. Building an SLA dashboard requires: (1) capturing the call acceptance timestamp, (2) tracking driver dispatch and en-route status, (3) calculating remaining SLA window based on each motor club's specific rules, and (4) predicting arrival time from GPS position and traffic. The data exists across Towbook (dispatch), GPS (driver position), and motor club portals (SLA rules) but isn't integrated.

## What to Build
A real-time dashboard overlaying all active motor club calls with SLA countdown timers, color-coded by risk (green >15 min remaining, yellow 5-15 min, red <5 min). Shows: call details, assigned driver position and predicted arrival, SLA window remaining, and escalation options (reassign to closer driver, call customer with updated ETA). Historical view shows SLA compliance trend by motor club program with projected scorecard impact.

## Target Customer
Dispatchers at towing companies with 5+ trucks handling 20-50 motor club calls per day across multiple programs.

## Impact If Built
Reduces SLA breaches from 8-15% to under 3% by surfacing at-risk calls 10-15 minutes before breach. Protecting rotation position preserves $30,000-$80,000/month in motor club call volume that would otherwise be lost to performance suspensions.
