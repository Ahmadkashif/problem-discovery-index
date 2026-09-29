# Niche Analysis — Crypto Exchanges

**Parent Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]

## Niche Selection

A centralised exchange runs a matching engine capable of enormous throughput and makes its most consequential customer decisions — freeze this deposit, close this account, file this report — from a third-party address risk score and an analyst's judgement. It sits at the only junction in the crypto landscape where a public, complete, permanent ledger meets verified real-world identity, generates the labels the analytics vendors sell, and buys them back as a scored feed. Ground truth on the control its whole compliance posture rests on almost never returns, so its precision has never been measured. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Deposit Screening | 🔵 High Market Share | ~$3.8B | Medium | Exchange compliance leadership |
| 2 | Custody & Key Operations | 🔵 High Market Share | ~$3.2B | High | Exchange security and custody leadership |
| 3 | Tax Basis & Reporting | 🟠 Low Digitized | ~$1.7B | Low | Exchange tax and product leadership |
| 4 | Token Listing Diligence | 🟠 Low Digitized | ~$1.4B | Very Low | Listings and legal leadership |
| 5 | The Blockchain Analyst | 🟣 Underserved Audience | ~$1.3B | Low | Compliance operations leadership |
| 6 | Market Operations On Call | 🟣 Underserved Audience | ~$1.2B | Medium | Exchange engineering leadership |
| 7 | Cross-Exchange Attribution | ⚡ Highly Automatable | ~$1.4B | Very Low | Exchange data and compliance leadership |
| 8 | Account Recovery | ⚡ Highly Automatable | ~$1.0B | Low | Support and risk leadership |

## Why These Niches

Deposit screening takes the largest share because it is the decision that touches every customer's money and the one nobody has evaluated. Custody is second because key compromise is the failure that ends an exchange and proof of reserves is the demand the category cannot refuse. The two low-digitized niches are the ones still done by hand: cost basis reconstructed for assets that arrived from somewhere else, now a legal obligation under 1099-DA, and token diligence redone independently by every venue for every asset. The two underserved audiences are the analyst tracing funds one hop at a time in a vendor's interface, and the engineer on call for a market that never closes with alerting that cannot distinguish a market event from a bug. The two automatable niches are the attribution asset the exchanges generate and rent back, and the locked-account queue that dominates support.

## Niches

- [[niches/crypto-exchanges/deposit-screening/profile|🔵 Deposit Screening]]
  - [[niches/crypto-exchanges/address-attribution/profile|🎯 Address Attribution & Taint Propagation]]
  - [[niches/crypto-exchanges/screening-decision-quality/profile|🎯 Screening Decision Quality]]
- [[niches/crypto-exchanges/custody-and-key-operations/profile|🔵 Custody & Key Operations]]
- [[niches/crypto-exchanges/tax-basis-and-reporting/profile|🟠 Tax Basis & Reporting]]
- [[niches/crypto-exchanges/token-listing-diligence/profile|🟠 Token Listing Diligence]]
- [[niches/crypto-exchanges/the-blockchain-analyst/profile|🟣 The Blockchain Analyst]]
- [[niches/crypto-exchanges/market-operations-on-call/profile|🟣 Market Operations On Call]]
- [[niches/crypto-exchanges/cross-exchange-attribution/profile|⚡ Cross-Exchange Attribution]]
- [[niches/crypto-exchanges/account-recovery/profile|⚡ Account Recovery]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Deposit Screening is not: the label names a function on the customer journey rather than a contest, and writing the contested statement produces two sentences with different winners. Address attribution asks who actually controls an address and how far taint legitimately travels through a public ledger — a graph inference problem over contested heuristics, where the winner is whoever attributes most accurately and can say how confident they are. Screening decision quality asks whether the control works at all: how to measure precision when ground truth returns on a fraction of a percent of cases, how to set a threshold without knowing the error rate, and how to explain a freeze to the customer whose money it is. One is inference about the chain and the other is evaluation and adjudication of a decision, and they are built by different people against different evidence. It therefore decomposes into **Address Attribution & Taint Propagation** and **Screening Decision Quality**.

Two candidates were considered and rejected. **Onboarding identity verification** is real work here but the contest over it belongs to [[industries/identity-verification-vendors|Identity Verification Vendors]]. **Stablecoin and payment rails** running through these venues are the contest of [[industries/payment-processors|Payment Processors]], where settlement and authorisation are analysed on their own terms.
