# Capping Across a Chain That Cannot Cap

**Niche:** [[niches/streaming-video-platforms/ad-supported-tier-operations/profile|Ad-Supported Tier Operations]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same advertiser arrives through six demand paths under six identifiers and the frequency cap sees six different advertisers.
**Tags:** #graph-theory #optimization-fundamentals #evaluation-metrics #confidence-intervals #time-series-forecasting #automation #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to forecast, fill and frequency-cap inventory across a supply chain that makes capping structurally difficult — and whoever solves the repetition viewers notice keeps the tier that is supposed to be the growth engine.

## The Problem
A viewer watching two hours on an ad-supported tier sees the same advertisement many times. The platform has a frequency cap and it does not work, because the advertiser reaches the inventory through direct sales, several programmatic paths and a reseller, each presenting a different identifier for what is in fact the same campaign. The platform cannot recognise that they are the same, so it caps six things once each rather than one thing six times, and the viewer's experience is what an advertiser would least want.

## Why Nobody Has Built This
Frequency capping was implemented per demand source because that is where the identifiers are, so the structural problem was inherited from the supply chain's design — a control applied at the wrong level cannot work no matter how well it is configured. Resolving advertiser identity across paths requires inference nobody built. Fill rate is measured and repetition is not. And the viewer's complaint does not reach the team configuring the caps.

## What to Build
Resolve the advertiser, then cap and fill properly. Resolve campaign identity across demand paths using creative fingerprinting, landing destinations and buyer metadata, which is the core and is what makes capping possible at all. Cap at the resolved advertiser and campaign level rather than at the identifier level. Forecast inventory against viewing volatility properly, since a streaming audience is far less predictable than a broadcast one and the forecasting practice was inherited from broadcast. Handle the unsold break deliberately rather than repeating whatever is available, because that is where the worst repetition happens. Measure repetition as experienced by the viewer rather than as configured, which is the honest metric and does not exist. Model the viewer experience cost — abandonment, session length, churn from the tier — against ad load, since it is measurable and is the trade the business is making blind. Allocate across demand sources on yield net of experience, not on price alone. Detect the creative that is being served far beyond its cap and act automatically. Report competitive separation and category conflicts, which viewers notice and advertisers care about. And give advertisers honest delivery and frequency reporting, since the current numbers describe configuration rather than experience.

## Target Customer
Advertising and product leadership, advertisers whose campaigns are wasted on repetition, viewers on the ad tiers, and ad technology vendors serving streaming.

## Impact If Built
A control applied at the wrong level cannot work no matter how well it is configured, and the level was inherited from the supply chain. Resolving campaign identity across demand paths is what makes frequency capping mean anything.
