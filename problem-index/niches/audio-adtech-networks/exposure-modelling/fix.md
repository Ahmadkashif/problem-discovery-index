# The Mid-Roll Past Where People Stop

**Niche:** [[niches/audio-adtech-networks/exposure-modelling/profile|Exposure Modelling]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The insertion point is set at a fixed timestamp by convention, the show's listening curve falls off well before it, and every impression sold at that position is billed and unheard.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #revenue-impact #survival-analysis #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to establish whether a listener reached the advertisement, from telemetry the platforms already collect — and whoever does that converts a download into something an advertiser can recognise as an impression.

## The Problem
Insertion points are configured at fixed timestamps — a pre-roll, a mid-roll at a set position, a post-roll — applied across a show's catalogue. For some shows the audience listens to the end and every position performs. For others the curve falls steeply and the second mid-roll sits past where most of the audience has stopped. The publisher sells that position at the same rate, the advertiser buys it at the same rate, and the impressions are billed. The listening curve that would reveal this is in the platform's own analytics, on a different screen from the one where insertion points are configured.

## Why It's Still Broken
Insertion configuration and listening analytics are separate surfaces owned by different teams, so the two facts never meet — a two-screen problem rather than a hard one. Moving an insertion point earlier reduces the number of slots and therefore the inventory count, which nobody volunteers for. Advertisers cannot see the curve and so cannot object. And the impressions are billed either way.

## What a Fix Looks Like
Put the curve where the decision is made. Show the show's listening curve on the insertion configuration screen, which is the fix, is a two-screen problem rather than a modelling one, and makes an obviously bad position obviously bad. Recommend insertion points from the curve, so the placement is derived rather than conventional. Report expected exposure per slot before it is sold, which lets a publisher price honestly and an advertiser buy knowingly. Set positions per show rather than by a global convention, since the curves differ enormously and a single convention is wrong for most shows. Adapt to episode length and type, because a bonus episode and a flagship interview have different shapes. Flag slots whose expected exposure falls below a threshold, so they can be removed or repriced rather than sold at parity. Sell position-adjusted rates, which rewards publishers with engaged audiences and is a fairer market. Give hosts the curve for their own show, connecting to the host niche, since it is their audience and they cannot currently see this. Monitor the curve over time, as it shifts with format changes. And report the share of impressions served past the median stopping point, which is a number every publisher could compute today and none publishes.

## Who Feels the Pain
Advertisers billed for impressions nobody reached; publishers with engaged audiences priced the same as those without; and hosts whose audience retention earns them nothing.

## Impact If Fixed
The listening curve and the insertion configuration are on different screens owned by different teams, which is why an obviously bad position persists. Showing the curve where the position is set, and reporting expected exposure per slot, makes the market price engagement rather than file requests.
