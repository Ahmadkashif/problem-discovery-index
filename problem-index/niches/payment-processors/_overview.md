# Niche Analysis — Payment Processors

**Parent Industry:** [[industries/payment-processors|Payment Processors]]

## Niche Selection

These businesses run globally distributed authorisation infrastructure at four or five nines and then make the decisions that determine merchant revenue with static configuration files. A large processor observes something no issuer and no merchant can — the same cardholder across thousands of merchants being approved and declined by hundreds of issuers, with the settlement outcome of every attempt — and uses it mainly for billing. The competitive frontier has moved from price to authorisation performance, and authorisation performance is a prediction problem the industry treats as a configuration problem. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Authorisation Performance | 🔵 High Market Share | ~$36B | Low | Payments product and merchant leadership |
| 2 | Merchant Underwriting | 🔵 High Market Share | ~$22B | Low | Risk and onboarding leadership |
| 3 | Settlement & Reconciliation | 🟠 Low Digitized | ~$16B | Low | Finance operations leadership |
| 4 | Fee & Interchange Optimisation | 🟠 Low Digitized | ~$12B | Low | Merchant finance and processor commercial teams |
| 5 | The Underwriter | 🟣 Underserved Audience | ~$10B | Low | Risk operations leadership |
| 6 | The Integration Engineer | 🟣 Underserved Audience | ~$9B | Low | Developer support leadership |
| 7 | Network Outcome Intelligence | ⚡ Highly Automatable | ~$10B | Very Low | Processor data leadership |
| 8 | Fraud & Chargeback Decisioning | ⚡ Highly Automatable | ~$5B | Medium | Risk and merchant leadership |

## Why These Niches

Authorisation performance takes the largest share because it is the single number that decides whether a merchant stays and because the processor controls only part of it. Underwriting is second because every acquirer independently rebuilds the same verification against the same registries and grades it against losses it never attributes back. The two low-digitized niches are where the money physically moves and is priced: a reconciliation done by people with spreadsheets, and an interchange structure that determines merchant cost and is navigated by convention. The two underserved audiences are the underwriter deciding a business's fate under a clock and the support engineer debugging somebody else's checkout from a screenshot. The two automatable niches are the network-scale outcome record used for billing and the fraud decisioning that sits on top of it.

## Niches

- [[niches/payment-processors/authorisation-performance/profile|🔵 Authorisation Performance]]
  - [[niches/payment-processors/decline-recovery/profile|🎯 Decline Recovery]]
  - [[niches/payment-processors/routing-and-network-optimisation/profile|🎯 Routing & Network Optimisation]]
- [[niches/payment-processors/merchant-underwriting/profile|🔵 Merchant Underwriting]]
- [[niches/payment-processors/settlement-and-reconciliation/profile|🟠 Settlement & Reconciliation]]
- [[niches/payment-processors/fee-and-interchange-optimisation/profile|🟠 Fee & Interchange Optimisation]]
- [[niches/payment-processors/the-underwriter/profile|🟣 The Underwriter]]
- [[niches/payment-processors/the-integration-engineer/profile|🟣 The Integration Engineer]]
- [[niches/payment-processors/network-outcome-intelligence/profile|⚡ Network Outcome Intelligence]]
- [[niches/payment-processors/fraud-and-chargeback-decisioning/profile|⚡ Fraud & Chargeback Decisioning]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Authorisation Performance is not: the label names an outcome metric rather than a contest, and writing the contested statement produces two sentences describing different winners. Decline recovery asks what to do after an issuer says no — whether to retry, when, how many times, and whether to refresh the credential — which is a prediction problem over decline codes, issuer behaviour and timing. Routing and network optimisation asks how to present the transaction in the first place — which acquiring route, which network, which token, which authentication path, what data to include — which is a network relationship and infrastructure contest decided before the decline happens. One acts on a failure, the other prevents it; one is modelling and the other is routing and partnership. It therefore decomposes into **Decline Recovery** and **Routing & Network Optimisation**.

Two candidates were considered and rejected. **The card networks themselves** set the rules this category operates under, but they are a different kind of participant rather than a niche here. **Issuing and banking-as-a-service** shares infrastructure but is the contest of [[industries/embedded-finance-platforms|Embedded Finance Platforms]], where it is analysed on its own terms.
