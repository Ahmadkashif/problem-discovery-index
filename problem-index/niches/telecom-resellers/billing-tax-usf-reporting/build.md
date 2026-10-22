# The 499-Q Projection That Trues Up Without Surprises

**Niche:** [[niches/telecom-resellers/billing-tax-usf-reporting/profile|Telecom Billing, Tax & USF Revenue Reporting]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** USAC bills a provider each month on the revenue it projected on its last Form 499-Q, and small providers guess the projection, then absorb a true-up when the annual 499-A tells the real story.
**Tags:** #time-series-forecasting #exponential-smoothing #confidence-intervals #feature-engineering #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to classify every billed dollar the way USAC's auditors and state tax administrators will read it (interstate or intrastate, end-user or reseller, taxable or not) and reuse that one classification across the invoice, the tax return and Form 499, and whoever does it once and consistently takes the account.

## The Problem
Form 499-Q reports last quarter's revenue and projects the next quarter's. USAC invoices contributions monthly from the projection at the current factor, and the annual 499-A trues everything up. A provider that under-projects faces a true-up bill after the fact. One that over-projects ties up cash. Recovery fees charged to customers are set from the same guesses, so they drift from what is actually owed. With the factor at a proposed 42.0%, a projection error of a few percent of assessable revenue is real money for a small provider.

## Why Nobody Has Built This
Billing platforms report what was billed, not what will be, and tax engines don't forecast. Consultants preparing 499s for many clients copy last quarter forward because that is what the time allows. The forecast also has to be made at the 499 line level, by assessable category, rather than as total revenue.

## What to Build
A line-level revenue forecast built from billing history, booked-but-not-billed orders, churn and promotions, mapped to 499 categories with intervals. It sets the 499-Q projection, estimates the year-end true-up as the year runs, and recommends the customer recovery rate so collections match obligations each quarter under the published factor. Each filing carries a variance explanation for the officer who certifies it.

## Target Customer
Controllers and regulatory managers at small and mid-sized resellers, and the consultants who file for them.

## Impact If Built
True-up surprises shrink, cash is not tied up in over-projected contributions, and recovery fees stay defensible against both customers and auditors.
