# The Appended Attribute Nobody Checked

**Niche:** [[niches/customer-data-platforms/profile-completeness-and-enrichment/profile|Profile Completeness & Enrichment]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The organisation buys third-party attributes for millions of profiles every year and has never measured how often they are right.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #quick-win #descriptive-statistics #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to say what is missing from a profile and what can be inferred rather than bought — and whoever does that replaces a third-party data purchase with the organisation's own observations.

## The Problem
A data provider appends life stage, income band, household composition and category affinities to millions of customer profiles for a substantial annual fee. Those attributes then drive segmentation, personalisation and targeting. Nobody has ever checked whether they are correct. The provider reports match rate, which measures how many records they returned something for, not how often that something is true. For a meaningful share of customers the organisation already knows the real value from its own data, which means the accuracy could be measured directly and cheaply, and in most organisations it never has been.

## Why It's Still Broken
Match rate is the metric the market runs on, and it measures coverage while looking like quality — the same substitution that runs through this whole cluster. Checking accuracy requires a deliberate exercise nobody is tasked with. Providers have no incentive to publish it. And the attributes feel plausible because they are plausible, which is different from being right.

## What a Fix Looks Like
Measure the accuracy against what you already know. Compare appended attributes against known values for the subset where the organisation has them, which is the fix, costs a day, and gives an accuracy figure the market does not provide — most organisations have never seen one for data they have bought for years. Report accuracy per attribute rather than in aggregate, since providers are good at some and poor at others and the aggregate hides both. Compare against an internally inferred alternative, connecting to the build note, because the relevant question is not whether the purchase is accurate but whether it beats the free option. Test whether the attributes improve outcomes, since an accurate attribute that changes no decision is still not worth buying. Check coverage bias, as appended data is systematically better for some populations than others and that skew propagates into every downstream decision. Re-measure periodically, because provider quality changes and a one-time check ages. Negotiate on measured accuracy rather than on match rate, which is the leverage this exercise creates and is currently unavailable. Flag appended attributes as third-party in the profile, so downstream consumers know what they are acting on. Review the privacy basis alongside the accuracy, since the justification for buying weakens as both are examined. And report the cost per correctly appended attribute, because that single figure usually settles the renewal conversation.

## Who Feels the Pain
Organisations paying for attributes of unmeasured accuracy; customers segmented on incorrect inferences about their lives; and data teams who suspect the appends are poor and have no evidence.

## Impact If Fixed
Match rate measures coverage while looking like quality, which is the same substitution running through this whole cluster. Comparing appends against known values costs a day and produces the accuracy figure the market does not supply and the renewal conversation needs.
