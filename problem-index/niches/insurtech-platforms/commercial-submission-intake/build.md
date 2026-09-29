# Triage Ranked by Probability of Quote and Bind

**Niche:** [[niches/insurtech-platforms/commercial-submission-intake/profile|Commercial Submission Intake]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier declines most of what it receives and allocates underwriting attention by arrival order and premium size, while holding a complete record of which submissions it has quoted, bound and profited from.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #causal-inference
**Contested on:** Every serious competitor in submission intake is fighting to turn a broker's email attachments into a structured, triaged submission and rank it by the probability it will be quoted and bound — and whoever raises quote-to-submission ratio most takes the account.

## The Problem
An underwriting team receives two hundred submissions a week and can properly underwrite forty. Which forty is decided by a mix of arrival order, premium size, broker relationship and whichever underwriter picked up the file. A submission that would have bound at a good price sits until the broker places it elsewhere; a submission that was never going to fit the appetite consumes two days of work before being declined. The carrier holds years of submissions with their outcomes — declined, quoted and lost, quoted and bound, and the subsequent loss experience of the bound ones — which is exactly the labelled dataset this decision needs.

## Why Nobody Has Built This
Decline reasons are recorded badly or not at all, which removes the labels for the most numerous outcome — the fix note below is the precondition for this build note. Beyond that, the outcome of interest is compound: a submission is worth attention if it will be quoted, and bound, and profitable, and those are three different models whose composition matters. There is also a live selection problem, since the carrier only observes the loss experience of what it bound, and a naive model learns the appetite it already has rather than the appetite it should have — the same structural issue that appears in plaintiff firm intake and merchant underwriting elsewhere in this vault.

## What to Build
A triage score composed of the three things the carrier actually cares about: probability the submission can be quoted within appetite, probability a quote binds given the broker and the account, and expected profitability conditional on binding. Features come from the extracted submission, the loss run's pattern, enrichment data, and — importantly — broker-level history, which underwriters use informally and which is one of the strongest available signals. Output is a ranked queue with the reasoning shown, not a gate: an underwriter must be able to see why a submission ranked low and override it, both because they are frequently right and because the override is the exploration the model needs. Appetite drift is handled explicitly, since a triage model trained on historical decisions will enforce yesterday's appetite indefinitely unless the carrier deliberately samples outside it.

## Target Customer
Carriers and MGAs with submission volume exceeding underwriting capacity, which is most of commercial insurance, and the submission platform vendors competing to own this layer.

## Impact If Built
Quote-to-submission ratio is the efficiency metric of a commercial underwriting operation and improving it means the same underwriters write more of the business worth writing. The speed effect matters as much: in a market where a broker places with whoever responds, moving quote turnaround from days to hours on the accounts the carrier wants is a distribution advantage rather than an efficiency one.
