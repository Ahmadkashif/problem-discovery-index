# The Transformer Sized by Rule of Thumb

**Niche:** [[niches/electric-utilities/new-service-connection-design/profile|New Service Connection Design & Estimating]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** Service transformers are sized from decades-old diversity tables, so new all-electric homes overload them while other units sit half-used during a transformer shortage.
**Tags:** #linear-regression #gradient-boosting #feature-engineering #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a builder's or customer's new-service request into a designed, estimated and scheduled job in days, and whoever cuts request-to-energise time without redesigns in the field takes the account.

## The Problem
Designers pick distribution transformer sizes from standard tables of expected demand per home, built before heat pumps, EV chargers and induction ranges. Some new neighbourhoods overload their transformers within a few years, causing failures and outages. Others are oversized while the utility waits on scarce units: Wood Mackenzie put pad-mount distribution transformers at ~75 weeks on average in mid-2024 and distribution transformer unit costs up 78–95% since 2019.

## Why It's Still Broken
Design standards change slowly, and the evidence to update them, actual AMI loading of transformers by home type and equipment, is held by meter operations, not design.

## What a Fix Looks Like
Use AMI data from recent developments to fit peak demand per home by size, heating type, EV presence and climate zone. Update the design tables, and flag in-service transformers already near overload for proactive replacement.

## Who Feels the Pain
Designers defending sizing choices; operations crews replacing failed units; customers with outages; supply-chain teams short of transformers.

## Impact If Fixed
~10%–30% fewer transformer failures in new all-electric developments and right-sized orders during a shortage that has pushed unit costs up 78–95% since 2019 (Wood Mackenzie; failure reduction is an estimate).
