# eBR Review by Exception, Configured Product by Product

**Niche:** [[niches/pharmaceutical-manufacturers/batch-record-review-release/profile|Batch Record Review & Release by Exception]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every major eBR system can review by exception; few plants have the configured, validated rules that let QA trust it.
**Tags:** #feature-engineering #autoencoders #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to cut QA's review of each executed batch record to the entries that need a human, and whoever releases the highest share of batches with no documentation error found after release takes the account.

## The Problem
Plants buy an eBR expecting faster release and keep full review because nobody configured which exceptions matter for each product.

## What Already Exists
Körber PAS-X, Emerson Syncade, Siemens Opcenter, Rockwell PharmaSuite, and frontline platforms such as Tulip and Apprentice.io, with in-process limits, enforced sequences, electronic signatures and exception reports.

## The Customization Gap
Each product needs its own critical-entry list, alarm-response rules, trend limits within specification, and links from exceptions to open deviations and the product's stability and complaint history. The rules must be validated and maintained as master records change. This configuration is where projects stall, and a tool that proposes and documents the rules from history fills it.

## Target Customer
QA and MES leads at plants with an eBR in place but full manual review still running.

## Impact If Solved
Switching on validated review by exception for a plant's top products could halve QA review hours on those records (estimate) without a new system purchase.
