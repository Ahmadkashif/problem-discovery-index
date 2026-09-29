# The Threshold Somebody Set in 2019

**Niche:** [[niches/customer-data-platforms/identity-resolution-accuracy/profile|Identity Resolution Accuracy]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The match confidence threshold was set during implementation by a consultant who is long gone, applies to every use case identically, and has never been revisited.
**Tags:** #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #quick-win #descriptive-statistics #bayesian-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to measure how often the identity graph merges two people or splits one — and whoever makes that measurable turns the category's central function from a threshold into an engineering discipline.

## The Problem
There is a number in the configuration. Records matching above it are merged; below it they are not. It was chosen during implementation, probably from a vendor default, by someone who no longer works there, before the organisation added three data sources and lost most of its cookie coverage. It applies identically to marketing suppression, personalisation, lifetime value reporting and privacy request fulfilment — use cases with opposite error preferences. It is the most consequential parameter in the customer data stack, it is a single number in a settings page, and nobody in the organisation knows what it is or what it does.

## Why It's Still Broken
The threshold is presented as a configuration setting rather than as a policy decision, which means it receives the attention a setting receives — the interface framing determines the governance. Its consequences are invisible in both directions. Changing it would change profiles and downstream numbers in ways nobody can predict without the measurement that does not exist. And no one owns it.

## What a Fix Looks Like
Make it a governed decision. Surface the threshold and what it means to the people accountable for its consequences, which is the fix and starts with the fact that most organisations cannot currently say what theirs is. Show the effect of moving it — how many profiles would merge or split, and which — so a change is a reviewable proposal rather than a leap. Set it per use case rather than globally, since suppression and privacy should be cautious about merging and marketing reach can afford not to be, and one number cannot express both. Express the choice in business terms: how many people would you accept seeing someone else's data, against how many duplicated customers. Review it on a schedule and whenever a data source changes, because the graph's behaviour shifts underneath a fixed threshold. Record the rationale, so the next person inherits a decision rather than a number. Escalate it to a governance forum, since it is a privacy-relevant policy rather than an engineering setting. Alert when the graph's behaviour drifts at a fixed threshold, which is the signal that the parameter has stopped meaning what it meant. Provide a recommended setting from measured error rates, connecting to the build note. And report the threshold and its consequences in the organisation's privacy documentation, because a probabilistic decision about who someone is belongs there.

## Who Feels the Pain
Organisations whose personalisation and suppression rest on an inherited number; privacy teams whose obligations depend on a setting they have never seen; and customers merged with or split from themselves by a default.

## Impact If Fixed
The interface presents a policy decision as a configuration setting, so it gets the attention a setting gets. Surfacing it, showing the effect of moving it and setting it per use case turns the stack's most consequential parameter into a governed choice.
