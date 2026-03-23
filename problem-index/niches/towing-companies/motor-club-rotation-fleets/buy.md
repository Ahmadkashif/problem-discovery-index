# Multi-Program Dispatch Priority Engine

**Niche:** [[niches/towing-companies/motor-club-rotation-fleets/profile|Motor Club Rotation Fleets]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Dispatch software exists but treats all calls equally — it doesn't model the different SLA rules, revenue rates, and performance consequences across AAA, Agero, Allstate, and police rotation.
**Tags:** #workflow-orchestration #automation #revenue-impact #quick-win

## The Problem
A towing company participates in 3-5 motor club programs plus police rotation, each with different rules: AAA requires 30-minute response with specific documentation; Agero allows 45 minutes but penalizes more harshly for customer complaints; police rotation requires immediate response but pays the highest per-call rate; private calls have no SLA but the highest margin. When multiple calls compete for the same truck, the dispatcher must weigh: which call has the tightest SLA? Which program penalizes most for a miss? Which call generates the most revenue? This multi-dimensional prioritization is done mentally, and errors are expensive.

## What Already Exists
Towbook, TOPS, and Beacon handle basic dispatch — assign a call to a truck, track status, record completion. None model program-specific SLA rules, revenue rates, or performance consequences. The dispatcher must remember: "AAA is 30 minutes and we're already on probation, so prioritize that over the Agero call which has 45 minutes and we're in good standing." This institutional knowledge lives in the dispatcher's head.

## The Customization Gap
The dispatch system needs program profiles: for each motor club and police rotation, define the SLA window, payment rate, performance scoring rules, current performance standing, and penalty consequences. When a new call arrives, the system should recommend priority based on a multi-factor score: SLA urgency x performance impact x revenue value. "Dispatch the AAA call first — you have 12 minutes of SLA left and you're at 88% compliance (threshold is 85%). The Agero call has 35 minutes and you're at 94% compliance."

## Target Customer
Dispatchers at companies participating in 3+ motor club programs who currently prioritize calls based on memory and gut feel.

## Impact If Solved
Optimizes call prioritization to protect the highest-value rotation positions first. A company that prevents one rotation suspension per year preserves $30,000-$80,000 in annual call volume while maintaining optimal revenue mix across programs.
