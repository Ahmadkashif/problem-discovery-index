# Commercial Policy Endorsement Tracker

**Niche:** [[niches/public-adjusters/commercial-property/profile|Commercial Property Claims]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document management systems exist, but none parse commercial property insurance policies to extract, index, and cross-reference endorsements that modify base coverage for specific loss types.
**Tags:** #llm #named-entity-recognition #nlp #compliance

## The Problem
Commercial property policies contain 50-150 endorsements that modify, expand, restrict, or replace base policy provisions. When a loss occurs, the PA must identify which endorsements apply — and the interaction between endorsements can be critical. An endorsement adding equipment breakdown coverage might be limited by another endorsement excluding losses caused by electrical surge. Experienced PAs develop mental maps of endorsement interactions over years of practice. Junior adjusters miss coverage or accept exclusions that an endorsement elsewhere in the policy overrides.

## What Already Exists
Document management systems (SharePoint, Google Drive, Dropbox) store policy documents. PDF readers offer text search. Legal document analysis tools (Kira Systems, Luminance) parse contracts but are designed for law firms, not insurance. None index endorsements by modification type, cross-reference them against base provisions, or flag endorsement interactions relevant to a specific loss type.

## The Customization Gap
The gap is an endorsement parsing engine specific to commercial property policies. It must recognize standard endorsement forms (ISO CP series, carrier-specific forms), map each endorsement's effect on base coverage (expands, restricts, replaces, adds sublimit), and enable the PA to query: "For a water damage loss at this property, which endorsements modify Coverage A?" The output is a coverage analysis memo with endorsement citations — not just a document index.

## Target Customer
PA firms handling commercial property claims where policies average 200+ pages with 80+ endorsements, typically on losses exceeding $250,000.

## Impact If Solved
Reduces commercial policy analysis time from 6-10 hours to 1-2 hours per claim. Identifies overlooked coverage endorsements on 15-25% of claims, increasing average settlement recovery by $10,000-$50,000 on affected claims.
