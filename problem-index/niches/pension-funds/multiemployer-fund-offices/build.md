# Hours-to-Credit Reconciliation Across Every Contributing Employer

**Niche:** [[niches/pension-funds/multiemployer-fund-offices/profile|Multiemployer Pension Fund Offices]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tradesperson's pension is built from hours reported by dozens of employers over a career, and nobody checks the hours against anything until the retirement application.
**Tags:** #gradient-boosting #k-nearest-neighbors #change-point-detection #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to post every contributing employer's monthly remittance to the right participant's hours and pension credit, and whoever credits every reported hour correctly with the fewest delinquencies and credited-service disputes takes the account.

## The Problem
An electrician works for six contractors in a year. Each reports hours on its own remittance. One misspells the name, one uses an old ID, one under-reports a month and another stops reporting altogether. The fund office posts what arrives. At retirement the member says they worked years the record does not show, and staff search decades of paper.

## Why Nobody Has Built This
Fund offices are small, and their systems are built to post contributions, not to model expected hours. The external signals that would reveal a gap, such as dispatch records from the union hiring hall, prevailing-wage certified payrolls and other funds' records, sit with other organisations.

## What to Build
A reconciliation layer that matches each remittance line to the participant with fuzzy identity matching, compares each member's and each employer's reported hours with their own history, flags drops and missing months, and links to hiring-hall dispatch data where the union shares it. Employers with gaps are flagged for the payroll auditor. Members get an annual hours statement prompting them to report errors while they still remember.

## Target Customer
Fund administrators and third-party administrators of construction and trades pension plans.

## Impact If Built
Missing hours are found within months, while the employer still exists and the member remembers the job, instead of at retirement when neither is true.
