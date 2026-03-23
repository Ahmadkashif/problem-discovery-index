# Relationship Knowledge Capture for Lending

**Niche:** [[niches/credit-unions/small-community-cus/profile|Small Community CUs (<$500M Assets)]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured system for capturing the behavioral signals and community context that veteran loan officers use in lending decisions — deposit pattern changes, employer stability knowledge, member life event awareness — so this relationship intelligence persists beyond any individual employee.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A veteran loan officer at a small community CU knows that the local factory's overtime has been cut (deposit amounts dropping for 30 members), that a specific borrower just went through a divorce (spending pattern shift), and that the new restaurant owner on Main Street has strong catering side revenue that doesn't show on tax returns yet. This contextual intelligence drives lending decisions that outperform credit score alone — but it exists only in the loan officer's head, is never documented, and disappears when they retire. No system captures the behavioral signals (deposit trends, spending shifts, employer patterns) or community context (local employer health, seasonal economic cycles) that make relationship lending work.

## Why Nobody Has Built This
The signals are informal and multi-modal — some come from transaction data analysis (deposit pattern changes), some from branch conversations (member mentions a job change), some from community awareness (a major employer announces layoffs). No CU technology vendor has attempted to structure these into a capturable format because core banking platforms are designed for transaction processing, not relationship intelligence. The data science capability required to build behavioral feature extraction from core banking data doesn't exist at small CUs — they have no data engineers or ML staff.

## What to Build
A relationship intelligence layer that sits on top of the core banking platform and continuously extracts behavioral signals from member transaction data: deposit amount and frequency trends, spending category shifts, overdraft patterns, external transfer changes, and product engagement trajectories. Combine with a lightweight structured note system where loan officers log contextual observations during member interactions (tagged by category: employment change, life event, community insight). The system surfaces relevant signals during loan review: "Member's deposit stability score has improved 15% over 6 months; last note: started new job at County Hospital in March."

## Target Customer
CEOs and VP of Lending at community CUs with $100M-$500M in assets who rely on 2-5 veteran loan officers for relationship-based lending decisions and face retirement-driven knowledge loss within 3-5 years.

## Impact If Built
Preserves relationship lending intelligence through staff transitions — a capability worth $200K-$500K annually in avoided loan losses per institution. Enables junior loan officers to access the same member behavioral context that veterans carry in their heads, reducing time-to-effectiveness from 5+ years to 6-12 months.
