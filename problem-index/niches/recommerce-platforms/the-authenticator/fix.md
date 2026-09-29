# No Way to Say I Am Not Sure

**Niche:** [[niches/recommerce-platforms/the-authenticator/profile|The Authenticator]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The decision field accepts genuine or counterfeit and nothing else, so an authenticator with real doubt must convert it into a confident-looking call, and the doubt disappears from every record the business keeps.
**Tags:** #worker-facing #confidence-intervals #evaluation-metrics #compliance #descriptive-statistics #hypothesis-testing #quick-win #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to let an authenticator make a hard call properly rather than quickly — and whoever does that keeps the capability, because the expertise takes years to build and the conditions it is exercised under are what drive it away.

## The Problem
An authenticator is sixty percent confident an item is genuine. The system offers two options. They pick one. The record shows a definite call, the item proceeds or is returned as though the question were settled, and the sixty percent is lost — to the business, which would have wanted to treat that item differently, to the reference data, which would have benefited from knowing which items are hard, and to the authenticator, who is now accountable for a certainty they never claimed. Multiply by every uncertain item and the platform has a dataset of confident decisions that contains no information about where its capability is weak.

## Why It's Still Broken
The database field is binary because the business outcome is binary — the item is either listed or returned — and nobody separated the judgement from the action. A confidence scale implies a process for the middle, which does not exist. Recording uncertainty looks like recording weakness. And nobody has asked the authenticators, who would all say the same thing.

## What a Fix Looks Like
Separate the judgement from the action. Record a confidence level alongside the decision, which costs one field, changes nothing operationally on its own, and immediately creates the dataset showing where the capability is weak — this is the fix and it can ship this week. Define what happens in the middle: a second reading, additional imaging, a request for further evidence from the seller, or a decline with a clear and non-accusatory explanation. Route by confidence rather than forcing a call, so the expert's uncertainty becomes an operational trigger. Track low-confidence items by brand, model and production period, since a cluster of them identifies exactly where the reference data needs work. Follow up on low-confidence accepts, since they are the items most likely to become an incident and are identifiable in advance. Use confidence in the seller communication, because a declined seller told the item could not be verified with confidence is treated better than one told it failed authentication. Report the confidence distribution as a capability metric, since a rising share of uncertain calls in a category is the earliest possible warning that the counterfeits have improved. And protect the authenticator who declares uncertainty, since a culture that rewards confident calls will produce them regardless of the field.

## Who Feels the Pain
Authenticators forced to state a certainty they do not have; sellers declined on a coin flip; and platforms holding a dataset of confident decisions that conceals exactly where they are weakest.

## Impact If Fixed
One field costs nothing operationally and creates the dataset showing where the capability is weak. A rising share of low-confidence calls in a category is the earliest available warning that the counterfeits have improved, and today it is invisible by construction.
