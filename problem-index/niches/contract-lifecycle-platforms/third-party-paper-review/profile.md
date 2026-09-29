# Third-Party Paper Review

**Parent Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to find the risk in a counterparty's contract, where the dangerous term is usually the one that is absent — and whoever detects absence takes the review, because checklist review structurally cannot.

## Profile
**Market Size:** ~$410M US third-party paper review
**Share of Parent Industry:** ~14% of category revenue
**Digital Adoption:** Low — the tooling reviews against a checklist and misses what is not there
**Target Buyer:** In-house counsel and legal operations
**Automation Potential:** High — absence detection is tractable and nobody attempts it

## What Makes This a Distinct Niche
Reviewing the company's own paper is a comparison against a known baseline. Reviewing the counterparty's paper is a different exercise: the document is unfamiliar, the structure is theirs, and the most dangerous feature is frequently something that is not in it. No limitation of liability at all. No data processing terms where the deal involves personal data. No termination for convenience. No cap on the indemnity. Silence on intellectual property ownership for work product. A checklist reviews what is present against a standard and by construction cannot see what is missing, which is why this review remains stubbornly manual and why it is where the real exposure sits. The company's own standard — what must be present in any agreement it signs — exists mostly in senior lawyers' heads rather than as a document, which is the second reason the review does not scale.

## Current Tools & Gaps
Playbook review features applied to incoming paper, clause extraction, comparison against template, and manual review by counsel or outside firms. The gaps: review is present-clause-oriented, so absence is invisible; the company's minimum requirements are not written down anywhere in a form that could be checked; interaction effects between clauses — a broad indemnity with no cap, an exclusivity with no termination right — are not modelled, though they are where the compounding risk lives; and definitions are not checked, though a defined term quietly narrowed in the definitions section is a well-known method of changing a clause without touching it.

## Problems
- [[niches/contract-lifecycle-platforms/third-party-paper-review/build|🔨 Build: The Risk Is the Clause That Is Not There]]
- [[niches/contract-lifecycle-platforms/third-party-paper-review/buy|🛒 Buy: Completeness Checking Instead of Content Checking]]
- [[niches/contract-lifecycle-platforms/third-party-paper-review/fix|🔧 Fix: The Definition That Changed the Clause]]
