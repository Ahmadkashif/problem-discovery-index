# The Exceptions That Live in the Acquired Bank's Staff

**Niche:** [[niches/community-banks/conversion-mapping-cutover/profile|Conversion Data Mapping & Cutover]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Fix (Pain Point)
**One-liner:** The fee waived for the church, the overdraft limit the old CEO approved, the business customer on a custom analysis plan: none of it is in the product file, and it disappears at conversion.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to move every product, fee code, GL account and customer exception correctly on the first live weekend, and whoever's conversion gets through the first statement cycle without a complaint spike takes the account.

## The Problem
Small banks run on exceptions granted by people. They are recorded, if at all, as account-level overrides, notes fields or memory. The conversion maps products, not exceptions, and the acquired bank's staff, some of whom are leaving after the deal, are interviewed once.

## Why It's Still Broken
Overrides are scattered across core fields and notes; nobody owns the list; and the people who know are distracted by their own job uncertainty.

## What a Fix Looks Like
Scan the source core for every account whose terms differ from its product's defaults (waived fees, custom rates, special limits), read notes fields for the reasons, and present the list to the acquired bank's staff for confirmation before the first mock conversion. Each confirmed exception is mapped explicitly and tested in reconciliation.

## Who Feels the Pain
Long-standing customers charged fees for the first time; branch staff fielding complaints; acquirers losing deposits they paid a premium for.

## Impact If Fixed
The relationships that made the acquired bank valuable survive the conversion weekend.
