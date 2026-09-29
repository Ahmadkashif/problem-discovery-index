# Authorisation Rate as an Unmeasured Decision

**Industry:** [[payment-processors|Payment Processors]]
**Type:** High Impact
**One-liner:** Every decline triggers a retry decision worth real revenue, the outcome arrives two days later in a settlement file, and almost nobody joins the two.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A transaction is declined. The issuer returns a response code — insufficient funds, do not honour, suspected fraud, invalid account, expired card — from a vocabulary that is standardised on paper and used inconsistently by thousands of issuers in practice. "Do not honour" is the catch-all and carries almost no information about whether a retry will work.

The processor now decides. Retry immediately, retry in six hours, retry on the merchant's next billing cycle, refresh the credential through account updater first, route through a different acquiring connection, request a network token, or give up. For a subscription merchant this decision, repeated across a monthly book, is the difference between a manageable involuntary churn rate and an unmanageable one. For a marketplace it is the difference between a completed checkout and an abandoned one.

The decision is made by rules. A retry schedule configured once, sometimes per merchant, sometimes per decline code, occasionally per issuer for the largest issuers. The schedules are inherited, copied between merchants, and rarely revisited.

The outcome is observable. Whether the retry was approved, whether the transaction eventually settled, whether the cardholder disputed it, whether the subscriber churned that month — all of it lands in the processor's own systems within days. It lands in settlement files and merchant reporting, not in the decisioning path, and the loop does not close.

There is a second cost to getting it wrong that is easy to miss. Excessive retrying against an issuer degrades the processor's own approval rates with that issuer, because issuers score inbound traffic quality. So the retry policy is not merely a per-transaction optimisation; it is a shared resource being spent without measurement.

## Why It's Unsolved
The feedback exists on a different timeline and in a different system than the decision. Authorisation is a synchronous, latency-bound path measured in milliseconds. Settlement is a batch file that arrives the next business day. Chargebacks arrive weeks later. Subscriber churn is visible at the end of the month. Joining a millisecond decision to a thirty-day outcome requires an identity that survives all four systems, and in many processors it does not exist cleanly.

Decline codes are the other obstacle. Issuers are not required to be informative and have reason not to be, since a precise code tells a fraudster what to change. So the most common code is the least informative, and any model has to infer the true reason from context rather than read it.

Attribution is genuinely hard. A retry that succeeds may have succeeded because the payday arrived, not because the retry timing was clever. Distinguishing the effect of the policy from the effect of time requires either experimentation or careful causal work, and merchants are reluctant to have revenue-bearing traffic randomised.

And the incentives are split. The processor earns on approved volume, which argues for retrying; the issuer bears the cost of the traffic; the merchant bears the churn. Nobody in the chain owns the full objective function, so the policy defaults to whatever is simple.

## What a Solution Looks Like
A joined event history per payment attempt: the authorisation request and its full context, the decline code, every subsequent attempt, the settlement result, the dispute if any, and the merchant-side outcome. This is an engineering artefact rather than a model and it is the precondition for everything else.

Retry propensity modelled per issuer, decline code, merchant category and time-since-decline, with the timing treated as what it is — a time-to-event problem. The right question is not whether to retry but when the probability of approval is maximised, and that surface differs sharply between an insufficient-funds decline (which resolves on payroll cycles) and a suspected-fraud decline (which usually does not resolve at all).

Honest causal measurement. Holdout groups on a small fraction of eligible traffic, or staggered rollout by issuer, are the only way to separate the policy's effect from the passage of time. A processor with sufficient volume can afford a holdout that is statistically decisive and commercially invisible.

Issuer-specific decline code semantics learned empirically rather than assumed from the specification, since the same code means different things at different issuers and the processor has the data to prove it.

Traffic quality as an explicit constraint. Model the degradation in issuer approval rates caused by retry volume and optimise against the constrained objective instead of the unconstrained one.

## Impact If Solved
Authorisation rate is the number merchants switch processors over, and a percentage point of it across a large book is a very large number. The processor is uniquely positioned to model it — no issuer sees across merchants, no merchant sees across issuers — and is currently spending the resulting advantage on a configuration file. Closing the loop between the decision and the settlement outcome is the highest-leverage data engineering project available in the category.
