# The Issuer Data Dispute Run by Email

**Niche:** [[niches/asset-managers/esg-ratings-providers/profile|ESG Ratings & Sustainability Research Providers]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Thousands of companies challenge the data behind their ESG ratings each year, and the provider processes the disputes as an email queue.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this pocket is fighting to show that its ratings measure something real and are produced by a documented, consistently applied method — and whoever can evidence that, issuer by issuer, keeps its asset-manager clients through the EU authorisation regime and the political backlash against ESG labels.

## The Problem
Rated companies review their profiles and send corrections: an outdated emissions figure, a controversy resolved, a policy the analyst missed. Analysts verify against disclosures, update, and reply. Volumes peak after methodology changes and reporting seasons, and the queue delays rating updates clients are waiting for.

## Why It's Still Broken
Disputes arrive unstructured, cite documents in varied formats, and are routed by issuer rather than by type. Nothing measures which data points are disputed most often, which is a direct signal of where the methodology or the data pipeline is weak.

## What a Fix Looks Like
Language-model triage that extracts the disputed data points, retrieves the cited disclosure, proposes a verified correction or a rejection with reason, and routes only genuine judgment calls to analysts; plus a dispute analytics view feeding methodology review.

## Who Feels the Pain
ESG analysts handling disputes; issuers waiting; asset managers holding stale ratings.

## Impact If Fixed
Faster, documented corrections and a feedback loop from disputes into data quality.
