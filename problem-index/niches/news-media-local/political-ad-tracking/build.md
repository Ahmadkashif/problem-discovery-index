# Complete Spend Data and No Model of What It Bought

**Niche:** [[niches/news-media-local/political-ad-tracking/profile|Political Advertising Tracking]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm knows every dollar spent in every race and sells a spend report, when the corpus supports estimating what the spending achieved.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #ml-time-series #evaluation-metrics

## The Problem
These firms track political advertising with near-complete coverage: which spots ran, in which markets, on which stations and platforms, when, and at what cost. Campaigns and committees buy the data to see what opponents are doing and where the money is going.

The product is descriptive. Spend by race, by market, by week, by advertiser. Share of voice. Creative libraries. All of it accurate and none of it answering the question every buyer has, which is whether the spending moved anything.

The corpus supports far more. Advertising exposure varies enormously across markets within a state for reasons that have nothing to do with the electorate — media market boundaries cut across districts, and a voter in one county sees a saturation campaign while a demographically identical voter twenty miles away sees almost nothing. That is a natural experiment repeated in every cycle, in hundreds of races, over a decade of tracking. Joined to precinct-level results, which are public, it is the largest available basis for estimating advertising effects — and it is not built.

## Why Nobody Has Built This
The customer asks for what they have always asked for. Campaigns want competitive intelligence and they want it now, and a product that says advertising in this race produced a smaller effect than the buyer hoped is not what the buyer requested.

The industry also has a strong prior that advertising works, and a measurement business that quantified the effect and found it modest in some contexts would be selling a conclusion its customers dislike. That is a real commercial tension and it is exactly why nobody has tested it.

And the analytical work is genuinely harder than the tracking. Advertising is not randomly assigned — campaigns spend where they think they can win — and estimating effects requires taking that selection seriously rather than correlating spend with outcomes.

## What to Build
Estimate advertising effects from the geography the corpus already contains.

**Exploit media market boundaries.** Where a media market spans a district boundary or a state line, voters on either side receive very different advertising for reasons unrelated to their own characteristics. That discontinuity is the identification strategy and it recurs across hundreds of races.

**Model dose and timing.** Effects almost certainly depend on saturation and on timing relative to the vote, and both vary widely across the tracked population. Estimating the shape rather than a single average is what would make the output usable for a buying decision.

**Separate media effects from selection.** Campaigns advertise where they expect returns, so naive analysis overstates effects. Handling that properly is the whole methodological problem and the corpus is large enough to support it.

**Test creative and message at scale.** The creative library is already catalogued. Message categories crossed with exposure variation and results is the closest thing to a national message-testing dataset that exists.

**Report intervals honestly.** A buyer allocating a budget can act on an effect with an interval. They cannot act on a share-of-voice chart, which is what they buy today.

## Target Customer
Chief Data Officer or VP of Research at a political advertising tracking firm. The commercial argument is durability: occurrence tracking is a coverage race that competitors can enter, and effect estimation over a decade of accumulated tracking is a position nobody can reach without the history.

## Impact If Built
Billions of dollars a year are allocated across local media on the assumption that advertising works, with no measurement of where and how much. Estimating it would change how campaigns buy — and, for the local stations that depend on political revenue, would establish what their inventory is actually worth rather than what scarcity pricing extracts.
