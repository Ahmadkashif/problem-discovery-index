# TPA Dashboard with Per-Claim 340B Margin Visibility and Audit Trail

**Niche:** [[niches/pharmacy-independents/340b-contract-pharmacy/profile|340B Contract Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** 340B TPAs like Sentry and Macro Helix process eligibility and replenishment but give the pharmacy minimal per-claim visibility — the pharmacy knows its aggregate 340B savings but cannot verify which specific claims were attributed, what margin each generated, or whether individual claims would survive audit scrutiny.
**Tags:** #data-integration #feature-engineering #compliance #revenue-impact #quick-win

## The Problem
Independent pharmacies in 340B contract arrangements receive monthly or quarterly reports from their TPA showing aggregate 340B savings and replenishment volumes. These reports answer "how much did we save?" but not "which claims drove the savings?" or "are those claims audit-defensible?" The pharmacy fills 200-400 prescriptions daily, some portion of which qualify for 340B pricing, but the TPA's summary report doesn't provide per-claim attribution. When the pharmacist wants to understand why 340B savings dropped 15% month-over-month, they cannot drill into claim-level data to determine whether it was patient eligibility changes, manufacturer restrictions, or TPA processing errors. This opacity is particularly dangerous during HRSA audits, where the pharmacy must defend individual claims.

## What Already Exists
Sentry Data Systems, Macro Helix, and Verity Solutions all provide TPA services: patient eligibility matching, virtual inventory management, replenishment coordination, and aggregate reporting. Their platforms are designed primarily for the covered entity's perspective (monitoring overall 340B savings and compliance), not the contract pharmacy's perspective (understanding per-claim margin and audit readiness). Some TPAs offer pharmacy-facing portals, but these show claim counts and total savings — not the per-claim breakdown with eligibility documentation.

## The Customization Gap
The gap is a pharmacy-facing analytics layer that sits on top of TPA data and PMS adjudication records to provide: (1) per-claim 340B attribution showing the eligibility basis (patient ID, provider, entity, date of service), the 340B acquisition cost vs. regular wholesale cost, and the resulting margin delta, (2) claim-level audit risk scoring based on eligibility strength (recently seen patient vs. patient not seen in 12+ months, established provider vs. newly added), (3) trend analysis showing 340B capture rate by payer, prescriber, and NDC — enabling the pharmacy to identify missed 340B opportunities, and (4) manufacturer restriction tracking with proactive alerts when new restrictions affect the pharmacy's 340B-eligible NDCs. This layer requires integrating TPA replenishment data, PMS claim records, and covered entity patient registry updates — data that exists in separate systems and must be merged for claim-level reconciliation. A standalone dashboard priced at $299-499/month fills this gap.

## Target Customer
Independent pharmacies with $50,000+ in annual 340B savings who rely on TPA-provided aggregate reports and have no per-claim visibility into eligibility, margin, or audit readiness.

## Impact If Solved
Gives pharmacies per-claim 340B margin visibility for the first time, enabling identification of missed 340B opportunities (typically 5-15% of eligible claims are not captured), detection of TPA processing errors, and proactive audit preparation. Pharmacies with claim-level visibility report identifying $10,000-30,000/year in missed 340B savings and significantly reducing audit preparation time from weeks to hours.
