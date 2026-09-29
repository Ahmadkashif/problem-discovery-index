# Lineage: Lending Marketplaces

**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the LendingTree qualification form — a single online credit request, matched by the Lend-X exchange against each lender's preset underwriting filters and transmitted to up to four lenders, each paying a per-transmission fee
**Builder:** LendingTree
**Builder in vault:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Verification:** partial — see Sources

## The Problem That Came First

Shopping for a loan meant applying for it, again and again.

In the mid-1990s a borrower comparing mortgages had to approach each lender separately: phone calls, branch visits, a fresh set of income and asset questions each time. Comparison was so expensive that most borrowers did very little of it, and lenders competed for them mainly through advertising and brokers rather than on the offer itself.

Doug Lebda, an accounting graduate who worked as an auditor and consultant at PricewaterhouseCoopers in Pittsburgh in the 1990s, applied for a mortgage in 1994 and found the process frustrating despite a finance background. The constraint was not information about rates — those were advertised. It was that **every comparison required a separate application.**

## What Got Built

One form, many answers.

The borrower filled in a single **qualification form** — income, assets, liabilities, loan preferences. Behind it sat an exchange LendingTree called **Lend-X**. Each participating lender had loaded its own underwriting criteria, which it could change in real time through a password-protected site called LenderWeb. The exchange matched the form against those filters and transmitted it to **up to four lenders** whose criteria it met; those lenders came back with offers.

By its fiscal-2002 annual report the exchange had nearly 200 banks, lenders and brokers, 139 of them offering mortgages. LendingTree had obtained a US patent on the Lend-X technology and the online loan-market process.

## Who Built It, And Why Them

Lebda, and specifically not a lender.

He founded the business in late 1996 as CreditSource USA, a mortgage marketing service; a year later it was renamed LendingTree. The site launched in 1998 and went public on 15 February 2000. IAC acquired it in May 2003.

**Why an outsider:** no bank could run this. A lender that forwards your application to three competitors has built a marketplace that disadvantages itself. The comparison had to be operated by a party with no loan book of its own — which meant a party whose revenue had to come from the lenders instead.

That requirement is what fixed the tool's shape. LendingTree charged lenders a **transmission fee** each time a form meeting their criteria was sent to them, and a **closed-loan fee** when one of those borrowers actually closed. In 2002 the mortgage transmission fee rose from $8 to $9, and the closed-loan fee moved from a flat $400 to a range of $300 to $750. Selling the same form to four lenders earned four transmission fees. The patent protected the exchange; the fee schedule defined the product.

## What It Cost

**The form was the product, and the form was sold before anyone knew whether a loan would result.** The transmission fee — earned on delivery, multiplied by the number of lenders — was the reliable revenue. The closed-loan fee depended on lenders reporting what happened afterwards.

So the marketplace was built to be paid at the moment of match, and to learn about outcomes only when a lender chose to tell it. That was a sensible trade for a startup that needed revenue before it had trust: lenders would pay for a qualified lead long before they would open their books.

The borrower paid too. One form sent to four lenders means four lenders calling, all of whom have paid for the chance.

## What You Still Touch

Fill in any loan-comparison form today and you are using a descendant of the qualification form: one request, fanned out against lender filters, priced per lead. The incentive it created — optimise for the transmission, hear about the outcome later or never — is still the industry's central problem.

- [[problems/lending-marketplaces/high-impact|🔴 Matching Optimised on the Click]] — the transmission fee's descendant
- [[problems/lending-marketplaces/low-impact-1|🟡 Lender Integration and Rate Table Freshness]] — the descendant of LenderWeb's preset filters
- [[problems/lending-marketplaces/worker-life-1|🟢 The Loan Consultant Working a Priced Lead]]
- [[niches/lending-marketplaces/outcome-data-recovery/profile|Outcome Data Recovery]]
- [[niches/lending-marketplaces/borrower-routing/profile|Borrower Routing]]

**Sources:** LendingTree, Inc., Form 10-K for fiscal 2002, SEC EDGAR (qualification form; Lend-X; LenderWeb; "up to four Lenders"; transmission and closed-loan fees and their 2002 changes; "nearly 200" lenders, 139 mortgage; US patent on Lend-X); Wikipedia, *LendingTree* (CreditSource USA late 1996, renamed a year later; 1998 online launch; IPO 15 February 2000; IAC May 2003); Wikipedia, *Doug Lebda* (PwC Pittsburgh; 1994 mortgage application; died 12 October 2025); CBS News and NBC News obituaries (October 2025). The Charlotte Ledger founder profile returned 403 and was not read. ⚠️ **Not established:** the patent's number and issue date; the fee levels at 1998 launch (the 10-K gives only 2002 figures); the original 1998 lender count; and whether "up to four" was the 1998 rule or a later one — the four-lender figure is sourced to the 2002 filing only.
