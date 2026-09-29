# Nobody Knows What Normal Looks Like

**Niche:** [[niches/llm-application-tooling/application-corpus-intelligence/profile|Application Corpus Intelligence]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** A team sees their own quality score, cost per request and latency and has no idea whether those numbers are good, because no reference exists for what comparable applications achieve.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #k-means-clustering #quick-win #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to turn the complete record of how these applications behave into empirical answers about what actually works — and whoever does that stops selling a trace viewer and starts defining the practice.

## The Problem
A team's support assistant resolves seventy-two percent of conversations, costs four cents per interaction and responds in two and a half seconds. Is that good? They have no idea. Seventy-two percent might be excellent for their domain or embarrassing. Four cents might be three times what comparable applications pay. Two and a half seconds might be the reason their users abandon. They optimise whichever number the loudest stakeholder mentions, with no sense of which has the most headroom. Every team in this category is in the same position, and the vendor they all log into could tell them.

## Why It's Still Broken
Cohort benchmarking requires comparable metric definitions across customers, which requires a shared grading approach nobody has established. Publishing where a customer sits relative to peers tells some of them they are below average, which is uncomfortable for an account team. Contracts do not contemplate aggregation. And the absence has become normal, so nobody asks for it.

## What a Fix Looks Like
Give every customer a reference. Define comparable cohorts by application type, domain and scale, and report each customer's position on quality, cost and latency within their cohort, which uses aggregated data that identifies nobody and is the artefact every customer wants — and it is derivable today. Report the distribution rather than a single average, so a team sees the spread and what the top of it achieves. Highlight which metric has the most headroom for them specifically, which converts a benchmark into a direction rather than a score. Report cohort norms for the secondary metrics too — prompt length, retrieval depth, cache hit rate, retry rate — since those are the levers and a team at three times the cohort's prompt length has found their cost problem immediately. Publish aggregate norms openly, which establishes the vendor as the field's reference and costs nothing competitively. Update continuously, since the norms move quickly as models change. Make participation reciprocal, so contributing customers see the benchmark, which is a fair exchange and the usual structure for this. And be careful with the statistics, since cohorts are small and a rank based on four comparable applications is noise presented as insight.

## Who Feels the Pain
Teams optimising blind and prioritising the wrong metric; buyers with no basis to judge whether their application is competitive; and the field, which has no shared sense of what good looks like.

## Impact If Fixed
Cohort position on quality, cost and latency is derivable today from aggregated data that identifies nobody, and it is the artefact every customer wants. Reporting the secondary levers alongside it — prompt length, retrieval depth, retry rate — turns a score into a direction.
