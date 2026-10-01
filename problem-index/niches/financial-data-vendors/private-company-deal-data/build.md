# Detecting the Round Before the Press Release

**Niche:** [[niches/financial-data-vendors/private-company-deal-data/profile|Private Company & Deal Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Form D filings, hiring surges and registry changes announce a financing weeks before a press release, and researchers assemble those signals by hand.
**Tags:** #gradient-boosting #large-language-models #graph-theory #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to find every private financing round and valuation before anyone else and resolve it onto the right company — and whoever has the earliest, most complete coverage wins the deal teams who source from it.

## The Problem
Many rounds are never announced, and announced ones are often late. Signals arrive scattered across filings, registries and the web.

## Why Nobody Has Built This
Each signal is weak alone; combining them needs entity resolution the vendor's graph provides and a researcher loop to confirm.

## What to Build
A model scoring each company for a probable recent financing from combined signals, routing high-probability cases to researchers for confirmation, with confirmed outcomes as labels.

## Target Customer
Company and deal research leadership at private-company data vendors.

## Impact If Built
Earlier coverage is the contest; signal fusion moves the discovery date forward.
