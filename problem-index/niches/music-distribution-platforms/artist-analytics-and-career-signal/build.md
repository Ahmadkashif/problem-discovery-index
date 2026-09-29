# The Earliest View of a Career

**Niche:** [[niches/music-distribution-platforms/artist-analytics-and-career-signal/profile|Artist Analytics & Career Signal]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The distributor sees an artist breaking before anyone else and shows them a bar chart.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #k-means-clustering #revenue-impact #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to turn the earliest visible evidence of an artist's trajectory into something the artist can act on — and whoever surfaces it first holds the signal the whole industry pays to discover late.

## The Problem
An artist's third release starts to move in a city they have never visited. Streams from one playlist placement are retaining unusually well. A track that was not the single is outperforming the one they promoted. All of this is visible in the distributor's own reporting within days, and the artist sees a dashboard of counts by service and by month, from which none of it is apparent. The decisions it should drive — where to play, what to push, when to release next — are made on instinct or not at all.

## Why Nobody Has Built This
Analytics was built to report what the services send, so the product's job ended at rendering — a dashboard assembled from upstream reports has no reason to develop a view. Career decisions are seen as the artist's or a manager's business. The distributor's revenue is a distribution fee, so the analytic product is a retention feature rather than a business. And nobody modelled trajectories across the artist base.

## What to Build
Model the trajectory and say what to do about it. Detect breakout early from growth shape, retention and playlist behaviour rather than from absolute counts, which is the core and is visible weeks before it is obvious. Identify the geographic concentration that should drive touring and promotion, since the data names cities and the artist is guessing. Measure what a playlist placement was actually worth in retained listeners rather than in streams during the placement, because the difference is enormous and never reported. Detect the track that is outperforming the promoted one, as it is common and is a directly actionable finding. Compare against trajectories of similar artists at the same stage, which is the distributor's unique aggregate view and gives context no individual dashboard can. Forecast the next release's likely reach, so plans are based on something. Tell the artist what the data implies rather than showing the data, since the audience is not analytical and the current product assumes otherwise. Flag the decline early too, because a fading trajectory is as actionable as a rising one and is harder to see from inside. Handle the small artist honestly, as most have too little data for confident claims and deserve to be told so. And connect the signal to concrete decisions — tour routing, release timing, promotion targeting — which is the product rather than the chart.

## Target Customer
Artist services leadership, independent artists and managers, labels seeking early signal, and music analytics vendors.

## Impact If Built
A dashboard assembled from upstream reports has no reason to develop a view, so the product renders counts. Early breakout detection and geographic concentration are visible weeks before they are obvious and point at decisions the artist is currently guessing.
