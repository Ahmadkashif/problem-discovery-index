# Programme Changes Applied to the Renewal Book Automatically

**Niche:** [[niches/it-value-added-resellers/licence-support-renewals/profile|Licence & Support Contract Renewals]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vendors publish dozens of price and programme changes a month, and no tool turns each into a rule and runs it against a reseller's customers.
**Tags:** #large-language-models #transformers #survival-analysis #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to renew each customer's expiring software licences, cloud subscriptions and hardware support contracts before the vendor's renewal date, and whoever renews the largest share of expiring contract value on time takes the account.

## The Problem
Microsoft's Partner Center alone posted more than thirty announcements in July 2026. Each change — a price increase from a date, an eligibility test, a renamed SKU, an end of sale — affects some renewals and some open quotes, and the reseller finds out which by having a specialist read and map it.

## Why Nobody Has Built This
Vendors write for partners in general; distributors push the announcements on; renewal tools store dates, not rules. Turning prose programme guides into executable rules needed language models that only recently became reliable enough to propose, with a human confirming.

## What to Build
A rule layer: each announcement parsed into what changes, for which SKUs and customer types, from what date, with the source text; the rule run against the renewal book and open quotes; per-customer actions for account managers; and a survival model ranking renewals by late risk.

## Target Customer
Software and renewals leaders at resellers and cloud distributors with large Microsoft, VMware and Cisco books.

## Impact If Built
Renewing a few more points of expiring value on time, before price changes and penalties apply, is worth ~$0.5–2M a year on a $50M renewal book (estimate), and halves the specialist's announcement triage.
