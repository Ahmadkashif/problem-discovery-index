# Inferring Where It Landed

**Niche:** [[niches/email-sms-marketing-platforms/email-inbox-placement/profile|Email Inbox Placement]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The mailbox provider knows whether the message reached the inbox and will not say, and every signal needed to infer it is sitting in the platform's own data across thousands of senders.
**Tags:** #bayesian-inference #hidden-markov-models #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #change-point-detection #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to infer where a message landed inside a mailbox provider that will not say — and whoever does it accurately from a cross-brand corpus owns the number the whole channel should be managed on.

## The Problem
Placement is a hidden state. What is observable is a set of consequences: whether recipients at a given provider engaged, how quickly, in what shape, compared with recipients at other providers and with the same provider historically; whether authentication passed; whether complaints rose; whether a sending pattern changed. These are exactly the observations from which a hidden state can be estimated, and the category treats them as unrelated dashboard panels. A brand landing in spam at one provider is visible in that provider's engagement collapse relative to every other, within a day, and is currently discovered weeks later by a specialist with a hunch.

## Why Nobody Has Built This
Placement was treated as an unknowable that specialists navigate by craft rather than as a latent variable to estimate — that framing is the obstacle and it is intellectual rather than technical. Seed panels appeared to solve the problem well enough to prevent a better approach. The signals live in separate systems within the platform. And the cross-brand baseline that makes the inference work requires treating the corpus as an asset, which the category has not done.

## What to Build
Estimate the hidden state. Model placement as a latent variable per sender, provider and segment, inferred from engagement shape, timing, authentication outcomes and complaint signals, which is the core and is a well-posed estimation problem rather than a craft. Use provider-level comparison as the primary instrument, since a sender's engagement at one provider relative to their own engagement elsewhere is a strong and immediate signal that requires no external data. Build the cross-brand baseline, because knowing what normal looks like for this provider this week separates a sender problem from a provider change and is impossible for a single brand. Detect provider policy shifts across the corpus, which affect everyone simultaneously and are currently discovered through community rumour. Incorporate seed panels as one input with appropriate scepticism rather than as ground truth, which is the fix note's subject. Report per-provider and per-segment rather than in aggregate, since placement failures are almost always concentrated. Diagnose the cause with a ranked set of candidates and the evidence, which is what turns an estimate into an action. Predict the trajectory, because reputation degrades gradually and a warning before a block is worth far more than a diagnosis after. Validate against whatever provider feedback exists, so the estimate is calibrated rather than asserted. And report placement with uncertainty as the channel's headline metric, since that is the number the whole channel should be managed on.

## Target Customer
Messaging platforms, deliverability service providers, and the brands whose email programme is managed on a number that cannot see its worst failure.

## Impact If Built
Placement was framed as an unknowable navigated by craft rather than as a latent variable to estimate, which is an intellectual obstacle rather than a technical one. Provider-relative engagement plus a cross-brand baseline detects a spam-folder problem within a day instead of weeks.
