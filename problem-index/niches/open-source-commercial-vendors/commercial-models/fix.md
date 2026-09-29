# Licence Changes Nobody Has Evaluated

**Niche:** [[niches/open-source-commercial-vendors/commercial-models/profile|Commercial Models]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Several well-known projects have changed licences under commercial pressure, each a substantial natural experiment, and none of the companies involved has published what happened to adoption or revenue.
**Tags:** #causal-inference #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #quick-win #revenue-impact
**Contested on:** Every serious competitor here is fighting to convert use of freely available software into revenue — and that contest is fought against the free edition in one model and against a hyperscaler in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
A company considering a licence change looks for evidence about what happens. What exists is commentary: strong opinions on both sides, anecdotes about forks, and assertions about community reaction. Several companies have made this change and each of them has the data — adoption before and after, revenue before and after, contribution rates, fork trajectories — and none has published anything beyond a statement of intent. The next company makes the decision with the same information as the first, which is to say with none.

## Why It's Still Broken
The companies that made the change have no incentive to publish a result that may be unflattering, and a favourable result would be read as self-serving. The analysis is also genuinely confounded, since a licence change coincides with other events and the counterfactual is unobservable. Adoption after the change is particularly hard to measure, which is the adoption visibility problem again. And the public discussion is sufficiently heated that publishing data invites an argument rather than informing one.

## What a Fix Looks Like
Assemble what is externally observable, carefully and from the outside. Use public signals that survive a licence change — dependent public repositories, package download trends, job postings, contribution rates, fork activity and the trajectory of any fork — to construct an adoption series for each event, which is observational and imperfect and is far better than commentary. Apply a proper comparison, using similar projects that did not change licence as a control rather than looking at a before-and-after trend, which addresses the most obvious confounding. Report each case individually rather than pooling, since the circumstances differ enormously and an average across a handful of events would mislead. State the limitations plainly, because the audience is technical and sceptical and an overclaimed analysis will be dismissed entirely. Include the fork outcomes, since whether a viable fork emerged and sustained is the outcome that matters most to the next company and is publicly observable. And invite the companies to contribute their own data under aggregation, since a shared evidence base is in the interest of everyone who has not yet made this decision.

## Who Feels the Pain
Companies facing this decision with no evidence; communities reacting to changes whose consequences nobody has characterised; and an industry conducting the same argument every time a licence changes.

## Impact If Fixed
Several substantial natural experiments have occurred and the externally observable signals survive them, which makes an outside-in analysis feasible today. Using comparable unchanged projects as controls is what separates a finding from a trend, and the fork outcomes are the part the next company most needs.
