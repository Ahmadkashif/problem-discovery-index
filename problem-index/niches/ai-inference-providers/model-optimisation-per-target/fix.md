# Nobody Knows How Far From Peak They Are

**Niche:** [[niches/ai-inference-providers/model-optimisation-per-target/profile|Model Optimisation Per Target]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Teams optimise until the gains slow down, with no estimate of what the hardware could theoretically deliver, so they stop early on some models and grind pointlessly on others.
**Tags:** #evaluation-metrics #numerical-methods #descriptive-statistics #confidence-intervals #optimization-fundamentals #hypothesis-testing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to serve a new architecture at near-peak hardware efficiency on the day it is released rather than six weeks later — and whoever does that takes the account, because the window between a model's release and its commoditisation is where the margin is.

## The Problem
A performance team gets a model to a certain throughput, sees the improvements flatten, and ships. On one architecture they stopped at sixty percent of what the hardware could do and left a large cost saving unclaimed. On another they were already at ninety-five percent and spent a further fortnight for two points. Nobody knows which situation they are in, because the denominator — what this model on this hardware could achieve — is never computed, even though the arithmetic relating memory bandwidth, arithmetic throughput and a model's operational intensity is standard and well understood.

## Why It's Still Broken
The bound requires a model of the workload's arithmetic intensity and memory movement, which is a modest analysis nobody has assigned. Progress is reported as improvement over the previous configuration, which is always a positive number and always feels like success. Diminishing returns is used as the stopping rule, and it is a rule about the search rather than about the hardware. And no provider publishes their efficiency against peak, so there is no external reference either.

## What a Fix Looks Like
Compute the denominator. Build a roofline-style bound for each model on each accelerator from arithmetic intensity, memory bandwidth and compute throughput, which is standard analysis, takes an afternoon per architecture, and immediately tells a team whether they are at sixty percent or ninety-five — this is the fix and everything else is reporting around it. Report achieved efficiency against that bound as the headline optimisation metric rather than improvement over last week, which changes the stopping decision from a feeling into a number. Compute the bound separately for the prefill and decode phases, since they are compute-bound and memory-bound respectively and a single figure averages two very different situations — this distinction alone redirects a lot of misplaced effort. Set an explicit target and stop there, so effort moves to the next model rather than grinding. Report efficiency across the whole model catalogue, which shows immediately where the remaining money is and is a ranking no provider currently has. Translate the gap into currency, since a fifteen-point efficiency gap on a heavily-served model is a large number and stating it is what gets the work resourced. And publish the methodology, because an industry-standard efficiency measure would let providers compete on something more meaningful than published tokens per second.

## Who Feels the Pain
Performance engineers with no stopping rule; providers leaving cost savings on models nobody revisited; and customers paying for inefficiency that was never measured.

## Impact If Fixed
A roofline bound per model per accelerator takes an afternoon and converts a stopping decision from a feeling into a number. Computing it separately for prefill and decode is the distinction that redirects the most misplaced effort, and catalogue-wide efficiency shows where the remaining money is.
