# Coverage Measurement

**Parent Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to say what fraction of a system's risk surface an assessment examined — and whoever does that takes the market, because without it a clean report is an assertion and with it it is evidence.

## Profile
**Market Size:** ~$150M US attributable to the coverage question
**Share of Parent Industry:** ~25% of category revenue
**Digital Adoption:** None — no method exists
**Target Buyer:** Anyone relying on a clean report: boards, regulators, deploying enterprises
**Automation Potential:** Medium — the measurement is constructible, the standard is a field problem

## What Makes This a Distinct Niche
A network penetration test can be scoped against an asset inventory, and a reader knows what was and was not in scope. A model has an unbounded input space and no equivalent inventory, so a report saying no critical findings might mean the system is robust, or that the team examined the wrong region of an enormous space, and nothing in the report distinguishes those. This is the industry's structural problem: regulatory demand is growing for documented testing, the documents are being produced, and their meaning is undefined. Whoever constructs a defensible coverage statement — over a stated harm taxonomy, a stated set of techniques and a stated effort — changes the artefact from an assertion into evidence, and that is the whole contest.

## Current Tools & Gaps
Engagement scoping documents, technique checklists, harm category lists, and effort described in person-weeks. The gaps: no coverage measure reported with any finding; no distinction between a system that resisted testing and testing that was insufficient; no standard for what a complete assessment examines; no decay estimate, so a report's currency is unstated; and no way to compare two firms' assessments of the same system.

## Problems
- [[niches/ai-red-teaming-firms/coverage-measurement/build|🔨 Build: A Clean Report That Means Nothing]]
- [[niches/ai-red-teaming-firms/coverage-measurement/buy|🛒 Buy: Test Coverage and Assurance Case Practice]]
- [[niches/ai-red-teaming-firms/coverage-measurement/fix|🔧 Fix: Effort Reported in Person-Weeks]]
