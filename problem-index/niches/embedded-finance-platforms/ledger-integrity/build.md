# Continuous Proof of Reconciliation

**Niche:** [[niches/embedded-finance-platforms/ledger-integrity/profile|Ledger Integrity]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The sub-ledger is the only record of who owns the pooled customer funds, and its correctness is checked on a daily or monthly cycle rather than proved at every moment.
**Tags:** #change-point-detection #graph-theory #evaluation-metrics #automation #compliance #hypothesis-testing #confidence-intervals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that the sub-ledger's record of who owns what matches the money actually held at the bank — and whoever can prove it at any moment rather than at month end wins the accounts where a break means customers lose access to their money.

## The Problem
The bank holds one balance for the for-benefit-of account. The platform's sub-ledger says that balance belongs to four hundred thousand end customers in specific amounts. Those two must agree, and the sum of the sub-ledger must agree with the bank, and the network settlement must agree with the authorisations recorded, and the pending holds must agree with what is actually encumbered. All of this is checked when a file arrives — daily at best, monthly in places — which means a discrepancy created on the third is discovered on the thirtieth, by which time the transactions that caused it are buried under a million others.

## Why Nobody Has Built This
Reconciliation inherited its rhythm from bank file delivery, which is daily, so the system was designed around the file rather than around the event — and nothing forced a redesign because the files kept arriving and the breaks kept eventually being found. Continuous reconciliation requires a real-time view of a bank balance that many partners do not expose. Attribution from a break to its cause requires lineage the ledger does not record. And breaks have historically been resolved by manual investigation, which works until volume makes it impossible.

## What to Build
Prove the invariants continuously. Maintain the reconciliation invariants as live assertions — sub-ledger sum equals bank balance, authorisations equal settlements plus pending, holds equal encumbrances — evaluated on every event rather than on every file, which is the core and converts a periodic check into a property of the system. Detect the break at the transaction that caused it, since a break found within minutes is attributable and one found at month end is archaeology. Record lineage on every ledger entry so that any balance can be decomposed into the events that produced it, which is what makes attribution possible at all. Model expected settlement against authorisation to flag the missing and the unexpected before the file confirms them, because settlement lag is predictable and deviations from it are informative. Classify break types automatically — timing, duplicate, reversal, fee, rounding, genuine loss — since most breaks are one of a handful of shapes and classification routes them. Quantify customer exposure per break immediately, because the only question that matters is whether anyone's access to their money is affected. Reconcile per programme as well as in aggregate, which localises a break to the product that caused it. Keep an immutable audit trail, since this record is what a bank and an examiner will test. Surface the invariant state continuously to both engineering and finance, so the two teams see the same number. And report mean time to detection as the function's metric, because a reconciliation process is only as good as how quickly it notices.

## Target Customer
Platform engineering and finance operations leadership, sponsor banks whose FBO accounts depend on this, and ledger infrastructure vendors selling correctness without proof of it.

## Impact If Built
The reconciliation rhythm was inherited from bank file delivery and nothing since has forced a redesign. Continuous invariant evaluation with entry-level lineage turns month-end archaeology into detection at the causing transaction.
