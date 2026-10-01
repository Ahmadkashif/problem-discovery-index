# Parsing the Announcement Once, Correctly

**Niche:** [[niches/financial-data-vendors/reference-corporate-actions/profile|Reference & Corporate Actions Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A complex corporate action is announced in prose and read by operators at every vendor and every custodian separately.
**Tags:** #large-language-models #transformers #evaluation-metrics #data-integration #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to produce a golden copy of corporate actions and security identifiers that downstream systems can process without manual scrubbing — and whoever's events are right first time removes the client's reconciliation team.

## The Problem
Mergers with elections, rights issues and special dividends arrive as notices whose terms must be structured into event fields.

## Why Nobody Has Built This
Event types are many and errors are expensive, so operators stay in the loop for everything.

## What to Build
Structured extraction of event terms with confidence, cross-checks against other sources, and operator review only where sources or confidence disagree; operator corrections as labels.

## Target Customer
Reference data operations at vendors.

## Impact If Built
Faster, more accurate events and smaller operations teams.
