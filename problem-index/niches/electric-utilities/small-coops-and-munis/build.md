# A Shared Planning Service Run Through the G&T

**Niche:** [[niches/electric-utilities/small-coops-and-munis/profile|Small Cooperatives & Municipal Utilities]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dozens of small utilities under one generation-and-transmission cooperative each lack a planner, while the G&T already holds their meter and load data.
**Tags:** #gradient-boosting #time-series-forecasting #k-means-clustering #feature-engineering #data-integration #ai-platform
**Contested on:** Every serious competitor in this niche is fighting to tell a small co-op or city utility with no engineer on staff where its feeders and transformers will run out of capacity, and whoever catches the most overloads before they cause a failure or stall a new connection takes the account.

## The Problem
A small co-op gets a request for a 5 MW crypto or data facility, a cluster of farm solar applications, or an EV fleet depot. It has no planner, so it calls its consulting engineer and waits weeks. Meanwhile its G&T sees the wholesale load and may hold AMI data for all its members, but offers planning only as occasional studies.

## Why Nobody Has Built This
Vendors sell to individual utilities and find small ones too costly to serve one by one. G&Ts have the relationship and data but are organised to sell power, not software.

## What to Build
A multi-tenant planning service operated by or through the G&T or joint action agency. It ingests each member's AMI, GIS (often a simple Milsoft model) and outage data. It provides feeder loading and capacity views, a quick screen for new loads and DER modelled on the large-utility version, transformer overload alerts from meter data, and load forecasts that roll up to the G&T's own wholesale planning.

## Target Customer
Member-services and engineering directors at G&Ts and joint action agencies, buying on behalf of 10–50 member utilities each.

## Impact If Built
New-load and DER requests answered in ~2–5 days instead of the ~3–6 weeks a consulting-engineer engagement takes (estimate), and member load growth visible to the G&T a planning cycle earlier.
