# One Shop Plan for Customer Work and Rigging

**Niche:** [[niches/powersports-and-boat-dealers/service-rigging-commissioning/profile|Service, Rigging & Commissioning]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Customer commissioning and new-unit rigging compete for the same technicians in the same spring weeks, and no tool plans the two together.
**Tags:** #time-series-forecasting #exponential-smoothing #dynamic-programming #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to turn technician hours into billed, right-first-time work, but the spring queue of customers' boats and machines and the rigging bay that prepares new inventory for delivery are won on different measures (billed hours per technician across the year; comebacks in the first 30 days after delivery) by different vendors. Decomposed into contested sub-niches below.

## The Problem
In April the service manager must choose, every day, between commissioning a customer's boat that has been waiting two weeks and rigging a new boat sold at the winter show whose buyer wants it for Memorial Day. Both are urgent. Customer work bills at the retail labour rate; rigging is internal, often paid at a set rate, but it releases a sale and its gross.

## Why Nobody Has Built This
DMS service modules schedule repair orders; rigging is usually tracked on a whiteboard as part of the sale. The two are owned by different managers (service and sales), and each vendor builds for one of them.

## What to Build
A shop plan covering both queues: forecast customer commissioning demand from storage contracts and last year's repair orders; list sold-not-delivered units with promised dates and rigging hours; and allocate technicians by skill across both, weighting each job by its value and its deadline, with water-test and lift slots as constraints. The output is a weekly plan the service and sales managers can both see and argue over.

## Target Customer
Fixed-operations directors at marine and powersports groups; service managers at single stores with a rigging bay.

## Impact If Built
Pre-booking 15–20% of commissioning into February and March and sequencing rigging around delivery dates (estimate) can add 100–200 billed hours a technician a year and cut late deliveries that cost sales.
