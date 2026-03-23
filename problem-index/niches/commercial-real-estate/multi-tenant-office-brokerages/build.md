# Submarket Tenant Migration Intelligence Platform

**Niche:** [[niches/commercial-real-estate/multi-tenant-office-brokerages/profile|Multi-Tenant Office Brokerages]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tracks where tenants move when they leave a building — the migration pattern data that experienced office brokers carry in their heads but junior brokers lack entirely.
**Tags:** #gradient-boosting #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
When a 10,000 sq ft tenant vacates Building A, the listing broker needs to know: where do tenants of this size and industry typically relocate within the submarket? Which competing buildings are absorbing tenants, and which are losing them? An experienced office broker tracks these migration patterns mentally over years of transactions, but this knowledge is never systematized. Junior brokers cold-call every company in the market without understanding which buildings are gaining vs. losing tenants, wasting months of prospecting effort on buildings with strong retention.

## Why Nobody Has Built This
Tenant migration data requires connecting lease origination records, business address changes, and deed/assignment filings across multiple properties over time — a data assembly problem that no single source covers. CoStar tracks current occupancy but doesn't model migration flows between buildings. Building this requires assembling a longitudinal tenant location dataset from fragmented public records, business filings, and USPS address change data — a data engineering challenge that CRE tech companies have avoided because the ROI accrues to boutique firms, not institutional landlords who already track their own portfolios.

## What to Build
A migration intelligence layer that tracks tenant movements between office buildings within a submarket over 3-5 years. Inputs: state business registration address changes, USPS NCOA data, commercial lease filings, CoStar occupancy snapshots. Output: migration flow maps showing which buildings are net gainers vs. losers of tenants by size and industry, feeding directly into tenant prospecting and competitive positioning for leasing pitches.

## Target Customer
Leasing directors at boutique office brokerages managing landlord leasing assignments in competitive urban submarkets — approximately 3,000-5,000 firms nationally. Average contract value: $300-$600/month per brokerage.

## Impact If Built
Brokers targeting competing buildings that are actively losing tenants convert prospects at 2-3x the rate of untargeted cold outreach. A single accelerated 5,000 sq ft lease from migration intelligence generates $15,000-$25,000 in commission — paying for years of subscription.
