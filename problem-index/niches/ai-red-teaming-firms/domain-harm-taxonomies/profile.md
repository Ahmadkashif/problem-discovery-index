# Domain Harm Taxonomies

**Parent Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to enumerate what actually goes wrong in one regulated deployment rather than what goes wrong in general — and whoever does that takes the account, because the generic list is the part the client already has.

## Profile
**Market Size:** ~$70M US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Very Low — generic categories, specific deployments
**Target Buyer:** Regulated sector buyers deploying models into consequential decisions
**Automation Potential:** Medium — elicitation is the bottleneck, application is automatable

## What Makes This a Distinct Niche
Generic harm categories are well established and widely published. What actually goes wrong in a clinical triage assistant is a plausible recommendation that is wrong for a patient with a specific comorbidity, a confident answer where the correct response is escalation, or an output that is clinically fine and violates a documentation requirement. In a lending system it is a chain of reasoning that reaches a decision correlated with a protected characteristic through a proxy, or an explanation that does not satisfy an adverse action requirement. None of those appear on any published harm list, they require a clinician or a credit officer to articulate, and the assessment that does not include them is examining the wrong surface regardless of how competently it examines it.

## Current Tools & Gaps
Published generic harm taxonomies, regulatory category lists, and domain expert interviews during scoping. The gaps: no reusable taxonomy per regulated domain; no method for eliciting domain-specific harms systematically; no reuse across clients in the same sector; no mapping from domain harms to the regulatory obligations they implicate; and no probes derived from a domain harm, so the taxonomy stops at a list.

## Problems
- [[niches/ai-red-teaming-firms/domain-harm-taxonomies/build|🔨 Build: What Goes Wrong Here Is Not on Any List]]
- [[niches/ai-red-teaming-firms/domain-harm-taxonomies/buy|🛒 Buy: Hazard Analysis From Safety Engineering]]
- [[niches/ai-red-teaming-firms/domain-harm-taxonomies/fix|🔧 Fix: The Taxonomy That Stops at a List]]
