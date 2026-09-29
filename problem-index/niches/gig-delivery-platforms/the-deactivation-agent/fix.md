# Fix: Two Complaints in Six Hundred Deliveries, With No Baseline

**Niche:** [[niches/gig-delivery-platforms/the-deactivation-agent/profile|The Deactivation Review Agent]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The agent sees a complaint count with nothing to compare it to, so a courier performing better than average gets deactivated for looking bad in isolation.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will put a percentile next to a count.

## The Problem

Deactivation criteria are counts and rates against fixed thresholds: complaints in a window, rating below a number, incidents of a type. The agent reviewing the case sees the count. They do not see what that count means.

Two missing-item complaints is a lot for a courier with forty deliveries and unremarkable for one with six hundred. A 4.6 rating is poor in one market and above median in another. A cancellation rate that looks high is normal for someone working a merchant corridor with chronic lateness. Without the distribution, every number looks like whatever the agent's intuition supplies, and intuition under a handle-time target is not reliable.

The platform holds the distribution for every one of these metrics, computed continuously for its own operational dashboards, and does not put it next to the number the agent is deciding on.

## Why It's Still Broken

Because the thresholds were set as absolutes and the review interface was built to display the absolute. Nobody designed it to mislead; it is what happens when enforcement criteria are written as policy text and then rendered directly.

Fixing it also has an implication that surfaces immediately: if a courier at the 88th percentile is being deactivated, the threshold is wrong, and correcting it reduces deactivations. Reduced deactivations mean more couriers on the platform who have generated complaints, and someone owns that risk. The count-based threshold is defensible precisely because it is dumb — it treats everyone the same and requires no judgement.

And the exposure-adjusted comparison has a second uncomfortable consequence: it makes visible that complaint rates vary systematically by market, merchant and order type, which means some couriers are flagged more because of where they work rather than how they work.

## What a Fix Looks Like

Put the distribution next to the number. It is a percentile lookup.

For every metric a deactivation decision turns on, display the courier's value, the population distribution for their delivery volume and market, and their percentile. Precompute it; it is a group-by refreshed daily. This single change converts the most common review from an impression into a comparison, and it is days of work.

Adjust the thresholds themselves for exposure. A raw count threshold penalises high-volume couriers mechanically — more deliveries, more chances for a complaint — which means the platform's most productive supply is structurally most at risk. Rate-based thresholds with confidence intervals fix this: a courier with two complaints in six hundred deliveries has a rate whose interval overlaps the population median, and that is the honest reading.

Surface the complaining customer's own history. A small share of customers generate a large share of complaints, and this is measurable. A complaint from a customer who has complained on most of their recent orders is weak evidence and currently indistinguishable from a complaint from someone who has never complained before.

Report deactivation rates by cohort. Market, tenure, volume, vehicle type, language. Systematic differences are either explained by something real or are a defect, and no platform currently produces the breakdown that would tell them which.

Give the courier the comparison too. A courier told their cancellation rate is high should be told what typical is. Most people who receive a warning have no idea whether they are near the line or far over it, and a percentile makes the warning actionable instead of alarming.

## Who Feels the Pain

Couriers deactivated for metrics that were actually above average, who lose a job and cannot articulate why the decision was wrong because they have never seen the comparison either. High-volume full-time couriers most of all, who are mechanically most exposed to count-based thresholds. Agents, who make the decision on a number they cannot interpret. And the platform, which is removing productive supply on a statistic it has not contextualised.

## Impact If Fixed

The most consequential decision the platform makes about a worker gets made against a baseline rather than an intuition. Count-based thresholds that penalise volume get replaced by rate-based ones that do not. And the platform finds out whether its deactivations fall evenly — a question it will be asked, and cannot currently answer.
