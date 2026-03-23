# Per-Building Profitability Blind Spot

**Niche:** [[niches/cleaning-companies/commercial-janitorial/profile|Commercial Janitorial Contracts]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Most janitorial operators don't know which buildings make money and which lose money until the annual P&L.
**Tags:** #data-integration #tabular-ml #revenue-impact

## The Problem
Labor hours, supply costs, and equipment wear are tracked in separate systems (or not tracked at all) from billing. A janitorial company with 25 buildings might know its overall margin is 12%, but can't tell you that Building A runs at 22% margin while Building B runs at -3%. Without per-building P&L, operators can't renegotiate losing contracts or double down on profitable ones.

## Why It's Still Broken
Time tracking captures clock-in/clock-out but not which building the hours went to (crews often clean multiple buildings per shift). Supply costs are purchased in bulk and allocated by guesswork. Equipment depreciation is never assigned to specific contracts. The data exists in fragments across payroll, purchasing, and scheduling systems with no unifying layer.

## What a Fix Looks Like
A per-building cost allocation engine that pulls labor hours from time-tracking (tagged by building), supply usage from inventory, and contract revenue from billing — then produces a monthly per-building P&L dashboard. The fix requires enforcing building-level time tagging at the crew level and automating supply allocation by consumption patterns.

## Who Feels the Pain
Company owners carrying 3-5 unprofitable buildings in a 20-building portfolio, unknowingly subsidizing losses with profitable contracts.

## Impact If Fixed
Identifying and renegotiating or exiting the bottom 15% of contracts can improve company-wide margins by 4-8 percentage points, often the difference between surviving and thriving.
