# Multi-State Early Intervention Billing Rules Engine

**Niche:** [[niches/physical-therapy/pediatric-pt/profile|Pediatric PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Fix (Pain Point)
**One-liner:** Pediatric PT practices stop losing revenue to state-specific billing errors — a rules engine encodes each state's Part C early intervention program requirements and automates compliant claim generation.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #compliance #revenue-impact #automation

## The Problem
Early intervention (Part C of IDEA) is the primary payer for pediatric PT serving children birth-to-3 with developmental delays. But each US state runs its own Part C program with unique rules: different billing codes (some use HCPCS, some use state-specific codes), different rate structures (fee-for-service vs. bundled rates vs. cost-based reimbursement), different provider qualification requirements (some states require specific certifications beyond PT licensure), different service authorization structures (some require physician referral, some don't), different documentation formats, and different claim submission portals. A pediatric PT practice operating in one state can't easily expand to an adjacent state because the billing rules are completely different. Practices near state borders that serve children from multiple states face the worst of it — billing for the same service under different rules depending on the child's home state.

## Why It's Still Broken
No PT EMR encodes state-level early intervention billing rules. The rules are published by each state's Part C lead agency (sometimes the health department, sometimes the education department, sometimes a developmental disabilities agency) in policy manuals that are updated annually. There's no centralized federal database of state Part C billing rules — each state's program is autonomous. Keeping up with 50 different programs' requirements is a research burden that individual practices can't sustain. EMR vendors won't invest in encoding these rules because the pediatric PT market is small and the rules change frequently, creating an ongoing maintenance cost that exceeds the addressable revenue.

## What a Fix Looks Like
A billing rules engine that encodes each state's Part C early intervention program requirements as structured data: accepted billing codes, rate schedules, provider qualification requirements, authorization workflows, documentation format specifications, and claim submission specifications. When a pediatric PT practice documents a session, the engine determines the child's state of residence, applies that state's billing rules, generates the correct claim format with appropriate codes and rates, and flags any compliance issues (missing documentation elements, provider qualification gaps, authorization expiration). For practices operating in multiple states, the engine handles the state-specific variations automatically. A maintenance layer tracks state policy updates and flags when rules change, with a changelog showing what's different and what existing claims or documentation need adjustment.

## Who Feels the Pain
Billing specialists and practice managers at pediatric PT practices who spend hours researching state-specific billing requirements, manually adapting claims to each state's format, and correcting claim denials caused by rule misapplication. Practice owners considering geographic expansion who are deterred by the complexity of learning a new state's early intervention billing system.

## Impact If Fixed
Reduces claim denial rates for early intervention services from 15-25% to under 5% by ensuring state-specific compliance at the point of claim generation. Saves billing staff 10-15 hours per week on manual rule research and claim formatting. Enables geographic expansion by removing the billing knowledge barrier — a practice can begin serving children in a new state without months of learning that state's Part C program rules.
