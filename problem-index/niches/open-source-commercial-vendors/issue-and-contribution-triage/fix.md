# The Contribution Nobody Wanted

**Niche:** [[niches/open-source-commercial-vendors/issue-and-contribution-triage/profile|Issue & Contribution Triage]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A contributor spends a weekend on a change the project was never going to accept, and finds out in the pull request, because the direction it conflicts with was never written down.
**Tags:** #bert #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to reduce the queue rather than to organise it — and whoever does that takes the maintainer teams, because templates, labels and bots have been standard for a decade and the arithmetic is unchanged.

## The Problem
A contributor implements a feature they need, carefully, with tests and documentation. The pull request sits for three weeks and is then declined, because the maintainers have a view about the project's scope that excludes it, a plan to solve the same problem differently, or a concern about a dependency the contributor could not have known about. The contributor has lost a weekend and will not return. The maintainer has lost the review time and feels bad. The information that would have prevented it — the project's scope, its direction, its architectural constraints — exists in the maintainers' shared understanding and in scattered issue comments, and nowhere a contributor would look.

## Why It's Still Broken
Project direction is held in the maintainers' heads and expressed in individual issue responses, because writing it down is work with no immediate return and feels like committing to something. Contribution guides cover process — formatting, testing, commit conventions — rather than substance, which is the part that actually determines acceptance. The cost falls on the contributor, who is outside the project and whose lost weekend is invisible. And declining a good-faith contribution is unpleasant enough that maintainers delay it, which makes the eventual outcome worse.

## What a Fix Looks Like
State the direction and check before the work. Write down what the project is and is not for, its architectural constraints, and the kinds of change that will not be accepted regardless of quality — which is a page, is uncomfortable to write, and prevents most of this. Require or strongly encourage a short proposal before substantial work, with a fast response commitment, since the cheapest possible rejection is of an idea rather than of an implementation. Extract the implicit direction from the maintainers' own history, since past responses to similar proposals contain the policy and can be surfaced to a prospective contributor and, usefully, to the maintainers themselves who may not have realised they had one. Match a new proposal against past declines and show the reasoning, which answers the contributor's question before they ask it. Maintain a list of changes the project actually wants, which is the positive form and is what converts willing contributors into useful ones. Decline quickly and explicitly rather than slowly and silently, because the slow version is worse for everyone and is chosen out of discomfort. And measure the decline rate and the time to decision, since a project with a high decline rate after long delays is losing contributors it needs.

## Who Feels the Pain
Contributors whose good-faith work is declined after three weeks; maintainers reviewing changes they were always going to refuse; and projects that lose willing contributors for reasons they could have prevented with a page of text.

## Impact If Fixed
Writing down scope and constraints prevents most of this and costs a page. A proposal-first convention with a fast response moves the rejection from an implementation to an idea, which is the difference between a lost hour and a lost contributor.
