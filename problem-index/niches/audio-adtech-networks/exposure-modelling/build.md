# The Listening Curve Nobody Uses

**Niche:** [[niches/audio-adtech-networks/exposure-modelling/profile|Exposure Modelling]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a listener reached the advertisement is estimable from position-in-episode listening data the platforms already collect, and the industry counts file requests instead.
**Tags:** #survival-analysis #bayesian-inference #confidence-intervals #evaluation-metrics #gradient-boosting #time-series-forecasting #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish whether a listener reached the advertisement, from telemetry the platforms already collect — and whoever does that converts a download into something an advertiser can recognise as an impression.

## The Problem
An advertisement is inserted at twenty-two minutes into a forty-minute episode. Some listeners reach it, some stopped at eight minutes, some skipped forward past it, some are listening at double speed with the device in a pocket. The platform knows the shape of the listening curve for this show and frequently for this episode. It bills the advertiser for every download that triggered an insertion. The difference between the served impressions and the reached ones is substantial, varies enormously by show and by position, and is entirely computable from data that is already being collected for other purposes.

## Why Nobody Has Built This
Publishing an exposure number lower than the download count reduces reported inventory and therefore revenue, which is a direct commercial disincentive for the party holding the data — the capability and the motive sit in the same organisation pointing in opposite directions. Listening telemetry is collected for product analytics and not routed to advertising systems. No buyer has demanded it. And the download standard's existence makes the current count defensible.

## What to Build
Model the exposure. Estimate the probability of reaching each insertion point from position-level listening data, by show, episode type and listener segment, which is the core and is a straightforward survival problem on data that exists. Handle skip behaviour explicitly, since a skipped advertisement is a served impression with no exposure and skipping is directly observable. Account for playback speed and background listening where the telemetry supports it, which is a second-order correction that matters for some formats. Report exposure alongside downloads with the ratio stated, which is the presentation that makes the transition possible — an advertiser shown both understands the correction rather than seeing a cut. Price by exposure rather than by download, which is the commercial consequence and makes well-positioned inventory worth more and poorly positioned inventory worth less, correctly. Feed exposure estimates into insertion decisions, connecting to that niche, since the position is choosable and is currently set without reference to the curve. Publish per-show exposure profiles, which gives buyers the information they need and gives good publishers a reason to want this. Validate against any direct measurement available, including device-level confirmation where a platform can obtain it. Standardise the method, since an exposure figure that differs by vendor is another incomparable number. And report the aggregate gap between downloads and exposures, because that single figure is the most important unpublished fact about this channel.

## Target Customer
Streaming and podcast platforms holding the telemetry, advertisers buying on downloads, and the measurement bodies who could adopt an exposure standard.

## Impact If Built
The capability and the commercial motive sit in the same organisation pointing in opposite directions, which is why the telemetry is unused. Estimating reach-probability per insertion point is a straightforward survival problem on existing data and converts a file request into something recognisable as an impression.
