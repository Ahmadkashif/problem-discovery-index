# The Weights Nobody Has Changed in Two Years

**Niche:** [[niches/game-hosting-providers/matchmaking/profile|Matchmaking]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The matchmaking parameters were set during a beta with a different population and have been inherited ever since.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #causal-inference #optimization-fundamentals #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to trade match quality against wait time against latency without knowing what any of the three costs in whether the player comes back — and whoever establishes that currency takes the account.

## The Problem
Ask who set the current matchmaking weights and the answer is usually a person who has left, during a period when the player population was a different size, a different skill distribution and a different geographic spread. The parameters have been inherited through several patches, a population decline and a regional expansion. Nobody has revisited them, and nobody can say whether they are still approximately right or badly wrong.

## Why It's Still Broken
Nobody owns the parameters — settings that everybody depends on and nobody maintains drift out of validity as the world changes around them, and there is no moment at which anyone is required to check. Changing them is risky without a measurement. The population shift was gradual. And nothing breaks visibly.

## What a Fix Looks Like
Audit the settings against the population you have now. Reconstruct when the parameters were set and against what population, which is the fix and frequently ends the discussion once the date is written down. Describe the current population's size, skill distribution and geography and compare to the original, since the mismatch is usually obvious. Report the distribution of match quality and queue time actually delivered rather than the targets, as the delivered distribution often differs sharply from what the settings imply. Show the tails rather than the medians, because the players having a bad experience are in the tail by definition and the median hides them. Break the figures out by region and time of day, which is where thin populations distort everything. Look at players who stopped queueing after a run of poor matches, as that cohort is the cheapest available evidence. Run a small controlled change and measure it rather than debating the parameters abstractly. Document the settings and their rationale so the next person inherits reasoning rather than numbers. Set a review cadence tied to population change. And check the latency threshold against the current region footprint, which usually expanded after the threshold was set.

## Who Feels the Pain
Players in regions or skill bands the settings were never meant for; studios losing retention to a cause nobody has named; platform teams inheriting parameters they cannot justify; and support handling the complaints.

## Impact If Fixed
Settings that everybody depends on and nobody maintains drift out of validity as the world changes around them. Comparing the delivered distribution against the population the parameters were set for is an audit, not a project.
