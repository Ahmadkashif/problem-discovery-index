# The Referenced Standard Edition That Went Stale

**Niche:** [[niches/testing-laboratories/product-compliance-regulatory-intelligence/profile|Product Compliance Regulatory Intelligence]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** Product regulations point to test standards by edition, and when the standard is revised the vendor's mapping silently keeps citing the old one.
**Tags:** #large-language-models #transformers #compliance #quick-win #automation
**Contested on:** Every serious competitor in this pocket is fighting to tell a manufacturer, before the effective date, exactly which of its products a new or changed regulation applies to and what evidence it needs — and whoever maps regulatory change to product scope most accurately and earliest keeps the compliance team's subscription.

## The Problem
Much product regulation works by reference: a rule requires compliance with a named standard, sometimes a specific edition, and regulators update the list of accepted editions on their own schedule. Vendors record the reference as text inside a summary. When the standard is revised or the accepted edition changes, the summary is not updated until an analyst happens to notice, and clients plan testing to an edition that no longer gives market access.

## Why It's Still Broken
Standards are published by standards bodies and regulations by governments; the vendor's content model treats the citation as prose rather than as a linked object with its own lifecycle.

## What a Fix Looks Like
Store every referenced standard as a linked record with edition, status and acceptance dates per regulation; monitor standards bodies' and regulators' publications for changes; and flag every summary and client mapping that depends on a changed edition.

## Who Feels the Pain
Regulatory analysts maintaining summaries, manufacturers' compliance engineers planning tests, and testing labs quoting to the wrong edition.

## Impact If Fixed
Edition changes reach clients when they happen rather than when a test report is rejected, and a common source of rework in test programmes disappears.
