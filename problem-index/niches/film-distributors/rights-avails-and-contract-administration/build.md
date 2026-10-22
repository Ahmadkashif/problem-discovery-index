# A Rights Grid Extracted From the Contracts, Clause by Clause

**Niche:** [[niches/film-distributors/rights-avails-and-contract-administration/profile|Rights, Avails & Contract Administration]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Rights systems assume someone has already turned every contract into structured grants; at an independent distributor nobody has, and the contracts are the only source of truth.
**Tags:** #large-language-models #transformers #bert #sets-and-logic #evaluation-metrics #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to answer whether a title is free for a given territory, medium and window on a given date correctly and in minutes, from contracts written in prose, and whoever never grants the same right twice keeps both its licensors and its licensees.

## The Problem
A 300-title library may rest on 1,000 to 3,000 agreements and amendments (estimate). Each needs reading to know what rights the distributor holds and has granted. The coordinator's spreadsheet captures the main grants and drops the conditions: holdbacks, language limits, carve-outs and "most favoured" clauses. Enterprise systems cost more to load than the library earns in a year.

## Why Nobody Has Built This
Until recently, extraction accuracy on contract clauses wasn't good enough to trust without a lawyer re-reading everything, so the economics only worked for studios. Media definitions also differ across contracts in ways only a specialist reads correctly.

## What to Build
An extraction pipeline that reads every contract and amendment and writes grants into a controlled schema (title, territory, medium, window, term, exclusivity, language, holdbacks, reversion), each row linked to the clause that created it. It runs amendment chains in order, flags ambiguous media definitions for a human decision that is then applied consistently, and answers avails and conflict questions from the grid with citations.

## Target Customer
Heads of business affairs at independent distributors, sales agents and library aggregators with a few hundred to a few thousand titles.

## Impact If Built
A library's rights become queryable in weeks rather than a year of data entry, and every answer can be traced to its clause, which is what makes a coordinator willing to sell on it.
