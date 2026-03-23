# Automated SPD-to-Adjudication-Rules Parser

**Niche:** [[niches/insurance-tpa/group-health-admin/profile|Group Health Benefits Admin]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product today can ingest a Summary Plan Description PDF and automatically generate machine-readable adjudication rules for a claims processing engine.
**Tags:** #llm #named-entity-recognition #nlp #automation #revenue-impact

## The Problem
Every new self-insured employer client requires a benefits analyst to manually read a 100-300 page SPD and translate its provisions into adjudication system configuration — deductible amounts, copay schedules, coinsurance tiers, exclusion lists, pre-authorization requirements, and coordination-of-benefits rules. This process takes 40-80 hours per client, costs $5,000-$15,000 in labor, and produces configuration errors that go undetected until a member disputes a claim. A single misconfigured provision can result in $50,000-$200,000 in mis-adjudicated claims before discovery.

## Why Nobody Has Built This
SPDs are written by attorneys in natural language with complex conditional logic ("Subject to the deductible, the Plan pays 80% of Allowed Charges for in-network providers, except for mental health services which are subject to a separate $500 deductible after January 1, 2025"). Extracting structured rules from this language requires both legal-document NLP and deep domain knowledge of benefit plan structures. The output must be provably correct — a 95% accuracy rate means thousands of mis-adjudicated claims.

## What to Build
An LLM-powered document parser that ingests SPD PDFs, extracts benefit provisions into a structured schema (JSON/XML), maps them to adjudication engine rule formats, and produces a human-reviewable diff showing extracted rules versus source text. The analyst reviews and approves rather than building from scratch — reducing setup time from 60 hours to 8 hours.

## Target Customer
Mid-market TPAs onboarding 10-50 new self-insured groups per year, each requiring manual plan configuration.

## Impact If Built
Reduces client onboarding time by 80% and configuration errors by 60-70%. For a TPA onboarding 30 groups per year, saves $150K-$400K in annual labor costs and eliminates $500K+ in mis-adjudication liability exposure.
