# The Construction Work Plan Nobody Updates

**Niche:** [[niches/electric-utilities/small-coops-and-munis/profile|Small Cooperatives & Municipal Utilities]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** A co-op's multi-year construction work plan is written by a consulting engineer, approved by the board, and overtaken by events within a year.
**Tags:** #time-series-forecasting #descriptive-statistics #data-integration #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell a small co-op or city utility with no engineer on staff where its feeders and transformers will run out of capacity, and whoever catches the most overloads before they cause a failure or stall a new connection takes the account.

## The Problem
Many co-ops borrowing from the Rural Utilities Service or other lenders base their capital programme on a construction work plan, typically covering several years and prepared by a consulting engineer (recalled). When a large load appears or a feeder starts overloading, the plan is out of date, but redoing it means another engagement and another wait.

## Why It's Still Broken
The plan is a document, not a model. Its load forecast, feeder analysis and project list are frozen at the date of writing, and the co-op has nobody to keep them current.

## What a Fix Looks Like
Turn the plan into a living model. The consulting engineer's feeder analysis and project list are loaded once, then updated monthly from AMI loading and new service requests. The co-op is alerted when a feeder or substation approaches the threshold that triggers a planned project earlier than scheduled, or when a new request changes the order.

## Who Feels the Pain
General managers explaining surprise capital needs to boards and lenders; consulting engineers re-doing analysis; members waiting for service.

## Impact If Fixed
Capacity needs flagged ~6–12 months earlier (estimate), fewer emergency projects, and board decisions grounded in current loading.
