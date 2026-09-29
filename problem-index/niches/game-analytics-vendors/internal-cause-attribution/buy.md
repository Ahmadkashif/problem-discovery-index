# Change Attribution From Web Analytics

**Niche:** [[niches/game-analytics-vendors/internal-cause-attribution/profile|Internal Cause Attribution]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Web analytics annotates every chart with the releases and campaigns that might explain it, and game analytics shows a bare line.
**Tags:** #data-integration #causal-inference #change-point-detection #evaluation-metrics #confidence-intervals #automation #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish which of a studio's own actions moved a metric, from data the studio already holds in four different systems — and whoever joins them takes the account.

## The Problem
Web and product analytics platforms established annotation as a basic feature: releases, experiments, campaigns and site changes appear as markers on every chart, so anyone looking at a movement sees immediately what happened around it. Experiment platforms go further and attribute movements to specific variants. These are ordinary expectations for a product team analysing a web funnel. Game analytics platforms, with richer change data available, present the metric alone.

## What Already Exists
Chart annotation from release and campaign feeds; experiment platform attribution to variants; automatic anomaly flagging with context; segment decomposition of movements; and integration with deployment and campaign systems.

## The Customization Gap
The adaptation is to a client application whose changes reach players gradually and unevenly. It requires: (1) client builds that roll out over days and are adopted at different rates by platform, so the change has no single timestamp — this is the substantive difference and breaks simple annotation; (2) remote configuration changes that take effect without a build, in combinations; (3) content and live event schedules as change sources with no web analogue; (4) console and mobile store release processes that add lag between submission and availability; and (5) effects measured in retention over days rather than in conversion within a session.

## Target Customer
Studio data teams, game analytics vendors, publishers, and product analytics platform vendors.

## Impact If Solved
Web analytics made release and campaign annotation an ordinary expectation. Client builds that roll out over days with uneven adoption have no single timestamp, which is what breaks the borrowed approach.
