# The Same Dispute Decided Both Ways

**Niche:** [[niches/bnpl-providers/disputes-and-arbitration/profile|Disputes & Arbitration]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Two identical non-delivery disputes reach two agents on the same afternoon and get opposite outcomes, and nobody at the provider can tell.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #quick-win #descriptive-statistics #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to adjudicate between a consumer and a merchant on evidence neither supplies — and whoever builds that evidence base decides a dispute rather than splitting the difference.

## The Problem
Two consumers, same merchant, same carrier, same claim, same evidence. One agent finds for the consumer and cancels the remaining instalments; another finds for the merchant and the payments continue. Both agents applied their judgement to an ambiguous case. The provider has no way to know this happened because consistency is not measured, and the two consumers, if they ever compare notes, will conclude the outcome depends on who answered. In a product where the provider is asking consumers to trust it with a credit obligation, that perception is expensive.

## Why It's Still Broken
Consistency requires defining what makes two disputes comparable, which nobody has done, so the property cannot be measured — the absence of a definition is what makes the variation invisible rather than tolerated. Decisions are recorded as an outcome and a free-text note. Agents are measured on resolution volume. And the inconsistency is only visible from outside, where consumers compare and the provider does not listen.

## What a Fix Looks Like
Define comparability and measure it. Classify disputes into types with structured attributes, which is the prerequisite — without a definition of similar, consistency is not a measurable property. Report outcome distributions by type and by agent, which is a single query once the classification exists and reliably identifies where the variation is. Run calibration exercises on the same cases, since inter-rater agreement is the direct measurement and is currently unknown. Show precedent at decision time, because seeing how eleven similar cases were decided is the most effective consistency mechanism available and requires no policy change. Convert recurring types into explicit rules, so the common situations stop being judged individually. Record structured reasoning rather than free text, which makes review possible and takes less time than a note. Track appeals and reversals by type and agent, since a reversal is the clearest evidence of a wrong decision and is currently used only to fix the case. Publish the decision framework to merchants and consumers, since predictability is most of what they want and an explained outcome is far better received. Feed decided cases back as training material. And report consistency alongside resolution time, because what is measured is what the team optimises and currently only one of the two is measured.

## Who Feels the Pain
Consumers whose outcome depended on who answered; merchants experiencing the provider's decisions as arbitrary; and agents blamed for inconsistency nobody has measured or defined.

## Impact If Fixed
The absence of a definition of comparability makes the variation invisible rather than tolerated. Classifying dispute types makes consistency measurable, and showing precedent at decision time fixes most of it without any policy change.
