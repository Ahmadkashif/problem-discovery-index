# Niche Analysis — Payment Fraud Vendors

**Parent Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]

## Niche Selection

This category runs mature ensemble modelling over device, behavioural, network and consortium signals, and trains it on chargebacks — which exist only for transactions that were approved. The decisions the model made to decline are the ones it will never learn from, which makes every published accuracy number a statement about a population the model itself selected. False declines are estimated to exceed actual fraud losses across card-not-present commerce and are largely never measured directly. The evidence that would fix it is neither exotic nor expensive, and almost nobody runs it, because the cost of the experiment is visible and immediate while the bias it corrects is invisible and permanent. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Fraud Decisioning | 🔵 High Market Share | ~$2.4B | High | Risk and data leadership |
| 2 | Chargeback Representment | 🔵 High Market Share | ~$1.4B | Low | Dispute operations leadership |
| 3 | Merchant Onboarding & Cold Start | 🟠 Low Digitized | ~$1.0B | Low | Onboarding and data leadership |
| 4 | Rules & Policy Operations | 🟠 Low Digitized | ~$700M | Low | Risk strategy leadership |
| 5 | The Review Analyst | 🟣 Underserved Audience | ~$600M | Low | Review operations leadership |
| 6 | The Risk Strategist | 🟣 Underserved Audience | ~$400M | Low | Risk leadership |
| 7 | Consortium Signal Sharing | ⚡ Highly Automatable | ~$300M | Medium | Network and data leadership |
| 8 | Good-Customer Recovery | ⚡ Highly Automatable | ~$200M | Very Low | Merchant success leadership |

## Why These Niches

Fraud decisioning takes the largest share because it is the product and because its evidence base is structurally incomplete. Representment is second because the chargeback is the label, the loss and a whole operation in itself. The two low-digitized niches are the ones still done by hand: every new merchant teaching a model a new definition of normal from scratch, and a rule set edited in response to whichever loss or complaint arrived most recently. The two underserved audiences are the analyst making irreversible decisions about strangers in forty seconds, and the strategist moving thresholds without being able to measure either direction. The two automatable niches are the consortium signal nobody pools well and the good customer who was declined and never came back.

## Niches

- [[niches/payment-fraud-vendors/fraud-decisioning/profile|🔵 Fraud Decisioning]]
  - [[niches/payment-fraud-vendors/counterfactual-labels/profile|🎯 Counterfactual Label Acquisition]]
  - [[niches/payment-fraud-vendors/decision-modelling/profile|🎯 Decision Modelling]]
- [[niches/payment-fraud-vendors/chargeback-representment/profile|🔵 Chargeback Representment]]
- [[niches/payment-fraud-vendors/merchant-onboarding-cold-start/profile|🟠 Merchant Onboarding & Cold Start]]
- [[niches/payment-fraud-vendors/rules-and-policy-operations/profile|🟠 Rules & Policy Operations]]
- [[niches/payment-fraud-vendors/the-review-analyst/profile|🟣 The Review Analyst]]
- [[niches/payment-fraud-vendors/the-risk-strategist/profile|🟣 The Risk Strategist]]
- [[niches/payment-fraud-vendors/consortium-signal-sharing/profile|⚡ Consortium Signal Sharing]]
- [[niches/payment-fraud-vendors/good-customer-recovery/profile|⚡ Good-Customer Recovery]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Fraud Decisioning is not: the label names the product's function rather than a contest, and writing the contested statement produces two sentences whose winners are different companies. Counterfactual label acquisition asks how to obtain honest outcomes in the region the model declines — an experimental design and commercial courage problem, where the winner is whoever is willing to pay a visible short-term cost to buy unbiased evidence nobody else has. Decision modelling asks how to build the best decision from the signals available — a conventional modelling contest over device, behavioural, network and consortium features, where the winner is whoever models best on whatever labels exist. One is buying evidence and the other is using it, and the first is a commercial decision made by an executive while the second is a technical one made by a data team. It therefore decomposes into **Counterfactual Label Acquisition** and **Decision Modelling**.

Two candidates were considered and rejected. **Identity verification at account opening** shares signals but the contest over it belongs to [[industries/identity-verification-vendors|Identity Verification Vendors]]. **Authorisation performance and routing** determines many declines that are not fraud decisions at all and is the contest of [[industries/payment-processors|Payment Processors]].
