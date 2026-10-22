# The Rent Roll Read Once a Year

**Niche:** [[niches/community-banks/cre-lending-concentration/profile|CRE Lending & Concentration Risk]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Fix (Pain Point)
**One-liner:** Borrowers send rent rolls as PDFs, analysts re-key a few totals at annual review, and lease expirations that will gut next year's NOI are never captured.
**Tags:** #large-language-models #transformers #feature-engineering #quick-win #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to show a CRE-concentrated bank's board and examiner, loan by loan, which properties will fail to refinance at today's rates before the maturity arrives, and whoever produces that answer from the bank's own rent rolls and maturity schedule fastest takes the account.

## The Problem
An analyst reviewing a retail centre loan receives a rent roll listing tenants, square footage, rent and lease end dates. The spread records total rent and occupancy. The anchor tenant whose lease ends in fourteen months, and the three tenants on month-to-month terms, disappear into a total.

## Why It's Still Broken
Rent rolls have no standard layout, abstracting them line by line takes longer than the annual review allows, and the spreading tools have fields for totals, not tenants.

## What a Fix Looks Like
Extract every rent roll into a tenant table at receipt: tenant, area, rent, lease start and end, options. Store it against the property, compute rollover exposure by quarter, and flag loans where leases covering more than a set share of rent expire before maturity.

## Who Feels the Pain
Credit analysts re-keying documents; chief credit officers surprised by a vacancy; examiners asking for lease rollover analysis the bank cannot produce.

## Impact If Fixed
A small extraction step makes lease rollover visible across the whole CRE book and feeds every stress test and refinance analysis that follows.
