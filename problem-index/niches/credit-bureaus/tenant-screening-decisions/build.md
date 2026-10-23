# Eviction Filings Read for Outcome, Not Existence

**Niche:** [[niches/credit-bureaus/tenant-screening-decisions/profile|Tenant Screening Reports & Decisions]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A screening report lists an eviction filing whether the case ended in judgment, settlement, dismissal or sealing, and landlords decline on the filing.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to return a screening decision in minutes that is matched to the right applicant and holds up under FCRA accuracy rules and fair-housing law, and whoever gives landlords instant decisions with the fewest wrong-person and disparate-impact findings takes the account.

## The Problem
Eviction cases are filed in thousands of local courts. Many are dismissed, settled or withdrawn, some are later sealed, and docket entries describing the outcome are inconsistent across courts. Screening bureaus often capture the filing when it is filed and never the disposition. The FTC–CFPB action against TransUnion's rental screening unit turned on exactly this kind of incomplete eviction record.

## Why Nobody Has Built This
Dispositions arrive later than filings, in free text, from court systems that publish differently; updating every past record costs money no landlord pays for directly.

## What to Build
Classify each eviction case's current disposition from docket text and later entries — judgment for possession, money judgment, dismissed, settled, sealed — with confidence; re-check open filings on a schedule; suppress sealed and dismissed cases where state law or policy requires; and report filings with their outcome so decision rules can treat them differently.

## Target Customer
Screening bureaus' data and compliance leads; court-record data vendors supplying them.

## Impact If Built
Fewer applicants declined on cases they won, and a defence against the accuracy claims that have produced the largest penalties in this niche.
