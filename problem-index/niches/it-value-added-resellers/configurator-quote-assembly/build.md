# No-Touch Rate Measured on the Reseller's Own Exports

**Niche:** [[niches/it-value-added-resellers/configurator-quote-assembly/profile|Quote Assembly From Configurator Exports & Distributor Quotes]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Quoting tools claim to import files; nobody measures how many lines a reseller's real exports produce without a human edit.
**Tags:** #large-language-models #transformers #word-embeddings #contrastive-learning #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn vendor configurator exports, distributor quotes and price files into a priced customer quote in the reseller's quoting tool without retyping a line, and whoever posts the highest no-touch line rate on the reseller's own files takes the account.

## The Problem
A data-centre quote may combine several configurator exports and two distributor quotes, each in its own layout, with vendor SKUs that differ from distributor part numbers. Import features handle the common formats and fail on the rest; reps fix lines by hand and nobody counts how many.

## Why Nobody Has Built This
Channel CPQ vendors integrate with distributor feeds first, and their import parsers are format-specific; matching across renamed SKUs needed learned matching that only became cheap recently.

## What to Build
An extraction and matching service that ingests any export or distributor quote, matches each line to the reseller's catalogue and distributor part numbers using embeddings trained on the reseller's own historical quotes, and writes priced lines into the CPQ. It reports no-touch line rate per vendor format and learns from each correction.

## Target Customer
Inside sales and operations leaders at resellers producing thousands of quotes a month.

## Impact If Built
Moving from rekeying to ~85–90% no-touch lines (estimate) saves ~20–30 minutes per solution quote, or several thousand rep-hours a year at a mid-sized reseller.
