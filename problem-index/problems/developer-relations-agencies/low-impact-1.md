# Community Health and Question Triage

**Industry:** [[developer-relations-agencies|Developer Relations Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A developer community is measured by member count and message volume, both of which rise as a community fills with unanswered questions from people who leave.
**Tags:** #graph-neural-networks #bert #large-language-models #k-means-clustering #gradient-boosting #evaluation-metrics #dbscan #worker-facing

## The Problem
Developer communities in Discord, Slack and forum platforms are reported on by member count, messages per day and active users. Those numbers can improve while the community gets worse: a channel filling with questions nobody answers has high message volume and is failing everyone in it.

The meaningful quantities are different. What proportion of questions receive a useful answer, and how quickly. Whether answers come from the company or from other community members — the second being the only version that scales. Whether newcomers get a response to their first question, which determines whether they return. Whether a small group is carrying all the answering and is heading for burnout.

Triage is the daily problem. Questions arrive continuously, mixed with discussion, across several channels and often several platforms. Many are duplicates of questions answered last week or documented already. Some are genuine bugs that should be issues. A few are from a major customer and nobody realises. Sorting that is manual and done by whoever is online.

## What Already Exists
Community CRM tools — Common Room, Savannah, and Orbit before it wound down — aggregate activity across platforms and attempt to identify influential members and connect community identity to product usage, which is the most serious existing attempt. Discord and Slack provide basic analytics. Forum platforms like Discourse have genuinely thoughtful trust and moderation mechanics. Bots handle routing, welcome messages and simple automation. Support platforms sit separately and rarely connect.

## The Customisation Gap
The analytics measure activity because activity is easy; the health of a developer community is a property of its answer graph. Response rate to questions, time to first useful answer, the proportion of answers coming from non-staff members, first-question response rate for newcomers, and the concentration of answering effort across members are all computable from the same message data and reported by nothing.

Triage is the second gap and is directly addressable. Classifying an incoming message as a question, a bug report, a feature request or discussion; recognising that it duplicates an answered question or is covered by documentation; assessing urgency; and identifying which community members have answered similar questions before — that is a routing problem with abundant training data in the community's own history.

The third gap is that answered questions are a documentation signal and are treated as ephemeral chat. A question asked repeatedly in a community is a documentation gap with a measured frequency, and the community's own answers are the raw material for the page that would stop it recurring. Nothing connects the two.

And the customisation is per-community norms: response expectations, tone, and what counts as a reasonable answer differ enormously between a community around a database and one around a frontend framework, so thresholds and classifications fitted globally will misjudge both.

## Impact If Solved
Community health determines whether a developer programme compounds or churns, and it is currently reported by metrics that can improve as it deteriorates. Answer-graph measurement surfaces the failures that matter — unanswered newcomers, concentrated answering load, declining community self-sufficiency — and triage automation addresses the largest recurring time cost, while turning repeated questions into a ranked documentation backlog closes a loop that currently leaks entirely.
