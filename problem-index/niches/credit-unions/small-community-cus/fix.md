# Veteran Loan Officer Knowledge Loss at Retirement

**Niche:** [[niches/credit-unions/small-community-cus/profile|Small Community CUs (<$500M Assets)]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** When a 20-year loan officer retires from a small CU, the institution loses the accumulated judgment from thousands of lending decisions — and discovers the loss only 12-18 months later when default rates rise or loan volume drops.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A veteran loan officer at a $200M community CU has processed 5,000+ loan applications over 20 years. They know which members are reliable despite mediocre credit scores, which local employers are stable, and which borrower behaviors predict trouble. When they retire, their replacement starts with credit scores and credit policy — the same tools available to any fintech lender, stripping the CU of its relationship lending advantage. The CU's loan quality deteriorates: default rates on unsecured personal loans increase 15-30% within 18 months of a veteran departure, and loan volume drops 10-15% as the new officer declines applications the veteran would have approved with conditions.

## Why It's Still Broken
Knowledge transfer between outgoing and incoming loan officers is informal — shadowing for 2-4 weeks, verbal guidance, and a few annotated files. The veteran's decision logic is tacit: they can't write down the 200 behavioral signals they process when reviewing an application because they don't consciously enumerate them. The CU has no mechanism to extract this knowledge systematically. Core banking platforms store transaction history but don't surface behavioral patterns. LOS platforms record the decision (approve/deny/counter) but not the reasoning.

## What a Fix Looks Like
A structured knowledge capture process initiated 12-18 months before a veteran loan officer's planned retirement: (1) behavioral feature extraction from core banking data to identify the member-level signals the veteran weights in decisions; (2) decision journaling — the veteran annotates a sample of loan decisions with their reasoning in a structured format; (3) model training on the veteran's historical decisions enriched with behavioral features to create a CU-specific risk scoring model; (4) parallel processing where the incoming officer handles applications with the model's risk signal alongside them, calibrating the model against the veteran's live judgment during the overlap period.

## Who Feels the Pain
CEOs and lending managers at small CUs facing imminent retirement of experienced lending staff, and junior loan officers who inherit portfolios without the contextual knowledge needed to manage existing member relationships.

## Impact If Fixed
Preserves 15-20 years of accumulated lending judgment in a transferable format. Reduces the post-retirement default rate increase from 15-30% to 5-10% by giving the successor data-driven risk signals. Prevents the 10-15% loan volume decline that typically follows a veteran departure by maintaining approval rates on relationship-dependent applications.
