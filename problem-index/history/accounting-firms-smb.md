# History: SMB Accounting Firms

**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Primary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** none — see note below
**Episode Tier:** 1
**Transferable Pattern:** When client-facing software commoditises the ledger, the professional's value moves to the workpaper a regulator or a peer reviewer will actually sign off on — and that workpaper is still built in the one tool nobody has to be trained on.

> **Origin Parent note.** None of the eighteen `origins/` fits. Retail banking's ERMA/ACH lineage governs how money moves, not how a firm proves its numbers; insurance carriers' pooled-statistics lineage has no analogue here. This industry is a direct child of Wave 3 itself, with no intermediate origin — consistent with the wave file's own claim that it "created no industry of its own."

## Before

A CPA firm in 1978 ran three separate manual systems that a bookkeeper reconciled by hand: a **general ledger** (pegboard or one-write systems if the client was lucky, a paper journal if not), a **working trial balance** built at year-end on columnar accounting paper, and a **tax return** prepared from that trial balance with a pencil, an adding machine, and IRS tables. Every one of those objects was a grid. The paper simply had to play the part a cell reference plays now.

The staff-hour cost of that arrangement fell almost entirely on arithmetic: footing columns, cross-casting totals, re-doing a page when one number changed. It is the same disease VisiCalc was built to cure, arriving in this industry a few years later than it arrived generally.

## The Origin Event — an accumulation, not a moment

There is no single founding story here. What exists is a run of separate products solving separate pieces of the same firm's workflow, each significant enough to date on its own:

| Year | What arrived |
|---|---|
| **1983** | **Intuit** founded by Scott Cook and Tom Proulx, Palo Alto — Quicken, personal/small-business bookkeeping on a PC. |
| **1984** | **ChipSoft** (Michael A. Chipman) ships the first version of what becomes **TurboTax**. |
| **1986** | **IRS e-file** begins as a pilot programme for paid preparers — electronic transmission of a return, not yet a mandate. |
| **March 12 1993** | Intuit goes public and simultaneously **acquires ChipSoft/TurboTax for a reported $225M**, folding consumer tax prep into the same company that owned the ledger. |
| **1992** | **QuickBooks** ships — Intuit's small-business ledger, distinct from consumer-grade Quicken. |
| **2011–2012** *(phase-in, confirm before script)* | IRS **Section 6011(e)** mandate takes effect requiring most paid preparers to e-file — the era of the paper 1040 leaving a CPA's office effectively ends. |

**Nothing on this list was aimed at accounting firms as such.** Intuit built consumer and small-business tools; the professional side of the industry (UltraTax, Lacerte, Drake, CCH Axcess) grew up alongside it, serving the preparer rather than the taxpayer. The firm-facing software this vault actually documents — Karbon, Canopy, Jetpack Workflow — is newer still, and handles workflow, not computation; none of it, per the hub note, "automate[s] document extraction or intelligent categorization." The ledger got a computer in 1992. The document chase did not.

## What Became Cheap

**Recording a transaction, once someone has already categorised it.** QuickBooks Online and Xero made the entry itself nearly free — auto bank feeds populate the ledger without a keystroke. What stayed expensive is exactly what the hub note names: **60–70% auto-categorization accuracy**, leaving hundreds of manual line items per client per month, because the software cannot see the client-specific rule ("this vendor is always COGS, that one is always an owner draw") that a bookkeeper carries in their head.

This is the same shape wave-03 describes for every industry on this list: the general-purpose ledger digitised the entry; it did not digitise the judgment.

## The Trade-Off

**Standardisation was traded for advisory value, and most firms haven't collected on it.**

QuickBooks Online and Xero's popularity means nearly every client's books live in one of two schemas — which should make cross-client benchmarking trivial. It doesn't, because, per the hub note, "firms struggle to standardize chart of accounts across their client base." Every client names their own accounts, and the mapping between "Bob's client's chart" and "an industry benchmark" is manual. The platforms solved data custody, not data comparability — the harder problem, and the one that would actually let a firm sell advisory services instead of write-ups.

