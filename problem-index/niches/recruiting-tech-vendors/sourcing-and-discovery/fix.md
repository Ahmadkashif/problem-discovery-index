# Fix: The Same Two Hundred People Get Contacted by Everyone

**Niche:** [[niches/recruiting-tech-vendors/sourcing-and-discovery/profile|Sourcing & Candidate Discovery]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every recruiter runs a similar search against the same database, so a small, highly legible population receives all the outreach and everyone else receives none.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #word-embeddings #workflow-orchestration #quick-win #automation #worker-facing
**Contested on:** Whether anyone will look at the concentration of outreach rather than at its response rate.

## The Problem

Sourcing searches are similar because the tooling, the training and the job descriptions are similar. So for any given role, the same profiles surface to every recruiter at every company running that search.

The consequence is extreme concentration. A small population — right title, recognisable employer, well-optimised profile, active on the platform — receives dozens of messages a month and ignores most of them. Everyone else receives nothing. Response rates fall, which recruiters respond to by sending more messages to the same people, which lowers response rates further.

Meanwhile the candidates nobody contacts include large numbers who would have been interested and qualified, and who never learn the role existed.

## Why It's Still Broken

Response rate is the measured metric and it is measured on messages sent. Nobody measures outreach concentration, so the dynamic driving the response rate down is invisible to the people responding to it.

The tooling also rewards the concentration. Search returns the most obviously matching profiles first, every recruiter works from the top, and the ranking that makes each individual search efficient makes the market as a whole dysfunctional.

And no individual recruiter can fix it. Broadening their own search costs them time for a benefit that is partly captured by everyone else.

## What a Fix Looks Like

Measure the concentration and build for the tail.

Compute outreach concentration. What share of messages in a role and geography go to what share of the available population — within the employer's own sending at minimum, and across the platform where a vendor can see it. This number will be startling and it is a group-by.

Track per-candidate contact load where the platform can see it, and deprioritise profiles that are already saturated. A candidate who has received forty messages this month is not a good prospect regardless of how well they match, and surfacing them to a forty-first recruiter serves nobody.

Surface the tail deliberately. A separate results section of capability-matched candidates who receive little outreach, presented as an opportunity rather than buried below the obvious matches. This is where response rates are actually high, and it is the direct commercial argument for the whole change.

Search the employer's own database first. Past applicants, silver medallists and previous candidates are the most neglected sourcing pool at almost every employer, have already expressed interest, and are entirely uncontacted. This is free and it is rarely done.

Report response rate by outreach concentration. The relationship — heavily-contacted candidates respond far less — is the evidence that reframes the metric and directs effort toward the tail.

And stop measuring recruiters on messages sent, which is the incentive producing the whole pattern.

## Who Feels the Pain

Candidates outside the legible population, who never hear about roles they would take — a systematic exclusion that no downstream fairness measurement can see. Candidates inside it, buried in irrelevant outreach they have stopped reading. Recruiters, watching response rates fall and sending more. And employers, competing for the same two hundred people while the rest of the market goes uncontacted.

## Impact If Fixed

Outreach concentration becomes a measured quantity rather than an invisible dynamic, and the response rate finally has an explanation. The under-contacted tail — where response rates are high and competition is low — becomes a deliberate target. And the employer's own past applicants, the most neglected pool anywhere in this industry, get searched first.
