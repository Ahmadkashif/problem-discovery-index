# The Adjustment Ledger Nobody Queries

**Niche:** [[niches/investment-banking-boutiques/quality-of-earnings-providers/profile|Quality of Earnings & Financial Due Diligence Providers]]
**Industry:** [[industries/investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A transaction advisory practice has proposed tens of thousands of EBITDA adjustments across its engagements and cannot say which kinds the other side accepted.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #evaluation-metrics #feature-engineering #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious QoE provider is fighting to deliver an adjusted EBITDA that survives the other side's diligence inside the banker's timetable — and whoever can show, from its own engagement record, which adjustments hold up takes the next mandate from the same sponsors and bankers.

## The Problem
Each QoE starts from the target's trial balance and walks to adjusted EBITDA through a schedule of diligence and management adjustments — owner compensation, non-recurring legal costs, pro-forma pricing, run-rate cost savings. A senior manager's judgment about which adjustments will survive a buyer's review is the core of the product and is tacit: they "know" a run-rate synergy add-back on a services business will be haircut, and an analyst two years in does not.

The outcome of every adjustment is observable — the buyer-side QoE, the LOI-to-close price bridge, the working capital true-up, sometimes a post-close dispute — and none of it is captured in a form the practice can query.

## Why Nobody Has Built This
Working papers are engagement-shaped, stored per client in audit-style file systems, with adjustments as free-text lines in Excel schedules. Outcomes arrive weeks or months later and often only through the banker. And professional confidentiality makes firms cautious about any cross-engagement reuse, even internal and de-identified.

## What to Build
A de-identified adjustment ledger: every proposed adjustment classified into a standard taxonomy by a language model, with amount relative to EBITDA, sector, deal size and side, joined where available to the counterparty's treatment and the price bridge. On top, an acceptance model that flags likely-contested adjustments as a draft QoE is assembled, with the firm's own precedents as evidence. All within the firm, never disclosed outside it.

## Target Customer
Transaction advisory services leaders at national accounting firms and mid-market diligence specialists.

## Impact If Built
Fewer re-trades on deals the firm's reports underpin, faster junior ramp-up, and a quantified quality claim in a market where every provider sells on reputation.
