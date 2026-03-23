# Lightweight Production Management for Short-Run CMs

**Niche:** [[niches/contract-manufacturing/small-run-consumer-goods/profile|Small-Run Consumer Goods CMs]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No production management system is designed for the specific workflow of a CM running 5-8 short production batches per day — where job setup takes 10 minutes but traditional MES job creation takes 30 minutes, and the overhead of the system exceeds the time saved.
**Tags:** #automation #workflow-orchestration #quick-win #revenue-impact

## The Problem
Small-run consumer goods CMs change products 3-8 times per day. Each changeover requires cleaning, material staging, and equipment adjustment. Traditional MES platforms (Rockwell FactoryTalk, Siemens Opcenter) are designed for long-run, high-volume production where setup overhead is amortized across thousands of units. Creating a production job in these systems — entering BOM, routing, quality specifications, and scheduling parameters — takes 15-30 minutes per job. For a CM running 6 jobs per day, this is 90-180 minutes of data entry daily — an unacceptable overhead on a shop floor where the production team is 5-10 people total.

## Why Nobody Has Built This
MES vendors target large manufacturing operations with $10M+ annual revenue and IT departments that can manage complex implementations. The small-run CM market is fragmented across product types (cosmetics, supplements, household products, small electronics) and lacks a unifying industry structure that attracts software investment. The price sensitivity of these operators ($50-200/month maximum SaaS spend) makes the market unattractive to enterprise software vendors.

## What to Build
A mobile-first production management app where creating a job takes under 2 minutes — scan a QR code on the job traveler, confirm BOM from a saved template, and start the timer. The system tracks job status (setup, running, QC, complete), actual labor time, and material consumption against the estimate. Daily production reports compare actual vs. quoted costs across all jobs, highlighting which products and customers are profitable and which are margin-negative. No installation, no IT requirements, no multi-week implementation — self-service onboarding in under an hour.

## Target Customer
Owner-operators and production managers at consumer goods CMs with 5-30 employees and $1-10M in annual revenue. Approximately 10,000-15,000 companies in the US.

## Impact If Built
Provides production visibility that these shops have never had — actual job cost vs. quoted cost for every production run. Identifies margin-negative products (estimated at 15-25% of a typical small CM's product portfolio) that are losing money without the owner's knowledge. Reduces scheduling errors and missed shipments by making job status visible to the entire team in real time.
