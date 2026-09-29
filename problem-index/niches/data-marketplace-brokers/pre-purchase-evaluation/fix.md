# The Sample File Chosen to Look Good

**Niche:** [[niches/data-marketplace-brokers/pre-purchase-evaluation/profile|Pre-Purchase Evaluation]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Sample files are selected by the provider from their best records, which makes them systematically unrepresentative, and every buyer knows this and evaluates on them anyway.
**Tags:** #descriptive-statistics #hypothesis-testing #probability-distributions #evaluation-metrics #confidence-intervals #monte-carlo-methods #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to let a buyer measure a dataset against their own requirement before paying for it — and whoever does that takes the market, because every purchase in it is currently made blind.

## The Problem
A provider supplies a ten-thousand-record sample. It is complete on every field, recent, and clean, because a person selected it. The full dataset is forty percent sparser on the key attributes and includes a long tail of records that have not been updated in three years. The buyer evaluates the sample, is impressed, and buys. Nothing dishonest was said; a sample is a sample, and the buyer had no way to ask for a random one and no way to verify that they got one. The market has converged on an evaluation artefact that is uninformative by construction, and everyone knows it.

## Why It's Still Broken
There is no convention requiring random sampling, so a curated sample is a legitimate choice and a competitive necessity once others do it. Verifying randomness requires access to the full dataset, which is what the buyer does not have. Buyers accept curated samples because refusing means having nothing. And a provider offering a random sample is at a disadvantage against one offering a polished one, which is exactly the dynamic a norm exists to break.

## What a Fix Looks Like
Make the sample verifiable. Require random sampling with a verifiable seed, so a buyer can check afterwards that the sample they evaluated was drawn as claimed — this is cheap, mechanically checkable, and would change the artefact's meaning entirely. Publish the sampling method with every sample, since a stated method is accountable and an unstated one is not. Provide a stratified sample across the dimensions that matter — recency, geography, segment, field completeness — which is more informative than a uniform random sample and harder to game. Report full-dataset statistics alongside the sample and let the buyer check the sample against them, which catches curation without needing the full data. Let the buyer specify the sampling criteria, so they can request the segment they actually care about rather than the one the provider chose. Offer a post-purchase remedy tied to the sample, so that a dataset materially worse than its sample triggers a refund — which puts a price on curation and is the mechanism that makes the rest credible. Have the marketplace draw the sample rather than the provider, which is the structural fix. And publish sample-versus-delivery discrepancy rates by provider, which the outcome intelligence niche develops.

## Who Feels the Pain
Buyers evaluating an artefact that was designed to persuade them; providers with genuinely complete data whose honest sample looks no better than a curated one; and the marketplaces whose transaction failure rate is driven by this.

## Impact If Fixed
A verifiable random seed costs nothing and turns the sample from a marketing artefact into evidence. A refund remedy tied to sample-versus-delivery discrepancy puts a price on curation, which is what makes every other disclosure credible.
