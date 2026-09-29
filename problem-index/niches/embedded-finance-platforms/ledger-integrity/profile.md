# Ledger Integrity

**Parent Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Category:** 🔵 High Market Share
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that the sub-ledger's record of who owns what matches the money actually held at the bank — and whoever can prove it at any moment rather than at month end wins the accounts where a break means customers lose access to their money.

## Profile
**Market Size:** ~$1.5B US
**Share of Parent Industry:** ~19% of category revenue
**Digital Adoption:** Moderate — batch reconciliation on daily or monthly cycles
**Target Buyer:** Platform engineering and finance operations leadership
**Automation Potential:** High — a continuous matching and detection problem

## What Makes This a Distinct Niche
Customer funds sit pooled in a for-benefit-of account at the sponsor bank. The bank knows the total. Only the platform's sub-ledger knows whose money is whose, and it is the sole record of that. Every deposit, transfer, card authorisation, reversal, fee and refund must land in it correctly, and it must reconcile against the bank's balance and against network settlement provably rather than approximately. A break is not an accounting inconvenience — it means people cannot reach their money, and it is the failure mode that has ended platforms.

## Current Tools & Gaps
Double-entry ledger implementations, daily bank file reconciliation, network settlement matching, and month-end close processes. The gaps: reconciliation on a cycle rather than continuously; breaks detected long after the transaction that caused them; no attribution from a break to its source; and the sub-ledger's correctness asserted rather than demonstrated.

## Problems
- [[niches/embedded-finance-platforms/ledger-integrity/build|🔨 Build: Continuous Proof of Reconciliation]]
- [[niches/embedded-finance-platforms/ledger-integrity/buy|🛒 Buy: Custody Reconciliation for Pooled Accounts]]
- [[niches/embedded-finance-platforms/ledger-integrity/fix|🔧 Fix: A Break With No Source]]
