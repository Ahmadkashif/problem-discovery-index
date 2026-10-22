# The Retiree Payroll Clerk Facing a Fraudster Before the Cutoff

**Industry:** [[pension-funds|Pension Funds]]
**Type:** Worker Life Changing
**One-liner:** A retiree payroll clerk must decide, before the monthly payroll closes, whether a request to change a pensioner's bank account comes from the retiree or from a fraudster. Getting it wrong either way lands on an 80-year-old who depends on that check.
**Tags:** #gradient-boosting #logistic-regression #k-nearest-neighbors #evaluation-metrics #worker-facing #compliance #automation

## The Problem
Every month a public retirement system pays tens or hundreds of thousands of retirees and beneficiaries (estimate). Before each payroll closes, the payroll and member records staff process changes: new direct deposit accounts, address changes, tax withholding, deaths reported by family members, and beneficiaries starting payments. Some of these requests are fraud. In July 2025 the New Hampshire Retirement System caught faxed attempts to redirect the pensions of five retirees and one beneficiary. The state attorney general linked them to spoofed robocalls impersonating banks. Massachusetts' pension regulator has issued alerts about fraudsters impersonating retirement board staff, and about one who passed a portal's identity checks with a stolen name, date of birth, Social Security digits and answers to four verification questions. A former PBGC contractor pleaded guilty to taking over participants' online accounts and redirecting their monthly pensions.

The clerk is the control. They compare signatures and look for a notarisation. They call the retiree back on the number on file, which is sometimes the number the fraudster just changed. And they decide whether to hold a change and risk a real retiree missing a payment, or let it through and risk the payment going to a thief.

## Why It Matters to the Worker
The clerk carries the consequence personally. A legitimate change held for verification means a retiree, often elderly, calls in distress because the rent payment bounced. A fraudulent change let through means a pension is stolen and the clerk's name is on the approval. The work peaks just before the payroll cutoff, when there is least time to call back. Fraudsters target exactly the moments, such as a retiree's death, a move or a new bank, when legitimate changes also arrive. Nothing tells the clerk which of the day's hundred changes is the one to worry about.

## What a Solution Looks Like
A risk score on every change request, built from the system's own history. Inputs include the channel, the time since the last contact-detail change, a new bank's routing number and account age where available, mismatches between the request and the member's prior correspondence, clusters of requests sharing a phone number or bank, and a recent death report. The clerk sees the few requests that warrant an out-of-band call, with the reason, and can release the rest before cutoff. Confirmed fraud and confirmed legitimate changes feed the model back.

## Impact If Solved
The clerk spends the hours before payroll on the handful of requests that look wrong, not on equal suspicion of everyone. Retirees are not held up by blanket verification, stolen payments fall, and the clerk is no longer the only thing standing between a pensioner and a fraud ring.
