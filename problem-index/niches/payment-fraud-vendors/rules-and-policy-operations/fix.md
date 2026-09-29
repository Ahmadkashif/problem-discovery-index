# The Rule From the Incident in 2021

**Niche:** [[niches/payment-fraud-vendors/rules-and-policy-operations/profile|Rules & Policy Operations]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody knows why the rule blocking a whole country was written, who wrote it, or whether anything would break if it went.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #compliance #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to manage a rule layer that grows after every incident and is never pruned — and whoever measures what each rule actually does takes back the decisions the model should be making.

## The Problem
The rule blocks all transactions from a particular country, or with a particular bank identification number range, or above an amount for a certain product category. It was added during an incident. The person who added it has left. There is no note explaining what it was for or what conditions would justify removing it. Every year someone asks about it, nobody can answer, and it stays — quietly declining legitimate business indefinitely.

## Why It's Still Broken
Rules are created in an emergency, so documentation is the first thing dropped — and there is no field that makes it mandatory because a form that slows down an incident response would be worked around anyway. Nobody owns the rule after the incident closes. Removing it has a visible downside and an invisible upside. And no report shows what each rule declines.

## What a Fix Looks Like
Document at creation and review on a cadence. Require a rationale, an owner and a review date on every rule, which is the fix and is a small form field that prevents a decade of ambiguity. Report each rule's decline volume and value, since that is the number that makes an unexplained rule discussable. Set a default expiry on incident rules, because an emergency measure should have to be renewed deliberately rather than persist by inertia. Review the oldest and highest-volume rules first, as they carry the most unexamined cost. Test removal on a small traffic slice rather than debating it, which converts an argument into an experiment. Record the incident that prompted each rule, so the context survives the person. Reassign ownership when someone leaves, since orphaned rules are the ones that never change. Show the rule's decline population — who it is actually stopping — because that usually settles the question immediately. Keep a changelog with reasons, as the current log records what changed and not why. And report the count and age of undocumented rules, which is the diagnostic that starts the cleanup.

## Who Feels the Pain
Risk strategists inheriting rules they cannot explain; merchants losing a market to a forgotten rule; data teams whose model is overridden by history; and customers declined for reasons that expired years ago.

## Impact If Fixed
Documentation is the first thing dropped in an emergency and no mandatory field survives an incident response. A rationale, an owner and a default expiry on incident rules prevent the permanent accumulation that follows.
