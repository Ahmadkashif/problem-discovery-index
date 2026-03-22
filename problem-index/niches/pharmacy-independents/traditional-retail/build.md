# Real-Time Prescription Profitability Calculator with DIR Fee Estimation

**Niche:** [[niches/pharmacy-independents/traditional-retail/profile|Traditional Retail Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tool that shows the owner-pharmacist estimated net margin per prescription AFTER projected DIR fees — replacing the current reality where profitability is unknowable until clawbacks hit 6-9 months later.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact #data-integration #tacit-knowledge-ml

## The Problem
Independent pharmacies fill 200-400 prescriptions per day and see an adjudicated reimbursement at point of sale that looks like margin. But DIR fees — retroactive clawbacks from PBMs based on quality metrics like medication adherence rates, generic dispensing ratio, and star ratings — reduce that margin by 6-15% across the entire book of business. The fees are assessed quarterly or semi-annually, meaning the pharmacist discovers a $30,000-80,000 liability months after the prescriptions were dispensed. Experienced owner-pharmacists develop an intuition for which payer-NDC combinations are "losers" after DIR — they steer patients toward generics, avoid certain plans, or proactively call patients about adherence — but this judgment is built over years of painful financial surprises and cannot be transferred to a new pharmacy manager or locum.

## Why Nobody Has Built This
DIR fees are calculated using opaque formulas that vary by PBM, plan, and contract tier. The pharmacy knows its current performance metrics (adherence rates, generic dispensing percentage) but not the exact thresholds or weightings the PBM uses to compute DIR assessments. Modeling DIR exposure requires historical data spanning multiple assessment periods (2-3 years minimum), correlation of per-prescription reimbursement with eventual DIR clawback amounts, and continuous updating as PBM contracts change annually. The data lives in multiple systems: the PMS (prescription and adjudication data), the PSAO portal (contract terms), and PBM remittance files (actual DIR assessments). No single vendor has access to all three data sources, and most independents lack the technical sophistication to export and merge them.

## What to Build
A SaaS platform that ingests adjudication data from the PMS, historical DIR assessment files from PBM remittances, and current quality metric standings to build a per-pharmacy gradient-boosted model predicting DIR fee exposure by payer, NDC, and quality metric trajectory. At point of sale, the system overlays estimated net-of-DIR margin on each prescription — green (profitable after DIR), yellow (marginal), red (likely underwater). The pharmacist sees a daily dashboard showing aggregate DIR exposure trending, which payer contracts are most punitive, and which patient adherence interventions would have the highest ROI for reducing DIR liability. The tacit knowledge of experienced pharmacists who "just know" which prescriptions lose money is codified into a predictive model that any pharmacy can use from day one.

## Target Customer
Independent pharmacy owners filling 150+ Rx/day who have been surprised by DIR fee assessments exceeding $50,000 annually and currently have no way to estimate prescription-level profitability at point of sale.

## Impact If Built
Gives 19,000 independent pharmacies real-time visibility into true prescription profitability. Early modeling suggests that pharmacies with DIR awareness can reduce exposure by 15-25% through targeted adherence interventions and payer mix optimization — translating to $8,000-20,000 in recovered annual margin per location. Eliminates the 2-3 year learning curve for new pharmacy owners to develop the financial intuition that veterans build through painful experience.
