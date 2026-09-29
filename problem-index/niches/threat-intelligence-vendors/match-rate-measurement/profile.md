# Match Rate Measurement

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether anyone will publish how often a feed's indicators actually fire against real telemetry, which is computable today and reported by nobody.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~12%
**Digital Adoption:** Very low — computable and uncomputed
**Target Buyer:** Vendors with telemetry, security operations buyers, procurement
**Automation Potential:** Very high — it is a join between a feed and a log

## What Makes This a Distinct Niche

This is the tractable half of feed quality. Did this indicator ever match anything, at how many organisations, over what period, against what volume of traffic.

It needs nothing except telemetry and the feed. No adjudication, no analyst verdict, no investigation outcome. A vendor with endpoint or network visibility across an installed base can compute it across millions of indicators in a batch job, and a customer can compute it for their own environment in a week.

That is what separates it from [[niches/threat-intelligence-vendors/precision-verification/profile|🎯 Precision Verification]], which needs ground truth about whether a match was real — scarce, slow, inconsistently recorded and contested in exactly the cases that matter. Match rate is available now; precision is a multi-year data collection problem.

The contest is over whether anyone will publish it. The number is uncomfortable — much of any large indicator feed has never matched anything anywhere, which is an unremarkable property of collection at scale and a poor advertisement. The first vendor to publish defines the metric the rest must report against, and takes the reputational cost of going first.

## Current Tools & Gaps

Threat intelligence platforms that ingest feeds and report which produced alerts, available to customers and rarely used analytically. Endpoint and network platforms that match indicators against telemetry at scale, with the match data held internally. Academic studies measuring feed overlap and disagreement, with limited commercial reach.

The gaps are conspicuous because the computation is trivial. No vendor publishes a feed-level match rate. No vendor publishes the distribution — how many indicators matched at many organisations, at one, at none. Customers do not compute their own, despite holding the telemetry. Nothing reports match rate by organisation segment, so a feed's relevance to a particular buyer is unknown. And nothing distinguishes an indicator that matched high-volume ordinary traffic from one that matched a rare event, which is a large difference in what a match means.

## Problems

- [[niches/threat-intelligence-vendors/match-rate-measurement/build|🔨 Build: The Match Rate, Published]]
- [[niches/threat-intelligence-vendors/match-rate-measurement/buy|🛒 Buy: Telemetry Platforms That Already Hold the Answer]]
- [[niches/threat-intelligence-vendors/match-rate-measurement/fix|🔧 Fix: The Customer Has the Telemetry and Never Looks]]
