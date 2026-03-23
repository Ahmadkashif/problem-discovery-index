# Sales Training Impact Attribution Engine

**Niche:** [[niches/corporate-training/sales-enablement-training/profile|Sales Enablement & Revenue Training]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform today causally attributes changes in sales rep performance (quota attainment, win rate, deal velocity) to specific training programs — enablement leaders present completion rates instead of revenue impact.
**Tags:** #gradient-boosting #causal-inference #tabular-ml #revenue-impact #data-integration

## The Problem
A VP of Sales Enablement launches a new objection handling course. Three months later, average close rates are up 6%. The enablement leader wants to claim credit, but the CRO points out that a new product launched in the same quarter, two underperforming reps were replaced, and territory assignments were rebalanced. Without isolating the training effect from these confounders, the enablement budget remains indefensible — and the enablement leader cannot identify which of their 15 active programs are actually driving revenue.

## Why Nobody Has Built This
The causal inference challenge requires joining data across LMS (training completions), CRM (pipeline and revenue outcomes), HRIS (tenure, role changes, manager assignments), and business context (product launches, territory changes, market conditions) — systems owned by different departments with different data stewards. The statistical methodology (difference-in-differences, propensity score matching, instrumental variables) is well-established in econometrics but has not been productized for the sales enablement buyer.

## What to Build
A causal analytics engine that ingests training completion events from the LMS, rep-level CRM outcomes (quota attainment, win rate, deal velocity, average deal size), and confounders from HRIS and business context. Using propensity score matching and double machine learning, it estimates the causal effect of each training program on specific revenue KPIs, with confidence intervals. The output is a dashboard showing ROI per program, recommended resource reallocation, and alerts when a new program shows early positive or negative signals.

## Target Customer
VP of Sales Enablement at companies with 50-500 reps, $5M+ annual training budgets, and mature Salesforce/HubSpot CRM data — organizations that spend heavily on enablement but cannot prove its value.

## Impact If Built
Enablement leaders gain defensible ROI metrics for every program, enabling reallocation from low-impact to high-impact training — estimated to improve aggregate rep performance by 8-15% through portfolio optimization, translating to millions in additional revenue for mid-market sales organizations.
