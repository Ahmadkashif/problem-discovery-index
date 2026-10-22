# A Refinance Test for Every Maturing CRE Loan

**Niche:** [[niches/community-banks/cre-lending-concentration/profile|CRE Lending & Concentration Risk]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A community bank knows which CRE loans mature next year but not which of them will qualify for a new loan at today's rate, cap rate and NOI, so the maturity wall is managed by phone calls in the final quarter.
**Tags:** #monte-carlo-methods #gradient-boosting #survival-analysis #large-language-models #feature-engineering #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show a CRE-concentrated bank's board and examiner, loan by loan, which properties will fail to refinance at today's rates before the maturity arrives, and whoever produces that answer from the bank's own rent rolls and maturity schedule fastest takes the account.

## The Problem
A $1B bank with CRE at 300% of capital may hold ~a few hundred investor property loans (estimate): strip centres, small office buildings, apartments, self-storage, mini-warehouses. Many were written at ~3.5–4.5% on five-year terms and are maturing into rates ~two or three points higher (estimate). Whether each can refinance depends on its own rent roll, lease expirations, operating expenses and the guarantor's liquidity. The bank's stress test applies a portfolio-wide shock to segment averages and tells the board the book can absorb it, which is not the question the examiner or the borrower is asking.

## Why Nobody Has Built This
The inputs are scattered and unstructured: rent rolls and operating statements arrive as PDFs or spreadsheets in each borrower's own format, appraisals are years old, and lease terms sit in documents the bank rarely abstracts. CRE data vendors model markets and CMBS loans, where the data is standardised by servicers; bank portfolio loans have no servicer reporting format.

## What to Build
A loan-level refinance engine. Extract rent rolls, operating statements and lease expirations as they arrive; project each property's NOI through maturity with lease rollover and expense growth; simulate rate and cap-rate paths; and compute, for each loan, the probability that it meets the bank's own refinance terms (debt service coverage and loan-to-value) at maturity. Rank the maturity wall by shortfall, show what paydown or guarantor support would close each gap, and produce the concentration stress test the 2006 guidance expects from the same data.

## Target Customer
Chief credit officers and CFOs at community banks above or near the 300% CRE threshold.

## Impact If Built
The bank starts refinance conversations twelve to eighteen months early with a number in hand, sizes its allowance and capital plan to loans it can name, and shows the examiner a stress test built from its own properties.
