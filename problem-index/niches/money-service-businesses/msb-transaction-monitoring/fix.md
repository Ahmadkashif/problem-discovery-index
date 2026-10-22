# Targeting-Order CTRs Filed by Hand

**Niche:** [[niches/money-service-businesses/msb-transaction-monitoring/profile|MSB Transaction Monitoring & SAR Operations]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** When FinCEN dropped the CTR threshold to $200 for MSBs in 30 border ZIP codes, small transmitters filed the extra reports by keying them one at a time.
**Tags:** #large-language-models #feature-engineering #compliance #automation #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to resolve each sender across agents, brands and name spellings into one person before a structuring alert is worked, and whoever resolves senders most accurately takes the account.

## The Problem
FinCEN's March 2025 Southwest Border Geographic Targeting Order required MSBs in 30 ZIP codes in California and Texas to file CTRs on cash transactions of $200 or more; a later order raised the floor to $1,000, a March 2026 order added New Mexico, and the Ninth Circuit upheld an injunction against the original. Each change of scope, threshold and court status had to be applied to filings within days.

## Why It's Still Broken
CTR filing logic is hard-coded around $10,000 and the transmitter's whole network. Location-specific, time-limited thresholds are handled by staff exporting transactions and keying reports.

## What a Fix Looks Like
Parameterised reporting rules by location, date range, threshold and injunction status; batch CTR generation from transaction data with ID completeness checks; and a log showing which order governed each filing.

## Who Feels the Pain
Compliance staff at border-region MSBs, their agents asked for extra ID on small transactions, and senders.

## Impact If Fixed
Geographic orders become a configuration change rather than a staffing crisis, and the filing record survives litigation-driven changes.
