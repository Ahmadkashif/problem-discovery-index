# Forty Variants, No Power

**Niche:** [[niches/app-marketing-firms/creative-performance-measurement/profile|Creative Performance Measurement]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The team ships forty variants a week into a budget that could meaningfully measure three, and reads the resulting noise as creative insight.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #quick-win #descriptive-statistics #revenue-impact #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to establish which creative actually worked when attribution arrives aggregated — and whoever does that recovers the measurement the privacy regime removed from the one lever still worth pulling.

## The Problem
Forty variants are shipped. The weekly budget divided across forty variants gives each a few hundred impressions and a handful of conversions. Differences between them are overwhelmingly noise. The team reads the top few as winners, briefs against them, produces forty more in that direction, and repeats. Over a year this generates a great deal of activity, a strong sense of accumulated creative knowledge, and a body of conclusions that are indistinguishable from a random walk. The production volume that was supposed to accelerate learning is the specific reason no learning occurs.

## Why It's Still Broken
More variants feels like more learning, and the networks encourage volume because their optimisers benefit from a larger candidate pool — the incentive and the intuition both point the wrong way. Nobody calculates the power available per variant. The production pipeline is measured on output. And the noise is indistinguishable from insight without a calculation nobody runs.

## What a Fix Looks Like
Ship fewer things and measure them. Calculate the detectable effect per variant given the budget, which is the fix, takes minutes, and typically shows that a fortieth of the weekly budget cannot distinguish a good concept from a bad one. Reduce variant count to what the budget can measure, or accept that the rest are for the network's optimiser rather than for learning — that distinction is the important one and is currently not made at all. Group into concepts and measure those, which is where the power is and where the transferable finding lives. Separate the exploration budget from the measurement budget explicitly, since supplying the network with variants and learning about creative are two different activities currently conflated into one. Run concept tests with enough allocation to conclude, even if that means fewer tests. Report uncertainty on every creative comparison, which stops a noise difference being briefed against. Accumulate across weeks so a concept's evidence builds rather than resetting. Use cross-account pooling where available, which is an agency's structural advantage. Record what was concluded and check it later, since the practice will only correct if its conclusions are ever revisited. And report how many of the week's creative decisions were statistically supportable, because that count is usually close to zero and it is the number that changes the process.

## Who Feels the Pain
Creative teams briefed against noise; advertisers whose creative strategy is a random walk; and designers producing volume that teaches nobody anything.

## Impact If Fixed
Volume feels like learning and the networks encourage it, so the incentive and the intuition both point the wrong way. Calculating the detectable effect per variant takes minutes and separates the variants supplied for the optimiser from the concepts being measured.
