# Wave 1 — Mainframe & Batch (1955–1975)

**Trigger:** ERMA unveiled Sept 1955, in production at Bank of America Sept 14 1959; MICR/E-13B adopted as the national banking standard by the ABA in 1956; SABRE built 1957–60, first live 1960, nationwide 1964
**What went to ~zero:** the cost of doing arithmetic over an entire customer file
**Failure class produced:** the missing join — in its purest and most innocent form

## What Was True The Day Before

Every large business kept its record of itself on paper, and the record could only be consulted one customer at a time. A bank knew what was in your account because a clerk looked it up. An airline knew whether a seat was free because someone in a room in another city read a card off a rack and said so over the phone. An insurer knew what it had underwritten because the policy was in a drawer.

The binding constraint was not that nobody could compute — actuaries and clerks computed constantly. It was that computation scaled linearly with people, so the *whole file* was never looked at. Businesses were run off samples and instinct because the population was unreachable.

## The Trigger

Bank of America was drowning in cheques. ERMA, built by SRI, was the answer, and its decisive invention was not the computer but **MICR** — the magnetic ink line along the bottom of a cheque. That line made a piece of paper machine-readable, which is the actual breakthrough: the physical world got a handle the machine could grip.

American Airlines and IBM did the same thing for seats. SABRE's achievement was not speed but **a single authoritative copy** of inventory that many distant terminals could read and modify without contradicting each other.

## What Became Possible

Overnight, an institution could touch every record it held. This sounds modest. It changed what a business could *be*: pricing off the whole book instead of a rule of thumb, dividends computed per policy, reconciliation at population scale, and — with SABRE — selling a perishable inventory item to the last minute without overselling it.

## The Competitive Fight

The fight was over **transaction volume you could serve without hiring**. Whoever could clear more cheques, book more seats or administer more policies at fixed headcount could price below competitors and take share. This is the original operating-leverage argument, and every SaaS pitch since is a restatement of it.

## What It Broke

Batch. The machine was expensive, so it ran overnight in one pass, and the whole enterprise arranged itself around a nightly cycle. That cycle is still here: card and ACH settlement windows, the "it'll show up tomorrow" of core banking, the reconciliation file that arrives after the decision it should have informed.

Crucially, **ACH inherited batch rather than choosing it** — it was designed as an electronic replacement for paper cheque clearing, which was already an overnight batch process. No one sat down and decided that money should move slowly.

This is the first and cleanest **missing join**: the result of a decision and the decision itself end up in different systems on different clocks, and nobody joins them. Not because anyone benefits — simply because the architecture separated them and the separation outlived its reason.

*(Correction carried from research: "T+2" is a securities-settlement term — US equities moved to T+1 in May 2024 — and does **not** describe card or ACH batch cycles. Do not use it for this wave. See `series/_plan.md` §5.)*

## Children in This Vault

**Primary:**
- [[industries/collections-agencies|Collections Agencies]]
- [[industries/credit-unions|Credit Unions]]
- [[industries/independent-insurance-agents|Independent Insurance Agents]]
- [[industries/wealth-management-rias|Wealth Management RIAs]]
- [[industries/payment-processors|Payment Processors]]
- [[industries/medical-billing|Medical Billing]]
- [[industries/payroll-platforms|Payroll Platforms]]
- [[industries/hotels-boutique|Boutique Hotels]]
- [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
- [[industries/municipal-services|Municipal Services]]

**Secondary:**
- [[industries/crypto-exchanges|Crypto Exchanges]]
- [[industries/payment-fraud-vendors|Payment Fraud Vendors]]

**Origins:** [[origins/airlines/profile|Airlines]] · [[origins/retail-banking/profile|Retail Banking]] · [[origins/insurance-carriers/profile|Insurance Carriers]] · [[origins/exchanges-market-makers/profile|Exchanges & Market Makers]]

**Sources:** SRI International (ERMA); Wikipedia, *Electronic Recording Machine, Accounting*; historyofinformation.com; ABA MICR/E-13B adoption 1956; ethw.org and IBM corporate history (SABRE); Computer History Museum Revolution exhibit (SABRE nationwide 1964); Federal Reserve History, *Automated Clearing House*; NACHA, *History of Nacha and the ACH Network*.
