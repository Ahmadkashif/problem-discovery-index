# Prediction Treated as Configuration

**Niche:** [[niches/payment-processors/authorisation-performance/profile|Authorisation Performance]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decisions that determine merchant revenue — whether to retry a decline, when, through which route — are made with static configuration files by businesses running five-nines infrastructure.
**Tags:** #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #survival-analysis #optimization-fundamentals
**Contested on:** This niche is not terminal — recovering a decline and preventing one are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A transaction is declined. What happens next — retry in an hour, retry in three days, retry twice, refresh the credential, route differently, or stop — is determined by a configuration the merchant or the processor set, largely from convention and folklore about what works. The decision is worth real revenue at scale, it is made millions of times a day, and the evidence that would settle it arrives two days later in a settlement file in a different system. The industry's most consequential operational decisions are made by a settings page inside businesses that are otherwise engineering-led to an extraordinary standard.

## Why Nobody Has Built This
The processing infrastructure was the hard problem and the decisioning inherited configuration because that is what the infrastructure exposed — the engineering excellence went into the rails and the settings page was always temporary. The outcome arrives in settlement, in a different system, owned by a different team, and nobody joins it. Merchants ask for control, which reinforces configuration. And authorisation rate improvements are attributed to relationships and routing rather than measured.

## What to Build
Turn the settings into models. Join every authorisation attempt to its settlement outcome, which is the prerequisite and is the corpus niche's build — the decision and the result exist and nobody connects them. Predict the value of each available action rather than executing a rule, which is the core reformulation and applies to retry, routing, tokenisation and credential refresh alike. Model issuer behaviour individually, since issuers differ enormously in how they use decline codes and how they respond to retries, and treating them as uniform discards the most useful available structure. Learn the timing, because when to retry is as consequential as whether and is currently a round number somebody chose. Distinguish a temporary decline from a permanent one, which the code vocabulary does badly and the observed outcomes reveal — this is the fix note's subject. Account for the cost of a retry, including network fees and the risk of an issuer penalising excessive attempts, so the optimisation is against net value. Feed the merchant's own context in, since a subscription renewal and a one-off purchase warrant different persistence. Experiment deliberately, since the processor can randomise at scale and learn causally rather than observationally — an advantage almost nobody in this analysis has and this category does. Report the uplift honestly against a baseline configuration, because the whole claim is that prediction beats convention and it should be demonstrated. And expose it to merchants as an outcome rather than as a control, which is the product change that lets the processor take responsibility for the number it is judged on.

## Target Customer
Processors and platform acquirers competing on authorisation rate, large merchants for whom a percentage point is material, and the optimisation vendors selling into the gap.

## Impact If Built
The engineering excellence went into the rails and the settings page was always temporary, and the decisions worth the most revenue still live there. Joining attempts to settlement outcomes and predicting each action's value turns folklore into a measurable advantage the processor can be judged on.
