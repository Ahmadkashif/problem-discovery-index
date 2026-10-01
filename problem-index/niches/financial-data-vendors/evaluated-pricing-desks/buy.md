# Comparable Selection for Bonds That Do Not Trade

**Niche:** [[niches/financial-data-vendors/evaluated-pricing-desks/profile|Fixed-Income Evaluated Pricing]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Similarity search and matrix pricing are well understood; choosing which traded bonds a never-traded bond should be priced off, and explaining the choice to a valuation committee, is not solved by either.
**Tags:** #k-nearest-neighbors #graph-neural-networks #gaussian-processes #feature-engineering #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to price illiquid bonds defensibly every day and survive the client's price challenges — and whoever's evaluations hold up under challenge keeps the fund administrator's NAV process.

## The Problem
Most bonds do not trade on most days. Evaluators price them off comparables chosen by sector, rating, maturity and issuer rules, and the choice drives the price.

## What Already Exists
Matrix pricing, spread-curve models, nearest-neighbour similarity methods and graph models of issuer relationships are standard techniques.

## The Customization Gap
Learning comparability from which bonds actually move together after trades, rather than from static attributes; using issuer, guarantor and sector graphs; producing an uncertainty for each evaluation; and generating a comparables explanation a fund's valuation designee can file as Rule 2a-5 evidence.

## Target Customer
Evaluated pricing quant and product leads.

## Impact If Solved
Better comparables mean fewer upheld challenges and defensible evaluations for the instruments where fair value is hardest.
