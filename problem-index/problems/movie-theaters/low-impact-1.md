# Film Rent Accrual and Settlement on the Exhibitor Side

**Industry:** [[movie-theaters|Movie Theaters]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every engagement carries its own sliding-scale terms and ends in a negotiated settlement, and exhibitors accrue and reconcile film rent in spreadsheets bolted to a general ledger that was never built for terms that change by week.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #automation #data-integration #quick-win

## The Problem
Film rent is a theatre's largest cost, and it is calculated engagement by engagement. A wide release in a 12-screen theatre runs on terms that may slide by week, with a floor, a house allowance or a percentage of gross above a threshold. Some films settle on firm terms, and others are renegotiated after the run on how the film performed. Cinemark accrues film rent on "estimates of the final settlement rate, which occurs at the conclusion of the film's run." The film accountant or the owner keeps a worksheet per engagement: weekly grosses from the point-of-sale system, the agreed terms, the accrual, the distributor's invoice and the settled figure once a sales rep and the buyer agree it.

At a small circuit this is one person's month-end. At an independent it is the owner's Sunday night. Errors flow in both directions: an accrual that misses a term change overstates profit until settlement, and an invoice that applies the wrong week's percentage goes unchallenged because nobody re-derives it.

## What Already Exists
General ledgers (QuickBooks, Sage Intacct, NetSuite) post the accruals and payments. Cinema management systems such as Vista and Veezi report grosses by film, screen and day, and some include film-hire reports that apply a simple percentage. Distributors send settlement statements as PDF or spreadsheet. The distributor's side of the same transaction is analysed under [[niches/film-distributors/theatrical-booking-and-settlement/profile|Theatrical Booking & Settlement]] in film distribution.

## The Customisation Gap
Generic accounting software has no concept of an engagement with sliding terms. The exhibitor-specific logic is: a terms record per film per theatre, with the weekly scale, floors, house allowances and any aggregate deal across a circuit; accruals that recompute as each week's grosses post; matching of the distributor's invoice against the terms and the reported grosses, flagging differences by cause (wrong week, wrong gross, wrong percentage, unrecorded renegotiation); a settlement history by distributor and film type that tells the buyer how far each sales office usually moves after the run; and reconciliation to the box office figures already reported to Comscore. Terms arrive in emails and booking confirmations, so the first step is extracting them into structure, which language models now do reliably enough to draft for review.

## Impact If Solved
For a 10–30 screen circuit, an engagement-level terms and accrual record turns a multi-day month-end into hours and catches invoice errors that otherwise pass, plausibly ~0.5–1% of film rent (estimate). It also gives the buyer a settlement history to negotiate with, which no general ledger provides.
