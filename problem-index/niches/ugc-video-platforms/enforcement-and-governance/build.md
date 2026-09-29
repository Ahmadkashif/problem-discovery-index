# A Decision That Can Be Examined

**Niche:** [[niches/ugc-video-platforms/enforcement-and-governance/profile|Enforcement & Governance]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that can rank a billion videos by subject, context and tone declines to say which passage of one video it objected to.
**Tags:** #large-language-models #cnns #compliance #evaluation-metrics #confidence-intervals #workflow-orchestration #transformers #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make an automated decision that changes someone's income explainable and contestable — and the contest splits cleanly enough that it is not terminal.

## The Problem
A classifier makes an economic determination about a person. The person receives a policy category. They do not learn which part of the video was at issue, how confident the system was, whether a human reviewed it, or what would have to change. They appeal into a queue and frequently receive the same category again. For someone whose livelihood depends on the platform this is a decision they cannot see, contest meaningfully or learn from, made by a system that is entirely capable of explaining itself.

## Why Nobody Has Built This
Explanation is a product decision rather than a technical limit, and the arguments against it — adversarial gaming, appeal volume, legal exposure — have won by default because no counterparty had standing to insist — a capability that creates obligations is not built until something requires it. Appeals are costly and unresourced. The affected creators have no leverage individually. And regulatory requirements are only now arriving.

## What to Build
Explain the decision and build a process that can overturn it. State which passage or element triggered the decision and with what confidence, which is one half and is within the capability of the classifiers already deployed. Build an appeal process that can actually reverse a decision at volume, which is the other half and is an operations problem rather than a modelling one. Surface distribution suppression, since the quiet reduction is the most common and least visible action and creators currently infer it from their own metrics. Tell the creator what would change the outcome, because an enforcement they cannot learn from will recur. Report reversal rates by category, as an appeal process that never overturns anything is not one. Handle the adversarial concern by calibrating the level of detail rather than refusing all of it, since a passage reference is useful to a creator and of limited help to a bad actor. Distinguish an automated decision from a reviewed one in the notification, which is basic and absent. Record the decision and its basis so a later review is possible. Prepare for the regulatory requirement rather than being compelled into it, as reasoned-decision obligations are arriving and a retrofit will be worse. And measure enforcement accuracy, which no platform publishes and which determines whether any of this is working.

## Target Customer
Trust and safety and policy leadership, creators whose income depends on these decisions, regulators requiring reasoned decisions, and governance tooling vendors.

## Impact If Built
A capability that creates obligations is not built until something requires it, which is why explanation is absent rather than impossible. The classifiers already deployed can name the passage and state a confidence, and the appeal process is a resourcing decision.
