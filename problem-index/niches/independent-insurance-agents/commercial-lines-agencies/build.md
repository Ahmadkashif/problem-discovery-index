# Carrier Appetite Intelligence Engine for Commercial Submissions

**Niche:** [[niches/independent-insurance-agents/commercial-lines-agencies/profile|Commercial Lines Agencies]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product exists that ingests a commercial risk profile and returns a ranked list of carriers most likely to quote competitively based on real submission-outcome data.
**Tags:** #gradient-boosting #ranking #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Producers spend 30-60 minutes per commercial account mentally cross-referencing a risk profile against 15-30 carrier appetite guides — PDF documents that reflect marketing intent, not operational underwriting reality. The real signal (which carrier is actively writing this class in this geography this quarter) lives in the heads of experienced producers and in the pattern of recent submission outcomes that no system aggregates.

## Why Nobody Has Built This
The training data does not exist in any single system. Submission outcomes (quoted, declined, bound, premium level) are scattered across carrier portals, email inboxes, and AMS activity logs. Building a model requires a multi-agency data consortium or a partnership with an AMS vendor, and neither has materialized because agencies view their carrier relationships as competitive advantages and carriers view appetite data as proprietary.

## What to Build
A ranking model trained on anonymized submission-outcome data across agencies that takes a commercial risk profile (NAICS, revenue, employee count, loss history, geography, coverage lines) and outputs carrier recommendations ranked by P(quote) x P(competitive premium) x P(bind). The model supplements structured appetite guide data with real-time signals like carrier rate filings and loss ratio trends.

## Target Customer
Commercial lines producers at independent agencies with 10+ carrier appointments who handle 200+ submissions per year — agencies large enough to benefit from intelligence but small enough to lack dedicated analytics staff.

## Impact If Built
Reduces commercial lines placement time by 50-70%, allowing producers to handle 2x the new business volume. Junior producers perform at the level of 10-year veterans on carrier selection, compressing the talent development timeline from years to months.
