# Change-Request Risk Scoring Before Payroll Cutoff

**Niche:** [[niches/pension-funds/payee-verification-overpayment/profile|Payee Verification & Overpayment Prevention]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every bank-detail change to a pension gets the same callback, or none, though a few carry nearly all the fraud risk.
**Tags:** #gradient-boosting #logistic-regression #graph-theory #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to stop payments to dead or impersonated payees before each monthly payroll runs, and whoever stops the most improper payments before the cutoff without holding a living retiree's check takes the account.

## The Problem
A retirement system processes thousands of direct deposit, address and contact changes a month (estimate). Fraud attempts arrive through the same channels as legitimate changes: fax, mail, phone and portal. They cluster around events such as a death, a move or a new bank. Staff verify by callback to the number on file, which a fraudster may have changed first.

## Why Nobody Has Built This
Plans see few confirmed fraud cases each, too few to model alone. Banks' fraud models do not see pension-side context, and PAS vendors treat changes as transactions to post, not decisions to score.

## What to Build
A scoring service on every change request. Features include the channel, the sequence of recent changes (contact detail changed before bank detail), new-account signals where available, request origin, links to other requests sharing phones, banks or fax numbers, and death reports. High-risk requests are held for out-of-band verification with the reason shown, and the rest clear before cutoff. Plans that opt in share fraud indicators through the vendor to overcome rare labels.

## Target Customer
Benefits operations directors at statewide and large county systems, multiemployer funds and DB administrators.

## Impact If Built
Fraud checks concentrate on the requests that warrant them, stolen payments fall, and legitimate retirees stop waiting on blanket callbacks.
