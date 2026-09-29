# Reading the Graph

**Niche:** [[niches/membership-community-platforms/community-health-and-structure/profile|Community Health & Structure]]
**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every structural failure the category complains about is a shape in a graph the platform already stores.
**Tags:** #graph-theory #spectral-graph-theory #k-means-clustering #evaluation-metrics #confidence-intervals #change-point-detection #descriptive-statistics #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to surface the structural failures that are plainly legible in the interaction graph — centralisation, closure, exclusion — before they become a shrinking community.

## The Problem
Community operators describe the same failures repeatedly and cannot see them until they have happened. A community centralised on the founder collapses when the founder takes a holiday. A subgroup that has closed to outsiders makes the community feel unwelcoming without anyone being rude. A few dominant voices set a tone that quietly excludes. Each of these is a measurable property of the reply graph — centrality, clustering, closure, share of voice — and each is reported nowhere.

## Why Nobody Has Built This
The analytics came from social media, where the objective was volume and the unit was the post, so the graph was never the object of measurement — a measurement tradition organised around content cannot describe structure. Network analysis is unfamiliar to community product teams. The failures are attributed to community management skill rather than to structure. And the diagnosis arrives as intuition, which is not actionable at scale.

## What to Build
Compute the structural measures and report them as health. Measure reply centralisation and identify how dependent the community is on individual nodes, which is the core and is the failure operators fear most. Detect subgroup formation and closure, since subgroups are how a community scales and closure is how it stops welcoming. Measure share of voice and its concentration, because a few dominant participants are both the community's engine and its exclusion mechanism. Identify members connected to nobody, which is a direct list of the people about to leave. Track structural change over time rather than reporting a snapshot, as decline is gradual and the trend is the signal. Distinguish a healthy core from a clique, which looks identical in aggregate and is the difference between depth and closure. Detect the tone shift, since a community's character changes slowly and the founder is the last to notice. Present findings as specific actions — introduce these people, invite this member to answer, seed this subgroup — rather than as a graph nobody can act on. Validate the measures against renewal, because a structural metric that does not predict retention is decoration. And benchmark against comparable communities, which is the platform's unique vantage and is entirely unused.

## Target Customer
Product and data leadership, community founders and managers, members who never connected, and community analytics vendors.

## Impact If Built
A measurement tradition organised around content cannot describe structure, so the graph was stored and never read. Centralisation, closure and isolation are standard graph measures and they name the failures operators currently only feel.
