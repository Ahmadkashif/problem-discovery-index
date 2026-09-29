# A Return With Nothing to Compare It To

**Niche:** [[niches/robo-advisors/outcome-measurement/profile|Outcome Measurement]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The client sees a percentage and a chart and has no way to tell whether it is good.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #automation #confidence-intervals #revenue-impact #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to tell each client what the platform actually delivered for them, net of fees, taxes and their own behaviour, against a stated alternative — and whoever publishes that number first makes every competitor's marketing average look like what it is.

## The Problem
The dashboard says the portfolio returned some percentage this year. Against what? The client does not know what a good outcome would have been, whether their own deposits and withdrawals distorted the figure, whether the number is before or after fees and taxes, or how much of it was simply the market. They cannot evaluate the product they are paying for, so they evaluate it by how it feels — which is exactly the mechanism that produces a panic sale.

## Why It's Still Broken
The performance display was inherited from brokerage convention, where showing a return is the norm and comparison is the client's job — so the omission was never a decision. Time-weighted and money-weighted returns answer different questions and nobody chose which the client needs. Adding a comparison invites an unfavourable one. And nobody asked clients what they were trying to find out.

## What a Fix Looks Like
Give the number a reference point. Show a simple comparison portfolio alongside the client's return, which is the fix and is a straightforward calculation that transforms an uninterpretable number. Report money-weighted return as well as time-weighted, since the client's actual experience depends on when their money was in and the two can differ dramatically. State clearly whether the figure is net of fees, as clients routinely assume the opposite of whichever is true. Show the fee in dollars rather than as a rate, because basis points are not a unit anyone has intuition for. Separate the market's contribution from everything else, since most of the number is the market and saying so is both honest and calming. Show progress toward the client's goal, as that is what they actually want to know and the return is a proxy for it. Put the drawdown in historical context, which is a cheap intervention at exactly the moment it helps. Avoid precision that implies certainty about estimated components. Test the display with real clients, since this is a comprehension problem and nobody has treated it as one. And measure whether clients who see a comparison behave differently, which connects directly to the intervention evidence.

## Who Feels the Pain
Clients unable to evaluate what they are paying for; service associates explaining performance figures on every call; and platforms whose retention depends on a number clients cannot interpret.

## Impact If Fixed
The display inherited brokerage convention, where comparison is the client's job, so the omission was never a decision. Adding a simple reference portfolio and a money-weighted figure makes the number interpretable for the first time.
