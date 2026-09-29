# The Private Set That Decays Every Time It Is Used

**Niche:** [[niches/ai-model-evaluation-firms/benchmark-integrity/profile|Benchmark Integrity]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A private held-out set is the field's answer to contamination, and every evaluation run against it leaks a little of it back, with nobody tracking how much is left.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #compliance #monte-carlo-methods #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a score that survives the question "was this in the training data?" — and whoever does that takes the account, because every number the industry currently sells is an upper bound of unknown looseness.

## The Problem
A firm builds a private evaluation set and sells access. A lab evaluates against it repeatedly during development, using the score to choose between checkpoints. No individual item was disclosed, and the set has nonetheless been used to tune the model — which is the same failure as contamination arriving by a slower route. Meanwhile items leak: through error analyses shared with the customer, through examples in reports, through a support conversation, through a screenshot. Nobody counts. Two years later the set is treated as private and performs like a public one, and no one can say when that happened.

## Why It's Still Broken
The decay is gradual and invisible, with no moment at which the set becomes compromised. Refreshing items is expensive, especially for expert-authored domain sets. Customers want repeated access, which is the commercially attractive product and the one that destroys the asset. And there is no convention for reporting a set's remaining integrity, so a two-year-old private set and a new one are presented identically.

## What a Fix Looks Like
Treat the set as a depleting asset and account for it. Track exposure per item — every evaluation run, every item shown in a report, every error analysis — which is straightforward bookkeeping and is the precondition for everything else, and almost nobody does it. Limit submissions per customer per period, borrowing directly from competition practice, since unlimited access is how a held-out set becomes a training signal. Rotate items on a schedule driven by exposure rather than by calendar, retiring the most-used and introducing fresh ones continuously so the set never fully expires or fully survives. Report a remaining-integrity estimate with every score, so a buyer can weigh a result from a fresh set against one from a depleted one. Hold back a never-used reserve subset, released only for the final measurement, which is the cleanest number available and is worth the discipline of not touching it. Separate the development-access set from the certification set entirely, since the customer needs both and conflating them is the mechanism of the slow leak. And report items retired and items added each period, which makes the depletion visible to buyers and creates the pressure to maintain it.

## Who Feels the Pain
Buyers relying on a private-set score that has quietly become a public-set score; firms whose most expensive asset is depreciating with nobody accounting for it; and the labs who used a held-out set in good faith and tuned against it anyway.

## Impact If Fixed
The field's answer to contamination decays silently and nobody tracks it. Per-item exposure bookkeeping is cheap and is the precondition for every other control, and a never-used reserve subset is the only truly clean number available.
