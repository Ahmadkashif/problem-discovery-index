# Accounts Receivable Built for Sliding-Scale Terms

**Niche:** [[niches/film-distributors/theatrical-booking-and-settlement/profile|Theatrical Booking & Settlement]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AR software expects an invoice amount known in advance; film rent is computed from grosses, terms that slide by week, and a settlement agreed after the fact.
**Tags:** #large-language-models #feature-engineering #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to settle every engagement at the terms actually agreed within days of the run ending, and whoever settles fastest with the fewest write-downs keeps exhibitors booking its films and producers trusting its statements.

## The Problem
Distribution finance runs film rent through a general ledger built for fixed invoices. Each settlement is calculated in a worksheet outside it, keyed in, and chased by email. Independent theatres pay late, circuits net disputes against other titles, and ageing reports can't tell a settlement still in negotiation from a debt.

## What Already Exists
NetSuite, Sage Intacct and QuickBooks with collections add-ons; Comscore box office feeds; exhibitor portals that publish statements.

## The Customization Gap
The adaptation needs:
- a terms engine (weekly percentages, aggregate terms, floors, house allowances, flat and per-capita deals) that computes the expected film rent from reported grosses;
- statuses for "in settlement", "settled" and "disputed";
- netting across titles per circuit;
- ingestion of exhibitor statements in their native formats;
- separate collection workflows for circuits and independents.

## Target Customer
Distribution finance leads and controllers at independent distributors running 10 to 30 theatrical releases a year.

## Impact If Solved
Film rent is computed rather than keyed, receivables reflect what is actually owed, and collections from small theatres speed up by weeks.
