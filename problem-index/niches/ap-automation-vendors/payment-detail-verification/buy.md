# Payee Verification From Payments

**Niche:** [[niches/ap-automation-vendors/payment-detail-verification/profile|Payment Detail Verification]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payment systems built account name verification to stop misdirected payments, and AP platforms verify by telephone.
**Tags:** #compliance #data-integration #evaluation-metrics #gradient-boosting #confidence-intervals #automation #graph-theory #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to confirm that a bank detail change is genuine using evidence an attacker cannot forge — and whoever replaces the callback to a number from the email itself removes the category's largest concentrated loss.

## The Problem
Payment infrastructure developed real answers to misdirected payments: account name verification services that check whether the name matches the account, account ownership validation, and confirmation-of-payee schemes that materially reduced authorised push payment fraud where they were deployed. The infrastructure exists in several markets. AP platforms, which initiate the payments, largely verify by asking someone on the phone.

## What Already Exists
Account name verification and confirmation-of-payee schemes; account ownership validation services; micro-deposit verification; payment fraud scoring at the network level; and the regulatory push behind all of it.

## The Customization Gap
The adaptation is to business payees and a change event rather than a payment event. It requires: (1) verification triggered at the detail change rather than at payment, since that is when the fraud is committed and payment-time checks come too late — this is the substantive difference; (2) business account name matching, which is harder than consumer matching because legal, trading and division names all differ legitimately; (3) coverage across markets where confirmation-of-payee does not exist, which is where the network corroboration substitutes; (4) integration with the vendor record lifecycle rather than with a payment instruction; and (5) a threat model of social engineering against a person rather than of account takeover, which changes what the control must defeat.

## Target Customer
Payment operations and risk leadership, banks and payment providers, insurers, and payee verification vendors for whom the AP change event is unaddressed.

## Impact If Solved
The verification infrastructure exists and fires at payment time, which is after the fraud has been committed. Moving the check to the detail change, backed by network corroboration where schemes do not reach, is the adaptation.
