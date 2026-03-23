# Fractionated Mineral Interest Royalty Engine

**Niche:** [[niches/oil-gas-field-services/tribal-land-operators/profile|Tribal Land Operators]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No software exists to automatically calculate and distribute royalties across hundreds of fractionated mineral interest holders on a single tribal allotment.
**Tags:** #graph-ml #regression #tabular-ml #data-integration #compliance

## The Problem
On tribal trust lands, mineral rights are held in trust by the federal government and have been subdivided through generations of inheritance without consolidation. A single allotment may have 200+ individual interest holders, each with a fractional ownership percentage calculated from probate records spanning a century. Every month, production revenue from that allotment must be split according to these fractions and reported to ONRR. Currently this is done manually by BIA staff or small operators using spreadsheets, leading to chronic payment delays (6-18 months is common) and frequent calculation errors that trigger federal audits.

## Why Nobody Has Built This
The fractionation data lives in legacy BIA systems (TAAMS — Trust Asset and Accounting Management System) that have no modern API. Extracting and maintaining the ownership graph requires parsing probate records, allotment histories, and BIA trust modifications that span decades and vary by reservation. No commercial software company has invested in this because the market is small, the data is messy, and the customer (tribal mineral offices and BIA field offices) has limited procurement budgets.

## What to Build
A royalty calculation engine that ingests production volumes and prices, maps them against a maintained graph of fractionated mineral interests per allotment, computes individual royalty payments, generates ONRR-compliant distribution reports, and flags discrepancies against historical payments. The system maintains the ownership graph as probate events and BIA modifications occur, rather than recomputing from scratch each month.

## Target Customer
Tribal mineral rights departments and BIA field offices managing production on allotted trust lands, particularly on reservations with active oil and gas production (Fort Berthold, Osage, Uintah-Ouray, Wind River).

## Impact If Built
Reduces royalty payment processing from 6-18 months to under 30 days, eliminates calculation errors that currently trigger federal audits, and gives individual allottees timely access to revenue they are legally owed.
