# Pipeline Risk Early Warning System

**Niche:** [[niches/mortgage-brokers/purchase-residential-brokers/profile|Purchase-Focused Residential Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that predicts which loans in a broker's pipeline are at risk of falling through or missing their close deadline — flagging the specific risk factor (appraisal, employment, document delay, borrower responsiveness) so the loan officer can intervene before the problem becomes a crisis.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
A purchase-focused loan officer manages 25 active files. Three of them will have problems this week — but which three? An experienced loan officer develops an intuition for "which files feel wrong": the borrower who stopped responding to document requests, the appraisal that's taking longer than normal for that zip code, the employer verification that hasn't come back. Junior loan officers lack this pattern recognition and discover problems when they become crises — 5 days before closing, not 20 days before. Each failed close costs the brokerage $3,000-$5,000 in lost commission and damages the real estate agent referral relationship.

## Why Nobody Has Built This
Pipeline risk prediction requires integrating data from multiple points in the loan process: borrower responsiveness metrics (time between document requests and uploads), appraisal status and historical turn times by appraiser/geography, lender underwriting velocity (how fast this lender typically moves at each stage), title search progress, and employment/income verification status. This data lives in the LOS but isn't structured for predictive modeling. LOS vendors focus on workflow management, not decision intelligence — they build systems of record, not systems of insight.

## What to Build
A pipeline risk scoring model that ingests loan-level data from the LOS and computes a daily risk score for each file: probability of falling through and probability of missing close deadline. Risk factors are decomposed: 40% risk driven by borrower responsiveness (3+ days since last document request with no response), 30% driven by appraisal (7 days past expected return date for this appraiser), 15% driven by lender turn time anomaly, 15% driven by title/insurance delays. The loan officer's morning dashboard shows files ranked by risk with specific action items: "File #1847: borrower hasn't responded to bank statement request in 5 days — call today to avoid close date slip."

## Target Customer
Brokerage owners and senior loan officers managing 20+ active purchase files simultaneously who want proactive risk management instead of reactive crisis management.

## Impact If Built
Reduces pipeline fall-through rate by 20-30% through early risk detection and intervention. Prevents 3-5 close date misses per month at a busy brokerage, preserving $15K-$25K in commission revenue and protecting real estate agent referral relationships. Enables junior loan officers to manage pipelines at near-senior-level quality by surfacing the risk signals that experience normally provides.
