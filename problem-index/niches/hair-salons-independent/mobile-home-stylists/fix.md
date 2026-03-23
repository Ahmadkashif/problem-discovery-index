# Travel Time & Cost Tracking for Mobile Service Pricing

**Niche:** [[niches/hair-salons-independent/mobile-home-stylists/profile|Mobile & Home-Based Stylists]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Fix (Pain Point)
**One-liner:** Mobile stylists charge flat travel fees or absorb travel costs entirely — neither approach is profitable because they have no data on actual per-client travel cost and time.
**Tags:** #linear-regression #regression #tabular-ml #revenue-impact #worker-facing

## The Problem
A mobile stylist charges a $25 "travel fee" for all clients, regardless of distance. The client 10 minutes away is profitable; the client 45 minutes away costs $15 in gas, $35 in opportunity cost (the stylist could have served another client in that time), and 90 minutes of total round-trip driving. Without tracking actual travel time and cost per client, the stylist cannot set profitable travel fees, decide which clients are worth serving, or identify geographic clusters where they should focus marketing. Many mobile stylists undercharge for distant clients and subsidize them with nearby-client margins.

## Why It's Still Broken
Mobile stylists don't think of themselves as logistics businesses — they're artists who happen to travel. Tracking mileage, time, and fuel costs per client feels like administrative work that takes away from the creative work they love. No tool makes this tracking effortless: start your drive, auto-log mileage and time, attribute it to the next client, and show the profitability impact at the end of the week.

## What a Fix Looks Like
A passive travel tracking tool that: (1) auto-logs drive time and mileage between appointments using phone GPS, (2) attributes travel cost (IRS mileage rate + time at the stylist's hourly rate) to each client visit, (3) calculates per-client profitability including travel costs, (4) identifies unprofitable geographic zones ("clients in this area cost you $45/visit in travel but you only charge $25"), and (5) recommends travel fee adjustments by zone to ensure profitability. All passive — the stylist just opens the app when they start their day and closes it at the end.

## Who Feels the Pain
Mobile stylists earning less than their salon-based peers despite working the same hours, because 20-30% of their working time is consumed by uncompensated travel.

## Impact If Fixed
Enables data-driven travel fee pricing that increases per-client profitability by 15-25%, identifies geographic focus areas that maximize daily revenue, and provides mileage documentation for tax deduction ($5,000-10,000/year in deductible mileage for most mobile stylists).
