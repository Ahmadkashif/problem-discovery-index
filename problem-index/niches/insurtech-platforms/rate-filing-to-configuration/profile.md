# Rate Filing to Configuration

**Parent Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in rating technology is fighting to turn an approved filing into working, verified configuration across fifty states without a specialist retyping it — and whoever shortens filing-to-production most takes the account.

## Profile
**Market Size:** ~$520M US spend on rating configuration, filing management and the specialist labour around them
**Share of Parent Industry:** ~3% of insurtech revenue, gating the speed of everything above it
**Digital Adoption:** Low — filings are documents and configuration is hand-built from them
**Target Buyer:** Product, actuarial operations and compliance leaders at carriers
**Automation Potential:** Very High — this is translation between two structured artefacts, performed by people

## What Makes This a Distinct Niche
A carrier that wants to change a rate must file it with each state's insurance department, wait for approval, and then implement it. The implementation is the niche: a filed rate manual — tables, factors, algorithms, rules, expressed in a document written for a regulator — must be translated into configuration in a rating engine, exactly, for every state, with the state-specific variations that filings inevitably contain. The translation is done by specialists who read the filing and build the configuration, and it is checked by testing sample risks. It is slow, it is a bottleneck on every product change, and its failure mode is severe: configuration that does not match the filed rate means the carrier is charging something other than what it filed, which is a regulatory matter in every state where it occurs. The work is pure translation between two structured artefacts and is performed by people because nobody has built the bridge.

## Current Tools & Gaps
Rating engines are mature and configurable. Filing management systems — SERFF and the commercial products around it — handle submission and tracking. Rate manuals are produced in document form for regulatory purposes. The gap is entirely in the middle: nothing translates a filing into configuration, nothing verifies that production configuration matches the filed rate, and nothing maintains the correspondence as either side changes. Carriers manage the risk with review processes and by keeping the specialists who understand both sides, which works and does not scale. The exposure grows with every state and every product, and the specialists are a small and ageing population.

## Problems
- [[niches/insurtech-platforms/rate-filing-to-configuration/build|🔨 Build: The Filing as a Machine-Readable Artefact]]
- [[niches/insurtech-platforms/rate-filing-to-configuration/buy|🛒 Buy: Document Extraction Applied to Rate Manuals]]
- [[niches/insurtech-platforms/rate-filing-to-configuration/fix|🔧 Fix: Nobody Verifies Production Against the Filed Rate]]
