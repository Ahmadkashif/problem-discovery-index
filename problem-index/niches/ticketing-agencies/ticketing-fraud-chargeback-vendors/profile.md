# Ticketing Payment Fraud & Chargeback Vendors

**Parent Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Fraud-decisioning and chargeback vendors that sell to ticketers and resale marketplaces among other merchants: Riskified, Forter and Signifyd for checkout decisions and chargeback guarantees, Chargebacks911 and Justt for dispute representment, and the card networks' alert services (Verifi, Ethoca). Ticketing is a valued vertical for them because high-demand onsales attract stolen cards and cancellations produce dispute waves.

## Insight Function
**Size:** 20-100 data scientists and risk analysts per vendor across all verticals, a fraction of them on ticketing (estimate)
**Output:** Approve or decline decisions, chargeback guarantees, dispute responses, fraud trend reports used as marketing
**Proprietary data:** Cross-merchant transaction, device and dispute outcomes, including ticketing onsales
**Clock:** Card-network dispute response deadlines on every representment case
**Buyer:** Head of data science or chief risk officer at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 4 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 4 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **38/60** |

**Kill switches:** none live. Merchants supply transaction and outcome data on terms that give the vendor rights to use it in its models and network, which is the basis of the product. This is the same ruling as [[niches/credit-card-issuers/synthetic-identity-fraud-consortia/profile|🔍 Synthetic Identity & First-Party Fraud Consortia]] and as this industry's bot-mitigation pocket, where aggregated signals are treated as the vendor's own.
**Verdict:** Logged — below threshold. Q4 stays at 4: network deadlines bind each representment case, but the fraud models and research are continuous, so no outside date governs the insight work itself. The invoice is the decision or the guarantee, not the analysis, and a handful of vendors serve ticketing. The vendor-side workflow is analysed in the vault as [[niches/payment-fraud-vendors/chargeback-representment/profile|Chargeback Representment]] under Payment Fraud Vendors, and the issuers' outsourced dispute operations fail the gate as [[niches/credit-card-issuers/dispute-back-office-outsourcers/profile|🔍 Dispute & Fraud Back-Office Outsourcers]]. Ticketing adds the cancellation-driven dispute, a friendly-fraud case that fraud models built for stolen cards handle badly.
