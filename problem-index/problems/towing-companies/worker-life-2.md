# Dispatcher Multi-Priority Call Management

**Industry:** [[towing-companies|Towing Companies]]
**Type:** Worker Life Changing
**One-liner:** Dispatchers juggle police rotation calls with 8-minute SLAs, motor club calls with 30-minute windows, and direct customer calls simultaneously — a priority-aware queue system prevents the cognitive overload that leads to burnout and errors.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #bias-variance-tradeoff #worker-facing

## The Problem
A towing company dispatcher on a busy shift manages 15–30 active calls simultaneously across three distinct priority channels: police/law enforcement rotation calls (highest urgency, strict response windows, penalties for non-response), motor club dispatches from AAA/Agero/Allstate (contractual SLA windows, rotation ranking at stake), and direct consumer calls (revenue-positive but no SLA enforcement). Each call has a different urgency profile, truck-type requirement, and geographic constraint. The dispatcher must mentally track which drivers are available, en route, or on-scene; estimate completion times for active jobs; and sequence incoming calls against available resources — all while answering phones, entering data into dispatch software, and communicating with drivers via radio. During peak periods (rush hour accidents, winter storms, holiday weekends), call volume can triple and the dispatcher's mental model breaks down, leading to missed SLA windows, double-dispatched trucks, and forgotten callbacks.

## Why It Matters to the Worker
Dispatcher burnout is the primary reason for turnover in the role, with average tenure under 18 months at high-volume shops. The stress is not just volume — it is the consequence asymmetry: a missed police rotation call can result in the company losing its rotation spot (worth thousands per month), while a forgotten consumer callback loses a $150 tow. Dispatchers internalize this pressure personally. Night-shift dispatchers working alone carry the entire operation's revenue risk on their decisions. Many describe the job as "air traffic control without the training, the pay, or the respect."

## What a Solution Looks Like
A priority-ranked call queue that ingests calls from all channels (police CAD integration, motor club API feeds, phone/web intake), assigns dynamic priority scores based on SLA deadline proximity, revenue value, and truck availability, and presents the dispatcher with a single ordered worklist. The system highlights calls approaching SLA deadlines with countdown timers, suggests driver assignments based on proximity and truck type, and flags conflicts (two high-priority calls requiring the same truck type with no available units). The dispatcher remains in control of every decision but is never mentally reconstructing the priority stack from scratch.

## Impact If Solved
Reduces dispatcher decision errors by 40–60% during peak periods, directly protecting motor club rotation positions. Extends average dispatcher tenure by reducing the cognitive burden that drives burnout. Enables a single dispatcher to handle 25–30% more concurrent calls without quality degradation.
