# Store-Level Limits From the Wholesaler's Own Ledger

**Niche:** [[niches/consumer-goods-wholesalers/independent-store-credit-manager/profile|The Credit Manager Selling to Independent Stores on Terms]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Score every small store on how it has actually paid and ordered with this wholesaler, and set terms and limits from that rather than from a thin bureau file.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide which independent stores get net terms and how much, and whoever writes off the least receivables per dollar of terms sales takes the account.

## The Problem
Bureaus know little about a two-person gift shop. The wholesaler knows years of its invoices, payments, disputes and order cadence, but the credit manager reads that history one account at a time.

## Why Nobody Has Built This
Credit tools are built around bureau data and large accounts, and wholesalers have not had the data science to model their own ledgers.

## What to Build
A time-to-delinquency model per store from the wholesaler's receivables and order history, seasonality, store type and region, with bureau scores where available. It recommends terms and limits, flags accounts whose payment or ordering pattern is changing, and records every override with its outcome.

## Target Customer
Credit managers at wholesalers with 2,000+ active store accounts.

## Impact If Built
Cutting write-offs from ~1.5% to ~1% of terms sales (estimate) on $40M saves ~$200K a year (estimate), while letting the desk approve more stores it now refuses.
