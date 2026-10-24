# A Recurrence Ledger Under Every Closed Root Cause

**Niche:** [[niches/pharmaceutical-manufacturers/deviation-capa-investigation/profile|Deviation & CAPA Investigation]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Plants close deviations against root causes and never learn which ones held, because nothing links a closed investigation to the next appearance of the same failure.
**Tags:** #tacit-knowledge-ml #transformers #large-language-models #survival-analysis #k-nearest-neighbors #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to close each deviation with a root cause that holds, and whoever leaves the fewest repeat deviations from causes already declared fixed takes the account.

## The Problem
A site's QMS holds years of deviations, each with a root cause and a CAPA. The same failure (a leaking seal on a granulator, a cleaning residue after a particular changeover, a sticking punch on one press) returns under new deviation numbers, described in different words by different people. Investigators recognise some recurrences from memory; FDA investigators find others by reading the records.

## Why Nobody Has Built This
QMS vendors sell workflow and reporting, not judgement on content. Narratives are inconsistent, equipment is named several ways, and root-cause taxonomies change with each system migration. Firms are also wary of a tool that writes down which investigations failed, because the record is inspectable.

## What to Build
Normalise historical deviations (equipment, product, step, material lot, failure mode), link likely recurrences with retrieval models, and compute for every root-cause category, CAPA type and investigator how often the failure returned within a year. Surface related history and the durability of candidate root causes when a new deviation opens, with the senior investigators' past links as training signal. Every suggestion shows its evidence so the investigator can defend the conclusion.

## Target Customer
Site QA directors and heads of quality at generic makers and CDMOs with high deviation volumes and repeat 483 observations.

## Impact If Built
At a site closing 2,000 deviations a year, halving repeat deviations would remove several hundred investigations and their batch holds (estimate), and would give QA an evidenced answer when FDA asks whether a CAPA worked.
