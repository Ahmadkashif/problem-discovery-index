# Fix: The Band Boundary Is Treated as a Cliff

**Niche:** [[niches/talent-assessment-platforms/score-interpretation/profile|Score Interpretation by Hiring Managers]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The cut score is 70, a candidate scores 69, and the instrument cannot tell the two apart.
**Tags:** #confidence-intervals #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #workflow-orchestration #quick-win #worker-facing
**Contested on:** Whether a cut score will be applied as though it were precise.

## The Problem

An employer sets a cut score. Candidates above it proceed; candidates below it do not. The cut is applied automatically, at scale, by the applicant tracking system.

The instrument's standard error of measurement means the difference between 69 and 70 is noise. A candidate who scored 69 on Tuesday might score 73 on Thursday — the same person, the same ability, a different draw. The cut is treating a measurement error as a decision.

At the boundary, and only at the boundary, this matters enormously: a large number of candidates sit within one standard error of any cut, and every one of them is being sorted by chance. With volume, that is a substantial population excluded arbitrarily.

## Why It's Still Broken

A cut score is operationally necessary — someone has to be advanced and someone not — and a sharp threshold is the simplest way to do it.

The measurement error is also known to the vendor and rarely surfaced to the employer setting the cut. The technical documentation reports it; the configuration interface asks for a number.

And nobody is accountable for the boundary population. They are rejected, they receive no feedback, and they do not appear in any metric.

## What a Fix Looks Like

Treat the boundary as a band, not a line.

Surface the standard error at configuration. When an employer sets a cut score, tell them what proportion of candidates fall within one standard error of it and therefore are being sorted by noise. Most employers have never seen this number and it reframes how they set the cut.

Define a boundary band and handle it deliberately. Candidates within one standard error of the cut get a defined treatment — advanced for human review, given a second assessment, or included in the next stage if capacity allows. This is a policy and it removes the arbitrariness at the only point where it is severe.

Use the interval in the decision rule. Advance candidates whose interval overlaps the cut, which is the statistically honest rule, and adjust the cut to achieve the intended selection ratio. This changes who is excluded from "everyone below a noisy line" to "everyone clearly below it".

Randomise within the band if capacity is truly binding, and say so. Explicit randomisation among candidates the instrument cannot distinguish is more defensible and more honest than a threshold that randomises implicitly while appearing precise.

Report the boundary population. How many candidates fell within the band, per requisition, and what happened to them. It is a count and it is the first time anyone will have looked at this group.

And never apply a cut below a stakes threshold without human review, which is a rule several regulatory directions are heading toward anyway.

## Who Feels the Pain

Candidates one point below a cut, rejected by measurement noise, with no feedback and no appeal — a large population in high-volume hiring. Employers, excluding capable applicants arbitrarily and carrying the legal exposure of a threshold they cannot defend as precise. And the I-O psychologists who know the standard error and watch the cut applied as a line.

## Impact If Fixed

The cut stops pretending to a precision the instrument does not have. The boundary population — large, arbitrary and currently invisible — gets a deliberate treatment. And the employer setting the cut finds out, at configuration time, how many people they are about to sort by noise.
