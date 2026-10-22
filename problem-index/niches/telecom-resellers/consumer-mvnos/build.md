# Port-Out Takeover Defence for MVNOs

**Niche:** [[niches/telecom-resellers/consumer-mvnos/profile|Consumer MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A criminal who moves a subscriber's number to a new SIM or a new carrier takes over their bank and email accounts, and an MVNO decides whether to allow the move with less information than the host network has.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #compliance #revenue-impact
**Contested on:** *Not terminal as stated.* Consumer MVNOs split into cable and converged MVNOs, which win on offloading traffic from the host network, and independent digital MVNOs, which win on keeping subscribers past acquisition payback; see the parent profile.

## The Problem
SIM swaps and port-outs are how one-time passcodes are stolen. A fraudster with a subscriber's name, address and a leaked PIN asks for a new eSIM, or requests a transfer PIN and ports the number to another carrier. The real subscriber loses service, and within the hour their bank and email accounts have new passwords. The FCC's November 2023 SIM-swap and port-out order (WC Docket 21-341) requires carriers to authenticate customers before a SIM change or port-out and to notify them immediately, but a July 2024 bureau order (DA 24-649) deferred compliance with all of its rules until OMB approval and a Federal Register compliance-date notice, and no such notice had appeared by October 2026. The obligation is coming for MVNOs too, and the method is unsettled.

## Why Nobody Has Built This
The hosts built protections for their own brands first. MVNOs sit on an enabler's BSS that treats a SIM change as a provisioning event, not a risk decision. The useful signals are spread across the MVNO's app logins, the host's device and network events, and payment history, and no single vendor joins them for a reseller.

## What to Build
A risk decision on every SIM change, eSIM transfer and port-out PIN request, scored from account age, recent profile changes, login device and location, payment changes, call and data patterns in the prior days, and network events from the host where the contract allows. Low-risk requests pass silently. Medium-risk ones get step-up verification in the app. High-risk ones are held with notice to the subscriber's existing device, and every decision is logged for the FCC record.

## Target Customer
Heads of fraud and security at MVNOs and at the MVNEs that run back offices for dozens of smaller brands. The hosts' own version of this contest, at carrier scale and with network-side signals, is [[niches/wireless-carriers/porting-sim-account-security/profile|Number Porting, SIM Changes & Account Takeover Defence]]. This build is the reseller that has to decide with less.

## Impact If Built
Account takeovers through the MVNO stop being the cheapest route to a victim's bank account. The MVNO arrives at the FCC compliance date with a working, documented control instead of a call-centre script.
