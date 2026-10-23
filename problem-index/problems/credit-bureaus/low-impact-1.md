# Purge Dates Computed From a Date the Furnisher Got Wrong

**Industry:** [[credit-bureaus|Credit Bureaus]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rules engines can delete or suppress records on schedule, but a credit file's suppression rules hang on the date of first delinquency, and that date is the one furnishers most often report wrong across sold, transferred and re-aged accounts.
**Tags:** #decision-trees #change-point-detection #feature-engineering #evaluation-metrics #compliance #automation #data-integration

## The Problem
Every adverse item in a consumer file has a scheduled exit. Under FCRA §605 most negative information may be reported for seven years, and for collections and charge-offs the clock starts when 180 days have passed from the commencement of the delinquency. On top of the statute sit settlement and voluntary rules — the 2015 National Consumer Assistance Plan with state attorneys general (recalled), the bureaus' removal of paid medical collections from July 2022, of medical collections with an initial balance under $500 from April 2023, and a one-year wait before unpaid medical collections appear — and a growing set of state medical debt laws that apply by the consumer's residence, now that the CFPB's federal medical debt rule was vacated in July 2025.

A bureau must apply these rules to every record, every day, and the arithmetic is easy. The input is not. A debt that was charged off, sold to a debt buyer and placed with two collection agencies appears as several tradelines from several furnishers, each of which is supposed to carry the original date of first delinquency. When one of them reports the date it acquired the account instead, the item's purge date moves years into the future. That is re-aging, and it is the classic way an obsolete debt keeps damaging a file.

## What Already Exists
General-purpose business rules engines and data quality platforms (open-source and commercial rules engines, data quality suites in the major data management stacks) and the bureaus' own purge jobs. Furnisher-side, loan servicing and collection platforms carry a date-of-first-delinquency field and pass it to the Metro 2 extract.

## The Customisation Gap
The rules are not the problem; reasoning about the date across furnishers is. The customisation needed: linking every tradeline that represents the same underlying debt (original creditor, debt buyer, agencies) and checking that their delinquency dates agree; flagging dates that move after an account changes hands or after a payment, a known re-aging pattern; computing each item's exit date under federal, settlement and state rules for the consumer's address history, with the governing rule recorded; and producing a record a bureau can show a regulator for why each item was suppressed or kept. Generic engines have no concept of a debt that changes owners or of a date that should never change.

## Impact If Solved
Obsolete debts leave files on time instead of when a consumer disputes them, and the bureau can evidence state-law suppression without hand-maintained exception lists. If re-aged or overdue-for-purge items drive even ~2% of a nationwide bureau's disputes (estimate), a bureau handling several million disputes a year (estimate) avoids on the order of 50,000–100,000 of them annually (illustrative arithmetic), along with the FCRA claims that re-aging attracts.
