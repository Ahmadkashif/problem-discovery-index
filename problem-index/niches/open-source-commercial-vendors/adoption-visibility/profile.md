# Adoption Visibility

**Parent Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to tell an open-source vendor who is actually running their software and how — and whoever does that takes the commercial function, because every decision it makes is currently based on download counts.

## Profile
**Market Size:** ~$2.4B US attributable to adoption measurement, developer analytics and commercial targeting
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** None — downloads are the only signal and they mean almost nothing
**Target Buyer:** Commercial, product and marketing leadership at open-source companies
**Automation Potential:** Very High — abundant public signal and a consent-based telemetry path both exist

## What Makes This a Distinct Niche
Open-source vendors are the only software companies with a structurally invisible customer base. A proprietary vendor knows every installation; an open-source vendor knows downloads, which conflate a build cache pulling an image a thousand times a day with a bank running a production cluster. The consequences run through every commercial decision: where to invest engineering effort, what to put behind a licence, which companies to approach, whether the open-source strategy is working at all. The signals that would answer it exist in two forms — telemetry the software could emit with consent, which the community regards with deep suspicion and frequently disables, and abundant public evidence in issues, job postings, conference talks, public code and container manifests. The contest is assembling a defensible picture from both, and the reason it is unsolved is as much about legitimacy as about analysis.

## Current Tools & Gaps
Package and container registry download counts, repository stars and forks, community platform activity, and product analytics where it is enabled. The gaps: downloads are the headline metric and are close to meaningless without deduplication and classification; telemetry is contentious, frequently disabled by default and rarely designed in a way the community would accept; public signals are abundant and scattered across a dozen sources with nobody assembling them; nothing distinguishes evaluation from production; and the relationship between any measured signal and commercial outcome has never been established, so nobody knows which signals matter.

## Problems
- [[niches/open-source-commercial-vendors/adoption-visibility/build|🔨 Build: A Build Cache and a Production Cluster Look Identical]]
- [[niches/open-source-commercial-vendors/adoption-visibility/buy|🛒 Buy: Telemetry Design That the Community Would Accept]]
- [[niches/open-source-commercial-vendors/adoption-visibility/fix|🔧 Fix: Downloads as the Headline Metric]]
