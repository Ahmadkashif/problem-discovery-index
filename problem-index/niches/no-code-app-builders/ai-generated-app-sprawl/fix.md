# Nobody Records That It Was Generated

**Niche:** [[niches/no-code-app-builders/ai-generated-app-sprawl/profile|AI-Generated App Sprawl]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** An app built from a prompt and an app built by hand are indistinguishable a month later, so nobody can tell which apps their author actually understands.
**Tags:** #descriptive-statistics #logistic-regression #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to make a generated application ownable — attributable, reviewable and maintainable — at the rate generation now produces them, and whoever does that takes the enterprise account, because generation without ownership is a governance problem arriving faster than any governance process.

## The Problem
An administrator reviewing the estate finds an app with an odd structure and an automation nobody can explain. They ask the owner, who says they think it came from the AI builder but cannot remember what they asked for. There is no record of the prompt, no record of which parts were generated and which were edited afterwards, and no way to tell how much of this the owner ever understood. The same question will be asked about a growing share of the estate, and the answer will be the same.

## Why It's Still Broken
Provenance metadata is trivially cheap to record at generation time and worthless to record later, which is exactly the shape of thing that gets omitted when a feature ships fast. Nobody asked for it because the questions it answers are asked months afterwards by a different person. And there is a quiet reluctance to label generated output prominently, since it invites scrutiny the feature's adoption metrics do not benefit from.

## What a Fix Looks Like
Record it, which is a schema change rather than a project. Store the prompt, the model and version, the timestamp and the generated definition as immutable metadata on the app. Record subsequent human edits separately, so the proportion of the app the owner actually touched is visible — which is the single most useful signal about how well they understand it and is free to compute. Surface generation provenance in the admin inventory as a filterable attribute, so an administrator can ask which apps were generated, by whom, from what. Retain the prompt in particular, since it is the closest thing to a statement of intent this category has ever had and solves part of the comprehension problem in the inherited-app niche directly — the prompt is the design note nobody ever wrote. Flag generated apps that have never been edited and are in active use, which is the population most likely to contain something the owner does not know about. And report the generated share of the estate over time, so the organisation can see the trend rather than discovering it.

## Who Feels the Pain
Administrators inheriting apps whose origin and intent are unrecoverable; security reviewers who cannot tell deliberate configuration from generated default; and owners asked to explain something they never designed.

## Impact If Fixed
The metadata costs nothing at generation and cannot be recovered afterwards, which makes every month of delay permanently lossy. The retained prompt doubles as the intent record the category has always lacked, and the edited-proportion signal is the best available measure of whether anybody understands a given app.
