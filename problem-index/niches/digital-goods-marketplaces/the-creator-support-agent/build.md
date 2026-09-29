# Cannot Say Why, Cannot Say When

**Niche:** [[niches/digital-goods-marketplaces/the-creator-support-agent/profile|The Creator Support Agent]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A support agent explains to a creator that their earnings are held, cannot say why because the risk system does not tell them, and cannot say when.
**Tags:** #worker-facing #large-language-models #confidence-intervals #evaluation-metrics #workflow-orchestration #compliance #automation #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to let the support agent explain a risk decision to the person it affects — and whoever makes automated holds explainable turns the category's worst customer interaction into an ordinary one.

## The Problem
A creator's payout is held. They contact support. The agent sees a flag with a code and no explanation, a policy page written in generalities, and an instruction not to disclose risk logic. The creator explains that their rent is due, that they have sold on the platform for six years, and asks what they can do. The agent cannot tell them why, cannot tell them how long, cannot tell them what would resolve it, and cannot escalate to anyone who will answer today. They say they understand the frustration. Both people leave the conversation worse off, and this happens dozens of times a day.

## Why Nobody Has Built This
Risk systems are built to be opaque, on the reasoning that explanation enables evasion, and that principle was adopted wholesale from fraud contexts where the counterparty is usually adversarial — here they usually are not, and nobody has revisited it. Support and risk report to different leaders with different metrics. Explainability was not a requirement when the models were built. And the affected party has no leverage.

## What to Build
Build the explanation layer between risk and support. Produce a reason for every hold at the moment it is placed, in terms a person can act on, which is the core — a decision that cannot be explained to the person it affects is a decision that should not be automated. Separate what can be disclosed from what cannot, deliberately and in advance, rather than defaulting the entire decision to secret: most holds rest on ordinary facts like a sales spike or a new payout account, and disclosing those enables nothing. Give the agent the case detail even where the creator gets a summary, since the agent's inability to see anything is what makes the conversation degrading for both parties. State an expected duration with a real distribution, because not knowing when is worse than the hold itself and the platform can compute this from its own history. Tell the creator what would resolve it — identity confirmation, an invoice, an address check — which converts a wait into an action and clears a large share of holds immediately. Route the resolution evidence back into the risk decision automatically rather than into a queue. Prioritise by dependence, since a creator for whom this is their whole income and one with a small side revenue are in entirely different situations and are currently treated identically. Let agents escalate with a real service commitment, which is the only way the escalation path means anything. Measure false positive rate on holds and report it, because nobody currently knows how often this is simply wrong. And design the creator-facing message deliberately, since it is the single most consequential communication the platform sends.

## Target Customer
Support and risk operations at digital goods and creator marketplaces, the agents themselves, and creators whose income depends on payouts.

## Impact If Built
Opacity was inherited from adversarial fraud contexts and never revisited for a counterparty who is usually legitimate. Most holds rest on ordinary facts whose disclosure enables nothing, and stating what would resolve one converts a wait into an action.
