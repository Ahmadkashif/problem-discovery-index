# Multi-Client ERA Payment Reconciliation

**Industry:** [[medical-billing|Medical Billing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Payment posting from electronic remittance advices is automated in theory, but in practice every ERA requires manual review because contractual adjustments, secondary billing triggers, and patient responsibility calculations don't reconcile cleanly.
**Tags:** #logistic-regression #feature-engineering #descriptive-statistics #evaluation-metrics #automation #revenue-impact #data-integration

## The Problem
When payers send Electronic Remittance Advices (ERAs), the billing system auto-posts payments against claims. But auto-posting frequently fails or produces incorrect results: contractual adjustments don't match the practice's fee schedule contracts, secondary insurance triggers aren't fired correctly, patient responsibility amounts don't account for already-collected copays, and bundled payments need to be allocated across component claims. For a billing company managing 20+ clients with different fee schedules and payer contracts, the reconciliation requires client-specific knowledge that generic auto-posting can't handle.

## What Already Exists
Clearinghouses deliver ERAs in standard 835 format. Practice management systems auto-post payments from 835 files. Revenue cycle dashboards (Waystar, Availity) provide payment analytics.

## The Customisation Gap
Auto-posting needs to be informed by each client's specific contracted rates with each payer (to validate contractual adjustments), the practice's patient collection policies (to correctly calculate and assign patient responsibility), and cross-client reporting requirements (the billing company needs to report payment metrics per client). The system also needs to flag underpayments — where the payer paid less than the contracted rate — which requires maintaining and comparing against each client's payer contracts.

## Impact If Solved
Reduces manual payment posting review from 15-20 minutes per ERA batch to 2-3 minutes (exception review only). Catches underpayments estimated at 1-3% of total collections that currently go unnoticed. Saves a mid-size billing company 15-25 hours per week in payment posting labor.
