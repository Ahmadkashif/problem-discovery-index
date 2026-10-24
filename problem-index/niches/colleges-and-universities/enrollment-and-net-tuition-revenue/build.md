# One Ledger From First Contact to Second-Year Retention

**Niche:** [[niches/colleges-and-universities/enrollment-and-net-tuition-revenue/profile|Enrollment Management & Net Tuition Revenue]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Recruitment and aid are optimised on different metrics by different vendors, and nobody measures what each enrolled student cost to recruit and price against the net tuition they actually paid.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #feature-engineering #data-integration #revenue-impact #evaluation-metrics
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to raise net tuition revenue from the next entering class", but it holds two contests with different winners: filling the funnel with students likely to enroll, won on enrolled students per recruitment dollar, and pricing each admit, won on the discount rate at target class size. Decomposed into contested sub-niches below.

## The Problem
An enrollment VP manages two budgets that compete for the same outcome. Recruitment buys names, travel, digital campaigns and CRM licences, and is reported on inquiries, applications and admits. Institutional aid is reported as a discount rate. A student recruited cheaply but given $28,000 in grant aid and a student recruited expensively who pays nearly full price look the same in both reports. So does a student who enrolled and left after one year and one who graduated. The board asks whether the college is buying its class efficiently, and nobody can answer.

## Why Nobody Has Built This
The data sits in three systems owned by three offices: the CRM in admissions, awards in the aid system, and enrollment, retention and billing in the SIS. Vendors sell into one office each, and the consultancies that see both funnel and aid do so client by client under contracts that limit reuse of student records.

## What to Build
A student-level ledger that joins every recruitment touch, the aid award and its changes, deposit, enrollment, retention and net tuition paid over time, built inside the institution's own data so FERPA is not an obstacle. On it: cost-per-retained-student by source and aid band, uplift estimates for both recruitment touches and grant dollars, and a planning view that moves budget between the two at fixed class size.

## Target Customer
VPs for enrollment and CFOs at private colleges of 1,000–10,000 students that run Slate or Salesforce and a major SIS.

## Impact If Built
For the first time the college can compare its recruitment and aid dollars on one measure, net tuition from retained students per dollar spent. At a college spending ~$3M on recruitment and ~$30M on institutional aid, moving 3% of the combined budget to better-yielding uses is worth ~$1M a year (estimate).
