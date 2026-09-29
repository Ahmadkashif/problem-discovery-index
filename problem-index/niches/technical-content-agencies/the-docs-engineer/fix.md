# The Build Broke and Only One Person Can Fix It

**Niche:** [[niches/technical-content-agencies/the-docs-engineer/profile|The Documentation Engineer]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The documentation site has not deployed since Tuesday and the person who understands the pipeline is on leave.
**Tags:** #worker-facing #quick-win #workflow-orchestration #automation #compliance #evaluation-metrics #data-integration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to stop a documentation platform everyone depends on resting on one person's spare time — and whoever supports that role takes the account.

## The Problem
The documentation pipeline is a chain of components assembled over years: a generator with custom plugins, a search integration, a reference build from the product's source, a redirect map, a deployment. One person understands how it fits together. When it breaks and they are unavailable, nothing publishes, nobody else can diagnose it, and the team discovers how much of the setup exists only as that person's knowledge.

## Why It's Still Broken
Nothing is written down — a pipeline assembled incrementally by one person with no documentation works perfectly until the day it does not, and there is never a moment before that day when writing it up feels urgent. The role is unrecognised. There is no second person. And the setup is only complex because it grew.

## What a Fix Looks Like
Write the runbook and have somebody else run it once. Document the pipeline end to end — components, versions, credentials, deployment, recovery — which is the fix and is a day against a real continuity risk. Have a second person build and deploy the site once from the runbook, which surfaces everything the document missed. Reduce the custom components where a standard one would do, since bespoke plugins are most of the fragility. Pin versions so an upstream change cannot break the build unannounced. Monitor the site and the build, so a failure is known rather than noticed. Keep a tested rollback to the last good build. Move credentials and access out of one person's accounts. Schedule the documentation as work rather than expecting it from spare time, since there is none. Allocate the role explicitly even at a fraction of a person, which is the organisational half. And treat the pipeline as infrastructure with an owner rather than as a thing that works.

## Who Feels the Pain
Writers whose finished work cannot publish; readers looking at stale documentation; the one person who cannot take leave without consequences; and the team, when that person resigns.

## Impact If Fixed
A pipeline assembled by one person with no documentation works perfectly until the day it does not, and writing it up never feels urgent before then. A day on a runbook, tested by someone else, removes the dependency.
