# Rural DME Route Optimization with Equipment-Specific Constraints

**Niche:** [[niches/medical-supply-retail/rural-home-medical-equipment/profile|Rural Home Medical Equipment Providers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No route optimization tool accounts for DME-specific delivery constraints — equipment setup time, two-person delivery requirements, home accessibility, and patient training needs — that make rural HME delivery fundamentally different from package delivery.
**Tags:** #reinforcement-learning #regression #tabular-ml #automation #worker-facing

## The Problem
A rural HME provider scheduling 8-12 deliveries across a 5-county territory must consider: drive time between stops (often 30-60 minutes), equipment type (a hospital bed delivery takes 45-60 minutes for setup and training; an oxygen concentrator takes 15-20 minutes), two-person requirements (bariatric equipment deliveries need two technicians), patient availability windows (many elderly patients have morning doctor appointments or afternoon naps), and home accessibility (second-floor apartments without elevators, narrow doorways, unpaved driveways). Google Maps can sequence the stops for minimum drive time, but it doesn't account for time-at-stop variability or patient constraints. The driver currently receives a printed list and plans the route from experience.

## Why Nobody Has Built This
General route optimization tools (OptimoRoute, Route4Me, Routific) handle multi-stop delivery with time windows but don't model variable service time per stop based on equipment type, crew requirements, or accessibility factors. Building a DME-specific optimizer requires: a service time model per equipment category (hospital bed = 50 min, walker = 10 min, wheelchair = 30 min), crew constraint logic (some stops need 2 people, constraining which stops can be grouped), and patient-side constraints (availability windows, accessibility notes). The rural HME market is too small to attract route optimization SaaS companies that target logistics and field service.

## What to Build
A delivery scheduling and route optimization tool designed for rural HME: each delivery is tagged with equipment type (determining service time), crew requirement (1 vs. 2 person), patient availability window, and accessibility notes. The optimizer produces a daily route plan that minimizes total time (drive + service) while respecting all constraints. It also groups deliveries by geographic area into "delivery days" — scheduling all patients in the northern counties for Tuesday and southern counties for Thursday — to minimize deadhead driving. The driver receives the optimized route on a mobile app with turn-by-turn navigation and patient notes at each stop.

## Target Customer
Rural HME owners scheduling 30+ deliveries per week across a multi-county territory, currently building routes manually based on driver experience and a paper map.

## Impact If Built
Reduces total daily drive time by 20-30% through optimized stop sequencing and geographic day-assignment. On a 5-day delivery schedule averaging 200 miles/day, this saves 40-60 miles/day in driving = $25K-40K/year in fuel and vehicle costs. Adds 1-2 additional deliveries per day by eliminating wasted transit time, increasing revenue capacity by 15-25% without adding a driver.
