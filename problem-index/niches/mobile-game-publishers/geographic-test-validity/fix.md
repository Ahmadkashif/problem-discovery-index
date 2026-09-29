# Soft Launch Said Yes and the Global Launch Said No

**Niche:** [[niches/mobile-game-publishers/geographic-test-validity/profile|Geographic Test Validity]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The game hit every soft-launch target, scaled globally, and returned numbers nobody recognised from the test.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #confidence-intervals #causal-inference #hypothesis-testing #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to know whether a number measured in a soft-launch market will hold when the game scales globally — and whoever can predict the transfer takes the account.

## The Problem
A title clears soft launch cleanly, receives global acquisition budget, and produces retention and revenue well below the tested figures. The post-mortem blames the campaign, the creative or the market conditions. The actual cause is usually that the test markets read high for that genre, or that the acquisition audience at scale is materially different from the small cheap audience the test bought, and neither was ever modelled.

## Why It's Still Broken
The test result is reported as a fact rather than as an estimate about a different population — a number measured in one market and reported without a transfer assumption invites everyone downstream to treat it as global, and they do. The scaled audience differs from the test audience in ways nobody records. Past transfer errors are not kept. And the failure is attributed downstream of where it was caused.

## What a Fix Looks Like
Restate the test number as a forecast with its assumptions attached. Report soft-launch metrics with an explicit transfer assumption rather than as a bare figure, which is the fix and changes how every downstream decision is framed. Keep a record of past titles' test-versus-global gaps by genre and market, since the publisher's own history contains the read rates and nobody has tabulated them. Show the acquisition audience composition in test against the planned global campaign, as broad targeting at scale reaches a different population than a cheap narrow test. Apply a genre-specific adjustment to the headline figures, which is a lookup rather than a model once the history exists. Flag titles whose test rested on a market historically known to read high. Stage the global scale-up rather than committing the full budget at once, which converts the bet into a sequence of smaller ones. Re-measure after the first scaling tranche before committing the rest. Attribute a shortfall to validation or to campaign explicitly, so the learning lands in the right place. Report the interval around the global forecast, not just the point. And write down the transfer assumption before launch rather than reconstructing it afterwards.

## Who Feels the Pain
Publishers who committed budget against a number that did not hold; UA teams blamed for a validation error; teams whose game was judged on a mismatched forecast; and the finance function funding the gap.

## Impact If Fixed
A number measured in one market and reported without a transfer assumption invites everyone downstream to treat it as global, and they do. Tabulating the publisher's own test-versus-global gaps by genre turns that into a stated adjustment.
