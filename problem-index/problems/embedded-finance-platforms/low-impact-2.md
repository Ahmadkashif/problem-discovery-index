# FBO Ledger Reconciliation

**Industry:** [[embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Customer funds sit pooled in a bank's for-benefit-of account and the only record of who owns what is a sub-ledger, which must reconcile continuously and provably or the failure mode is people losing access to their money.
**Tags:** #change-point-detection #gradient-boosting #k-nearest-neighbors #time-series-forecasting #evaluation-metrics #feature-engineering #data-integration #compliance

## The Problem
End customers of a fintech programme do not usually hold individually titled bank accounts. Their funds sit in a pooled for-benefit-of account at the sponsor bank, and ownership is recorded in a sub-ledger maintained by the platform, sometimes with the programme maintaining its own ledger on top of that.

Three ledgers must agree: the bank's record of the FBO balance, the platform's sub-ledger sum, and the programme's own record. They disagree routinely for ordinary reasons — a payment in flight, an ACH return not yet posted, a card authorisation held but not captured, a fee assessed at a different moment, a reversal applied to a different period.

Most breaks are timing and resolve. Some are real. Distinguishing them is the work, and it is done by a reconciliation team comparing files.

The stakes are not ordinary accounting stakes. If the sub-ledger and the FBO position cannot be reconciled, nobody can say with certainty who owns what, and the practical result is that end customers cannot access their own deposits. That is what happened when Synapse collapsed, and it is the event that defines the risk profile of the entire category.

Multi-bank programmes multiply it. Funds spread across several sponsor banks for capacity or insurance reasons require a reconciliation per bank plus an allocation model, and the allocation model is itself a source of breaks.

## What Already Exists
Modern Treasury, Increase and several platforms provide ledger infrastructure with double-entry guarantees. Banks provide statement and transaction files. Reconciliation tooling exists generically. Post-Synapse, the market has moved toward platforms that maintain a verifiable ledger and toward individually titled accounts where the economics permit.

## The Customisation Gap
Break classification is manual and repetitive. Breaks fall into a modest number of causes — in-flight ACH, pending authorisation, fee timing, return not posted, duplicate file, genuine error — and classifying them against historical resolutions is directly supervised and largely unattempted.

Nothing anticipates. A break is usually preceded by an observable event: a file arriving late, a volume anomaly in a programme, a settlement window shifting for a holiday, a programme deploying a change. Reconciliation runs as a daily post-mortem rather than as a monitor with a forecast.

Per-customer provability is the gap that matters most and is treated as an accounting nicety. Reconciling totals is not the same as being able to prove, for each individual end customer, the sequence of entries that produced their balance and that it is backed by funds at a named bank. The totals-only approach is what fails catastrophically.

And multi-bank allocation is rule-driven and rarely optimised against the constraints that actually bind — insurance limits, bank capacity, settlement timing — which makes it a source of avoidable breaks.

## Impact If Solved
This is the control whose absence produced the category's defining failure and the question every bank partner and every regulator now asks first. Classifying breaks automatically, anticipating them from their precursors and maintaining per-customer provable backing turns the platform's largest existential risk into a reportable control, which is also the strongest thing it can show a prospective bank partner.
