# Multi-Carrier Commission Statement Auto-Parser

**Niche:** [[niches/independent-insurance-agents/commission-reconciliation-ops/profile|Commission Reconciliation Operations]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool can ingest commission statements from 20+ carriers — each in a different PDF or CSV format — and automatically extract policy-level commission data into a standardized structure.
**Tags:** #ocr #named-entity-recognition #nlp #automation #data-integration

## The Problem
A mid-size agency with 20 carrier appointments receives 20+ commission statements monthly, each in a proprietary format. Some are multi-page PDF tables; others are CSV files with carrier-specific column headers; others are line items on a direct deposit summary. The bookkeeper must open each statement, identify the format, extract the policy number, premium, and commission amount for each line item, and enter this data into a reconciliation spreadsheet or the AMS. This manual parsing takes 4-8 hours per month and is error-prone.

## Why Nobody Has Built This
The variety of carrier statement formats is enormous — even within a single carrier, statement layouts change when IT systems are upgraded. Building a parser that handles 200+ carrier formats requires ongoing maintenance as formats change. The market (independent agency bookkeepers) is fragmented and price-sensitive, making the ROI uncertain for a standalone product. IVANS handles policy downloads but does not standardize commission data.

## What to Build
A document processing engine that accepts commission statements in any format (PDF, CSV, Excel, XML), identifies the carrier and statement layout using template matching or ML-based document classification, extracts per-policy commission data (policy number, insured name, premium, commission rate, commission amount, effective dates), and outputs a standardized dataset that can be imported into the AMS or reconciliation tool. The system learns new carrier formats from a few labeled examples.

## Target Customer
Agency bookkeepers at agencies with 15+ carrier appointments who spend 4-8 hours per month manually parsing commission statements.

## Impact If Built
Reduces commission statement parsing from 4-8 hours to under 30 minutes per month. Catches formatting errors and missing policies that manual parsing misses, recovering an estimated 1-3% of commission revenue that goes uncollected due to parsing oversights.
