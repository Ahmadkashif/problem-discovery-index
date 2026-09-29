# Lineage: Mortgage Brokers

**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** Desktop Underwriter — Fannie Mae's automated underwriting engine, in production June 1995 — and Desktop Originator, the front end through which a broker reaches it
**Builder:** Fannie Mae
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A broker could take an application but could not say yes.

The broker's product is a promise to the borrower that some lender will fund this loan. Until the mid-1990s that promise rested on a human underwriter. The underwriter worked at a lender, applied Fannie Mae's published guidelines to a file of what the builders later counted as "over 700 data items," and returned an answer weeks later.

Fannie Mae's own engineers described the constraint in 1997. Manual underwriting "is often dependent upon scarce and expensive resources." And "because underwriters may interpret Fannie Mae guidelines differently, the process can lead to inconsistent results." **The same file could be approved at one lender and declined at another, on the same rulebook.** Fannie's chief executive gave the cost in round numbers: origination took "eight weeks, or longer," and the goal was to cut $1,000 from each mortgage and get it to five days.

## What Got Built

A rules engine that read a loan application and returned a recommendation in under a minute.

Design took nearly six months. Development began in **early 1994**, with a team of twenty to thirty. A pilot went out in **October 1994**, and the first production release followed in **June 1995**. The engine ran on Brightware's ART-IM rule language, with a Visual C++ front end. It was reached over Fannie's MORNETPlus network, either through Fannie's own **Desktop Originator / Desktop Underwriter** software or through any third-party origination system.

The originator keyed the borrower's Form 1003 and submitted it. DU sent back two answers. A **credit** recommendation said approve, or *refer* to a human underwriter. An **eligibility** recommendation said whether Fannie would buy the loan. The system was built "to reason and underwrite loans with incomplete, unverified and conflicting data." Its designers named the broker's case outright: a broker wanting "a point-of-sale decision based entirely on unverified information." After the first year in production, a statistical credit score was added to the rules.

## Who Built It, And Why Them

Fannie Mae, with contractors Brightware and The Parallax Corporation credited on the 1997 paper.

**Why them and not a lender:** the rules were Fannie's. It wrote the Selling Guide, bought the loans, and carried the cost of every underwriter reading that guide differently. A lender could encode its own reading — Countrywide had already built a rule-based underwriter, CLUES, which the DU paper cites. But a lender's engine gave only that lender's answer. Only the buyer of the loan could issue an interpretation that every seller had to accept. The programmers turned published guidelines into rules, and Fannie's credit policy group approved them.

The commercial reason was volume at lower cost. DU sat inside Fannie's "Technology to Lower Costs" initiative, part of its Trillion Dollar Commitment. Freddie Mac built a rival, Loan Prospector, in the same period. I did not verify its launch date this session.

## What It Cost

**The broker gained a yes that did not bind anyone to fund the loan.** DU said whether a loan met Fannie's standard. It did not say whether a given wholesale lender would take it. Lenders stack their own *overlays* on top of the GSE answer, and those vary lender by lender. Underwriting became a commodity; routing did not. The broker's scarce knowledge moved from "will this be approved?" to "which lender will actually close it?"

Access was mediated too. Today a broker reaches DU through Desktop Originator only under a *sponsoring lender*. The tool that let the broker decide was licensed to the broker through the party it sells to.

## What You Still Touch

The "Approve/Eligible" line on every findings report is this 1995 engine's output format:

- [[problems/mortgage-brokers/high-impact|🔴 Lender-Borrower Matching Intelligence]] — what was left for the broker once underwriting became a commodity
- [[problems/mortgage-brokers/worker-life-1|🟢 Condition Clearing Automation for Loan Processors]] — DU's findings become the processor's to-do list
- [[niches/mortgage-brokers/lender-submission-routing/fix|Rate Sheet Parsing & Overlay Tracking Fragmentation]] — overlays, the layer DU never saw
- [[niches/mortgage-brokers/gse-selling-guide-content/profile|Investor Guideline Content & Interpretation]] — the guide DU was built to enforce

**Sources:** David W. McDonald, Charles O. Pepe, Henry M. Bowers and Edward J. Dombroski, "Desktop Underwriter: Fannie Mae's Automated Mortgage Underwriting Expert System," *IAAI-97 Proceedings* (AAAI, 1997), PDF read directly. It is the source for the six-month design, early-1994 start, 20–30 staff, October 1994 pilot, June 1995 production, ART-IM and Visual C++, MORNETPlus, Desktop Originator, Form 1003, the two-part recommendation, the 700-data-item, inconsistency and point-of-sale quotations, CLUES, the credit-policy role, the added credit score, and James Johnson's $1,000 / eight-weeks-to-five-days goal. It is an insider account by Fannie Mae staff and contractors. Fannie Mae, *Desktop Underwriter & Desktop Originator* and *Mortgage Brokers and Correspondents* pages (search summaries, **not read at source**) for the sponsoring-lender requirement. This vault's `history/mortgage-brokers.md` and niche notes for overlays (vault material, not independent corroboration). ⚠️ **Not established:** Loan Prospector's launch date; the first year DO was usable by brokers directly, as distinct from lenders; the names of Fannie Mae executives who sponsored the project.
