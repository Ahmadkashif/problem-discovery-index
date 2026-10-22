# SLA Credits Computed From Outage Logs by Hand

**Niche:** [[niches/satellite-operators/enterprise-backhaul-capacity/profile|Enterprise, Backhaul & Government Data Capacity]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Every month someone reconciles outage tickets, rain-fade exclusions and customer complaints into an availability figure the customer then disputes.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to sell guaranteed throughput across GEO, MEO and partner LEO capacity at a price per megabit that survives comparison with Starlink, and whoever can design, quote and prove a multi-orbit service level fastest takes the carrier or enterprise contract.

## The Problem
Managed-service contracts promise availability per site, often excluding rain fade above a threshold, sun outages, customer-caused faults and planned maintenance. Computing the month's figure means joining network management alarms, NOC tickets, weather data and maintenance windows, then deciding which minutes count. Customers keep their own logs and frequently disagree.

## Why It's Still Broken
The exclusion rules are written differently in each contract, the data needed sits in four systems, and the customer has no visibility of the operator's evidence. A dispute costs less than building a system, so each one is settled by negotiation.

## What a Fix Looks Like
A contract-aware availability engine that encodes each contract's rules, computes availability per site from network data, attaches evidence for every excluded minute (radar rain rate, sun-outage calendar, maintenance notice), and shares the report with the customer continuously rather than monthly.

## Who Feels the Pain
Service managers who assemble the reports; account managers who negotiate the credits; customers whose own numbers never match.

## Impact If Fixed
SLA reports in minutes, fewer disputed credits, and the evidence that makes a multi-orbit SLA credible against LEO competitors.
