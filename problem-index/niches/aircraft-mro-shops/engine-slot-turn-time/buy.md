# Production Scheduling Adapted to Repair-Vendor Loops

**Niche:** [[niches/aircraft-mro-shops/engine-slot-turn-time/profile|Engine Shop Slot & Turn-Time Commitments]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Factory scheduling software assumes the shop makes the parts; an engine shop sends hundreds of piece parts out to repair vendors and waits.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to quote an engine's release date at induction and hit it while parts and repair vendors slip, and whoever keeps the most engines inside their quoted turn time takes the account.

## The Problem
A disassembled engine produces hundreds of piece parts. Some are inspected and returned to stock, some are repaired in-house, and many go out to specialist repair vendors (blades, vanes, cases, seals) and come back weeks later, if they come back on time. The shop's schedule is a network of these loops plus the test cell, and it is re-planned by hand.

## What Already Exists
Advanced planning and scheduling tools (Siemens Opcenter, Dassault DELMIA Ortems, PlanetTogether), MRO system planning modules, and generic project scheduling.

## The Customization Gap
The adaptation needs: (1) repair-vendor loops modelled as uncertain-duration operations with each vendor's history by part type; (2) kitting logic that reassembles a module only when all its parts are back or substituted; (3) the test cell as a finite shared resource with re-test probability; (4) substitution rules for used serviceable or new parts when a repair loop runs late; and (5) re-planning when teardown changes the workscope. Factory schedulers model none of this by default.

## Target Customer
Production planning managers at engine and large component shops.

## Impact If Solved
A scheduler that reflects repair loops could raise on-time releases by ~10 points (estimate) and cut planners' daily re-planning from hours to minutes, at a shop releasing ~150–300 engines a year.
