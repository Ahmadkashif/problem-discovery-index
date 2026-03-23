# Pricing Confidence for New Caterers

**Niche:** [[niches/catering-companies/small-social-event-caterers/profile|Small Social Event Caterers]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** New small caterers chronically underprice because they do not know the true cost of an event — counting only ingredient cost and forgetting labor, transport, disposables, and overhead.
**Tags:** #linear-regression #regression #tabular-ml #revenue-impact #quick-win

## The Problem
A new caterer prices a 50-person party at $25/head because that is what the ingredients cost. They forget to account for 8 hours of prep labor, 4 hours of service, $150 in disposables, $80 in gas and vehicle wear, $200 in commissary kitchen rental, and $50 in insurance allocation. The true cost is $38/head. They just worked 12 hours for free. This happens on every event for the first 1-2 years until the caterer either learns to price correctly, burns out, or quits.

## Why It's Still Broken
There is no industry-standard cost framework for small social catering. Enterprise caterers use cost-plus pricing with established overhead allocations, but micro-caterers have never learned this methodology. Online resources give conflicting advice ("charge 3x ingredient cost" vs. "charge $40-$60/head"), and none account for the caterer's specific cost structure. The caterer has no tool that says "your all-in cost for this event is $38/head — if you charge $25, you are losing $650."

## What a Fix Looks Like
A pricing calculator that walks the caterer through all cost components for a specific event: ingredients (with recipe costing), prep labor (hours x hourly rate the caterer should be paying themselves), service labor, transport, disposables, commissary rental, insurance allocation, and a margin target. The output is a minimum viable price per head and a recommended price with target margin. Over time, post-event actuals train the system to improve estimates based on the caterer's specific cost patterns.

## Who Feels the Pain
The new caterer who works 12-hour days and cannot understand why they are not making money — and who will quit within 18 months if they do not learn to price correctly.

## Impact If Fixed
Correcting pricing from cost-only to full-cost-plus-margin transforms a $50K revenue/break-even operation into a $50K revenue/$15K profit operation — the difference between a hobby and a sustainable business.
