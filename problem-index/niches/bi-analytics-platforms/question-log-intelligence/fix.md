# The Roadmap Built From Requests Instead of Demand

**Niche:** [[niches/bi-analytics-platforms/question-log-intelligence/profile|Question Log Intelligence]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Data teams plan their quarter from a backlog of tickets, which measures who asked most persistently, while the usage log measures what the organisation actually needs.
**Tags:** #descriptive-statistics #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor that gets here is fighting to turn the record of how an organisation questions itself into a product — and whoever does that takes a position no competitor can copy, because the query log is the one asset each platform holds exclusively.

## The Problem
The data team's quarterly plan contains eleven projects. Each came from a request, each request came from someone with the standing to make one, and the resulting plan reflects organisational seniority rather than organisational need. Three of the eleven serve a handful of people. Meanwhile forty people across three departments open the same inadequate dashboard weekly, work around its gaps by exporting and recombining, and have never filed a ticket because none of them individually finds it worth the effort. The log shows all of this and nobody consults it when planning.

## Why It's Still Broken
Backlog-driven planning is the default in every function and requires no data, and the ticket is a legible artefact where a usage pattern is not. The people best served by the current arrangement are senior enough to keep it. Usage analysis for planning purposes has no owner — the platform team reports adoption, the analytics team plans work, and nobody joins the two. And there is a real worry that measuring usage could be read as measuring people, which is manageable with aggregate reporting and has not been articulated, so the topic is avoided.

## What a Fix Looks Like
Bring the log to the planning meeting. A demand report per quarter: the most-used assets and their trajectory, the assets with high usage and poor quality signals, the concepts queried most often and their coverage in the modelled layer, and the abandonment hotspots where people repeatedly fail to find an answer. Weight the backlog by measured reach rather than by requester seniority, and show both, since the point is to inform the argument rather than to replace judgement — a project serving four executives may well be the right call, and it should be made knowingly. Track what happened after previous quarters' work, which nothing currently does: did the new dashboard get used, did the ad hoc requests about that subject stop, did the export behaviour change. And report the concepts with high demand and no governed definition, which is simultaneously a roadmap for the semantic layer and the list of things most likely to be computed inconsistently today.

## Who Feels the Pain
Data teams delivering work that is not used; the majority of users whose needs never reach a ticket; and organisations investing in analytics against a demand picture they have never looked at.

## Impact If Fixed
The log is complete in every platform and consulting it at planning time is a meeting change rather than a technology project. The post-hoc check on whether previous work was used is the part that compounds, and almost no data team does it.
