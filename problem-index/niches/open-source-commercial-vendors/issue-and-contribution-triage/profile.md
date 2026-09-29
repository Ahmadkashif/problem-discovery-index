# Issue & Contribution Triage

**Parent Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to reduce the queue rather than to organise it — and whoever does that takes the maintainer teams, because templates, labels and bots have been standard for a decade and the arithmetic is unchanged.

## Profile
**Market Size:** ~$410M US attributable to project triage and contribution tooling
**Share of Parent Industry:** ~1% of category revenue
**Digital Adoption:** Medium — the tooling is universal and ineffective
**Target Buyer:** Maintainer teams and the vendors employing them
**Automation Potential:** Very High — classification, deduplication and answering are all mature

## What Makes This a Distinct Niche
Issue templates, labels, stale bots and contribution guides are standard practice in every project, and a small maintainer team still faces a queue from a community orders of magnitude larger than itself. The tooling organises the queue and does not reduce it, because none of it addresses the composition: a large share of incoming issues are usage questions rather than defects, another share are duplicates of existing issues, another are reports missing the information needed to act, and a further share are contributions that will never be merged because they do not fit a direction nobody wrote down. Each of those is a mechanical problem with a mature solution — classification, semantic deduplication, guided information collection, and a stated scope — and the standard tooling addresses none of them. The contest is composition rather than organisation.

## Current Tools & Gaps
Templates, labels, stale bots, contribution guidelines, and code owner routing. The gaps: templates collect fields and do not ensure the information is sufficient, so the first response on most reports is a request for more; duplicates are found by a maintainer recognising one, not by search; usage questions are routed to the same queue as defects; contributions arrive without knowing whether the change is wanted, which wastes the contributor's effort and the maintainer's; stale bots close issues by age rather than by relevance, which annoys everyone and reduces nothing meaningful; and the queue's composition is never measured, so nobody knows what the tooling should be addressing.

## Problems
- [[niches/open-source-commercial-vendors/issue-and-contribution-triage/build|🔨 Build: Tooling That Organises and Does Not Reduce]]
- [[niches/open-source-commercial-vendors/issue-and-contribution-triage/buy|🛒 Buy: Duplicate Detection and Question Answering]]
- [[niches/open-source-commercial-vendors/issue-and-contribution-triage/fix|🔧 Fix: The Contribution Nobody Wanted]]
