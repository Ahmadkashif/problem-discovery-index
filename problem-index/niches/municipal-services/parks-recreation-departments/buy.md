# Recreation Registration with Dynamic Pricing

**Niche:** [[niches/municipal-services/parks-recreation-departments/profile|Parks & Recreation Departments]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ACTIVE Network and CivicRec handle registration but lack dynamic pricing, waitlist optimization, and scholarship allocation logic specific to public recreation.
**Tags:** #linear-regression #regression #tabular-ml #revenue-impact #automation

## The Problem
Parks departments fill programs on a first-come-first-served basis at flat rates set once per year. Popular programs sell out in minutes, creating equity concerns (only parents who can register at 8 AM on a Tuesday get spots). Unpopular time slots run at 30% capacity, losing money. Scholarship slots are allocated manually and inconsistently, with no data on whether subsidized participants convert to paying customers in future seasons.

## What Already Exists
ACTIVE Network, CivicRec, RecDesk, and PerfectMind all handle online registration, payment processing, and basic waitlisting. These platforms model pricing as a static field — an admin enters a fee and it stays fixed until someone changes it. None support time-of-day pricing, demand-based pricing tiers, or automated scholarship allocation based on income verification and program availability.

## The Customization Gap
Public recreation has unique pricing constraints: council-approved fee schedules, resident/non-resident differentials, income-based scholarship tiers, and political sensitivity around "charging more" for popular programs. A vertical pricing layer needs to work within these constraints — suggesting off-peak discounts rather than surge pricing, optimizing scholarship distribution to maximize participation across demographics, and modeling the revenue impact of fee changes before they go to council for approval. Integration must be bidirectional with existing registration platforms, not a rip-and-replace.

## Target Customer
Recreation program managers and finance officers at departments generating $500K–$10M in annual program revenue.

## Impact If Solved
Dynamic off-peak pricing increases average facility utilization from 55% to 75%, generating $200K–$800K in additional annual revenue. Optimized scholarship allocation increases low-income participation 25% without increasing the subsidy budget.
