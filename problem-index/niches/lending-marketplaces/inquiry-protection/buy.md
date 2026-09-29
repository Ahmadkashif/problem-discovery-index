# Prequalification and Soft-Pull Infrastructure

**Niche:** [[niches/lending-marketplaces/inquiry-protection/profile|Inquiry Protection]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Soft-pull prequalification and prescreen infrastructure exist and work, and marketplaces use them inconsistently because nothing forces the choice.
**Tags:** #compliance #data-integration #evaluation-metrics #automation #workflow-orchestration #confidence-intervals #logistic-regression #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to stop spending the borrower's credit file on applications that will be declined — and whoever treats the inquiry as a cost rather than as free takes the trust the category has never had.

## The Problem
The infrastructure to check eligibility without a hard inquiry exists: soft-pull credit access, prequalification APIs, prescreen and firm offer of credit programmes, and the regulatory framework governing all of them. Many lenders support prequalification. The marketplace uses it where it is convenient rather than where it would help, because nothing in its objective function values the difference.

## What Already Exists
Soft-pull credit access and prequalification APIs; prescreen and firm offer of credit programmes; bureau prequalification products; rate-shopping window conventions; and the disclosure framework around all of it.

## The Customization Gap
The adaptation is orchestrating prequalification across many lenders for one borrower. It requires: (1) a routing layer that prefers prequalifying lenders where outcomes are comparable, which is a ranking change rather than an integration and is the substantive adaptation; (2) reconciliation of prequalified offers that differ from final terms, since a prequalification is not a commitment and borrowers reasonably treat it as one; (3) sequencing logic across lenders, as the infrastructure is built per lender and nobody orchestrates the set; (4) commercial terms that do not penalise the marketplace for fewer applications, which is the incentive problem underneath; and (5) disclosure that explains soft versus hard pulls in terms a borrower understands.

## Target Customer
Product and compliance leadership, lenders offering prequalification, bureaus supplying the infrastructure, and consumer advocates examining the category.

## Impact If Solved
The infrastructure exists and is used where convenient rather than where it helps. Making the routing layer prefer prequalifying lenders is a ranking change that removes most of the borrower's cost.
