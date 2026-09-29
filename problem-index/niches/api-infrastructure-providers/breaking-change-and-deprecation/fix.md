# Deprecation Announced Into Silence

**Niche:** [[niches/api-infrastructure-providers/breaking-change-and-deprecation/profile|Breaking Change & Deprecation]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** An API product manager announces a deprecation, hears nothing, cannot tell whether anyone is migrating, and extends the deadline — repeatedly, forever.
**Tags:** #descriptive-statistics #time-series-forecasting #survival-analysis #evaluation-metrics #confidence-intervals #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a provider exactly which consumers a proposed change would break, before it ships — and whoever does that takes the platform, because the inability to answer it is why nothing is ever retired.

## The Problem
A deprecation is announced with a twelve-month sunset. It goes in the changelog, a portal banner and a response header. Nothing measurable happens. At eleven months the product manager cannot tell whether consumers have migrated, whether the remaining traffic is from active integrations or forgotten scripts, or who would be affected on the day. Turning it off feels like an unbounded risk, so the deadline moves to eighteen months. It moves again. The endpoint is still there four years later, and the team has learned that deprecation deadlines are not real, which makes the next one less effective.

## Why It's Still Broken
The announcement is a communication and nothing measures its effect, so the process has no feedback at all. Traffic to the deprecated endpoint is visible in aggregate and is not decomposed by consumer, so the product manager cannot distinguish two hundred consumers who have not started from four who will never move. Contacting consumers requires the credential-to-owner mapping that nobody maintains. And extending a deadline is free and individually safe, which is why it always happens.

## What a Fix Looks Like
Measure the migration instead of announcing the deadline. Report traffic to the deprecated surface by consumer over time, which turns silence into a curve and is a grouping of data the gateway already has. Classify the remaining consumers: not started, partially migrated, complete — each of which needs a different action, and only the first two need contact. Project the completion date from the observed trend and compare it with the deadline, which is what makes an extension a decision rather than a reflex. Contact the owners directly rather than relying on headers and changelogs, which requires the credential mapping and is the step that actually moves the number. Use graduated enforcement — brief planned interruptions well before the deadline, announced in advance — since the consumers who will not act are precisely those for whom nothing has yet broken, and a scheduled five-minute outage is a kinder discovery than a permanent one. And publish an honest sunset record, because a provider whose deadlines have held before will find the next one much easier.

## Who Feels the Pain
API product managers carrying endpoints they announced the end of years ago; platform teams maintaining versions for consumers who may not exist; and the consumers who will be broken eventually by a deadline nobody believed.

## Impact If Fixed
Per-consumer migration curves are a grouping of existing gateway data and convert an unmeasurable process into a managed one. Graduated interruption before the deadline finds the non-responders while the consequence is still recoverable.
