# ITIN Borrower Lender Matching & Eligibility Engine

**Niche:** [[niches/mortgage-brokers/hispanic-immigrant-borrowers/profile|Hispanic & Immigrant Borrower Specialists]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool maps an ITIN borrower's profile — residency status, income documentation type, alternative credit history, property type — to the handful of wholesale lenders who actually originate ITIN loans, each with radically different guidelines.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Only 5-10 wholesale lenders nationally offer ITIN mortgage programs, and their guidelines differ dramatically: one requires 2 years of US tax filing, another accepts 1 year with 6 months bank statements, a third requires a foreign credit report from a specific bureau. Maximum LTV ranges from 70% to 90% depending on lender, property type, and documentation strength. Brokers who serve ITIN borrowers carry this matrix in their heads — a senior broker can look at a borrower's profile and know which 2-3 lenders are viable within minutes, but this knowledge is accumulated over years and is not written down anywhere accessible to junior staff.

## Why Nobody Has Built This
The ITIN lending market is small (estimated $10-20B annually), making it commercially unattractive for fintech companies. ITIN lender guidelines change frequently and are often communicated verbally or via PDF rate sheets rather than structured data. The borrower profiles are non-standard — US credit scoring models don't apply, income verification follows different paths, and property eligibility varies — making it impossible to repurpose conventional lender matching tools.

## What to Build
An eligibility engine that takes an ITIN borrower's profile (years of US tax filing, income documentation available, alternative credit sources, property type, target LTV, state) and outputs a ranked list of ITIN lenders with eligibility confirmation, rate estimates, and documentation requirements for each. The system maintains a continuously updated matrix of ITIN lender guidelines scraped from rate sheets and program bulletins.

## Target Customer
Bilingual brokerages specializing in Hispanic/immigrant homebuyers, typically processing 5-15 ITIN loans per month. These are often community-embedded shops where the brokerage owner's personal knowledge of ITIN lender programs is the entire competitive advantage — and a single point of failure.

## Impact If Built
Democratizes ITIN lending expertise from a handful of veteran brokers to any licensed loan officer, potentially doubling the number of brokerages that can effectively serve ITIN borrowers. Reduces ITIN loan denial rates (currently estimated at 30-40%) by ensuring submissions go to the right lender from the start. Shortens ITIN file processing from 45-60 days to 30-40 days by eliminating lender mismatch re-submissions.
