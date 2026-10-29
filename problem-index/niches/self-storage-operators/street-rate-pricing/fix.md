# Promotions Compared at Face Value

**Niche:** [[niches/self-storage-operators/street-rate-pricing/profile|Street-Rate Pricing & Move-In Promotions]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Fix (Pain Point)
**One-liner:** One competitor advertises, say, $59 plus a $29 admin fee and the next store $89 with the first month free, and the rate survey records $59 and $89.
**Tags:** #large-language-models #feature-engineering #quick-win #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to set each vacant unit type's web rate and promotion every day against nearby competitors, and whoever earns the most rental revenue per available square foot takes the account.

## The Problem
Storage pricing is promotion-heavy: first month $1, 50% off three months, a free truck, an admin fee. Surveys and many data feeds record the headline rate. The store then matches a competitor who is not actually cheaper, or misses one who is. Slate's January 2025 reporting described a 5x10 advertised at $19 against a street rate about five times that.

## Why It's Still Broken
Promotions are free text, change weekly and combine with fees and terms in fine print. Data feeds standardise rates, not offers, and the people collecting rates by hand have no rule for comparing them.

## What a Fix Looks Like
Parse every competitor offer into an effective monthly rent over a standard expected stay, for example 12 months including fees and promotions. A language model reads the offer text and a rule set computes the effective rent. The rate board shows effective rent next to the headline, and pricing rules use the effective figure.

## Who Feels the Pain
Revenue managers and district managers matching the wrong competitor; owners losing revenue to promotion wars nobody needed.

## Impact If Fixed
If a quarter of a store's rate changes respond to misread promotions (estimate), correcting them could lift revenue per available square foot by ~0.5% (estimate), ~$3,500 a year at a $700,000 store, from a parser that costs almost nothing to run.