## The Binding Constraint

**AICPA peer review.** Firms performing attest work must undergo a peer review, typically every three years, under AICPA and state-board oversight — and a peer reviewer's job is to trace a reported number back to a supporting workpaper. That requirement is why the spreadsheet survives inside firms that have otherwise gone all-in on QBO/Xero: **the workpaper that ties the client's trial balance to the filed return is the audit trail a reviewer inspects**, and an Excel model with visible formulas is easier to defend under review than a black-box SaaS calculation. This vault's own [[niches/accounting-firms-smb/peer-review-entities/profile|Peer Review Entities]] niche exists because of exactly this mechanism.

Put in wave-03's terms: the switching cost of replacing the workpaper is not training cost, it is **re-certifying that the new tool's output survives a peer reviewer's trace-through** — which is compliance work, not software work.

## Why There Is No Fight, and One Adjacent Fight Worth Naming

**Between accounting firms and their tooling vendors, there is no contest** — Intuit, Thomson Reuters and Wolters Kluwer sell to firms, not against them, and firms have no reason to root for one ledger platform's defeat of another. Absence recorded, not manufactured.

**One real fight exists nearby, and it is worth naming because it explains the vendor landscape.** Intuit spent years defending TurboTax's "free" consumer tax filing while allegedly steering eligible free-filers toward paid products — a practice **ProPublica's 2019 reporting** documented and the **FTC found deceptive in a January 2022 order**, followed by a **multistate settlement of roughly $141M announced May 2022**. Intuit withdrew from the IRS Free File Alliance in **July 2021**. None of this is a fight *this* industry's firms were party to — it is Intuit's war with the IRS and the FTC over who gets to serve the taxpayer who would otherwise pay a preparer nothing. It matters here only as context: the same company built both the consumer product accused of steering people away from free filing and the small-business ledger every firm in this file now runs on.

## What's Still Open

- [[problems/accounting-firms-smb/high-impact|🔴 Client Document Collection and Data Extraction]] — 30–40% of busy-season capacity
- [[problems/accounting-firms-smb/worker-life-2|🟢 Bookkeeper Transaction Categorization Tedium]] — the 60–70% ceiling
- [[problems/accounting-firms-smb/low-impact-1|🟡 Chart of Accounts Standardization]] — the benchmarking gap
- [[niches/accounting-firms-smb/document-intake-ops/profile|Document Intake Ops]]
- [[niches/accounting-firms-smb/bookkeeping-advisory/profile|Bookkeeping & Advisory]]
- [[niches/accounting-firms-smb/sole-practitioner-cpas/profile|Sole Practitioner CPAs]]
- [[niches/accounting-firms-smb/seasonal-tax-prep/profile|Seasonal Tax Prep]]
- [[niches/accounting-firms-smb/peer-review-entities/profile|Peer Review Entities]] — the binding constraint, as a business

## The Transferable Pattern

> **Find the document the regulator or the reviewer will actually ask to see, and build for what that document has to survive — not for how fast you can produce a number.**

An FDE proposing to replace a firm's workpapers is not competing against Excel's convenience. They are competing against Excel's **legibility to a third party who did not build the model** — a peer reviewer, a state board investigator, an IRS examiner. A faster tool that produces a number a firm cannot defend under review is not a firm firms will actually adopt, whatever the demo looks like.

**Sources:** Wikipedia, *Intuit*, *TurboTax*, *QuickBooks*; IRS.gov, e-file history and Section 6011(e) mandate; ProPublica, *TurboTax Deliberately Hides Its Free File Page From Search Engines* (2019) and subsequent Free File reporting; FTC, *In the Matter of Intuit Inc.* (Jan 2022) and multistate TurboTax settlement announcements (May 2022); this vault's `industries/accounting-firms-smb.md` and `problems/accounting-firms-smb/*.md`.
