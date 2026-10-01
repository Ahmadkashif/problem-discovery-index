# The Non-GAAP Reconciliation Keyed by Hand

**Niche:** [[niches/financial-data-vendors/filings-transcript-ingestion/profile|Filings & Transcript Ingestion]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Adjusted EBITDA and its reconciliation sit in an earnings-release exhibit with no XBRL, and are keyed manually every quarter.
**Tags:** #large-language-models #transformers #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a filing or a call into structured, cited data within minutes rather than hours — and whoever is first and right on earnings night becomes the feed quant and fundamental clients wire into their models.

## The Problem
Press-release exhibits filed with 8-Ks carry the non-GAAP figures clients most want, outside structured tagging.

## Why It's Still Broken
Layouts vary by issuer; extraction errors are costly.

## What a Fix Looks Like
Table extraction with per-issuer layout memory and arithmetic checks that the reconciliation sums.

## Who Feels the Pain
Collection analysts on earnings night; clients waiting for adjusted figures.

## Impact If Fixed
Minutes instead of hours for the most-requested numbers.
