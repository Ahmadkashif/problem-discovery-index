# The Seventy-Five Percent That Should Have Been Fifty

**Niche:** [[niches/indie-game-studios/sale-events-and-pricing/profile|Sale Events & Pricing]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The studio discounted deeply, sold a lot of units, earned less than a shallower sale would have, and has no way to know.
**Tags:** #quick-win #revenue-impact #evaluation-metrics #descriptive-statistics #causal-inference #confidence-intervals #time-series-forecasting #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a studio what a discount at a given depth and moment will actually earn over the title's remaining life — and whoever answers it takes the account.

## The Problem
A studio runs a deep discount, sees a unit spike, and calls it a success. Whether it was depends on what a shallower discount would have earned from the same audience and on what the deep one cost the next sale — neither of which the studio can observe. Over several sales the pattern compounds: the audience learns to wait, each subsequent sale needs to go deeper, and the title's earning power erodes in a way that looks like natural decay.

## Why It's Still Broken
There is no counterfactual — a decision evaluated only by its own outcome, with no view of the alternative, cannot be learned from no matter how many times it is repeated. Unit spikes feel like success. Platform event traffic flatters every sale. And the erosion is slow enough to look like the title simply ageing.

## What a Fix Looks Like
Evaluate against the alternative, not against zero. Estimate what the same sale at other depths would have earned, which is the fix and is the number the studio has never seen. Separate platform event traffic from the discount's own lift, since conflating them makes every sale look effective. Show revenue rather than units as the headline, as the unit spike is what misleads. Track the trend across the sale history — whether each one needs to go deeper for the same return — which is the erosion signal and is visible in the studio's own data. Record the conditions of each sale so comparisons are honest. Warn before a depth that the history suggests is unnecessary, which is where the money is. Show the recovery period after a sale, since revenue at full price does not resume immediately. Include regional revenue rather than only headline currency, as that is where a chunk of the answer sits. Keep it to a one-page verdict, because this decision gets ten minutes. And run it after every sale automatically, so the record builds without anyone maintaining it.

## Who Feels the Pain
Studios whose catalogue earns less than it should; owners funding the next project from the last one's tail; publishers with the same blind spot at scale; and players trained to wait for the seventy-five.

## Impact If Fixed
A decision evaluated only by its own outcome, with no view of the alternative, cannot be learned from no matter how many times it is repeated. Estimating the counterfactual depth and stripping out platform event traffic makes the sale history teachable.
