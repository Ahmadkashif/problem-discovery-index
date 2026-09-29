# Platform Engineer as Internal Support

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Type:** Worker Life Changing
**One-liner:** Platform engineers spend their weeks answering questions about the abstractions they built, in a support channel with no ticketing, no metrics and no way to tell whether the same question has been asked forty times.
**Tags:** #bert #word-embeddings #k-means-clustering #large-language-models #gradient-boosting #evaluation-metrics #automation #worker-facing

## The Problem
A platform team has a support channel. It is where every question about deployment, configuration, access, pipelines, environments and the platform's own behaviour arrives, from every engineering team, continuously.

The questions are mostly repeats. How do I add a secret. Why did my deployment fail with this message. How do I get access to that environment. Where do the logs go. Why is the template doing this. Each has been answered before, in the same channel, weeks ago, in a thread that is not searchable in any useful way.

The team answers because the alternative is a colleague being blocked. But the channel has no structure — no ticketing, no categorisation, no metrics — so the load is invisible to everyone including the platform team. They know it consumes their week and cannot say how much or on what.

Meanwhile the roadmap slips, and the reason given is support load, which nobody can quantify, so it reads as an excuse.

## Why It Matters to the Worker
Platform engineering attracts people who want to build systems that make other engineers effective, and the reality is being a help desk for their own abstractions. The gap between the intent and the day is a well-documented source of frustration in the discipline.

The interruptions are also continuous and social. A message in a channel from a colleague carries an expectation of prompt response that a ticket does not, so the engineer is interrupted constantly and cannot batch.

There is a specific demoralising quality to answering the same question repeatedly. Every instance is evidence that the platform is confusing, and the engineer is repairing a documentation or design failure by hand, one conversation at a time, without ever having the time to fix the cause.

And the invisibility compounds it. Work that consumes half a week and appears in no system cannot be staffed for, prioritised against, or credited in a review.

## What a Solution Looks Like
Structure the channel. Classifying questions by topic, detecting repeats and measuring volume converts an invisible load into a dataset — and that dataset is simultaneously the support metric and the product backlog, because the most-asked question is the platform's worst interface.

Answer from the corpus. Most questions have been answered before, in the channel, and retrieval over that history plus the platform's documentation resolves a large share without a human.

Route the diagnosable. A failed deployment with a specific error is a classification problem with a known remedy, and the answer should reach the developer at the point of failure rather than through a conversation.

Documentation generated from what is actually asked. The gap between the documentation and the questions is the documentation's real backlog, and it is measurable rather than guessed.

And the load made visible: hours consumed, by topic, per week, which is what lets a platform team argue for either headcount or the time to fix the causes.

## Impact If Solved
Platform teams lose a large and unmeasured share of their capacity to a support channel that has no structure, answering questions whose repetition is itself the product backlog. Structuring it produces both the deflection and the evidence, and the evidence is what finally lets the team spend time on causes rather than instances.
