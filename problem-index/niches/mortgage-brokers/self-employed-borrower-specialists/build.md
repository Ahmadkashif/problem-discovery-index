# Automated Self-Employed Income Calculator with Lender-Specific Rules

**Niche:** [[niches/mortgage-brokers/self-employed-borrower-specialists/profile|Self-Employed Borrower Specialists]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today takes a self-employed borrower's tax returns and outputs lender-ranked qualifying income with add-backs calculated per each lender's specific overlay rules.
**Tags:** #ocr #nlp #tabular-ml #automation #workflow-orchestration #revenue-impact

## The Problem
A processor handling a self-employed borrower file must manually read 2-3 years of personal and business tax returns (1040, Schedule C, K-1, 1120-S, 1065), identify income lines, apply add-backs (depreciation, amortization, depletion, meals/entertainment), subtract obligations, and calculate a two-year trending average — then repeat this calculation with variant rules for each lender being considered. This takes 2-4 hours per file and is the single biggest bottleneck in self-employed mortgage origination.

## Why Nobody Has Built This
The calculation logic isn't just math — it requires interpreting tax return context (is this depreciation recurring or one-time? is this K-1 income from an active or passive entity?) and mapping those interpretations to lender-specific overlays that change quarterly. Building a rules engine that covers 30+ wholesale lenders' self-employed income guidelines requires deep mortgage domain expertise combined with engineering capability — a rare intersection. Lender guidelines are distributed as PDFs and rate sheets, not APIs.

## What to Build
An engine that ingests parsed tax return data (from OCR or manual entry), applies the full Fannie Mae 1084/1088 calculation methodology, then layers each wholesale lender's specific overlays (add-back treatment, trending requirements, entity type restrictions) to output a ranked list of qualifying income figures by lender. The output shows exactly which lender yields the highest qualifying income for the borrower's specific tax situation.

## Target Customer
Self-employed borrower specialist brokerages (typically 5-20 loan officers) where 50%+ of volume is self-employed — these firms process 200-500 self-employed files per year and the income calculation bottleneck directly limits their capacity.

## Impact If Built
Reduces self-employed file processing time from 2-4 hours to 15-30 minutes per file. Enables processors to handle 3-4x more self-employed files, directly increasing brokerage revenue capacity without hiring. Eliminates income calculation errors that cause late-stage denials — estimated at 8-12% of self-employed submissions.
