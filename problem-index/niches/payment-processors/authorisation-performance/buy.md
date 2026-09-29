# Decision Optimisation Practice

**Niche:** [[niches/payment-processors/authorisation-performance/profile|Authorisation Performance]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sequential decision optimisation under uncertainty is a mature field with real tooling, and payment retry logic is a cron schedule.
**Tags:** #markov-decision-processes #gradient-boosting #optimization-fundamentals #confidence-intervals #evaluation-metrics #monte-carlo-methods #survival-analysis #hypothesis-testing
**Contested on:** This niche is not terminal — recovering a decline and preventing one are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Deciding what action to take, when, under uncertainty, with a cost per attempt and a value on success, is a well-formed problem with a substantial toolkit: sequential decision processes, optimal stopping, bandits for choosing among actions, and survival methods for timing. It is applied in operations, logistics, clinical scheduling and marketing. Payment retry and routing is exactly this shape — a sequence of attempts with costs, an uncertain success probability that varies by issuer and timing, and a clear payoff — and is implemented as a fixed schedule.

## What Already Exists
Sequential decision and optimal stopping frameworks; contextual bandits for action selection; survival models for timing; cost-aware optimisation; and off-policy evaluation from logged decisions.

## The Customization Gap
The adaptation is to an adversarial-adjacent counterparty and a two-day feedback loop. It requires: (1) issuers who respond to the processor's behaviour, since excessive retrying can trigger an issuer to block or penalise a merchant — the environment reacts, which the standard formulations do not model and which caps aggressive optimisation; (2) outcomes arriving two days later in settlement, so the feedback loop is delayed and the state must persist across it; (3) enormous scale with per-attempt costs that are small but not zero, which makes the economics finely balanced and worth optimising precisely; (4) regulatory and network rules constraining retry behaviour, which are hard constraints rather than costs; and (5) merchant-visible behaviour, since a customer seeing repeated declines or unexpected charges is a consequence the optimisation must carry.

## Target Customer
Processor product and data teams, platform acquirers, and optimisation practitioners for whom payment decisioning is an unusually well-posed application.

## Impact If Solved
The problem is a textbook sequential decision under uncertainty and the industry implements a cron schedule. Issuers reacting to the processor's own behaviour is the environmental response the standard formulations do not model and which bounds how aggressive the policy can be.
