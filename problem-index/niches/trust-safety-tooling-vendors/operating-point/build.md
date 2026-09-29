# Build: A Decision, Not a Configuration Field

**Niche:** Operating Point & Threshold Setting
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured process for stating what each error costs, computing the operating point that follows, maintaining it as distributions drift, and recording why it sits where it does.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #convex-optimization #compliance #worker-facing #automation
**Contested on:** Whether the number that decides how much harm is missed and how much legitimate speech is removed is chosen with a framework.

## The Problem

Someone types 0.85 into a field.

Behind that number sits a set of judgements nobody made explicitly. How bad is it to leave a piece of harassment up, relative to removing a post that was not harassment. How does that compare for a child safety category, where the asymmetry is extreme, or for a spam category, where it is mild. What the platform owes its users on each side. What the regulatory environment expects. And what the review capacity can absorb.

None of it is written down. The number was chosen by an engineer during integration, or adjusted after a complaint, or set to whatever produced a queue the review team could handle.

Then it stays. Score distributions drift as content changes and as the model is updated. The threshold does not move, so the actual error rates shift underneath a number that looks constant.

And nobody measures where the operating point landed. The false positive rate — legitimate content removed — is the harm the platform is least likely to see, because the affected user appeals into a process rather than showing up in a metric.

## Why Nobody Has Built This

**Stating error costs requires taking a position.** A vendor providing a framework for weighing over-removal against under-removal is expressing a view about which harm matters more, which every vendor avoids.

**The customer does not want to state it either.** Making the trade explicit produces a document saying how much legitimate speech the platform accepts removing, which is uncomfortable to have written down.

**Review capacity is the real constraint.** Thresholds are frequently set to produce a manageable queue, and acknowledging that means acknowledging the operating point is an operations decision.

**The false positive side is invisible.** Wrongly removed content produces an appeal, not a metric, so the cost that should anchor the trade is unmeasured.

**A configuration field is a defensible product.** Giving the customer control means the choice is theirs, which distributes responsibility usefully.

**Nobody asks.** No regulator or buyer currently asks how the threshold was set or what considerations informed it.

## What to Build

**Provide a structured elicitation.** Per category, a short process that makes the customer state the relative cost of the two errors — through paired comparisons, scenario ranking or a stated exchange rate. Uncomfortable, and it produces the input everything else needs.

**Compute the operating point from the stated costs.** Given the costs and the score distribution, the threshold minimising expected harm is a computation. It is the easy half and it is not available anywhere because the input does not exist.

**Support tiering, not a single cut.** Auto-action above, review between, ignore below, with two thresholds set from the costs and the review capacity. Most products offer this and few help set the boundaries.

**Separate the capacity constraint explicitly.** Where review capacity is what actually determines the threshold, say so. A platform whose operating point is set by staffing rather than by harm considerations should know that, and it is frequently the truth.

**Monitor drift and re-optimise.** Score distributions move. A threshold set once is a different operating point a year later, and maintaining it against the stated costs is automatable.

**Measure both error rates.** Sampled review of actioned content gives the false positive rate; sampled review of unactioned content gives the false negative rate. Both are measurable, only the first is occasionally measured, and neither is routine.

**Record the rationale.** What costs were stated, by whom, when, and what the resulting threshold was. This is what makes the decision reviewable and is what a regulator will eventually ask for.

## Target Customer

Platform trust and safety and policy leadership, who own the values judgement and currently have no instrument for expressing it.

Vendors willing to differentiate on decision support rather than on model accuracy, which is a crowded axis with unverifiable claims.

Regulators, who increasingly require platforms to explain their moderation approach and will find that the most consequential parameter was set by an engineer with no recorded basis.

## Impact If Built

The most consequential decision in automated moderation acquires a framework, where it currently has a configuration field and an undocumented judgement.

Separating the capacity constraint from the harm judgement would reveal how often the operating point is actually an operations decision, which is true more often than anyone states.

And measuring both error rates would tell a platform where its operating point actually landed — including the over-removal side, which is the harm it is structurally least able to see.
