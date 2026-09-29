# Settlement and Fee Reconciliation

**Industry:** [[payment-processors|Payment Processors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Money moves through networks, currencies, fee schedules and settlement timetables that each report differently, and the work of proving the totals agree is done by people with spreadsheets.
**Tags:** #gradient-boosting #k-nearest-neighbors #change-point-detection #time-series-forecasting #evaluation-metrics #feature-engineering #data-integration #workflow-orchestration

## The Problem
An authorisation becomes a capture, a capture becomes a clearing record, clearing becomes a settlement position, and settlement becomes money in a bank account — across several networks, sometimes several currencies, net of interchange, network assessments, scheme fees and the processor's own pricing, less chargebacks and refunds, plus or minus timing differences.

Each party reports its own version. The networks send files in their own formats on their own schedules. Issuers dispute and reverse. Currency conversion happens at a rate set at a moment that has to be reconstructed. Interchange is a matrix of hundreds of rates that depend on card product, merchant category, transaction characteristics and whether the transaction qualified for a rate it was priced at.

The reconciliation team proves that the bank account matches the ledger matches the network files. It rarely matches on the first pass. Breaks are investigated individually: a capture that never cleared, a refund netted in a different period, a fee assessed at a rate nobody expected, a duplicate file, a downgrade where a transaction failed to qualify for its intended interchange rate.

Interchange downgrades are the recurring quiet leak. A transaction that should have qualified for a lower rate and did not, because of a missing data element or a late capture, costs basis points on every occurrence and is visible only in a reconciliation that few merchants and not all processors perform in detail.

Month end concentrates all of it into a week.

## What Already Exists
Network file specifications are published and stable. Reconciliation platforms exist (Modern Treasury, Sigma, FloQast and a long tail of ledger tooling). Most large processors have built substantial internal reconciliation engines. Interchange qualification rules are documented by the networks.

## The Customisation Gap
Break classification is the manual core. A reconciliation break has a cause, the causes repeat in a few dozen patterns, and the platform reports the break rather than the pattern. Classifying breaks from their own characteristics — amount, timing, counterparty, file, transaction attributes — against historical resolutions is directly supervised and nobody does it.

Downgrade attribution is unautomated in most shops. Knowing that a transaction downgraded is easy; knowing that it downgraded because the capture was three days late or because an address verification field was absent, and therefore what to change, requires joining the clearing record back to the original authorisation and comparing against the qualification criteria. It is mechanical and it pays for itself in basis points.

Nothing anticipates. Settlement discrepancies have precursors — a file that arrives late, a volume anomaly in a single merchant category, a network fee schedule change effective this cycle — and reconciliation is run as a post-mortem rather than as a monitor.

Fee schedule change management is the last gap: network fee updates arrive as documents, are read by a person, and are implemented in pricing logic by hand, with errors discovered in reconciliation months later.

## Impact If Solved
Reconciliation is pure overhead that scales with volume and consumes its team entirely at month end, and the leaks it is supposed to catch — downgrades, misapplied fees, unbilled interchange — are measured in basis points on very large numbers. Classifying breaks against historical resolutions and attributing downgrades to their cause converts an accounting exercise into a margin recovery programme.
