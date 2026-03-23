# Specialty Product Allocation When Supply Is Limited

**Niche:** [[niches/restaurant-suppliers/fine-dining-specialty-purveyors/profile|Fine Dining Specialty Purveyors]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** When a limited-supply specialty product is available (200 lbs of A5 Wagyu, 50 lbs of white truffles), the purveyor must allocate across 10-15 competing chef requests — and the allocation is done by the owner's gut feel rather than any systematic framework, creating relationship strain when top accounts feel under-served.
**Tags:** #ranking #tabular-ml #revenue-impact #worker-facing

## The Problem
A specialty purveyor receives 50 lbs of white truffles — their entire allocation from an Italian importer this month. Twelve chefs want truffles. Total requested volume: 120 lbs. The purveyor must allocate 50 lbs across 12 chefs, knowing that: Chef A is the highest-revenue account but buys truffles only for tasting menu (2 lbs), Chef B runs a truffle-focused prix fixe and needs 15 lbs to execute, Chef C is a new account the purveyor is trying to grow, and Chef D was shorted on the last allocation and is upset. The owner makes this allocation decision intuitively, considering account value, relationship history, promotional commitments, fairness, and strategic growth — but the decision is never documented, and chefs who feel under-allocated may start sourcing from a competing purveyor without explanation.

## Why It's Still Broken
Product allocation is a judgment call that blends commercial logic (prioritize highest-revenue accounts) with relationship management (rotate priority to prevent any chef from feeling consistently deprioritized). No tool captures the allocation history or provides the data needed to make fair, defensible decisions. The owner makes allocations from memory of past decisions and current relationship temperature — an inherently inconsistent process. When the owner is unavailable, the office cannot make allocation decisions because the context lives in one person's head.

## What a Fix Looks Like
An allocation management system that: (1) ranks chef accounts by allocation priority score — a weighted composite of revenue, loyalty (years as customer), fairness (time since last allocation), growth potential, and commitment level (pre-committed vs. opportunistic), (2) suggests an allocation split when supply is limited ("allocate 15 lbs to Chef B (core program), 10 lbs each to Chefs A and D (top accounts, D was shorted last time), 5 lbs to Chef C (growth), 10 lbs held for same-day requests"), (3) records every allocation decision with rationale for future reference, and (4) tracks allocation fairness over time by account, preventing the common pattern where the squeakiest-wheel chef gets disproportionate allocations.

## Who Feels the Pain
Owners who agonize over allocation decisions 3-5 times per week, knowing that every allocation creates a winner and a loser. Chefs who feel they are not getting fair access to limited products and begin sourcing from competitors. Sales reps who must explain allocation decisions to unhappy chefs without clear documentation of why the decision was made.

## Impact If Fixed
Chef satisfaction with allocation fairness improves — documented, consistent allocation reduces the perception of favoritism. Account retention improves 5-10% as chefs who previously felt under-served see equitable treatment. Allocation decision time reduced from 20-30 minutes of deliberation to 5 minutes of reviewing system recommendations. Competitive defection from allocation dissatisfaction reduced by 30-50%, retaining $50K-$200K in annual revenue from accounts that would have partially or fully switched purveyors.
