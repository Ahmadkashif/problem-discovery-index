# The Builder Resigned and Owns Nine Apps

**Niche:** [[niches/no-code-app-builders/load-bearing-app-detection/profile|Load-Bearing App Detection]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** Offboarding checklists cover laptops, badges and system access, and nobody asks what the departing person built that other people are using.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to detect the moment an app crosses from a personal convenience into a business process the company cannot lose — before the person who built it leaves — and whoever does that takes the platform governance account, because that crossing is the category's only genuine crisis.

## The Problem
Somebody resigns on the first. The offboarding process runs: hardware returned, accounts disabled on the last day, access revoked. Three weeks later a warranty tracker stops working because its automation ran under the departed person's credentials. Two weeks after that a team discovers the approval app nobody can edit. Nobody at any point in the process asked what this person had built, and the platform that holds that list was never consulted, because it is not on the checklist and nobody owns adding it.

## Why It's Still Broken
Offboarding was designed around a model of software where people consume applications rather than create them, and it has not been updated for a decade in which a large share of employees build things. The no-code platform is usually not integrated with the identity and offboarding workflow, so the ownership data is present and unreachable at the moment it matters. Disabling an account also silently breaks anything running under it, which is correct security practice with an unanticipated consequence nobody mitigates. And the failures appear weeks later, disconnected from their cause.

## What a Fix Looks Like
Put the estate into the offboarding process. On a departure notice, produce the list of apps the person owns, built or is the sole editor of, ranked by usage and criticality, with the dependent systems listed — a query against data the platform already holds, delivered at the moment it is useful. Reassign ownership before the last day rather than discovering the gap afterwards, which requires only that somebody be named. Identify automations and connections running under the departing person's credentials, which is the specific technical failure that happens weeks later and is entirely preventable, and migrate them to a service identity. Require a short handover note for anything above a criticality threshold, prompted while the person is still there and still knows. And run the same check periodically rather than only at departure, since sole-ownership risk exists continuously and the departure is merely when it becomes acute.

## Who Feels the Pain
Teams whose tools break weeks after a colleague leaves; IT administrators inheriting applications with no context; and the departing person themselves, who is often contacted after leaving because nobody else can answer.

## Impact If Fixed
The ownership data exists in the platform and the departure event exists in the directory, and joining them is an integration rather than a capability. The credential-migration step alone removes a failure class that currently surfaces weeks after nobody can connect it to its cause.
