# The Review Burden Nobody Accounted For

**Niche:** [[niches/developer-tools-vendors/ai-coding-assistants/profile|AI Coding Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Generation capacity rose sharply and review capacity did not, so the bottleneck moved to the humans reading the code and nobody planned for it.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to be the assistant an engineering organisation actually runs on — and that contest is decided twice, by the developer and by the security function, which is why this niche is not terminal and is decomposed below.

## The Problem
Pull request volume rises forty percent after an assistant rollout. The number of people reviewing does not change. Review latency climbs, reviews get shallower, and the engineers who review carefully — who are a small minority, as the invisible-contribution work elsewhere in this vault documents — absorb the increase. Six months later the organisation has more code, slower reviews, and a growing quantity of merged changes that nobody read properly, which is a worse position than before and was entirely predictable from the first month's throughput numbers.

## Why It's Still Broken
The rollout was justified on generation and nobody modelled the downstream constraint, which is a classic bottleneck displacement and is obvious in retrospect. Review capacity is not measured anywhere, so the constraint was invisible until it bound. Reviewer load distribution is equally unmeasured, so the concentration on a few people is invisible too. And the organisation's reported metrics — throughput, deployment frequency — improve during exactly the period the problem is accumulating.

## What a Fix Looks Like
Measure and manage the downstream constraint deliberately. Track review capacity and load alongside generation, by person, which immediately shows both the aggregate shortfall and its concentration. Watch review depth rather than review count — time spent, comments made, change requests raised per thousand lines — since the first thing to give under load is thoroughness and it gives silently. Size changes deliberately, because generated changes are frequently larger than hand-written ones and large changes are reviewed worse; a limit on change size does more for review quality than any tooling. Route review by the risk of the change rather than uniformly, so that substantial and security-relevant changes get the scarce careful attention and trivial ones do not consume it. Use automated review to reduce the mechanical load rather than to replace judgement, which is where it genuinely helps. And report the bottleneck alongside the throughput gain, so the organisation sees the whole picture rather than the flattering half.

## Who Feels the Pain
The minority of engineers who review carefully and absorbed the increase; teams whose review latency has become the slowest part of delivery; and organisations accumulating merged code nobody read.

## Impact If Fixed
Bottleneck displacement is predictable and was predicted by nobody, and the review load measurement is a query over data every platform holds. Change-size limits and risk-based review routing are ordinary practices that address the constraint directly.
