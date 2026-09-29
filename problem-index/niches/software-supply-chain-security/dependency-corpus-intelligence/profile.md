# Dependency Corpus Intelligence

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of dependency graphs, dismissals, fixes and upgrade outcomes — and whoever does that can estimate real exploitability, real upgrade risk and real remediation effort, which are the three questions every finding raises.

## Profile
**Market Size:** ~$290M US, largely latent
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** None — the corpus ships severity scores
**Target Buyer:** The vendors themselves; secondarily security leadership
**Automation Potential:** Very High — the corpus is large, structured and labelled by outcome

## What Makes This a Distinct Niche
These vendors observe the dependency graph of a large share of commercial software, joined to which vulnerabilities were fixed, which were dismissed, which were exploited and how upgrades actually went. That is the corpus from which real exploitability, real upgrade risk and real remediation effort could be estimated — the three questions every finding raises and none of the tools answer. The category instead ships severity scores computed by someone who has never seen the application, which is why its output is filed rather than acted upon. The corpus is unusually favourable: the components are literally the same software across customers, the dismissal and fix outcomes are recorded, and the useful representation contains no customer code — only which public components are present and what happened. That combination makes this the cleanest cross-customer learning opportunity in the vault and it is unexploited.

## Current Tools & Gaps
Per-customer finding histories, public advisory and exploitation databases, and aggregate research reports published as marketing. The gaps: dismissal outcomes across customers are the single best available estimate of real-world applicability and are discarded; upgrade outcomes across customers would answer the risk question directly and are not collected; exploitation evidence is consumed from public sources rather than observed; benchmarking a customer's exposure against comparable organisations is a question asked constantly and answered nowhere; and no vendor has articulated a governance position for corpus use, so the topic is avoided rather than designed.

## Problems
- [[niches/software-supply-chain-security/dependency-corpus-intelligence/build|🔨 Build: Three Questions, One Corpus, No Answers]]
- [[niches/software-supply-chain-security/dependency-corpus-intelligence/buy|🛒 Buy: Cross-Customer Learning Over Public Components]]
- [[niches/software-supply-chain-security/dependency-corpus-intelligence/fix|🔧 Fix: Every Dismissal Discarded]]
