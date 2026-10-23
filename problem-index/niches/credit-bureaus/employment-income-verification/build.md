# A Freshness Score on Every Employment Record

**Niche:** [[niches/credit-bureaus/employment-income-verification/profile|Employment & Income Verification]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A verification database answers "employed" from the last payroll file it received, and nothing tells the buyer how likely that answer is to be out of date.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #feature-engineering #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to hold a current, employer-sourced record on the applicant at the moment a lender, landlord or benefits agency asks, and whoever answers the most applicants instantly without a paystub upload takes the account.

## The Problem
Employers and payroll processors contribute records on their own cadence — every pay cycle for some, monthly or less for others — and a termination may appear weeks after it happened. A verification returned as "active, $X a year" can describe a job the applicant has already left, which a lender discovers at the pre-closing re-verification or never. The same staleness makes the record a disputed consumer report when it is wrong.

## Why Nobody Has Built This
Coverage is the headline metric, so freshness is reported as an aggregate "as of" date rather than per record. Measuring staleness needs outcomes — later terminations, re-verifications, disputes — that sit in different systems.

## What to Build
A per-record probability that the employment status or pay is out of date, from the contributor's reporting cadence and lag, industry turnover, time since last pay event, and the history of corrections and disputes on that contributor; survival models for time-to-separation by employer and role. Returned with every verification so the buyer can decide when to re-verify or ask for a document.

## Target Customer
Product and data leaders at verification bureaus; mortgage and auto lenders' verification operations.

## Impact If Built
Re-verifications aimed where they matter, fewer loans closed on a job that ended, and fewer disputed reports — a measurable quality claim in a coverage contest.
