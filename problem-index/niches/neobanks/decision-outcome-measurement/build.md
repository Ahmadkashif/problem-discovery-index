# The Labelled Dataset Nobody Constructs

**Niche:** [[niches/neobanks/decision-outcome-measurement/profile|Decision Outcome Measurement]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A neobank observes the consequence of nearly every decision it makes in its own ledger, and nobody constructs the dataset because the decision lives in a vendor's system and the outcome lives in operations.
**Tags:** #data-integration #evaluation-metrics #confidence-intervals #gradient-boosting #causal-inference #compliance #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to join several million decisions a year to the outcomes already sitting in the ledger — and whoever assembles that dataset has the only thing that makes every other decision in the institution improvable.

## The Problem
An account is frozen on Tuesday. Within days the institution knows a great deal about whether that was right: the member supplied documents and was reinstated, or the account was closed with confirmed fraud, or the member disappeared, or deposits resumed and continued for a year. Every one of those is a label. The decision was made by a vendor's model, recorded in the vendor's system. The outcome was recorded by an operations team in a case management tool. Nobody joins them. The institution therefore cannot say how accurate any of its decisions are, despite having all the evidence, and the same is true of approvals, declines, holds and dispute decisions.

## Why Nobody Has Built This
The decision and the outcome belong to different teams with different systems and different vendors, and a join that belongs to nobody does not happen — this is a pure ownership gap rather than a technical one. Constructing the dataset would reveal error rates the institution has never had to state. Vendors have no incentive to expose their decisions for evaluation. And the institution's model risk obligations are lighter here than in lending, so nothing forces it.

## What to Build
Build the join and make it the institution's asset. Record every decision with its inputs, the model or rule that made it, and a timestamp, which is the prerequisite and requires vendor cooperation the institution should contractually require. Define the outcome labels carefully for each decision type — what constitutes a correct freeze, a correct decline, a correct hold — since the definitions are genuinely debatable and getting them wrong invalidates everything built on them. Join them continuously rather than as a project, so the dataset grows rather than being reconstructed. Handle the censored outcomes properly, since a declined applicant and a closed account produce no further evidence and treating absence as confirmation is the specific error that makes these systems look better than they are. Estimate the invisible error deliberately, by approving or reinstating a random sample near the threshold and observing what happens, which is the only way to see false positives and is affordable. Report accuracy by decision type, model, vendor and segment, which is what turns the dataset into action. Feed it back into every model and rule, which is the point and is what the rest of this analysis depends on. Use it for vendor evaluation, since a vendor score can now be judged on this population. Support fairness analysis, which becomes possible only once outcomes are joined. And make one team accountable for the dataset, because the reason it does not exist is that it is nobody's.

## Target Customer
Risk and data leadership at digital banks, sponsor banks overseeing programme performance, and the vendors whose scores could be evaluated for the first time.

## Impact If Built
The join belongs to nobody, which is a pure ownership gap rather than a technical one, and it is why an institution with all the evidence cannot state its own error rates. A random sample approved near the threshold buys visibility of the false positives that censored outcomes otherwise hide.
