# Adoption Counted as Services Onboarded

**Niche:** [[niches/internal-developer-platforms/platform-as-product/profile|Platform as Product]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The platform reports the number of services onboarded, which counts a service that was onboarded and abandoned identically to one that is used daily.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to make a platform team behave like a product team — measuring adoption, abandonment and what developers do instead — and whoever does that takes the platform account, because the category error explains most of its failures.

## The Problem
The quarterly report says one hundred and forty services are on the platform, up from ninety. It is presented as adoption. Of the one hundred and forty, thirty were onboarded during a migration mandate and are deployed through a separate mechanism the teams kept; twenty are dormant services nobody has touched in a year; and the number includes several that were registered in the catalogue and never actually used the platform for anything. Active daily use is perhaps sixty. The reported number will keep rising as long as services are registered, regardless of whether anybody uses the platform.

## Why It's Still Broken
A count of registered services is trivially available from the catalogue and became the metric for that reason, exactly as downloads and coverage did in other categories. Measuring use requires defining what use means and instrumenting for it, which nobody specified. The number also flatters and rises monotonically, which makes it a comfortable thing to report to a leadership team funding the platform. And nobody has asked for a harder number.

## What a Fix Looks Like
Report use rather than registration. Define active use explicitly — deployed through the platform in the last period, using the platform's pipeline, using its provisioned infrastructure — and count that, which immediately separates registration from adoption and is the single most informative change. Report retention as a cohort curve, so a team that adopted eight months ago and stopped is visible, which registration counts cannot show. Distinguish mandated from voluntary adoption, since the second is the honest measure of whether the platform is good and the first measures whether the mandate was enforced. Report depth: which platform capabilities each team actually uses, since a team using the pipeline and nothing else has adopted a fraction of the platform and is counted as fully adopted. Report the shadow estate — teams doing it themselves, which is observable — as the denominator, since adoption is a share rather than a count. And report support contacts per active team, which is the inverse quality signal and rises when the platform is confusing.

## Who Feels the Pain
Platform teams whose metric cannot show whether their work helped; leadership funding a platform on a number that rises regardless; and developers whose abandonment is counted as adoption.

## Impact If Fixed
Defining active use and reporting a retention cohort are both straightforward over data the platform holds and turn a monotonic count into a measure of whether anything is working. The voluntary-versus-mandated split is the honest signal and is the one nobody separates.
