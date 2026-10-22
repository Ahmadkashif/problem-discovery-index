# Finding the Member Before the 90-Day Clock Runs Out

**Niche:** [[niches/health-insurance-carriers/dual-eligible-snp-members/profile|Dual-Eligible & Special Needs Plan Members]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** SNP outreach teams call every new member down the same list in the same order, when the members they cannot reach share predictable patterns of address, phone and Medicaid history.
**Tags:** #gradient-boosting #survival-analysis #markov-decision-processes #feature-engineering #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to reach each new special needs plan member for a health risk assessment and care plan inside CMS's 90-day window, and whoever completes the most assessments with hard-to-reach dual-eligible members, and keeps them enrolled, takes the account.

## The Problem
A new D-SNP member must be assessed within 90 days. Outreach staff call the phone number on the enrolment file, mail letters and, failing that, send someone to the door. Many members are unreachable at the listed number. Several attempts are wasted before anyone tries the pharmacy, the Medicaid case manager or the primary care office that sees the member monthly.

## Why Nobody Has Built This
Outreach is run as call-centre work, measured on attempts. The signals that predict reachability (Medicaid address changes, pharmacy fills, recent claims, housing status, prior enrolment history) sit in different feeds, some owned by the state.

## What to Build
A contactability model that estimates, for each new member, the probability of reaching them by each channel and time and the hazard of the 90-day deadline passing. A sequencing policy then picks the next best action: call the pharmacy where they filled last week, ask the primary care office to complete the assessment at the next visit, route to a community health worker, or try a text. Results feed back daily.

## Target Customer
SNP operations and care management leaders at plans with large D-SNP enrolment.

## Impact If Built
More assessments completed on time with the members hardest to reach, fewer wasted attempts, and care plans built while there is still time to act on them.
