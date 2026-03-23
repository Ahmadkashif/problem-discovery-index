# BHPH Portfolio Risk Analytics Dashboard

**Niche:** [[niches/auto-dealers-independent/buy-here-pay-here/profile|Buy Here Pay Here (BHPH) Dealers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Business intelligence dashboards exist, but none are configured for the unique metrics of a BHPH portfolio — collection percentage, net yield, charge-off rate, and equity position per account.
**Tags:** #gradient-boosting #regression #tabular-ml #data-integration #revenue-impact

## The Problem
A BHPH dealer needs to know at any moment: What is my portfolio's net yield? What is my collection rate by deal vintage? Which cohort of deals is underperforming? What is my equity position (remaining vehicle value vs. remaining balance) on accounts approaching charge-off? These are standard finance company metrics, but BHPH dealers use DMS tools built for car sales, not portfolio management. The owner pieces together this data from payment reports, vehicle valuation lookups, and manual spreadsheets — often finding out a cohort is failing only after charge-offs mount.

## What Already Exists
Tableau, Power BI, and Looker provide general-purpose dashboards. DealerCenter and Wayne Reaves provide basic payment tracking and delinquency reports. Consumer finance platforms (LoanPro, Nortridge) offer full portfolio analytics but are designed for institutional lenders with 10,000+ accounts, not BHPH dealers with 200-500.

## The Customization Gap
The gap is a BHPH-specific analytics layer that sits on top of existing DMS data and computes the metrics that matter for an in-house lending operation: collection percentage by deal month (are Q3 deals performing worse than Q1?), static pool analysis (what percentage of each cohort has charged off by month 6, 12, 18?), vehicle equity tracking per account (is the car worth more or less than the remaining balance?), and optimal deal structure analysis (do 24-month deals with 20%+ down payment outperform 36-month deals with 10% down?). These require BHPH-specific financial models that generic BI tools don't include.

## Target Customer
BHPH dealer principals managing $2M+ in outstanding loan portfolio value who currently rely on monthly spreadsheet compilations to understand portfolio health.

## Impact If Solved
Enables data-driven deal structuring that reduces charge-off rates by 3-5 percentage points (worth $60K-100K annually on a $3M portfolio). Identifies underperforming cohorts 2-3 months earlier, enabling intervention before losses compound. Provides lender-ready reporting for dealers seeking warehouse lines of credit to scale.
