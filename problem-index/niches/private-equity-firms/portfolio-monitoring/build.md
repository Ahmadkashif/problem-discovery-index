# Twelve Companies, Twelve Definitions of EBITDA

**Niche:** [[niches/private-equity-firms/portfolio-monitoring/profile|Portfolio Monitoring & KPI Reporting]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The monitoring platform stores what it is given, and what it is given is each CFO's own definition of every metric, mapped by hand.
**Tags:** #large-language-models #feature-engineering #change-point-detection #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a dozen portfolio companies' differently-defined monthly packages into comparable, on-time KPIs — and whoever does that is the system the deal partner opens when something starts going wrong.

## The Problem
A fund's portfolio review compares companies on revenue growth, EBITDA margin, cash conversion, leverage and a few sector KPIs. Each company computes them differently, and the definitions shift when CFOs change, add-ons close or a lender renegotiates. The fund finance team maps each package by hand every month.

## Why Nobody Has Built This
Monitoring vendors built for the clean case — a template the CFO fills — because that is what is easy to sell and support. Mapping each company's chart of accounts is bespoke work that looks like services. Only recently has extraction from arbitrary spreadsheets become cheap enough to automate.

## What to Build
A per-company mapping layer that learns each package's layout and accounts, maps them to the fund's standard definitions with explicit adjustments, and versions the mapping. Detect definitional change when a line's behaviour or label shifts. Reconcile management, covenant and sponsor EBITDA automatically. Feed normalised data into whichever monitoring platform the fund already uses.

## Target Customer
Fund CFOs and COOs at sponsors with eight or more portfolio companies; monitoring platforms as OEM partners.

## Impact If Built
Comparable, on-time KPIs turn the monitoring platform from a quarterly archive into a monthly early-warning system.
