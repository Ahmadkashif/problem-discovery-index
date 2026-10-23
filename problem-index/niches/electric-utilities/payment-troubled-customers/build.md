# Arrangement Matching Before the Notice Goes Out

**Niche:** [[niches/electric-utilities/payment-troubled-customers/profile|Payment-Troubled Residential Customers]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Utilities offer the same arrangement terms to every customer in arrears, and many arrangements fail within months.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep a payment-troubled household connected and paying, and whoever matches each household to the right arrangement or assistance programme before its disconnection notice takes the account.

## The Problem
A household falls behind. The collections system sends notices on a fixed schedule, and a representative offers the standard deferred payment arrangement if the customer calls. Many arrangements break (estimate), the household returns to the disconnection queue with a larger balance, and assistance programmes the household qualified for were never offered.

## Why Nobody Has Built This
Collections strategy has been designed for compliance with notice rules, not for outcomes. Arrangement performance by household type is rarely analysed, and assistance eligibility data sits with outside agencies.

## What to Build
A model of arrangement success, as time to default, given payment history, usage pattern from AMI, seasonality, balance and arrangement terms. Paired with an eligibility engine for the state's programmes and protections, it recommends the arrangement and assistance mix most likely to keep each household current. It triggers outreach before the disconnection notice and measures results against randomised holdouts where commissions allow.

## Target Customer
Credit and collections directors at utilities under commission scrutiny for disconnections and arrears.

## Impact If Built
~10%–20% fewer broken arrangements and disconnections among households scored (estimate), more eligible households enrolled, and lower bad-debt expense that otherwise flows back into rates.
