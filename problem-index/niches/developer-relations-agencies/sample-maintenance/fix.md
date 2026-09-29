# The Repository From the Conference Talk

**Niche:** [[niches/developer-relations-agencies/sample-maintenance/profile|Sample & Tutorial Maintenance]]
**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The sample linked from a popular talk has had open issues saying it does not build for over a year.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #data-integration #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep dozens of sample applications and tutorials working, because a developer's first experience of the product is running one — and whoever maintains them takes the account.

## The Problem
A sample repository from a well-attended talk continues to receive traffic long after the talk. Its issue list contains reports that it no longer builds, going back months, unanswered. Every developer who follows the link has the same experience. The repository is public, carries the company's name, and is the most visible artefact of a programme whose purpose is to make the product look approachable.

## Why It's Still Broken
Nobody owns it after the event — a repository created for a talk has no maintainer once the talk is over, and the issues accumulate where prospective users can read them. Nothing tests it. Nobody monitors the traffic. And the advocate who created it has moved on.

## What a Fix Looks Like
Inventory the samples, check them, and act on each one. List every public sample the programme has produced, with its traffic and its issue state, which is the fix and is a morning's work and usually a shock. Run each one and record whether it works, which is the only fact that matters. Fix, archive or clearly deprecate each — those are the three options and leaving it as it is should not be one. Answer or close the open issues, since an unanswered issue saying the sample is broken is worse than the breakage. Assign an owner to the samples that stay, even nominally. Add a test to the ones with real traffic. Mark archived samples unmistakably in the repository and in any content linking to them. Update the links in talks and posts where possible, or add a note. Track the sample inventory as a standing asset rather than an accumulation. Make creating a sample include deciding who maintains it. And prioritise by traffic, since a handful carry almost all the first impressions.

## Who Feels the Pain
Developers evaluating the product who hit a broken build; the company's public repositories, full of unanswered breakage reports; advocates whose past work is now a liability; and the programme's credibility with exactly the audience it exists to reach.

## Impact If Fixed
A repository created for a talk has no maintainer once the talk is over, and the issues accumulate where prospective users read them. A morning's inventory tells you which of them are still making a first impression.
