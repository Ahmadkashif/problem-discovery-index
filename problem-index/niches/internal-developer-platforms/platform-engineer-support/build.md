# A Help Desk for Your Own Abstractions

**Niche:** [[niches/internal-developer-platforms/platform-engineer-support/profile|The Platform Engineer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platform engineers spend their weeks answering questions about the abstractions they built, in a support channel with no ticketing, no metrics and no way to tell whether the same question has been asked forty times.
**Tags:** #bert #k-means-clustering #large-language-models #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop a platform team being the help desk for its own abstractions — and whoever does that takes the platform function, because that support load is what prevents the platform improving.

## The Problem
The platform channel has two hundred messages a week. Most are questions: how do I give this service access to that queue, why did my deployment not pick up the new configuration, what is the right way to add an environment variable. Each is answered within the hour by a platform engineer who knows the answer and has given it before. The team's roadmap has not moved in two months. Nobody has counted the messages, categorised them, or noticed that a quarter of them concern one confusing concept that a day of work on the abstraction would eliminate.

## Why Nobody Has Built This
The channel is chat, which is convenient for the asker and invisible as a work system. Ticketing has been tried and abandoned in most platform teams, because a form is friction for a colleague and the colleague is frequently blocked. Nobody has framed the questions as product feedback, although that is exactly what they are. And the load is absorbed by individuals whose availability is the reason the channel works, which makes it both sustainable enough to persist and corrosive enough to prevent anything else.

## What to Build
Answer the repeated questions and read the rest as a specification. Deflect with an answering layer over the platform's own documentation, configuration, prior answers and the catalogue, which handles the substantial share of questions that have been answered before and requires no behaviour change from the asker — it answers in the channel where they already are. Retain every answer an engineer gives as a reusable artefact automatically, since the corpus builds itself from work that is happening anyway and is currently discarded. Classify the questions into the three kinds — supported but unexplained, unsupported and unstated, and defect — because each implies a different action and only the third is a bug. Cluster them, since the ranked list of what the platform is most often asked about is the documentation and abstraction backlog derived from evidence. Route the unsupported ones into the gap-capture mechanism from the provisioning niche, since a question about something the platform does not do is a requirement. Measure the channel passively — volume, composition, repeat rate, time consumed — which requires nothing of the askers and is the number that makes the load visible to management. And report it as a measure of the platform's clarity rather than of the team's responsiveness, which is both accurate and the framing under which the team will support being measured.

## Target Customer
Platform engineering leadership, the engineers carrying the channel, and the platform tooling vendors whose products could ship this instrumentation.

## Impact If Built
The support load is the symptom of the platform's own difficulty and consumes the capacity that would reduce it. Passive measurement requires nothing of the askers, and the clustered question list is the platform backlog derived from evidence rather than from the team's assumptions.
