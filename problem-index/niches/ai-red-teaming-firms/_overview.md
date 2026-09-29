# Niche Analysis — AI Red Teaming Firms

**Parent Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Coverage Measurement | 🔵 High Market Share | $150M | None — no method exists | Anyone relying on a clean report |
| 2 | Assessment Services & Tooling | 🔵 High Market Share | $170M | Moderate | Labs and regulated enterprises; separately, engineering teams |
| 3 | Domain Harm Taxonomies | 🟠 Low Digitized | $70M | Very Low — generic categories, specific deployments | Regulated sector buyers |
| 4 | Assessment Revalidation | 🟠 Low Digitized | $55M | Low — a model update makes the report stale | Clients on a model upgrade path |
| 5 | The Red Team Researcher | 🟣 Underserved Audience | $35M | None — exposure as a job requirement | The researchers and the firms employing them |
| 6 | The Report Writer | 🟣 Underserved Audience | $30M | None — the best researchers write documents | Assessment delivery organisations |
| 7 | Severity & Exploitability | ⚡ Highly Automatable | $60M | Low — severity is contested and unscored | Everyone receiving a findings list |
| 8 | Assessment Corpus Intelligence | ⚡ Highly Automatable | $50M | None — the only cross-model failure record, unused | The firms themselves |

## Why These Niches

Coverage is unmeasurable and everything follows from it. A network test can be scoped against an asset inventory; a model has an unbounded input space and no equivalent, so a report saying no critical findings might mean the system is robust or might mean the team looked in the wrong places — and neither the firm nor the client can tell. Regulatory pressure is generating demand for documented testing regardless, which means the market is growing on an artefact whose meaning nobody can establish. That makes coverage the largest contested surface and the one that would change what this industry is able to sell.

Assessment **failed the filter as one niche**. Expert engagement work is won by finding what automation and the client's own team missed, is bought by a small number of labs and regulated enterprises under confidentiality, is priced per engagement, and competes with an internal team. Automated probing is won on breadth, currency and cost per system, is bought by engineering and security teams as a continuously-running product, and competes with open jailbreak datasets and a script somebody wrote. The skills, the buyers, the pricing and the definition of a good result are all different. Decomposed below.

The two underdigitised areas are both places where the generic does not fit the specific. Generic harm categories are well established and published, and what actually goes wrong in a clinical triage assistant or a lending system is on none of those lists. And a client's model update invalidates an entire assessment with no established way to revalidate short of another engagement.

The two underserved constituencies are the researcher whose working day consists of deliberately eliciting the worst outputs a model can produce, in an industry that has largely not addressed what that does to people, and the senior researcher who spends the end of every engagement writing documents rather than doing research.

The automation niches are severity assessment, which is far more contested here than in conventional security and is scored by nothing, and the cross-model record of what actually fails, which is this industry's unique asset and is commercially awkward to publish.

## Niches
- [[niches/ai-red-teaming-firms/coverage-measurement/profile|🔵 Coverage Measurement]]
- [[niches/ai-red-teaming-firms/assessment-services-and-tooling/profile|🔵 Assessment Services & Tooling]]
  - [[niches/ai-red-teaming-firms/manual-expert-assessment/profile|🎯 Manual Expert Assessment]]
  - [[niches/ai-red-teaming-firms/automated-probing-platforms/profile|🎯 Automated Probing Platforms]]
- [[niches/ai-red-teaming-firms/domain-harm-taxonomies/profile|🟠 Domain Harm Taxonomies]]
- [[niches/ai-red-teaming-firms/assessment-revalidation/profile|🟠 Assessment Revalidation]]
- [[niches/ai-red-teaming-firms/the-red-team-researcher/profile|🟣 The Red Team Researcher]]
- [[niches/ai-red-teaming-firms/the-report-writer/profile|🟣 The Report Writer]]
- [[niches/ai-red-teaming-firms/severity-and-exploitability/profile|⚡ Severity & Exploitability]]
- [[niches/ai-red-teaming-firms/assessment-corpus-intelligence/profile|⚡ Assessment Corpus Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Assessment Services & Tooling** is not: it names the delivery of the same nominal service through two businesses with unrelated contests. Manual expert assessment competes on judgement and novelty — finding the thing nobody else thought of — for a handful of high-value clients under confidentiality, against their own internal capability. Automated probing competes on breadth, freshness and cost per system for many clients as a continuously-running product, against freely available datasets and an afternoon of scripting. The skill base, the buyer, the pricing model and the evidence that wins each deal differ completely. Decomposed into two contested sub-niches.

Two candidates were rejected. *Runtime guardrail products* was rejected because its contest is low-latency filtering of live traffic, bought as infrastructure by engineering teams, which belongs with the trust and safety tooling industry covered separately in this vault. *Capability evaluation and benchmarking* was rejected because it belongs to the AI model evaluation industry, also covered separately, where the contest is measuring what a model can do rather than what it can be induced to do.
