# Continuous Proof of Solvency and Control

**Niche:** [[niches/crypto-exchanges/custody-and-key-operations/profile|Custody & Key Operations]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Proof of reserves shows that assets existed at one moment and says nothing about liabilities, encumbrance, or the next moment.
**Tags:** #graph-theory #change-point-detection #evaluation-metrics #compliance #automation #confidence-intervals #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that customer assets exist, are controlled, and are not encumbered — without revealing the operational detail that would help an attacker — and whoever proves it best takes the institutional accounts.

## The Problem
The attestations published after 2022 demonstrate that certain addresses held certain balances at a point in time and that an auditor reviewed a liability figure the exchange supplied. They do not demonstrate that the exchange controls those keys rather than borrowing a signature, that the assets are unencumbered, that customer liabilities are complete, or that any of it is still true a day later. The demand these attestations answer is real and the instrument is weak, and the parties who most need the proof — institutional depositors — know it.

## Why Nobody Has Built This
Proof of reserves emerged as a crisis response, so its shape was set by what could be produced in weeks rather than by what would actually be probative — and nothing since has forced an upgrade because the market accepted the artefact. Proving liabilities requires a commitment structure exchanges have not adopted. Continuous proof risks leaking operational detail an attacker would use. And the exchanges with the weakest position have the least interest in a stronger standard.

## What to Build
Make the proof continuous, complete and safe to publish. Prove control rather than balance, using signing challenges that demonstrate current key custody rather than historical address ownership, which is the core and is the gap the current instrument leaves widest. Commit to the liability set cryptographically so customers can verify inclusion without the exchange publishing its book, since liabilities are the half that is currently just asserted. Update continuously rather than quarterly, because solvency at a past instant is not the question anyone is asking. Detect and disclose encumbrance, as assets that exist but are pledged are the failure mode that took down the last cycle. Design the disclosure so it proves solvency without mapping the custody architecture, which is the real constraint and is why continuous proof has not simply been adopted. Monitor signing patterns for anomalies in real time, since a compromise shows in the pattern before it shows in the balance. Model quorum availability and rehearse recovery, because a custody scheme that cannot assemble its quorum has lost the assets as surely as one that was stolen from. Attest to the process as well as the state, since an examiner and an institutional counterparty both want the controls rather than a number. Make verification independently runnable, as a proof that only the exchange can perform is an assertion. And track how many counterparties actually verify, because an unverified proof is a marketing artefact.

## Target Customer
Exchange custody and security leadership, institutional depositors who cannot currently verify anything meaningful, auditors attesting to figures they cannot independently derive, and regulators specifying safeguarding requirements.

## Impact If Built
The instrument's shape was set by what a crisis allowed in weeks and the market accepted it. Proving current control and committed liabilities continuously is the difference between an attestation and a proof.
