# The Creative That Stopped Working Three Weeks Ago

**Niche:** [[niches/programmatic-ad-platforms/creative-decisioning/profile|Creative Decisioning]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Response to the advertisement decayed steadily from day nine and the campaign kept running it until the flight ended, because nobody was watching for fatigue and there was nothing ready to replace it.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #confidence-intervals #revenue-impact #quick-win #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to build a system that knows why a creative works rather than which variant won — and whoever does that turns the largest untouched lever in the category into an optimisable one.

## The Problem
The creative launched well. By day nine, response among people who had already seen it several times had fallen substantially, and by day twenty it was barely better than nothing. Aggregate campaign performance declined gently, which looked like ordinary variation. Nobody identified fatigue as the cause, because the report shows a campaign average rather than a response curve by exposure count. The campaign ran the same asset for six more weeks, spending most of its budget after the creative had stopped working, and the post-campaign review concluded that the audience was saturated.

## Why It's Still Broken
Creative fatigue is diagnosed by exposure count and reports are aggregated by day, which is the wrong axis and hides it completely. Replacing a creative mid-flight requires production capacity and approvals that take longer than the decay. Fatigue is confounded with audience exhaustion and the two get the same diagnosis by default. And nobody is accountable for creative performance after launch.

## What a Fix Looks Like
Measure response by exposure, not by date. Report performance against cumulative exposures per person rather than against the calendar, which is the fix, uses data already collected, and makes fatigue immediately visible as the curve it is. Separate fatigue from audience exhaustion by comparing first-exposure response over time — if it is flat, the audience is fine and the creative is tired, which are opposite remedies and are currently confused constantly. Alert when the decay crosses a threshold, with a projection of what continuing will cost, since the cost of running a dead creative for six weeks is large and never stated. Prepare rotation in advance, because detecting fatigue without a replacement ready achieves nothing and this is the practical reason campaigns run tired assets. Rotate automatically within an approved pool, which removes the approval bottleneck at the moment it matters. Identify which attributes fatigue fastest, connecting to the build note, since a refresh that changes nothing meaningful fatigues immediately. Adjust frequency caps in response to measured decay rather than to a fixed rule set at launch. Detect recovery, as creatives rested for a period often perform again and rotation pools are currently discarded rather than reused. Report fatigue-adjusted performance so the campaign's real trajectory is visible rather than a flattering average. And quantify the wasted spend, because that number is what creates the production capacity the fix needs.

## Who Feels the Pain
Advertisers spending most of a budget after the creative stopped working; audiences shown the same tired advertisement forty times; and creative teams blamed for a decline that was a rotation failure.

## Impact If Fixed
Reports aggregate by date and fatigue lives on the exposure axis, so it is invisible by construction. Plotting response against cumulative exposures makes it obvious with data already collected, and comparing first-exposure response separates a tired creative from an exhausted audience.
