# Finite Scheduling Taught Aerospace Constraints

**Niche:** [[niches/aerospace-parts-suppliers/aerostructures-detail-parts/profile|Aerostructures & Airframe Detail Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Finite schedulers model machines and labour; they don't model FAI, source inspection, outside special processing or the prime's shipset sequencing.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to show a prime that a supplier can hold the next rate break, and whoever builds a capacity plan from the shop's own routings and machine data that survives the prime's rate-readiness review takes the account.

## The Problem
Shops buy a scheduler, load routings and get a plan that falls apart the first week, because the constraints that bite in aerospace are not in it: the first article that must be accepted before the second lot ships, the customer source inspector who visits on Tuesdays, the heat treater's furnace schedule, and the prime's requirement to ship complete shipsets in sequence.

## What Already Exists
Siemens Opcenter APS, PlanetTogether, Epicor's advanced planning and ProShop's scheduling handle machines, labour and due dates competently.

## The Customization Gap
An aerospace layer adds FAI and delta-FAI gates as schedule constraints, outside-processing calendars and learned turn times per processor, source inspection windows, shipset completeness rules by customer, and rate-step scenarios exported in each prime's format. It also needs to accept that some machines are qualified for some part numbers only, which customers approve.

## Target Customer
Planning managers at suppliers already running an APS or ERP scheduler that the floor ignores.

## Impact If Solved
A schedule that respects the real constraints lifts on-time delivery by ~5–10 points (estimate) without new machines and keeps the existing software investment.
