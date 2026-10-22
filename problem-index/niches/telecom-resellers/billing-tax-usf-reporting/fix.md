# The Reseller Certificate That Expired Last Year

**Niche:** [[niches/telecom-resellers/billing-tax-usf-reporting/profile|Telecom Billing, Tax & USF Revenue Reporting]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** A wholesale provider exempts a customer's revenue from USF contributions as resale, can't produce that customer's current reseller certificate when audited, and owes the contributions itself.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to classify every billed dollar the way USAC's auditors and state tax administrators will read it (interstate or intrastate, end-user or reseller, taxable or not) and reuse that one classification across the invoice, the tax return and Form 499, and whoever does it once and consistently takes the account.

## The Problem
A wholesaler may report revenue from a customer as reseller revenue, not subject to its own contribution, only if it has a reasonable expectation the customer contributes. The safe harbor is an annual certification from that customer, kept with its 499 filer ID and contact details. Small wholesalers collect certificates by email when an account opens and rarely again. Customers go out of business, stop filing, or never had a filer ID. An audit finds the gap, and the wholesaler pays the contribution it never collected.

## Why It's Still Broken
Certificates sit in an inbox or a shared drive, not linked to the billing account or to the revenue they exempt. Nothing checks whether the customer's filer ID is active in USAC's records, and nobody owns the annual renewal.

## What a Fix Looks Like
Attach each certificate to the billing account it covers, read the filer ID, name and date from the document, check them against USAC's public filer records, and schedule renewal before expiry. Revenue from customers without a current certificate is automatically reported as end-user revenue until the certificate arrives, and their contacts receive a pre-filled request using USAC's template.

## Who Feels the Pain
Controllers and regulatory managers at wholesale and white-label platform providers, and the officers who certify their 499s.

## Impact If Fixed
An avoidable audit exposure becomes a renewal reminder, and exempt revenue is exempt because the evidence exists.
