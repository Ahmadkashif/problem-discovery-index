# Bank-Feed-to-Schedule-C Expense Classifier

**Niche:** [[niches/tax-prep-firms/schedule-c-sole-proprietors/profile|Schedule C / Sole Proprietor Specialists]]
**Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product ingests a sole proprietor's bank and credit card transactions and automatically classifies them into Schedule C expense categories — preparers manually categorize hundreds of transactions per client.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #automation #revenue-impact

## The Problem
A gig worker client hands the preparer 12 months of bank and credit card statements containing 500-2,000 transactions. The preparer must identify which transactions are business-related, categorize them into Schedule C expense lines (advertising, car expenses, supplies, utilities, meals, etc.), separate personal from business transactions, and document the business purpose. This categorization takes 60-90 minutes per client and is the most time-consuming step in sole proprietor return preparation.

## Why Nobody Has Built This
Transaction categorization seems simple but is contextually complex: "Amazon $47.32" could be office supplies, materials, or personal shopping. "Shell Gas $62.18" is deductible only if the vehicle is used for business. "Home Depot $234.56" could be a home office improvement, a rental property repair, or personal home maintenance. Accurate classification requires knowing the client's business type, whether they use a vehicle for work, whether they have a home office, and whether they own rental properties. Building this requires transaction data + client business context + tax domain knowledge — a combination no existing tool provides.

## What to Build
An ML-powered transaction classifier that ingests the client's bank/credit card feed (via Plaid or statement upload), applies business-type-specific classification rules, and outputs transactions categorized by Schedule C expense line. The classifier uses the client's business description (NAICS code, business type from prior year return) as context to distinguish business from personal transactions. The preparer reviews the classifications in a verification interface, correcting errors that train the model for future returns.

## Target Customer
Firm owners processing 200+ sole proprietor returns per season who spend 200-300 hours on manual transaction categorization.

## Impact If Built
Reduces per-client expense categorization time from 60-90 minutes to 15-20 minutes. At 300 sole proprietor clients, that is 200-350 hours saved per season — equivalent to 2 FTEs during peak season or capacity for 100+ additional clients.
