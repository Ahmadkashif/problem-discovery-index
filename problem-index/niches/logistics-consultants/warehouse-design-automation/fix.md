# Vendor Throughput Claims Compared on Different Order Profiles

**Niche:** [[niches/logistics-consultants/warehouse-design-automation/profile|Warehouse Design & Automation Advisory]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Two vendors' units-per-hour figures sit side by side in the selection deck, calculated on different order mixes, and the owner picks the bigger number.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #feature-engineering #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to predict the throughput a redesigned or automated building will actually reach on the client's own order profile, and whoever's projections hold at go-live wins the next site.

## The Problem
The request for proposal includes the client's order data, but each vendor extracts its own design day and makes its own assumptions about lines per order, units per line and order release. Their throughput claims arrive as single numbers. The selection deck compares them directly, and the difference that decides the award is often a difference in the profile each vendor chose rather than in the systems.

## Why It's Still Broken
Specifying the profile exactly enough to bind vendors takes analysis time the consultant has not budgeted, and vendors resist being held to a profile they did not choose. Rebuilding every proposal in a common simulation is too slow for the selection timeline.

## What a Fix Looks Like
Issue a fixed, machine-readable order-profile package with the RFP — design-day orders, peak hour, growth years — and require every vendor to report throughput against it, along with the assumptions they changed. Check each submitted claim against the package with a short automated comparison before the steering committee sees it.

## Who Feels the Pain
Owners who commit tens of millions to a system on a misleading comparison; operations teams who inherit the shortfall; consultants whose recommendation is judged at go-live.

## Impact If Fixed
A cheap specification step removes one avoidable reason automation projects miss their projected throughput, and removes it at the selection stage, before any capital is committed.
