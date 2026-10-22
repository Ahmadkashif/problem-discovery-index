# Redraw Risk Scored Before the Appointment

**Niche:** [[niches/notary-signing-services/borrower-loan-package-signings/profile|Borrower Loan Package Signings]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most failed signings were predictable the afternoon before — late documents, a lender with a fussy package, a borrower who never confirmed — and nobody acts on the signs.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to return a fully executed, error-free loan package before the lender's funding cutoff, and whoever has the lowest redraw rate per hundred signings takes the title company's order flow.

## The Problem
A signing service handles hundreds or thousands of orders a month. A small share fail: the borrower disputes a number at the table, a spouse who must sign is missing, the documents arrive an hour before the appointment, or the package has an error that forces a redraw. Coordinators treat every order the same until something goes wrong.

## Why Nobody Has Built This
Signing services are small operators without data teams; their history sits in a mix of Snapdocs, email and spreadsheets. Failures are logged as anecdotes rather than coded reasons.

## What to Build
A risk score for each order the day before, from document arrival time, lender and title client, loan type, page count, borrower confirmation status, number of signers, agent history and prior disputes on the same file. High-risk orders get early document review against the lender's checklist, a confirmation call that asks about cash-to-close surprises, and the most reliable agent. Coded failure reasons feed the model back.

## Target Customer
Owners and operations leads of regional and national signing services; title companies with in-house notary networks.

## Impact If Built
Coordinator attention goes to the orders that need it, and the service's redraw rate — the number title clients judge it on — falls.
