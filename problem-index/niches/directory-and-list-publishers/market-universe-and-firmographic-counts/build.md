# A Universe Count With Error Bars

**Niche:** [[niches/directory-and-list-publishers/market-universe-and-firmographic-counts/profile|Market Universe & Firmographic Counts]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every compiler sells a segment count ("there are 14,212 firms in your segment", illustrative); none says how many of them are dead, duplicated or in the wrong size band.
**Tags:** #bayesian-inference #confidence-intervals #gradient-boosting #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give a revenue team the complete, de-duplicated and correctly sized universe of accounts in its market, and whoever's count survives the customer's own match test — no dead, duplicate or mis-banded firms — becomes the system of record for targeting and territories.

## The Problem
A market-sizing analyst compares counts from two vendors for the same segment and gets numbers that differ widely. Neither vendor can explain the gap beyond sources and methodology, and the analyst picks the larger count because it makes the plan look better — which is exactly the incentive that keeps dead records in files.

## Why Nobody Has Built This
Stating error invites comparison on accuracy rather than size, and the ground truth needed — a sample of records checked by call, registry and web — costs money no buyer explicitly pays for.

## What to Build
A count that ships with its own audit: for each segment, a stratified sample verified by call and registry, an estimate of dead, duplicate and mis-banded share with intervals, and a modelled-size field that carries a band probability rather than a single band. The vendor publishes a count with its error stated — "~14,200, of which ~4% dead and ~6% mis-banded" (illustrative) — and refreshes it quarterly.

## Target Customer
Compilers selling universe data to revenue operations, strategy and investor teams who plan on counts.

## Impact If Built
Buyers can compare vendors on accuracy instead of size, and the compiler that purges honestly stops losing deals to inflated counts.
