# Neobanks

## Profile
**Category:** Fintech
**Market Size:** ~$10B US revenue across consumer digital banking challengers, dominated by interchange and a widening interest-income base
**Tech Maturity:** Modern at the surface, borrowed underneath — Chime, Varo, Current, Dave, Cash App and SoFi run excellent mobile products on top of a core provider (Galileo, Marqeta, i2c, Q2) and, in most cases, a sponsor bank's charter. The decisioning that matters — who is approved, whose account is frozen, whose deposit is held — is a mixture of vendor scores, purchased rules and internally tuned thresholds, almost none of which is evaluated against what actually happened.
**Workforce:** Risk and fraud analysts, BSA/AML compliance staff, dispute and Reg E specialists, member support agents, sponsor-bank relationship managers, data scientists, mobile and backend engineers

## Key Pain Themes
The defining tension is that a neobank holds a customer's entire financial life — direct deposit, balance, rent, groceries — while carrying fraud exposure that a branch network would have absorbed through friction. The response is automated risk decisioning, and the response to automated risk decisioning is the account freeze: funds locked, card declined, a form letter citing the deposit agreement. Some of those accounts are fraudulent. Many are not, and the institution never finds out which, because a closed account produces no further evidence and a reinstated one is not recorded as a model error.

Underneath it sits the sponsor-bank relationship, which after the 2023–24 consent orders against Blue Ridge, Choice, Evolve and Lineage became the binding constraint on every product decision. Compliance reporting is built bespoke to each bank partner's expectations. Disputes run against Reg E clocks that do not care how large the queue is. And the front line — the support agent a member reaches — can see that the account is restricted and cannot see why, because the reason codes live in a risk system the agent has no access to.

## Current Tech Landscape
Core banking is outsourced to Galileo, Marqeta, i2c or Q2 Helix; ledger and card issuing come with it. Fraud and identity are bought — Socure, Sardine, Unit21, Alloy, Sift, Prove — and stacked, each vendor scoring a slice. Transaction monitoring runs on Unit21, Hummingbird or the sponsor bank's own system. Disputes are handled in Quavo, Pega or something homegrown. Data sits in Snowflake or BigQuery with dbt on top and a BI layer nobody in risk operations uses during a shift. The stack is capable of recording every decision and every outcome; almost nowhere are the two tables joined.

## Problems
- [[problems/neobanks/high-impact|🔴 High Impact: The Account Freeze Nobody Grades]]
- [[problems/neobanks/low-impact-1|🟡 Low Impact: Sponsor Bank Compliance Reporting]]
- [[problems/neobanks/low-impact-2|🟡 Low Impact: Reg E Dispute Processing]]
- [[problems/neobanks/worker-life-1|🟢 Worker Life: The Risk Analyst Clearing the Freeze Queue]]
- [[problems/neobanks/worker-life-2|🟢 Worker Life: The Support Agent Who Cannot See the Reason]]
- [[problems/neobanks/ml-opportunity|🧠 ML Opportunities]]
- [[problems/neobanks/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A neobank makes several million consequential predictions a year — approve, decline, hold, freeze, reimburse — and observes the consequence of nearly all of them in its own ledger. Deposits resume or they do not. The disputed transaction is represented or written off. The frozen account is reinstated or closed. That is a labelled dataset assembling itself continuously inside the institution, and it is the one dataset nobody constructs, because the decision lives in a vendor's system, the outcome lives in operations, and no team owns the join. The competitive question in consumer fintech is no longer distribution; it is which institution can tell the difference between a fraudster and a customer having a bad month, and that is a measurement problem before it is a modelling one.
