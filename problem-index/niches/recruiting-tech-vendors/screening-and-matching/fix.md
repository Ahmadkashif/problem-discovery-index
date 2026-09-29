# Fix: The Match Score Is Presented as a Prediction

**Niche:** [[niches/recruiting-tech-vendors/screening-and-matching/profile|Screening & Matching]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The interface shows "92% match" and the recruiter reads it as a prediction about the candidate, which no evidence anywhere supports.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #quick-win #worker-facing #hypothesis-testing
**Contested on:** Whether the score will be labelled as what it is.

## The Problem

A candidate list shows match percentages. 92%, 87%, 61%. The recruiter reads down from the top.

The number is a similarity score between the application and the job description, or a model's estimate of whether a recruiter would advance this candidate, or a weighted combination of keyword overlaps. It is not a prediction of job performance and no evidence exists that it correlates with one.

The presentation does not say that. A percentage with a decimal, colour-coded, sorted descending, reads as a measurement of fit. So the recruiter treats 87% and 61% as a meaningful difference in candidate quality, and the candidate at 61% is not looked at.

## Why It's Still Broken

The percentage sells. It demos well, it makes the product feel intelligent, and it gives the recruiter a defensible-looking basis for triaging four hundred applications.

Labelling it honestly makes the product look weaker than a competitor's, and there is no standard requiring the label, so the first vendor to be honest loses.

And the recruiter has no way to know. Nothing in the interface or the documentation explains what the number is computed from, so a reasonable user assumes it means what it appears to mean.

## What a Fix Looks Like

Say what the number is, at the point it is shown.

Label it accurately. "Keyword and skill overlap with the job description" or "similarity to previously advanced candidates" — whichever it is — as the column header or immediately beside the score. This is a string change and it substantially changes how the number is read.

Show the components. Which requirements were matched, which were not, and what drove the score. A recruiter who can see that a candidate scored 61% because they lack one keyword can make a judgement; one who sees 61% cannot.

Stop showing a precise percentage. The underlying computation does not support two significant figures. Bands — strong, partial, weak match on stated requirements — are honest and less misleading, and they resist the false-precision sorting that a percentage invites.

Surface the candidates the score buries. A deliberate sample of lower-scored candidates presented alongside the top, so the recruiter sees what the ranking is excluding. This is cheap and it is the only mechanism by which a recruiter ever notices the screen is wrong.

State the limits in the documentation and in the product. This score does not predict job performance and is not validated against it. Every vendor in this category could write that sentence truthfully today.

And record what the recruiter did with it, per candidate, which is what makes the audit possible and is what a growing set of regulatory obligations will ask for.

## Who Feels the Pain

Candidates below a threshold on a number that measures phrasing overlap, never looked at. Recruiters, given a number that looks like a measurement and told nothing about what it is, then held responsible for the decisions they made from it. Employers, whose screening rests on a score nobody in the building could define. And vendors, whose strongest claim is the one they cannot support.

## Impact If Fixed

The number gets labelled as what it computes, which changes how it is read at negligible cost. Components become visible, so a recruiter can override it intelligently. False precision disappears with the percentage. And the sample of lower-scored candidates gives the screen its only chance of being caught when it is wrong.
