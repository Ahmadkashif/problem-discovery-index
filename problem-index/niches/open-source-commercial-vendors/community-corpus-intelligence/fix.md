# Roadmaps Set by Whoever Posts Most

**Niche:** [[niches/open-source-commercial-vendors/community-corpus-intelligence/profile|Community Corpus Intelligence]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Product direction is set from issue volume and reaction counts, which measure how vocal a user is rather than how many users have the problem or how much they are worth.
**Tags:** #descriptive-statistics #k-means-clustering #logistic-regression #hypothesis-testing #confidence-intervals #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor that gets here is fighting to turn the abundant, textual, scattered public record of a project's community into commercial and product intelligence — and whoever does that takes the analytical position, because the record is public and nobody reads it.

## The Problem
A feature request has one hundred and forty reactions and has been open for two years. It is the most-reacted issue in the tracker and is cited in every roadmap discussion. It is wanted by a vocal group of enthusiast users, almost none of whom are customers, and building it would take a quarter. Meanwhile a difficulty that affects most production deployments generates almost no issues, because the people hitting it work around it silently and are not the kind of users who open issues. The roadmap is being set by a metric that measures vocalness.

## Why It's Still Broken
Reaction counts are the only quantitative signal a tracker provides and are therefore used, exactly as download counts are used for adoption. The silent majority is silent by definition, and nobody has constructed a way to hear them. The commercial dimension — which requests come from customers or prospective ones — is not attached to issues because the identity is not resolved. And the vocal group's persistence makes ignoring their request politically costly regardless of its merit.

## What a Fix Looks Like
Weight the signal by something other than volume. Attach organisational context to requesters where it can be resolved, which immediately separates a request from forty enthusiasts from one from four large production users and is the single most useful change available. Weight by deployment scale and by commercial relationship, stated openly rather than applied secretly, since a vendor prioritising paying customers is legitimate and pretending otherwise is not. Seek the silent difficulties deliberately: analyse the community corpus for workarounds described in passing, questions that recur, and configurations that indicate a problem being lived with — which is where the widely-experienced issues actually appear. Ask directly with a periodic structured survey of production users, which reaches a different population from the tracker. Distinguish the request from the underlying problem, since a popular feature request is frequently one proposed solution to a problem with a better answer. Report the composition of support for each request, so a roadmap discussion knows whether one hundred and forty reactions represent one hundred and forty organisations or a community of enthusiasts. And publish the prioritisation basis, because an unstated one is assumed to be arbitrary and is resented accordingly.

## Who Feels the Pain
Production users whose widely-shared difficulties never reach a roadmap; maintainers pressured by a metric they know is misleading; and companies building the wrong things because they are measuring loudness.

## Impact If Fixed
Attaching organisational context to requesters separates a vocal group from a large one and is achievable with the entity resolution the rest of this niche needs. Seeking the silent difficulties in the corpus is where the widely-experienced problems actually are, and the tracker structurally cannot show them.
