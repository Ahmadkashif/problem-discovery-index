# PSAO Dashboard with Contract Comparison and DIR Fee Modeling

**Niche:** [[niches/pharmacy-independents/dir-fee-pbm-optimization/profile|DIR Fee & PBM Optimization]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PSAOs negotiate PBM contracts on behalf of independent pharmacies, but member pharmacies have minimal visibility into how their PSAO's terms compare to alternatives — and cannot model the financial impact of switching PSAOs or renegotiating specific contract provisions.
**Tags:** #data-integration #feature-engineering #revenue-impact #quick-win

## The Problem
Independent pharmacies join PSAOs (Pharmacy Services Administrative Organizations) to access PBM contracts with better reimbursement rates and DIR fee terms than they could negotiate individually. There are 10-15 major PSAOs (Innovatix, APCI, LeaderNET, Keystone, ProCare), each negotiating separate contracts with each PBM. A pharmacy's total PBM reimbursement and DIR fee exposure depends heavily on which PSAO they belong to — but pharmacies cannot compare PSAO terms side-by-side because: (1) contract terms are confidential between the PSAO and PBM, (2) PSAOs share aggregate performance data but not the specific reimbursement formulas or DIR fee tier structures, and (3) pharmacies lack the analytical tools to model how their specific prescription mix and performance metrics would perform under a different PSAO's contract. A pharmacy generating $1.2M in annual reimbursement might save $30,000-80,000 by switching PSAOs — but has no way to quantify this without actually switching and waiting a year to see the results.

## What Already Exists
PSAO member portals show aggregate performance metrics, DIR fee assessments, and basic financial summaries. Some PSAOs provide quarterly performance reports comparing the member pharmacy to PSAO averages. PBM portals show claim-level reimbursement data. Third-party consultants (pharmacy brokers) offer PSAO evaluation services, but charge $5,000-15,000 per analysis and rely on self-reported data from PSAOs rather than independent modeling.

## The Customization Gap
The gap is a pharmacy-facing analytics platform that: (1) ingests the pharmacy's actual claim-level adjudication data (payer, NDC, reimbursement, acquisition cost), (2) applies known or estimated contract terms from multiple PSAOs to model what the pharmacy would have been reimbursed under each PSAO's contracts, (3) models DIR fee exposure under each PSAO's performance tier structure based on the pharmacy's actual quality metrics, (4) produces a side-by-side financial comparison showing estimated annual reimbursement, DIR fee exposure, and net margin under each PSAO option, and (5) identifies specific contract provisions (GER rates, brand reimbursement, specialty drug handling) that drive the largest financial differences. This requires building a contract term database (assembled from pharmacy-contributed data, public PSAO disclosures, and reverse-engineering from claim-level reimbursement patterns) — a data asset that becomes more valuable as more pharmacies contribute. Priced at $199-399/month or offered as a free tool by PSAOs seeking to recruit members.

## Target Customer
Independent pharmacy owners evaluating whether their current PSAO membership is optimal, and pharmacies considering switching PSAOs but unable to quantify the financial impact without real data.

## Impact If Solved
Enables pharmacies to make data-driven PSAO membership decisions for the first time, potentially recovering $20,000-80,000/year in improved reimbursement and reduced DIR fees. Creates competitive pressure among PSAOs to offer better terms, benefiting all independent pharmacies. Reduces pharmacy reliance on expensive consultants for contract evaluation.
