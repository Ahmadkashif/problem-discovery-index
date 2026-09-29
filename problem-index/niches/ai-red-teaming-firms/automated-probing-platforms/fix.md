# Pass or Fail on a Probabilistic Behaviour

**Niche:** [[niches/ai-red-teaming-firms/automated-probing-platforms/profile|Automated Probing Platforms]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A probe is reported as passed or failed when the underlying behaviour has a success rate, so a technique that works one time in five hundred and one that works every time appear identically.
**Tags:** #hypothesis-testing #confidence-intervals #probability-distributions #evaluation-metrics #monte-carlo-methods #descriptive-statistics #quick-win #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to cover broad ground cheaply and stay current as models are updated against known techniques — and whoever does that takes the account, because the alternative is a public dataset that goes stale.

## The Problem
A suite runs each probe once and reports a result. A technique that elicits the harmful behaviour on the first attempt and one that requires five hundred attempts both show as failed. A technique that succeeded on this run and would fail on the next shows as failed too, and next week shows as passed, producing a report that oscillates for no reason anybody can explain. The engineering team receiving it cannot prioritise, cannot tell whether last week's fix worked, and after two months of noise stops reading the report.

## Why It's Still Broken
Running each probe once is cheap and produces a clean binary that fits a findings table. Repetition multiplies the cost of a suite that is sold on being cheap. The scanning heritage the product inherited assumes deterministic results, so the data model has a boolean where it needs a rate. And the oscillation is attributed to the model being unpredictable rather than to the measurement being underpowered.

## What a Fix Looks Like
Measure the rate. Run each probe enough times to estimate a success rate with a usable interval, sizing the repetition to the precision needed rather than to a round number, which is elementary and is the fix — and the cost is modest when applied selectively. Report the rate and its interval rather than a binary, so a team can prioritise a technique that works half the time over one that works once in five hundred. Concentrate repetition where it matters, using few attempts to rule out the clearly-negative and many on the borderline, which keeps the cost proportionate. Report a change in rate between runs with a significance test, so a fix can be confirmed and an oscillation within noise is not reported as a change. Aggregate a category's rate across its techniques, which is more stable than any individual probe and is the right level for a trend. Report the sampling parameters, so a reader knows how much the number can support. State a minimum detectable change per category, which tells a team in advance what improvement their next report will be able to show. And stop reporting binary results, since they are the direct cause of both the false alarms and the false reassurance this product currently generates.

## Who Feels the Pain
Engineering teams prioritising from a table that cannot distinguish severities; compliance functions filing reports that oscillate; and vendors whose product is ignored after two months of noise.

## Impact If Fixed
A binary on a probabilistic behaviour is the direct cause of both the oscillation and the false reassurance. Concentrating repetition on the borderline probes keeps the cost proportionate while making the rates usable, and a significance test on the change is what lets a team confirm a fix.
