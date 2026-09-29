# The Rule Nobody Can Remove

**Niche:** [[niches/neobanks/risk-decisioning/profile|Risk Decisioning]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The rules engine contains four hundred rules, each written after an incident, none ever removed, and nobody can say what any individual one is catching.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #compliance #quick-win #hypothesis-testing #revenue-impact #automation
**Contested on:** This niche is not terminal — judging a stranger at the door and judging an existing customer from their own ledger are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Every rule in the engine was added for a reason: a fraud pattern appeared, someone wrote a rule, the pattern stopped. Four years later there are four hundred rules, many overlapping, several catching nothing, some catching almost entirely legitimate customers whose behaviour happens to match a pattern that was relevant in 2021. Nobody removes any of them, because removing a rule that was added after a loss feels like inviting the loss back, and nobody can demonstrate that a given rule is now useless. The accumulation degrades the customer experience continuously and invisibly.

## Why It's Still Broken
Adding a rule has a clear justification and removing one has none, so the population only grows — the asymmetry between the two actions is the entire mechanism. Nobody measures per-rule precision, so a rule catching nothing looks identical to one catching a great deal. The institution remembers the loss that prompted each rule and not the customers each has cost. And the person who would remove a rule bears the risk of being wrong.

## What a Fix Looks Like
Measure each rule and retire on evidence. Report per-rule hit rate and precision against confirmed outcomes, which is the fix, requires the outcome record, and reliably shows that a large minority of rules catch nothing and a few catch mostly legitimate customers. Report each rule's false positive cost in customers affected, so the two sides of every rule are visible together. Shadow-run candidate removals, evaluating what a rule would have caught without acting on it, which makes removal a measured decision rather than a leap of faith. Deduplicate overlapping rules, since coverage is frequently tripled and the redundancy is invisible without analysis. Attach an owner and an expiry to every rule at creation, which prevents the accumulation rather than remedying it. Record the incident that prompted each rule, so a future reviewer can judge whether the pattern still exists. Review the population on a schedule, which is ordinary model governance applied to a rules engine. Report the total customer impact of the rules layer, which is a number no institution has and which typically changes the conversation. Separate rules that exist for regulatory reasons from those that exist for loss reasons, since only the second are removable on evidence. And measure the rule population over time, because a set that only grows is a set that is not being managed.

## Who Feels the Pain
Customers declined or frozen by a pattern that stopped being relevant years ago; risk teams unable to reason about their own system; and institutions whose false positive rate rises quietly every quarter.

## Impact If Fixed
Adding a rule has a justification and removing one has none, so the population only grows and the asymmetry is the whole mechanism. Per-rule precision against confirmed outcomes, with shadow-run removals, turns retirement from a leap of faith into a measured decision.
