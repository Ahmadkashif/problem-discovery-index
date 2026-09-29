# The Natural Experiments Nobody Analysed

**Niche:** [[niches/streaming-video-platforms/title-causal-valuation/profile|Title Causal Valuation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A licensed title left the catalogue last month and nobody looked at what happened to the subscribers who watched it.
**Tags:** #quick-win #causal-inference #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #survival-analysis #automation
**Contested on:** Every serious competitor in this niche is fighting to attribute subscribers acquired and retained to the titles that caused them — and whoever produces a number a chief financial officer will defend changes what the industry spends billions on.

## The Problem
Titles leave the catalogue constantly when licences expire. Each departure is a clean withdrawal of a specific piece of content from a known population of viewers, followed by an observable churn outcome. It is the strongest causal evidence the business generates about what content is worth, it happens dozens of times a year, and it is handled as a content operations task. Nobody runs the analysis, and the licensing renewal decision is made without it.

## Why It's Still Broken
Catalogue departures are an operations event with an operations owner, so nobody in analytics sees them as experiments — an event classified as logistics never reaches the people who could read it as evidence. The analysis requires connecting departures to churn, which crosses team boundaries. Licence renewal decisions are made on price and relationship. And nobody asked.

## What a Fix Looks Like
Read the departures as evidence. Track churn among viewers of each departing title against a matched comparison group, which is the fix and is the closest thing to an experiment the business produces. Do the same for arrivals, since a title entering the catalogue is the other half and is equally unanalysed. Report the result before the renewal decision, because the evidence is currently produced after the negotiation if at all. Build a standing process so every departure is analysed automatically rather than by request. Match on viewing history rather than on demographics, as similar viewers are the right comparison and the data supports it. Look at viewers for whom the title was a large share of their viewing, since the effect concentrates there and is diluted in the average. Track the effect over months rather than weeks, because churn is a monthly decision and the effect is delayed. Accumulate the results into a body of evidence about what kinds of title matter, which compounds across departures. Report with intervals, since individual departures are noisy and the accumulation is what is informative. And feed it into licensing negotiations, which is where the analysis pays for itself immediately.

## Who Feels the Pain
Licensing teams negotiating without evidence; subscribers losing the one thing they watched; data teams unaware the experiments happened; and a business that generates causal evidence dozens of times a year and reads none of it.

## Impact If Fixed
An event classified as logistics never reaches the people who could read it as evidence, so catalogue departures pass unanalysed. Tracking churn among a departing title's viewers against a matched group is the strongest causal evidence the business produces.
