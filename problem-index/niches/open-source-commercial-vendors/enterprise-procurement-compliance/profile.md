# Enterprise Procurement & Compliance

**Parent Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to get open-source software through an enterprise's legal, security and procurement review without a three-month project — and whoever does that takes the enterprise adoption, because the review is where it currently stops.

## Profile
**Market Size:** ~$2.6B US attributable to open-source compliance, review and enterprise enablement
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Low — the review is conducted by lawyers and spreadsheets
**Target Buyer:** Enterprise procurement, legal, security and architecture review functions
**Automation Potential:** High — licence analysis and dependency provenance are mechanical

## What Makes This a Distinct Niche
An enterprise adopting an open-source component runs a review that has almost nothing to do with the software's merits: which licence, what obligations does it impose, who maintains it, what is its security posture, what happens if the maintainer stops, are there patent implications, can we get support and indemnity, and is it on the approved list. The review takes weeks to months, is conducted largely by hand, and is repeated by every enterprise for every component. It is also the point at which a great many adoptions stop, which makes it a commercial problem for the vendors and a productivity problem for the enterprises. The information required — licence terms, dependency trees, maintainer activity, vulnerability history, release cadence — is entirely public and machine-readable, and the review is a reading exercise.

## Current Tools & Gaps
Software composition analysis tools that inventory dependencies and licences, approved-component registries maintained internally, legal review processes, and vendor support agreements offering indemnity. The gaps: composition analysis identifies licences and stops short of the obligations they impose in the specific usage context, which is the actual legal question; maintainer health and project sustainability are not assessed at all, although abandonment is the enterprise's real risk; every enterprise repeats the same review of the same popular components independently; the approved list goes stale and becomes a bottleneck; and the vendor's side of the process — supplying the evidence a review needs — is an unstructured effort per deal.

## Problems
- [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/build|🔨 Build: Every Enterprise Reviews the Same Component]]
- [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/buy|🛒 Buy: Licence Obligation Analysis Beyond Identification]]
- [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/fix|🔧 Fix: The Approved List That Became a Bottleneck]]
