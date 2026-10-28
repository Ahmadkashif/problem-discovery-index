# Contracts Compiled Into Settlement Rules

**Niche:** [[niches/renewable-power-producers/ppa-settlement-rec-delivery/profile|PPA Settlement, Curtailment Claims & Certificate Delivery]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each PPA's negative-price, curtailment and settlement-point clauses are rewritten by hand into a spreadsheet, and the buyer's adviser rewrites them differently.
**Tags:** #large-language-models #transformers #descriptive-statistics #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to settle each contract month without a dispute, and whoever has the smallest share of invoiced settlement value disputed or restated takes the account.

## The Problem
Disputes come from interpretation, not arithmetic: whether an interval with a negative hub price settles, whether an ISO instruction counts as compensable curtailment, which meter value applies after a resettlement. Every workbook embeds its author's reading.

## Why Nobody Has Built This
Contract terms vary deal by deal, ETRM vendors expect a trading desk to configure instruments, and language models good enough to read clauses into rules arrived only recently.

## What to Build
A compiler that reads each executed PPA and hedge into explicit, reviewable settlement rules, has a commercial manager confirm each rule once, then runs every month and every resettlement automatically from ISO statements, meter data and dispatch instructions, producing an invoice with interval-level working that the buyer can check line by line.

## Target Customer
Commercial operations directors at IPPs with 15+ corporate PPAs and hedges.

## Impact If Built
Halving the disputed share from ~2% to ~1% (estimate) of ~$150M settled a year brings ~$1.5M of cash forward and frees ~1 analyst per 15 contracts.
