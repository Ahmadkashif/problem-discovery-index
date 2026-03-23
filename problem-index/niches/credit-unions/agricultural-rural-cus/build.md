# Seasonal Farm Cash Flow Lending Model

**Niche:** [[niches/credit-unions/agricultural-rural-cus/profile|Agricultural & Rural CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Standard credit models evaluate monthly income stability — a metric that reads every farmer as insolvent for 8 months of the year; ag CUs need a cash flow model that understands crop cycles, commodity price exposure, and seasonal income concentration.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A corn farmer applies for a $200K operating line in February. His bank account shows $15K. His income last year was $0 from January through August, then $450K in September-October from harvest sales. Standard credit underwriting flags this as extreme income instability and insufficient current cash flow. An experienced ag loan officer knows this is a perfectly normal cash flow pattern for a 1,500-acre corn operation with average yields and current commodity prices — and can assess the likelihood that this year's harvest will service the operating line. But the LOS platform can't model this, so every ag loan requires manual underwriting with the loan officer overriding system-generated risk flags.

## Why Nobody Has Built This
CU technology vendors serve the broader CU market where consumer and auto lending dominate. The ag lending segment is small (~400 CUs, many very small) and requires domain-specific modeling that CU platform companies don't have expertise in. Farm Credit System institutions (Farm Credit Banks, PCAs) have proprietary lending models built over decades but don't share them with CUs. USDA and land grant university research produces farm financial analysis frameworks but not operational lending software.

## What to Build
A farm-specific cash flow projection model integrated into the CU's lending workflow. Inputs: crop plan (acres by crop), historical yield data (USDA county-level or farm-specific), current and futures commodity prices, input cost estimates, crop insurance coverage, FSA program payments, and off-farm income. Output: projected monthly cash flow for the next 12-18 months with probability bands reflecting yield and price uncertainty. The model replaces the standard DTI check with a farm-specific coverage ratio — projected net farm income to debt service — that accounts for seasonal concentration and commodity price risk. Experienced ag loan officers validate and calibrate the model against their own judgment.

## Target Customer
Ag lending specialists and CEOs at rural CUs with $10M+ in agricultural loan portfolios who currently underwrite every ag loan manually because standard LOS risk models are inappropriate for seasonal agricultural income.

## Impact If Built
Reduces ag loan underwriting time from 4-8 hours to 1-2 hours by automating cash flow projection and risk assessment. Enables junior lending staff to evaluate ag loans with confidence, reducing dependence on 1-2 senior ag specialists. Decreases ag loan delinquency by 10-15% through more accurate cash flow stress testing that identifies over-leveraged operations before funding.
