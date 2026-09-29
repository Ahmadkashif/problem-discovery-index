# Product Normalization Adapted to Rate Structure

**Niche:** [[niches/credit-unions/deposit-loan-pricing-data/profile|Deposit & Loan Pricing Benchmark Data]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data integration tools normalize fields; two accounts advertising the same rate can pay materially differently once tiers, relationship qualifiers, promotional periods, and balance caps are applied, and that is the whole comparison.
**Tags:** #bert #transformers #large-language-models #feature-engineering #random-forests #evaluation-metrics #transfer-learning #automation #data-integration #workflow-orchestration

## The Problem
Every benchmark depends on deciding that two products are comparable, and deposit and loan products are engineered to resist that. A headline rate applies to a balance tier, may require a relationship qualifier such as direct deposit or a linked account, may be promotional for a defined window before reverting, and may cap the qualifying balance. Loan pricing carries rate sheets adjusted for credit tier, term, loan-to-value, and relationship discounts. Contributed data arrives in each institution's own product structure, and analysts normalize it by hand into comparable buckets. That reduction limits how much data can enter the benchmark, and inconsistency between analysts introduces variance into the numbers institutions price against.

## What Already Exists
Data integration and transformation tooling is mature and cheap. The cloud ETL platforms, dbt, and the master data products all handle ingestion, schema mapping, versioning, and testing well. Document extraction handles rate sheets competently. For moving and reshaping the data, nothing needs building.

## The Customization Gap
Those tools map fields to fields. Comparability here requires computing an effective rate under a defined customer profile, which means modelling the product's rate structure rather than recording its headline. Two money market accounts with identical advertised rates pay differently to the same customer if one tiers at twenty-five thousand and the other at one hundred thousand, and no schema mapping expresses that. The adaptation is a product structure model as the normalization target — tiers with thresholds, qualifier conditions, promotional period and reversion, balance caps, and for lending the full adjustment grid — with effective rates computed for standard customer profiles from that model. Confidence must be per-component, so an ambiguous qualifier condition routes to an analyst while a standard tier table does not. And structure change detection matters as much as level change: an institution quietly moving a tier threshold changes what customers actually earn without touching the advertised rate, which is invisible to any system tracking headline numbers.

## Target Customer
Heads of data operations and product methodology at pricing data providers, and the analysts who currently bucket contributed products by hand and cap how much data reaches the benchmark.

## Impact If Solved
Raises contribution throughput, which directly deepens the benchmark, and removes an unmeasured source of analyst variance from the number institutions price against. Structure change detection is also a genuinely new signal — competitive repricing executed through tier and qualifier changes rather than headline rates is common and currently invisible.
