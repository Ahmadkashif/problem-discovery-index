# Telecom Carriers

**Layer:** Origin — a parent industry, not a prospect
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]] → [[series/eras/wave-07-big-data|7 — Big Data]]
**Founding event:** OSS/BSS billing industrialised through the 1990s; **Mozer et al., churn prediction on ~47,000 wireless subscribers, NeurIPS 1999 / IEEE Trans. Neural Networks 2000**
**Children in this vault:** crm-platforms, customer-support-platforms, subscription-commerce, streaming-video-platforms, membership-community-platforms, and every retention model in the index

## Profile

**What it is:** The provision of voice and, later, data connectivity to a subscriber base, billed on a recurring or metered basis. A telecom carrier's product is invisible when it works and its business is, underneath, an extremely large accounting problem: correctly rating and billing every call, every subscriber, every month, at a volume no other industry faced this early.

**Who pays:** Subscribers, on a contract that renews itself unless someone actively leaves it. That renewal default is the whole story of this origin — it is the first industry where a customer's *continued* custom, rather than their next purchase, was the thing worth modelling.

**The economics:** High fixed infrastructure cost, low marginal cost per additional subscriber, and — once the Bell System's monopoly ended — a subscriber who could leave for a competitor with a phone call and a new contract. That combination made **churn**, not acquisition, the number that decided who made money.

## Why This Is an Origin

Telecom built the plumbing — OSS (operations support systems) and BSS (business support systems) — that rated and billed calls at a scale no other consumer business approached in the 1980s and 1990s. But the more consequential thing built on top of that plumbing is this origin's subject: one of the earliest documented, named, production-scale applications of statistical machine learning to predict an individual customer's future behaviour and act on it before it happened. Every propensity-to-churn, propensity-to-upgrade and lifetime-value model in this vault is a descendant of that idea.

## The Contested Decision

> **Which subscribers are about to leave, and what does it cost to keep them versus losing them?**

Get the first half wrong and you either waste retention budget on customers who were never leaving, or lose customers you never flagged. Get the second half wrong and you overpay to keep someone who was never worth the discount.

## The Files

- [[origins/telecom-carriers/origin-story|Origin Story]] — billing at scale, and why churn became a number worth modelling
- [[origins/telecom-carriers/the-fight|The Fight]] — deregulation creates a subscriber who can leave
- [[origins/telecom-carriers/the-mechanism|The Mechanism]] — what the Mozer team actually built
- [[origins/telecom-carriers/legacy|Legacy]] — the retention model, everywhere

**Sources:** Mozer, Wolniewicz, Grimes, Johnson & Kaushansky, *Predicting Subscriber Dissatisfaction and Improving Retention in the Wireless Telecommunications Industry*, IEEE Trans. Neural Networks 11(3), 2000 (NeurIPS 1999 precursor); *United States v. AT&T* (1982) and the Modified Final Judgment, effective Jan 1 1984; Wikipedia, *Advanced Mobile Phone System*.
