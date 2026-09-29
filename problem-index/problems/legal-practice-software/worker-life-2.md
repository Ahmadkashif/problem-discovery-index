# Trust Accounting Support Anxiety

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Type:** Worker Life Changing
**One-liner:** Support staff stop absorbing panicked calls about three-way reconciliation the week before a bar audit, because the system catches the error on the day it happens rather than at quarter end.
**Tags:** #descriptive-statistics #change-point-detection #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #worker-facing #automation

## The Problem
Client funds held in trust are subject to strict rules in every US jurisdiction: separate accounts, no commingling, per-client ledgers, and a three-way reconciliation between the bank statement, the trust account balance and the sum of individual client ledgers. Getting it wrong is not an accounting error, it is a disciplinary matter, and the consequences fall on the lawyer personally.

Practice management platforms implement trust accounting, and the calls that come into support about it are unlike any others in the product. They arrive urgent, often from a firm that has discovered a discrepancy while preparing for an audit or a bar filing, frequently concerning transactions from months earlier. The support representative is being asked to explain a variance in someone's fiduciary account under time pressure, with limited visibility, to a caller who is frightened.

The underlying error is usually mundane — a disbursement recorded against the wrong client, a fee transfer taken before it was earned, a deposit applied to an operating account, a bank fee against a trust balance. Any of them would be trivial to correct on the day. Months later, with dependent transactions on top, it is an unpicking exercise.

## Why It Matters to the Worker
Trust support is emotionally the hardest queue in the product. Representatives are not accountants and cannot give legal or ethics advice, but the caller is treating them as the person who will make this all right. They must be precise, calm, and careful not to say anything that sounds like advice, on a matter that could end the caller's career.

It is also the queue where a representative's help is most constrained by how late the problem is found. Everyone involved knows the error was visible months earlier and that nothing looked at it. The representative absorbs the consequence of a monitoring gap they did not create and cannot fix.

## What a Solution Looks Like
Continuous reconciliation instead of periodic. The three-way reconciliation should run every day against every account, and any variance should surface the day it appears, when the causing transaction is still obvious and reversible.

Anomaly detection on the transaction stream itself, tuned to the specific error patterns this domain produces: a disbursement exceeding a client's ledger balance, a fee transfer without a corresponding invoice, an operating expense against a trust account, a client ledger that has been negative at any point. These are deterministic checks with clear rules, and the reason they are not universally enforced is product convention, not difficulty.

For support, the queue changes shape entirely: instead of forensic reconstruction, a representative is handling a variance that is days old with the causing transaction already identified.

## Impact If Solved
Trust compliance is the highest-consequence, lowest-tolerance function in a small law firm, and the software that holds it currently reports on it at month end. Moving detection to the day of the transaction removes an entire class of career risk for the customer and the most stressful recurring work in the vendor's support organisation.
