# The Tracker That Dies With the Deal

**Niche:** [[niches/investment-banking-boutiques/sell-side-ma-advisory/profile|Sell-Side M&A Advisory]]
**Industry:** [[industries/investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Fix (Pain Point)
**One-liner:** The buyer tracker for each process is the richest record the firm will ever have of that market, and it is archived in a deal folder and never opened again.
**Tags:** #data-integration #feature-engineering #large-language-models #evaluation-metrics #quick-win #automation
**Contested on:** Not terminal as stated — every competitor is fighting to deliver the highest certain price, but a sponsor selling its fifth portfolio company and a founder selling the only company they will ever own buy that outcome on different evidence, from different banks, and the two contests are stated in the sub-niches below.

## The Problem
Every process ends with a tracker: two hundred buyers, each with dates, stage reached, comments, indication ranges and bids. It is saved to the deal folder with the closing documents. Six months later a different team running a process in the same sector starts a fresh tracker from a database screen.

## Why It's Still Broken
Each tracker has its own columns and naming. Nobody owns the cross-deal record, and the people who know what the comments mean move on. CRM fields are filled inconsistently because deal teams treat them as overhead.

## What a Fix Looks Like
Ingest every historical tracker, normalise columns and buyer names with language-model-assisted extraction and entity resolution, and load them into a single buyer-interaction table connected to the CRM. Require the closing step of every new process to reconcile its tracker into that table. Surface each buyer's history automatically whenever its name appears on a new list.

## Who Feels the Pain
Associates rebuilding buyer lists; MDs relying on memory; clients whose processes miss bidders the firm already knew about.

## Impact If Fixed
A cheap data-engineering fix that converts years of archived spreadsheets into the firm's most defensible asset, and the prerequisite for any buyer-propensity model.
