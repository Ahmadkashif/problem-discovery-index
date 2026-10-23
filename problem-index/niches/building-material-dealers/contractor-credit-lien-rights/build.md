# Notice Clocks Started by the Delivery Ticket

**Niche:** [[niches/building-material-dealers/contractor-credit-lien-rights/profile|Contractor Credit, Job Accounts & Lien Rights]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The date that starts every lien clock is the first delivery, which sits on a driver's ticket the credit department never sees in time.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a dealer's losses on contractor credit down while it keeps selling on account, and whoever delivers the lowest write-offs as a share of credit sales takes the account.

## The Problem
A dealer that misses a preliminary notice deadline can lose lien rights on the earlier deliveries to a job. The first-furnishing date is on a delivery ticket, the owner and lender details are in a credit application or a permit, and the deadline rules differ by state and project type.

## Why Nobody Has Built This
Notice services start from data the dealer sends them, usually in batches; ERPs record deliveries but don't compute legal clocks; and credit risk tools score accounts, not jobs.

## What to Build
A job-level engine that opens a job record on the first delivery ticket, pulls owner, lender and contract details from the permit and the application, computes every applicable deadline, drafts and sends the notice, tracks waivers and joint checks, and ranks open jobs by expected loss using payment behaviour and public signals. A two-week demo works on synthetic tickets and public permit data for one state.

## Target Customer
Credit managers at pro dealers selling on account across several states.

## Impact If Built
If a dealer with ~$100M of contractor sales writes off ~0.5% a year (estimate), keeping lien rights alive on every job and catching the riskiest accounts a month earlier could recover a third to a half of that, ~$150,000–$250,000 a year (estimate), while notice work shrinks to an exception queue.
