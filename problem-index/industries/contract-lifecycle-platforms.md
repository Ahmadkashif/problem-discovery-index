# Contract Lifecycle Platforms

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$3B US contract lifecycle management software
**Tech Maturity:** High promise, poor realisation — Ironclad, Icertis, Agiloft, LinkSquares, Evisort and DocuSign CLM have built capable authoring, workflow and repository products. Implementation failure rates in the category are notorious, and the reason is consistent: the value depends on the executed back catalogue being structured, and structuring it was always someone else's problem.
**Workforce:** Legal operations specialists, contract managers, implementation consultants, clause library administrators, obligation and compliance analysts, in-house counsel

## Key Pain Themes
Companies do not know what they have promised. The obligations they carry — service levels, notice periods, exclusivity, most-favoured-nation clauses, data commitments, indemnity caps — are in thousands of executed agreements, and the only way to answer a question about them is for a lawyer to read. CLM systems were sold to fix this and mostly manage new contracts going forward while the back catalogue, which is where the liability lives, stays a folder of PDFs. Around that sit two persistent burdens: clause libraries and negotiation playbooks that require constant curation and go stale; and third-party paper review, where counsel reads a counterparty's contract against a standard the company holds mostly in senior lawyers' heads. Legal operations triages a queue with no way to distinguish a routine NDA from something genuinely dangerous, and counsel spends its most expensive hours on first-pass redlines.

## Current Tech Landscape
Ironclad and Icertis lead enterprise CLM from different directions — workflow-first and obligation-first respectively; Agiloft competes on configurability; LinkSquares and Evisort grew from the extraction and repository side. DocuSign has extended from signature into agreement management. Clause libraries and playbooks are standard features. Extraction quality improved substantially with transformer models and has improved again with large language models. Negotiation analytics — what terms this counterparty accepted before — exists in the more mature products and is thin. Adoption remains concentrated in large enterprises with legal operations functions.

## Problems
- [[problems/contract-lifecycle-platforms/high-impact|🔴 High Impact: The Unstructured Back Catalogue]]
- [[problems/contract-lifecycle-platforms/low-impact-1|🟡 Low Impact: Clause Library and Playbook Curation]]
- [[problems/contract-lifecycle-platforms/low-impact-2|🟡 Low Impact: Third-Party Paper Review]]
- [[problems/contract-lifecycle-platforms/worker-life-1|🟢 Worker Life: Legal Operations Queue Triage]]
- [[problems/contract-lifecycle-platforms/worker-life-2|🟢 Worker Life: Counsel on First-Pass Redlines]]
- [[problems/contract-lifecycle-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/contract-lifecycle-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A CLM vendor serving many enterprises observes what terms are actually achievable — which positions counterparties accept, how often, in which industries, at which deal sizes, and how long each negotiation takes. Every in-house legal team asks that question constantly and answers it from the memory of whoever has been there longest. It is the one thing the category could know that no single company can, and it is almost entirely unexploited because the vendors sell repositories rather than evidence.
