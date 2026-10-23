# Invoices Issued on Day 31

**Niche:** [[niches/ocean-shipping-carriers/demurrage-detention-billing/profile|Demurrage & Detention Billing and Disputes]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A D&D charge invoiced more than 30 days after it stopped accruing is lost, and billing runs that batch monthly miss the window.
**Tags:** #compliance #workflow-orchestration #quick-win #automation #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to bill every chargeable container day inside the FMC's 30-day window on an invoice that survives dispute, and whoever collects the highest share of billed demurrage and detention without waiver takes the account.

## The Problem
Billing teams invoice D&D in monthly batches or wait for the container's return to close the charge. Some invoices go out after the 30-day limit or miss a required element, and the billed party is not obliged to pay.

## Why It's Still Broken
Batch billing predates the rule, and nobody monitors each charge's deadline individually.

## What a Fix Looks Like
Track a deadline per charge from the last chargeable day, invoice continuously, and block any invoice missing a required element before it is sent.

## Who Feels the Pain
Billing teams, finance controllers writing off charges, and customers receiving invoices they can legally ignore.

## Impact If Fixed
Every 1% of charges invoiced after day 30, on ~$50M a year of US D&D billing (estimate), is ~$500,000 a year that need not be paid.
