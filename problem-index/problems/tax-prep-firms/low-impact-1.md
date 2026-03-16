# Multi-State Filing Complexity Engine

**Industry:** [[tax-prep-firms|Tax Prep Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic tax software calculates state taxes but cannot reason about nexus triggers, apportionment rules, or state-specific credit eligibility for remote workers and multi-state businesses.
**Tags:** #llm #text-classification #nlp #compliance

## The Problem
Post-2020 remote work has created a nexus explosion: a small business client with employees in three states now potentially has income tax, withholding, and sales tax obligations in all three, each with different thresholds, apportionment formulas, and credit mechanisms. Preparers at small firms spend 45-90 minutes per multi-state return researching whether a state's economic nexus threshold has been met, which income allocation method applies (separate accounting vs. formula apportionment), and whether the resident state grants a credit for taxes paid to the non-resident state. This research is repeated from scratch each season because rules change annually and no tool tracks the state-by-state matrix automatically.

## What Already Exists
Tax software like Drake and UltraTax CS supports multi-state return preparation — you can file a non-resident return in any state. State tax research tools (Bloomberg Tax, Checkpoint) provide the raw regulatory text. But the gap is between "this state's rules exist in a database" and "this specific client triggers nexus in Ohio based on 23 days of remote work and $48,000 of sourced income, and here is the optimal filing position." The software computes taxes once you tell it what to file; it does not tell you what you should file.

## The Customisation Gap
A tax-prep-specific compliance layer needs to ingest client facts (employee locations, days worked per state, revenue by state, entity type), apply current-year nexus rules from all 50 states, determine filing obligations, recommend apportionment method, identify available credits and deductions unique to each state (e.g., Illinois' pass-through entity tax election, California's R&D credit), and flag year-over-year changes in state law that affect the client. This requires continuous ingestion of state legislative updates, classification of which clients are affected, and integration with the tax software's state module.

## Impact If Solved
Reduces per-return multi-state research time from 45-90 minutes to under 10 minutes. For a firm with 300 multi-state returns, that is 175-400 hours recovered per season — roughly one full-time seasonal employee. Eliminates missed filing obligations that result in penalty notices and client attrition.
