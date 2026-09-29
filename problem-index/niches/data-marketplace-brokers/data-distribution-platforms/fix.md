# Self-Reported Metadata in Every Catalogue

**Niche:** [[niches/data-marketplace-brokers/data-distribution-platforms/profile|Data Distribution Platforms]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Every catalogue entry's record count, coverage, freshness and field list is typed in by the provider and checked by nobody, which makes catalogue search a search over claims.
**Tags:** #descriptive-statistics #evaluation-metrics #compliance #hypothesis-testing #data-integration #automation #quick-win #confidence-intervals
**Contested on:** Not terminal — the contest differs by whether the platform is delivering data or finding it, and the decomposition is recorded in the profile.

## The Problem
A buyer filters a catalogue for datasets covering at least fifty million records, refreshed weekly, with a particular field present. The filter returns eleven listings. Every attribute it filtered on was typed in by the provider at listing time, never verified, and in several cases never updated since. Two of the eleven no longer refresh weekly. Three define the field differently from the buyer's meaning. One has not been updated in a year and is still listed. The search returned a set of claims, which is not what the buyer thought they were searching.

## Why It's Still Broken
Verification costs the marketplace money on a listing that may never transact, and listings are the inventory the marketplace's value depends on. A verification regime would reduce catalogue size, which reads as a weaker marketplace. Providers would resist. And buyers cannot tell the difference between a verified and an unverified catalogue from the outside, so there is no demand pressure.

## What a Fix Looks Like
Verify what is cheap to verify and label the rest. Verify the mechanically checkable attributes — record count, field list, field population rates, actual refresh cadence — by running a profiler against the delivered data for any listing that transacts, which costs almost nothing and converts the most-used filters into facts. Label every attribute as verified, self-reported or stale, so a buyer knows what kind of claim they are filtering on, which is the minimum honest step and requires no new measurement. Timestamp every attribute and expire the ones that age, since a listing that has not been touched in two years should not present as current. Re-verify on a schedule for active listings. Report provider-level accuracy — how often their claims match delivery — which the outcome intelligence niche develops and which gives providers a reason to be careful. Let buyers report discrepancies and route them into the listing, which is cheap crowdsourced verification. Require a structured definition for each field rather than a name, since definitional mismatch is as common as factual error and is entirely undetectable today. And rank verified listings above unverified ones, which is the incentive that makes providers ask to be verified.

## Who Feels the Pain
Buyers filtering on claims and discovering the difference after purchase; providers whose accurate listings rank alongside careless ones; and the marketplaces whose search function does not do what buyers believe it does.

## Impact If Fixed
Labelling every attribute as verified, self-reported or stale requires no new measurement and tells a buyer what kind of claim they are filtering on. Verifying the mechanically checkable attributes on any listing that transacts is nearly free and covers the filters buyers actually use.
