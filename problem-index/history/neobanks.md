# History: Neobanks

**Industry:** [[industries/neobanks|Neobanks]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Origin Parent:** [[origins/retail-banking/profile|Retail Banking]]
**Episode Tier:** 1
**Transferable Pattern:** A company can rebuild every part of a regulated product's interface and operations and still not own the one asset that determines whether it survives — and the asset it does not own is rarely the one its own roadmap is focused on.

## Before

Opening a bank account meant a branch, a signature, and a relationship with an institution that had itself been chartered by a state or federal regulator — a process [[origins/retail-banking/origin-story|retail banking's origin story]] traces to the same postwar decade that gave the industry ERMA and MICR. Chartering a *new* bank from scratch was never a software problem. It required capital (millions of dollars in reserves before a single deposit is taken), a multi-year federal or state application, and continuous supervision once running. That constraint predates every neobank in this vault and, as this file sets out, none of them has actually removed it. They have found ways to operate without clearing it themselves.

## The Origin Event

**Simple** — founded in Brooklyn in 2009 by Joshua Reich and Shamir Karkal as "BankSimple," funded from an initial $10M raise in August 2011, launched to a limited beta in 2012 — is the industry's own founding case, and its subsequent history is the argument this file makes. Simple never held a charter. It partnered first with U.S. Bancorp for FDIC-insured accounts, then moved to BBVA USA in 2016. BBVA had backed Simple's early funding round and bought the company outright on **20 February 2014 for $117 million**. That did not make Simple a bank; it made Simple a product sitting on top of a bank BBVA already owned.

The chain of custody matters more than the founding date. **PNC Financial Services completed its acquisition of BBVA USA on 1 June 2021.** Simple was formally closed on **8 May 2021** — weeks before that deal closed, folding remaining customers into BBVA's own checking and savings products. Public reporting does not establish that PNC ordered the shutdown as a condition of the deal; that Simple's charter host was sold and Simple ceased to exist almost simultaneously is a documented fact, and the inference that the two are connected is the industry's own plainest lesson, not an invented one.

## What Became Cheap

Cloud infrastructure and a layer of specialised middleware — core-ledger and card-issuing platforms such as Galileo and Marqeta, identity and fraud vendors such as Socure and Sardine — made it cheap, for the first time, to assemble the *operational appearance* of a bank: a mobile app, instant notifications, virtual and physical cards, categorised spending, early paycheck access. This is [[series/eras/wave-06-cloud-saas|Wave 6]]'s general story, applied to a regulated product. What did not become cheap, and has not, is the one component this stack cannot buy off a vendor's price list: the charter itself, and the FDIC insurance and supervisory relationship that come with it.

## How It Was Actually Solved — the sponsor-bank workaround

Every neobank in this vault's hub note — Chime, Varo (until 2020), Current, Dave, Cash App, SoFi (until 2019) — built its business on a **sponsor bank**: a small, chartered institution that holds the deposits and takes the regulatory exposure, while the neobank owns the brand, the app, and the customer relationship. Chime, the largest by users, is explicit about this on its own site: "Chime is not a bank." It routes deposits through Stride Bank and The Bancorp Bank, both nationally chartered, both far smaller than Chime itself.

The arrangement is not merely convenient; it is frequently the economic point. **Regulation II — the rule implementing the Durbin Amendment, described in this vault's [[origins/retail-banking/legacy|retail banking legacy file]] and its `history/payment-processors.md` sibling — caps debit interchange only for issuers holding $10 billion or more in assets.** A sponsor bank kept deliberately below that threshold earns uncapped interchange on every debit swipe its fintech partner generates, and shares it back. The smallness of the sponsor bank is not an accident of the model; in Regulation II's shadow, it is close to the model's reason for existing.

**In September 2026, Chime announced it would acquire Stride Bank outright for $590 million**, converting one of its two sponsor relationships into ownership — a live, current instance of a neobank moving to internalise the asset it had spent over a decade renting. Whether that changes the calculus above once Chime itself controls an asset large enough to matter for Regulation II is a question this vault cannot yet answer; the deal was announced to complete in 2027.

## The Binding Constraint

**The charter, not the interface, is what actually governs a neobank's fate**, and 2023–24 is when that stopped being a background fact and became an operating risk every sponsor-fintech relationship had to price in. The Federal Reserve issued a formal enforcement action against **Evolve Bank & Trust in June 2024**, citing deficiencies in anti-money-laundering programmes, risk management, and consumer compliance, and naming failure to manage fintech-partnership risk specifically. The **FDIC issued a cease-and-desist order against Cross River Bank in April 2023** over what it characterised as unsafe or unsound banking practices. Both banks are named, sizeable sponsors in the same BaaS ecosystem this industry's hub note describes.

Regulators cannot directly discipline Chime, Dave, or Cash App — none of them is a chartered depository. They can only reach the sponsor bank, which means the entire industry's compliance posture is downstream of institutions the fintech does not control and, in the consent-order cases above, was already failing at the job before the fintech's own customers noticed anything.

## The Graveyard

Two failures, at two different layers of the same rented stack, teach two different lessons.

**Simple** (2009–2021, above) shows what happens when the *charter relationship* itself is sold out from under the product. The app worked. The customers were satisfied. None of that mattered once the bank behind it changed hands.

**Synapse Financial Technologies** shows what happens when the *middleware* fails instead. Founded 14 April 2014 by Sankaet Pathak and Bryan Keltner, Synapse built the banking-as-a-service ledger connecting more than 100 fintech apps — including Yotta and Juno — to partner banks, serving an estimated 10 million end customers, and raised $51 million along the way. **Synapse filed for Chapter 11 bankruptcy in April 2024.** What followed was not a straightforward collapse but a reconciliation failure: former FDIC Chair Jelena McWilliams, appointed bankruptcy trustee, reported in May 2024 an estimated **$65–96 million gap** between Synapse's own ledger and its partner banks' records — nobody could say with confidence which of Synapse's ledger entries corresponded to real, held funds. Evolve, one of Synapse's partner banks, froze customer withdrawals for five months; reconciliation efforts formally concluded in October 2024 with tens of millions still unrecovered. By November 2024, data from a single downstream fintech, Yotta, showed 13,725 customers who had lost deposited funds receiving only $11.8 million in refunds against $64.9 million in deposits.

**This is the vault's missing join, made literal and made to hurt.** A ledger that says a customer's money exists, and a bank account that does not confirm it, are exactly the two tables `origins/retail-banking/legacy.md` describes never being joined — except here the two tables belong to two different companies, neither of which the customer ever chose or could see, and the gap between them was measured in tens of millions of dollars of somebody else's money.

## What's Still Open

- [[problems/neobanks/high-impact|🔴 High Impact: The Account Freeze Nobody Grades]] — the decision-outcome join this file's mechanism section describes, one layer up from Synapse's ledger gap
- [[niches/neobanks/sponsor-bank-compliance/profile|Sponsor Bank Compliance]] — every neobank rebuilding the same bespoke reporting pack per bank partner
- [[niches/neobanks/risk-decisioning/profile|Risk Decisioning]] and [[niches/neobanks/ongoing-account-risk/profile|Ongoing Account Risk]]
- [[niches/neobanks/decision-outcome-measurement/profile|Decision-Outcome Measurement]] — whether a freeze was ever right, written back to nothing
- [[niches/neobanks/disputes-and-reg-e/profile|Disputes & Reg E]]
- [[niches/neobanks/onboarding-identity-decisioning/profile|Onboarding & Identity Decisioning]]
- [[niches/neobanks/deposit-and-interchange-economics/profile|Deposit & Interchange Economics]] — the Regulation II arithmetic this file traces to the sponsor bank's balance sheet
- [[niches/neobanks/the-risk-analyst/profile|The Risk Analyst]] and [[niches/neobanks/the-support-agent/profile|The Support Agent]]

## The Transferable Pattern

> **Find the regulated or licensed asset the company itself does not hold, then ask who does, how small they are, and what happens to the product the day that relationship changes hands.** A neobank's app, its fraud models, its onboarding flow — all genuinely built, all genuinely its own — sit on top of a charter it rents from an institution most of its customers have never heard of. Simple died when its landlord was sold. Synapse's customers lost money when nobody could prove whose ledger was right. Both failures were invisible from inside the product roadmap, because the product roadmap was never where the risk lived.

An FDE evaluating any "X, but digital-first" business should ask this before anything about the technology: which licensed, regulated, or otherwise gate-kept asset does this company rent rather than own, and who is the landlord? That answer, not the app, is where the company's actual risk — and its actual valuation ceiling — sit.

**Sources:** Wikipedia, *Simple (bank)*, *BBVA USA*, *Synapse Financial Technologies*, *Chime (company)*, *Evolve Bank & Trust*, *Cross River Bank*, *Banking as a service*; Federal Reserve Board enforcement action against Evolve Bank & Trust (June 2024, reported by Reuters); FDIC cease-and-desist order against Cross River Bank (April 2023, reported by The Wall Street Journal and Bloomberg); this vault's `industries/neobanks.md` and `origins/retail-banking/legacy.md`.
