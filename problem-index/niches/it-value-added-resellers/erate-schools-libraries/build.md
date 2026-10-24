# Eligibility Checked on the Quote, Not After the Invoice

**Niche:** [[niches/it-value-added-resellers/erate-schools-libraries/profile|K-12 Schools & Libraries Buying Through E-rate]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Resellers learn which E-rate lines were ineligible when USAC reduces the invoice, months after the equipment was installed.
**Tags:** #large-language-models #bert #word-embeddings #compliance #evaluation-metrics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to deliver E-rate category two equipment and services that USAC reimburses in full, and whoever has the lowest share of invoiced dollars reduced or denied takes the account.

## The Problem
A category two quote mixes eligible switches, access points and licences with items that are ineligible or only partly eligible (some security features, end-user devices, bundled services). Cost allocation is required for the mixed ones. Errors are found at review or invoicing, after delivery.

## Why Nobody Has Built This
The eligible services list and its interpretations live in FCC orders, USAC guidance and consultants' experience; reseller quoting tools know prices, not programme rules.

## What to Build
A rules and retrieval layer that reads each quote line against the eligible services list, USAC guidance and the reseller's own history of reductions; proposes cost allocations with the documentation USAC expects; and checks the Form 471 line items against what is ordered and invoiced, flagging mismatches before the invoice is filed.

## Target Customer
Education practice leads at resellers with E-rate service-provider IDs and tens of district customers.

## Impact If Built
Cutting the share of invoiced dollars reduced or denied by even 2 points on $10M of E-rate work saves ~$200K a year (estimate), and protects district relationships.
