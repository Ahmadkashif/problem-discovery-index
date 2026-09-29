# Build: Fast Settlement and Landed-Amount Transparency

**Niche:** [[niches/crowdsourcing-platforms/payments-and-micropayments/profile|Payment, Micropayments & Cross-Border]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Settle approved work quickly, underwrite the approval risk with the platform's own data, and show the worker what a dollar earned actually lands as.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #descriptive-statistics #compliance #worker-facing #revenue-impact
**Contested on:** Whether the platform will bear the approval risk it currently passes to the worker.

## The Problem

A worker completes tasks today and may be paid in four weeks. The requester has an approval window; auto-approval sits at the end of it; and the worker's money is held throughout. For someone earning small amounts, a month's lag on the whole balance is the difference between the work being useful and not.

The delay exists to protect the requester from paying for bad work. But the risk is small, measurable and concentrated: most requesters approve nearly everything, most workers are never rejected, and the platform can predict both from its own history with high confidence.

Meanwhile the amount that arrives is unknown until it does. Transfer fees and currency conversion apply at rates nobody shows, on balances where a two-dollar fee is a quarter of the payment.

## Why Nobody Has Built This

Holding the money costs the platform nothing and protects the requester at the worker's expense, which is a comfortable default that nobody has been asked to change.

Fast settlement means the platform carries the approval risk — advancing payment on work that might be rejected — which is a balance-sheet decision, a small one at these amounts, and one nobody has modelled because nobody framed it as underwriting.

And fee disclosure is absent for the same reason as everywhere else in platform labour.

## What to Build

An approval-risk model, a fast-settlement product built on it, and honest payout arithmetic.

**Predict approval.** Probability that a submission will be approved, from the requester's history, the task type, the worker's record and the batch's early approval pattern. For the large majority of work this probability is very high and tightly estimated, and it is the whole basis for settling early.

**Settle immediately where the risk is low.** Pay on submission for work above a confidence threshold, and reconcile the rare rejection afterwards. The expected loss is small, computable, and far smaller than the value of same-day payment to the recipient. This is the product and it is underwriting rather than engineering.

**Shorten the default window.** Auto-approval at four weeks is a platform default. Setting it to a few days, with an extension available on request for requesters who genuinely need it, resolves most of the delay without any risk model at all.

**Remove or minimise the threshold.** Minimum payout thresholds trap small balances, most heavily for new and occasional workers — precisely those for whom the money matters most. Where the cost of a transfer makes a threshold necessary, choose rails where it is not, and pay the difference.

**Show the landed amount.** Gross, fee, FX rate against mid-market, and the local-currency figure that arrives. Six lines, on every payout, with the spread shown as an amount rather than absorbed into a rate.

**Optimise the corridor.** Landed amount by rail and corridor, measured from the platform's own payouts, with routing on the best result and the choice offered where the trade is speed against amount. The platform has the volume to negotiate and the worker has none.

## Target Customer

Platforms competing for worker supply, particularly in a market where the workforce compares platforms openly in forums and where payment speed is a frequent topic. Also the payout providers, for whom sub-dollar cross-border settlement at volume is a distinct technical and commercial problem.

## Impact If Built

Workers are paid in days rather than weeks, which for small and irregular earnings is the difference between the work being worth doing and not. The approval risk sits with the party who can measure and absorb it. And the worker can see what a dollar earned becomes, which is currently unknowable until it arrives.
