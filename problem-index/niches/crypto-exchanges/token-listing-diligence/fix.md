# Listed and Never Looked At Again

**Niche:** [[niches/crypto-exchanges/token-listing-diligence/profile|Token Listing Diligence]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** The listing assessment is a snapshot, and the concentration, the team activity and the liquidity all move afterwards with nothing watching.
**Tags:** #change-point-detection #graph-theory #quick-win #automation #evaluation-metrics #descriptive-statistics #compliance #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to assess an asset's code, distribution, team, legal characterisation and market integrity faster and more accurately than the venue that listed it first — and whoever does it without redoing the same analysis every other exchange already did takes the listing advantage.

## The Problem
An asset was approved on the basis of reasonable distribution, an active team and adequate liquidity. Eighteen months later the distribution has concentrated, the repository has been silent for a year, the liquidity has collapsed, and the exchange still lists it. The facts that would have prevented listing are now true and nobody is checking, because checking was an admission activity rather than an ongoing one. Delisting happens after an incident or a complaint.

## Why It's Still Broken
The assessment was designed as a gate, so once an asset passed there was no process that would ever look again — the workflow simply ends at approval. Delisting is commercially unpleasant and operationally awkward. The monitoring data is public but nobody assembled a feed. And nothing counts how many listed assets would fail their own listing criteria today.

## What a Fix Looks Like
Re-run the criteria on a schedule. Recompute the quantitative listing signals for every listed asset monthly, which is the fix and is almost entirely automatable from public data. Report how many listed assets would fail admission today, since that single number will force the conversation. Alert on material change rather than on absolute level, because the deterioration is the signal and the level alone is ambiguous. Watch distribution concentration continuously, as it is the most mechanical signal and the one that moves most consequentially. Track repository and team activity, since abandonment is visible months before it is acknowledged. Monitor liquidity and market integrity signals, because a thin book is a customer harm and an integrity exposure simultaneously. Define a deficiency process with a stated path, so deterioration has a response other than doing nothing or delisting abruptly. Tell customers when an asset is under review, since they hold it and are the last to know. Record every delisting with its cause, which is the outcome data the calibration work needs. And assign ownership for continued listing, because a gate with no keeper afterwards is what produced this.

## Who Feels the Pain
Customers holding deteriorated assets nobody flagged; listings teams surprised by incidents; compliance functions defending a listing that no longer meets its own criteria; and exchanges whose delistings always look reactive.

## Impact If Fixed
The workflow was designed as a gate and ends at approval, so nothing ever looks again. Recomputing the admission signals monthly from public data is close to fully automatable and reveals how much of the listed book would not pass today.
