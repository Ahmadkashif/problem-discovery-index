# The Listing That Expired Unsold

**Niche:** [[niches/online-marketplaces/liquidity-engineering/profile|Liquidity Engineering]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** A listing that never sells produces no event anybody analyses, so the marketplace's most common outcome is also the one it knows least about.
**Tags:** #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #quick-win #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to raise the probability that a one-of-a-kind listing finds its buyer — and whoever does that takes the market, because both sides stay or leave on that number and it is worst exactly where marketplaces are most valuable.

## The Problem
Most listings on a long-tail marketplace never sell. That is the modal outcome and it is invisible in every dashboard, because the analytics are built on transactions and a listing that expires generates nothing. Nobody knows how many were never seen by anyone, how many were seen and not clicked, how many were clicked and not bought, or which attributes separate the sold from the unsold. The operator optimises conversion among listings that got as far as a view, which is a small and unrepresentative slice of their own inventory, and the seller experience the platform's growth depends on is the one it does not measure.

## Why It's Still Broken
Transaction analytics came from retail, where inventory is fungible and an unsold unit sits in a warehouse rather than representing a person's disappointment. Impression and view data exists but is used for ranking rather than for listing outcomes. Reporting that most listings never sell is an uncomfortable number for a growth narrative. And the seller who gives up does so silently.

## What a Fix Looks Like
Make the unsold listing a measured outcome. Build a listing lifecycle funnel — created, indexed, impressed, viewed, saved, contacted, sold or expired — and report the drop-off at each stage by category and cohort, which uses data the platform already has and immediately locates where inventory dies, and is the fix. Report the share of listings that received no impressions at all, since that population is invisible, is usually larger than anyone expects, and is fixable by ranking and indexing changes rather than by anything the seller can do. Use survival analysis on time-to-sale rather than a conversion rate, since listings are censored by expiry and a rate over completed sales is systematically misleading. Report sell-through by seller cohort, so the relationship between early listing outcomes and seller retention becomes visible. Attribute failure where it is attributable — price, photograph, category, attributes, demand absence — and tell the seller, which converts a measurement into a product. Distinguish thin demand from poor presentation, because the remedies differ entirely and sellers are currently left to guess. Surface aging inventory to buyers deliberately, which is a ranking choice nobody makes because ranking optimises for the click. And put sell-through on the operator's main dashboard next to gross merchandise value, since what is reported is what gets worked on.

## Who Feels the Pain
Sellers whose listings vanish into silence; buyers who never saw the item they would have bought; and operators optimising a slice of their inventory while the majority goes unexamined.

## Impact If Fixed
A listing lifecycle funnel uses data the platform already holds and locates where inventory dies. The share of listings receiving no impressions at all is usually larger than anyone expects and is fixable by the platform rather than by the seller.
