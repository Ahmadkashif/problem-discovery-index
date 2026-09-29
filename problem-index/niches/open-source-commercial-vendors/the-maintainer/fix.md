# The Silent Exit and the Unplanned Succession

**Niche:** [[niches/open-source-commercial-vendors/the-maintainer/profile|The Maintainer]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A maintainer stops without announcing it, the project is not marked as unmaintained, and downstream users discover it months later when a security issue goes unanswered.
**Tags:** #descriptive-statistics #survival-analysis #change-point-detection #hypothesis-testing #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make maintaining a widely used project sustainable for the person doing it — and whoever does that takes the projects, because maintainer departure is the category's most common and least addressed failure.

## The Problem
A maintainer's activity declines over six months and then stops. There is no announcement, because stopping is not a decision anybody makes on a particular day — it is an accumulation of evenings not spent on it. The project remains listed as maintained, its download count continues, and its dependents assume nothing has changed. Four months later a vulnerability is reported and receives no response, and thousands of downstream projects discover simultaneously that their dependency has no maintainer and no successor.

## Why It's Still Broken
There is no convention for declaring a project unmaintained that does not feel like an admission of failure, so maintainers rarely do it. The decline is gradual and its interpretation is ambiguous — a maintainer who has not committed in three months may be busy or may be gone. Succession is uncomfortable to plan and is therefore not planned, in the overwhelming majority of projects. And the downstream users who would benefit from knowing have no mechanism to be told.

## What a Fix Looks Like
Make the status observable and the succession routine. Publish a maintenance status signal derived from observable activity — response latency, release cadence, issue and pull request handling — which lets dependents see the trend rather than discovering the outcome, and is computable from public data with no participation from the maintainer. Make declaring a project unmaintained or seeking maintainers a normal and respected act rather than an admission, which is a convention change the platforms and foundations can lead with a supported status field and a handover path. Establish succession as a routine part of maintainership: a documented second party with publication rights, which addresses both the abandonment risk and the single-credential compromise risk together. Alert dependents when a dependency's maintenance signal declines, which is the notification that would have given those thousands of projects four months of warning. Provide a handover mechanism through the platforms and foundations, since the common obstacle is not unwillingness but the absence of a process. And normalise stepping back with the project continuing, because the current alternative — continuing joylessly or disappearing — is worse for everybody including the dependents.

## Who Feels the Pain
Maintainers who cannot stop without letting people down; downstream users discovering an abandoned dependency during a security incident; and an ecosystem in which stepping back has no respected path.

## Impact If Fixed
The activity signal is public and computable and would convert a silent exit into a visible decline months in advance. A routine succession convention addresses both abandonment and single-credential compromise, which are the two realised failure modes of unmaintained critical software.
