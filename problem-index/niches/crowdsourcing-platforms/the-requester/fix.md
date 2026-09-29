# Fix: Ten Thousand Labels and a Single Kappa

**Niche:** [[niches/crowdsourcing-platforms/the-requester/profile|The Requester]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The results summary reports one agreement number with no benchmark, no decomposition and no indication of what to do about it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #automation #worker-facing
**Contested on:** Whether the results summary will tell the requester anything they can act on.

## The Problem

The batch completes and the requester gets a number. Krippendorff's alpha, Fleiss' kappa, percentage agreement — one figure, for the whole batch, with no context.

They cannot interpret it. Is 0.58 good for this kind of task? Where is the disagreement concentrated? Is it three categories or spread evenly? Are particular items responsible? Did certain workers drive it? Is it worse than their last batch?

Every one of those is answerable from data already in the results file, by grouping it. None is presented. So the requester either accepts the data, or discards the batch, and in both cases learns nothing that would make the next one better.

## Why It's Still Broken

The summary was built to report the statistic, because reporting the statistic is what was asked for. Nobody specified the decomposition because nobody articulated that the statistic alone is uninterpretable to the population receiving it.

Benchmarks require the platform to aggregate across requesters, which is a small analysis nobody has run.

And the decomposition tends to point at the requester's own design, which makes it a less comfortable feature to prioritise than one that reports a neutral number.

## What a Fix Looks Like

Decompose the number and give it a reference point. All of it is grouping over the results file.

Report agreement by category, not just overall. Disagreement is nearly always concentrated, and knowing that categories B and C account for most of it turns an abstract statistic into a specific problem with a specific boundary.

Report it by item and list the worst. The twenty most contested items, with their responses. A requester reading those twenty items will usually see the ambiguity immediately, which no summary statistic will ever convey.

Report it by worker, shrunk. Whether disagreement is spread across the crowd or driven by a few workers is the difference between a design problem and a quality problem, and it changes the response entirely.

Give a benchmark. The distribution of agreement for comparable task types on the platform, so the requester knows whether 0.58 is poor, typical or good here. This is a percentile lookup and it is the single most useful addition.

Compare to their own previous batches, where they have any. Trend across a requester's own work is the most relevant reference available and requires no cross-requester aggregation at all.

And say what to do. Three sentences: your disagreement concentrates on the B/C boundary; here are five items where it happened; consider specifying the boundary explicitly and rerunning those items. That is the difference between a report and a result.

## Who Feels the Pain

Requesters, who receive an uninterpretable number and make a consequential decision on it — publishing on the data, training on it, or discarding a batch they paid for. Workers, rejected because a requester read a low kappa as crowd quality rather than as instruction ambiguity. And the platform, whose requesters conclude that crowdsourcing is unreliable when the issue was their own category boundary.

## Impact If Fixed

The agreement statistic becomes interpretable, with a benchmark, a decomposition and the twenty worst items attached — all from grouping a file the requester already has. Instruction problems get identified as instruction problems. And a requester who would have discarded a batch instead fixes a category boundary and reruns two hundred items.
