# Detection and Correction Before the Employee Looks

**Niche:** [[niches/payroll-platforms/disbursement-failure-recovery/profile|Disbursement & Failure Recovery]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A failed direct deposit is known to the provider through a return before the employee opens their banking app on payday, and the process waits for the employee to call.
**Tags:** #gradient-boosting #logistic-regression #change-point-detection #evaluation-metrics #confidence-intervals #automation #worker-facing #revenue-impact
**Contested on:** Every serious competitor in payroll disbursement is fighting to detect and correct a failed payment before the employee opens their banking app — and whoever closes that window takes the account.

## The Problem
An employee changed banks and updated their details a week late, so Friday's deposit goes to a closed account. The bank returns it. The provider receives the return, which is processed in a batch. The employee checks their account on Friday morning, finds nothing, assumes an error, worries, and contacts their employer, who contacts the provider. A correction is issued the following week. Rent was due Friday. Everything after the return was avoidable: the provider knew, the employee did not, and nobody told them.

## Why Nobody Has Built This
Returns processing was built as a reconciliation function rather than as an incident response, so its cadence is batch and its output is a corrected record rather than an immediate action. The employee is not the provider's customer, which means there is no established channel to notify them and no product manager whose metric is their experience. And the failure feels like the employee's fault — they changed banks late — which has been enough to keep it framed as their problem to discover.

## What to Build
Failure prediction before the payment and immediate response after it. Prediction: account validation at every detail change, first payments to a new account flagged as elevated risk, and a model over the provider's own return history identifying the characteristics that precede failure — recently changed details, accounts at institutions with high return rates, patterns in the entry itself. High-risk payments can be verified with a micro-deposit or held for confirmation before the run rather than failing after it. Response: returns are acted on within minutes of receipt rather than in a batch, with the employee notified directly and immediately, in plain language, with what happened, what is being done and when the money will arrive. The correction is initiated automatically where the failure is correctable, and same-day or instant payment rails are used for the reissue, since the whole point is the delay. The measured outcome is the time between the provider knowing and the employee knowing, which is currently negative in the sense that matters — the employee finds out first, from an empty account.

## Target Customer
Payroll providers, payment operations teams, and employers whose payroll support burden is dominated by disbursement failures.

## Impact If Built
A missed wage payment is a household financial event with consequences that compound within days — a bounced rent payment, an overdraft fee, a late charge. Validation at setup eliminates the most preventable class outright, and immediate notification with an automatic reissue converts the remainder from a multi-day emergency into an inconvenience the employee was told about before they noticed.
