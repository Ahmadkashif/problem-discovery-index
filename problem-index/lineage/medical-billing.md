# Lineage: Medical Billing

**Industry:** [[industries/medical-billing|Medical Billing]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** Current Procedural Terminology — the copyrighted five-digit code set a physician's service must be named in
**Builder:** American Medical Association
**Builder in vault:** **ABSENT**
**Verification:** verified — see Sources

## The Problem That Came First

Two surgeons performing the identical operation wrote it up in different words, and a claims clerk had to decide whether they were the same thing.

Before a code set existed, a physician's bill was **prose**. "Repair of hernia, right side, with mesh" against "inguinal herniorrhaphy, prosthetic." A clerk read the description, matched it to a fee schedule that was itself narrative, and formed a judgement — tolerable when the payer was a local Blue plan working through a few thousand claims by hand.

**Medicare began paying claims on 1 July 1966**, and the tolerance ended. One federal payer now sat at the receiving end of every physician in the country, each describing their own work in their own vocabulary. The cost of adjudication was no longer the price of the care; it was the price of reading.

## What Got Built

A dictionary in which every billable thing a physician does is a number.

**The AMA published the first edition of Current Procedural Terminology in 1966** — four digits, and heavily weighted toward surgery, because surgery was the part of medicine with discrete, nameable events. A second edition around 1970 moved to the five-digit codes still in use and widened coverage into medicine and laboratory work.

What matters is the artefact's shape. CPT is not a classification of *disease* — ICD does that. It is a classification of **work performed**, revised annually by an editorial panel, published as a book, and **owned**. Upwards of 11,000 copyrighted codes, changing every 1 January.

## Who Built It, And Why Them

A physicians' trade association, and the reason is that nobody else could get the definitions agreed.

Deciding whether two written descriptions denote the same procedure is not an administrative question; it is a clinical one, and any answer imposed from outside would have been contested by the specialty societies procedure by procedure. The AMA already convened those societies. That is the whole advantage — not technology, not distribution, **consensus authority over what a procedure is**.

The commercial move came later. **In 1977 Congress instructed HCFA to adopt a uniform code for identifying physicians' services.** HCFA did not write one. It licensed the AMA's — taking a non-exclusive, royalty-free, irrevocable licence, and agreeing in exchange **not to use any other system of procedure nomenclature**. In 1983 CPT was folded in as HCPCS Level I and mandated for Medicare billing.

Read the trade plainly: the AMA gave the federal government free use and took federal exclusivity, then charged everyone downstream. Hospitals, billing companies, coding schools, clearinghouses, EHR vendors and publishers all require a licence. **The AMA's 2024 annual report shows $326M of "royalties and credentialing products" revenue against $32.5M of membership dues** — roughly ten to one.

## What It Cost

A court called it misuse. In *Practice Management Information Corp. v. AMA*, **decided 6 August 1997**, the Ninth Circuit upheld the AMA's copyright in CPT but held that conditioning HCFA's licence on the exclusion of competing code sets was **copyright misuse**, and refused to enforce the copyright against the challenger while that misuse persisted. The ownership survived; the exclusivity clause did not.

The structural cost is still being paid. The vocabulary in which American medicine gets paid is a **licensed commercial product on an annual release cycle**, defined by the trade body representing the people receiving the payment. Every January the dictionary changes underneath every system that speaks it, and the industry absorbs a migration it did not choose and cannot decline.

## What You Still Touch

A coder looks up a number for something a clinician already described in words — the 1966 translation step, still done by hand, against a copyrighted book that was different last month.

- [[problems/medical-billing/worker-life-2|🟢 Coding Specialist Context Switching]] — the translation step, sixty years on
- [[problems/medical-billing/low-impact-1|🟡 Payer Rule Change Monitoring]] — what an annual release cycle feels like downstream
- [[problems/medical-billing/high-impact|🔴 Predictive Denial Prevention Engine]] — the wrong number, caught before it is sent
- [[niches/medical-billing/medical-coding-content-publishers/profile|Medical Coding Content Publishers]] — an entire trade built on licensing and reselling the dictionary
- [[niches/medical-billing/coding-certification-bodies/profile|Coding Certification Bodies]] — credentialing people to read it
- [[niches/medical-billing/independent-coding-consultants/profile|Independent Coding Consultants]]
- [[niches/medical-billing/coding-audit-compliance-firms/profile|Coding Audit & Compliance Firms]]

**Sources:** *Practice Management Information Corp. v. American Medical Ass'n*, 121 F.3d 516 (9th Cir., decided 6 August 1997) — read via FindLaw; establishes the 1977 congressional instruction to HCFA, the terms of the AMA–HCFA licence, and the copyright-misuse holding. AAPC and AMA materials on CPT's 1966 first edition and the 1983 merger of CPT into HCPCS as Level I. *American Journal of Neuroradiology* 37(11), "Current Procedural Terminology: History, Structure, and Relationship to Valuation" (citation confirmed; used for the 1966/four-digit framing). AMA 2024 annual report figures for royalties-and-credentialing revenue ($326M, up from $308M in 2023) and membership dues ($32.5M), as reported in Medscape's 2025 coverage of federal scrutiny of CPT revenue — **secondary, not read against the AMA's own filed statements this session.** ⚠️ **Not established:** the exact year and content of the second CPT edition; "around 1970, five digits" is the consistent secondary account but I could not confirm it against a primary AMA source. ⚠️ **Note on the royalty line:** $326M is a combined *royalties and credentialing products* figure; the CPT-only share is not separately disclosed and is **not** claimed here. This note deliberately does not restate `history/medical-billing.md`, which covers DRG-based reimbursement and the clearinghouse layer; that file is cited as vault material, not as corroboration.
