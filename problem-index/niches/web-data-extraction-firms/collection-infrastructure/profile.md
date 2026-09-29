# Collection Infrastructure

**Parent Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Category:** High Market Share
**Contested on:** Not terminal — the contest differs by whether the problem is reaching the page or reading it, and the decomposition is recorded below.

## Profile
**Market Size:** ~$620M US
**Share of Parent Industry:** ~31% of category revenue
**Digital Adoption:** High
**Target Buyer:** Extraction engineers; separately, data teams
**Automation Potential:** High

## What Makes This a Distinct Niche
This is the stack that turns a target list into delivered data: address pools, request routing, browser automation, rendering, parsing and structuring. It is the industry's largest revenue line and the surface every firm competes on.

It is **not terminal**, because collection names a pipeline whose two halves are contested on unrelated axes. Reaching a page that does not want to be reached is an adversarial economics problem: success rate against evolving detection, address pool quality and provenance, geographic coverage, and cost per successful request. Reading that page correctly is a parsing correctness problem: given arbitrary markup, return the fields the customer asked for, with the cost measured in model tokens per page rather than in bandwidth. The buyers differ — an engineer procuring access against a data team procuring structure — the competitors differ, and the cost structures have nothing in common. Filter Notes in the overview records the two rejected alternatives; the sub-niches below are the split.

## Current Tools & Gaps
Residential and datacentre address pools, headless browser automation, rendering farms, selector-based and model-based extraction, and scheduling. The gaps are specific to each half and are stated in the sub-niches.

## Problems
- [[niches/web-data-extraction-firms/collection-infrastructure/build|🔨 Build: Reaching the Page and Reading It Are Different Businesses]]
- [[niches/web-data-extraction-firms/collection-infrastructure/buy|🛒 Buy: Distributed Crawling and Politeness]]
- [[niches/web-data-extraction-firms/collection-infrastructure/fix|🔧 Fix: Cost Reported Per Request, Not Per Useful Record]]
