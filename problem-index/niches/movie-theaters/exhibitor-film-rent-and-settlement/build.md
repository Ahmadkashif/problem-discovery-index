# A Terms Ledger That Re-Derives Every Invoice

**Niche:** [[niches/movie-theaters/exhibitor-film-rent-and-settlement/profile|Exhibitor Film Rent & Settlement]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Exhibitors pay film rent invoices they cannot easily recompute, because the terms behind them were never stored as data.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #automation #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to hold an engagement-level record of the terms the theatre actually agreed, so that accruals are right every week and each distributor's invoice is checked before it is paid, and whoever catches the most overcharges and knows each sales office's settlement habits takes the account.

## The Problem
A 20-theatre circuit settles hundreds of engagements a quarter, each with its own scale, floor or firm terms. The film accountant checks the largest invoices by hand and pays the rest. Overcharges from a wrong week, a wrong gross or a percentage that was renegotiated by phone go through.

## Why Nobody Has Built This
Terms vary by distributor and change mid-run; most exhibitors are too small to justify custom software; and ticketing vendors treat film hire as a report, not a ledger.

## What to Build
A ledger that extracts terms from booking confirmations and emails into a schema for review, recomputes the accrual daily from posted grosses, and re-derives every distributor invoice, flagging each difference by cause with the calculation attached. It keeps a settlement history per distributor and film type for the buyer.

## Target Customer
Film accountants and controllers at circuits of 5–100 theatres; outsourced bookkeepers serving independents.

## Impact If Built
Re-deriving every invoice rather than spot-checking recovers an estimated ~0.5–1% of film rent in errors and turns month-end from days into hours (estimate).
