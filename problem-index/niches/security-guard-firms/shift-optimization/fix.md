# Overtime Cost Spiral

**Niche:** [[niches/security-guard-firms/shift-optimization/profile|Guard Scheduling & Shift Optimization]]
**Industry:** [[industries/security-guard-firms|Security Guard Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Security companies bill clients at straight-time rates but pay guards overtime to fill callouts and coverage gaps — the 50% overtime premium comes directly from margin.
**Tags:** #automation #revenue-impact #data-integration

## The Problem
Security contracts are priced at a fixed bill rate (e.g., $25/hour). The company pays guards a base wage (e.g., $16/hour) with the spread covering overhead and margin. When callouts force overtime coverage, the guard earns $24/hour (time-and-a-half) while the company still bills $25/hour — margin collapses from $9/hour to $1/hour. On a busy week, a company might have 200 overtime hours at barely-breakeven rates. Over a year, unmanaged overtime can reduce company-wide margins from 10% to 3%.

## Why It's Still Broken
Overtime accumulates through multiple small decisions: a callout filled by a guard already at 38 hours, a site that "needs" a specific guard who's already worked 5 days, a last-minute event add-on covered by the nearest available guard regardless of hours. Each decision makes sense individually, but no one tracks the cumulative impact until payroll runs. By then, the overtime is spent. There's no real-time visibility into fleet-wide overtime exposure or per-site overtime attribution.

## What a Fix Looks Like
A real-time overtime dashboard showing: current week hours per guard (with overtime threshold proximity), projected overtime if current assignments hold, overtime cost by site (which clients are causing the most overtime), and alternative staffing options that would reduce overtime (which straight-time guard could cover the shift instead). The system should flag every scheduling decision that would push a guard into overtime and suggest a lower-cost alternative. Weekly reports should show overtime cost by root cause: callout backfill, understaffing, client request for specific guard, or scheduling error.

## Who Feels the Pain
Security company owners who discover at month-end that their 10% target margin is actually 4% because overtime consumed $30,000-$50,000 in expected profit.

## Impact If Fixed
Making overtime visible in real time and attributable by cause typically reduces overtime hours by 25-40%. On a company spending $400,000/year in overtime, that's $100,000-$160,000 in recovered margin.
