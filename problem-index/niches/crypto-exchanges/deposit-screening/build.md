# The Control Nobody Has Evaluated

**Niche:** [[niches/crypto-exchanges/deposit-screening/profile|Deposit Screening]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision that freezes a customer's deposit runs on a vendor score and a threshold, and no exchange can state its precision.
**Tags:** #graph-theory #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #hypothesis-testing #cross-validation #expectation-maximization
**Contested on:** Every serious competitor in this niche is fighting to decide correctly whether arriving funds are criminal proceeds — and the contest splits cleanly enough that it is not terminal.

## The Problem
An exchange's entire anti-money-laundering posture rests on deposit screening. The score comes from a vendor, the threshold was set by a compliance team years ago, and the decision to freeze is made thousands of times a month. Ask what fraction of frozen deposits were actually criminal proceeds and there is no answer, because the outcome almost never returns: law enforcement confirms occasionally, a customer produces satisfying provenance occasionally, and the overwhelming majority of cases simply close. The control has been tuned by feel for a decade.

## Why Nobody Has Built This
Ground truth is genuinely scarce, so the absence of measurement looked like an unavoidable condition rather than a solvable one — nobody built for the scarce-label case because the abundant-label case was assumed necessary. The score is a purchased input, which places the model outside the exchange's control. Regulatory incentive runs entirely toward freezing more, which makes false positives costless to the institution. And the customers who bear the error have no channel that produces a statistic.

## What to Build
Treat scarce labels as the design constraint rather than as a blocker. Assemble every resolved outcome the exchange has — law enforcement confirmations, satisfying provenance, subsequent account behaviour, chargeback and complaint records — which is the core asset and is small, expensive and genuinely labelled. Estimate precision from that sample with explicit uncertainty, since a wide interval honestly stated is infinitely more useful than the current nothing. Use the released-and-later-implicated and frozen-then-cleared cases as the two error classes, because both exist in the record and neither is counted. Model the decision rather than consuming the score, so the threshold becomes a choice with a stated cost on each side. Calibrate the vendor score against the exchange's own outcomes, which is possible today and would reveal how much of the score is informative. Run a deliberate sampling regime on cases near the threshold, since that is where information concentrates and where a small labelling budget buys the most. Separate the attribution question from the decision question, which is the decomposition below and is what makes each tractable. Quantify customer harm from false freezes explicitly, because a control measured only on detection will always be set to freeze. Report precision and recall estimates to the board and the regulator, since the institution that measures honestly is in a stronger position than one that cannot answer. And revisit the threshold on evidence rather than on incident.

## Target Customer
Exchange compliance and risk leadership, blockchain analytics vendors whose scores are consumed unevaluated, and regulators examining a control nobody has quantified.

## Impact If Built
Scarce ground truth was treated as a permanent condition rather than a modelling constraint. The resolved outcomes an exchange already holds are a small, genuinely labelled dataset about the one thing the industry claims to measure and never has.
