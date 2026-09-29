# Niche Analysis — Neobanks

**Parent Industry:** [[industries/neobanks|Neobanks]]

## Niche Selection

A neobank makes several million consequential predictions a year — approve, decline, hold, freeze, reimburse — and observes the consequence of nearly all of them in its own ledger. That is a labelled dataset assembling itself continuously inside the institution, and it is the one dataset nobody constructs, because the decision lives in a vendor's system, the outcome lives in operations, and no team owns the join. Around it sit a sponsor-bank relationship that became the binding constraint on every product decision, a dispute queue running against clocks that do not care about volume, and two front-line roles absorbing the consequences. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Risk Decisioning | 🔵 High Market Share | ~$2.8B | High | Risk and product leadership |
| 2 | Deposit & Interchange Economics | 🔵 High Market Share | ~$1.5B | Medium | Commercial and product leadership |
| 3 | Sponsor Bank Compliance | 🟠 Low Digitized | ~$1.2B | Low | Compliance and partnership leadership |
| 4 | Disputes & Reg E Operations | 🟠 Low Digitized | ~$1.0B | Low | Operations and compliance leadership |
| 5 | The Risk Analyst | 🟣 Underserved Audience | ~$900M | Low | Risk operations leadership |
| 6 | The Support Agent | 🟣 Underserved Audience | ~$800M | Low | Member support leadership |
| 7 | Decision Outcome Measurement | ⚡ Highly Automatable | ~$1.3B | Very Low | Risk and data leadership |
| 8 | Cash-Flow Intelligence | ⚡ Highly Automatable | ~$500M | Low | Product leadership |

## Why These Niches

Risk decisioning takes the largest share because it determines who is approved, whose account is frozen and whose deposit is held, and because the competitive question in consumer fintech is which institution can tell the difference between a fraudster and a customer having a bad month. Deposit and interchange economics is second because it decides whether a neobank holds a primary relationship or a secondary card. The two low-digitized niches are the ones where the regulatory environment has real teeth and the tooling has none: a compliance pack rebuilt per sponsor bank, and a dispute queue running against clocks that do not adjust for volume. The two underserved audiences are the analyst deciding from a screenshot whether a stranger can reach their own wages and the agent apologising for a decision they cannot see. The two automatable niches are the labelled dataset nobody assembles and the cash-flow picture the institution holds and does not use.

## Niches

- [[niches/neobanks/risk-decisioning/profile|🔵 Risk Decisioning]]
  - [[niches/neobanks/onboarding-identity-decisioning/profile|🎯 Onboarding & Identity Decisioning]]
  - [[niches/neobanks/ongoing-account-risk/profile|🎯 Ongoing Account Risk]]
- [[niches/neobanks/deposit-and-interchange-economics/profile|🔵 Deposit & Interchange Economics]]
- [[niches/neobanks/sponsor-bank-compliance/profile|🟠 Sponsor Bank Compliance]]
- [[niches/neobanks/disputes-and-reg-e/profile|🟠 Disputes & Reg E Operations]]
- [[niches/neobanks/the-risk-analyst/profile|🟣 The Risk Analyst]]
- [[niches/neobanks/the-support-agent/profile|🟣 The Support Agent]]
- [[niches/neobanks/decision-outcome-measurement/profile|⚡ Decision Outcome Measurement]]
- [[niches/neobanks/cash-flow-intelligence/profile|⚡ Cash-Flow Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Risk Decisioning is not: the label names a function rather than a contest, and writing the contested statement produces two sentences describing different winners. Onboarding decisioning judges a stranger from third-party identity data, device signals and a document, with no behavioural history and a heavy application-fraud adversary — a data-vendor and identity contest. Ongoing account risk judges an existing customer from the institution's own ledger, where the adversary is different, the evidence is behavioural and abundant, and the error is freezing someone's wages rather than declining an application. Different data, different adversaries, different consequences, and visibly different vendors serve each. It therefore decomposes into **Onboarding & Identity Decisioning** and **Ongoing Account Risk**.

Two candidates were considered and rejected. **Card issuing and core banking infrastructure** is the layer these institutions run on, and the contest over it belongs to [[industries/embedded-finance-platforms|Embedded Finance Platforms]] and [[industries/payment-processors|Payment Processors]]. **Credit underwriting** is adjacent and increasingly present in these products, but it is the contest of [[industries/lending-marketplaces|Lending Marketplaces]], where it is analysed on its own terms.
