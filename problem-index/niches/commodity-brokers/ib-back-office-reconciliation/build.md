# A Clearing-Agnostic Book for Every Introducing Broker

**Niche:** [[niches/commodity-brokers/ib-back-office-reconciliation/profile|Introducing Broker Back Office & Commission Reconciliation]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An introducing broker's entire history lives in its clearing FCM's formats, so every change of FCM means rebuilding its records from PDFs.
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn the clearing FCM's daily statements and commission runs into a per-account, per-broker book an introducing broker can reconcile, pay its brokers from and show an NFA examiner, and whoever closes the month with no payout disputes and a clean NFA exam takes the account.

## The Problem
An IB's accounts, trades, commissions and fees exist in the clearing FCM's system. The IB keeps copies: monthly PDFs, CSV extracts, portal downloads. When it changes FCMs, adds a second one or is moved by a merger, it loses continuity. It also loses the ability to show a customer, a departing broker or an examiner a clean history.

## Why Nobody Has Built This
IBs are small and numerous, and per-FCM integrations were too expensive for any vendor to build for them. Clearing FCMs have no incentive to make their IBs portable.

## What to Build
A document-first ledger that parses any FCM's statements and commission reports, whatever their layout, into one normalised book of accounts, trades, fees and adjustments per IB. It keeps a continuous history across FCM changes, runs payouts, and serves the per-broker supervision views and the customer histories examiners request.

## Target Customer
Principals and compliance officers at independent IBs with 3–50 associated persons (estimate), especially those clearing through more than one FCM.

## Impact If Built
An IB owns its own records for the first time, cuts its monthly close from days to hours, and can change clearing relationships without losing its history.
