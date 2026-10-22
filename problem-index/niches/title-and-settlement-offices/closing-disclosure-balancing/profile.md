# Closing Disclosure Balancing & Settlement Statements

**Parent Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to make the lender's Closing Disclosure and the settlement agent's statement agree to the cent in one round inside TRID's three-business-day window, and whoever eliminates the redisclosure round gets onto the lender's preferred settlement-agent list.

## Profile
**Market Size:** ~$700M annual escrow staff time spent preparing settlement statements and balancing them with lenders (estimate)
**Share of Parent Industry:** ~6% of industry receipts (estimate)
**Digital Adoption:** Medium — both documents are system-generated; the reconciliation between them is email and marked-up PDFs
**Target Buyer:** Escrow manager; lenders' closing managers on the other side
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Every financed closing produces two statements of the same money, and TRID requires the borrower to receive the Closing Disclosure at least three business days before consummation. The lender owns the CD; the settlement agent owns the payoffs, prorations, commissions, recording fees, transfer taxes and title charges that populate it. The balancing loop is rule-bound and repeated on every file: map each fee to its CD section and tolerance bucket, apply the title premium disclosure rule, settle which figure governs, and avoid changes that restart the clock. Lenders rank settlement agents partly on how cleanly this goes.

## Current Tools & Gaps
Lender origination and closing systems with settlement-agent portals; production systems generating ALTA settlement statements and exporting fees. Gaps: the two never sync both ways; agents rekey fees into each lender's portal; title premium disclosure is recomputed by hand; nothing tells the officer which difference will trigger redisclosure.

## Problems
- [[niches/title-and-settlement-offices/closing-disclosure-balancing/build|🔨 Build: A TRID-Aware Reconciliation Engine]]
- [[niches/title-and-settlement-offices/closing-disclosure-balancing/buy|🛒 Buy: Lender Closing Portals With Two-Way Fee Sync]]
- [[niches/title-and-settlement-offices/closing-disclosure-balancing/fix|🔧 Fix: The Title Premium That Never Matches]]
