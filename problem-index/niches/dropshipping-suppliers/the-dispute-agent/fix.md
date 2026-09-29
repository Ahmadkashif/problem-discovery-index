# The Same Case Decided Both Ways

**Niche:** [[niches/dropshipping-suppliers/the-dispute-agent/profile|The Dispute Agent]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** Two identical disputes reach two agents on the same afternoon and get opposite outcomes, and nobody at the platform can tell, because consistency is measured nowhere.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #confidence-intervals #compliance #quick-win #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to give the dispute agent evidence instead of two accounts — and whoever does that makes the platform's adjudication defensible, which is what merchants are actually buying.

## The Problem
Two merchants with the same complaint about the same supplier on the same product get different answers. One is refunded, one is refused. Both talk to other merchants. The conclusion the community reaches is that the outcome depends on which agent you get, which is corrosive in a way no individual bad decision is — it turns every future adjudication into a negotiation and every refusal into a grievance. The platform has no idea this is happening, because it measures resolution time and satisfaction scores and has never measured whether two similar cases get similar answers.

## Why It's Still Broken
Consistency requires defining case similarity, which nobody has done, so it cannot be measured. Decisions are recorded as an outcome and a free-text note, which resists analysis. Policy is written in prose and interpreted individually. And the inconsistency is only visible from outside, where merchants compare notes and the platform does not listen.

## What a Fix Looks Like
Measure consistency, then engineer it. Classify disputes into a small set of case types with structured attributes, which is the prerequisite — without a definition of similar, consistency is not a measurable property. Report outcome distributions by case type and by agent, which is a single query once the classification exists and reliably exposes the two or three agents and case types responsible for most of the variance. Run calibration exercises where agents decide the same real cases independently, since inter-rater agreement is the direct measurement and is currently unknown. Show precedent at decision time — here are eleven similar cases and how they went — which is the most effective consistency mechanism available and requires no policy change. Convert recurring case types into explicit decision rules, so the common situations stop being judged individually. Record structured rationale rather than free text, which makes review possible and takes less time than writing a note. Track appeals and reversals by case type and agent, because a reversal is the clearest available signal of a wrong decision and is currently used only to correct the individual case. Publish the decision framework to merchants, since predictability is most of what they want and an explained refusal is far better received than an arbitrary one. Feed decided cases back as training material, which is how new agents currently learn by accident. And report consistency as an operational metric alongside handling time, because what is not measured will drift back.

## Who Feels the Pain
Merchants who conclude outcomes depend on luck; agents blamed for inconsistency they cannot see; and platforms whose adjudication is their core promise and is unmeasured.

## Impact If Fixed
Perceived arbitrariness is more corrosive than any individual bad decision, and the platform measures handling time instead. Classifying case types makes consistency measurable at all, and showing precedent at decision time fixes it without changing policy.
