# Wave 12 — Transformers (2017– )

**Trigger:** *Attention Is All You Need* posted to arXiv **June 12 2017** (Vaswani et al., presented at NeurIPS Dec 2017); ChatGPT released as a free public research preview **Nov 30 2022**
**What went to ~zero:** the cost of **inference over unstructured text**
**Failure class produced:** too early to say — and saying so is the correct entry

## What Was True The Day Before

Unstructured text was the largest and least usable asset most businesses held. Contracts, notes, tickets, emails, transcripts, filings. Extracting structure from it required either a person reading it or a narrow model trained on labelled examples for that one task, in that one format.

The cost of the second option was the labelling. That is why, in wave after wave of this vault, the pattern recurs: the organisation has the document and does not have the field.

## The Trigger

The Transformer made sequence modelling parallelisable, which made it scalable, which made general-purpose language models economically possible. Five years later ChatGPT made the capability legible to people who buy software.

The commercially decisive property is not fluency. It is that **a single model performs tasks it was not specifically trained for**, which removes the per-task labelling cost that gated every previous approach.

## What Became Possible

Reading the document at population scale. Every "the record exists but the field does not" problem in this vault becomes tractable — not solved, tractable. Clinical history condensed into a pre-visit brief. Decline-reason vocabularies normalised across thousands of issuers. Rejection reasons made explicit. Contract obligations extracted without a template.

Note what this does to the earlier waves' failure classes. **The missing join becomes cheap to close.** Where two systems never spoke because normalising between them required bespoke engineering per pair, a model can often do the normalising.

**It does nothing whatsoever to the declined join or the asymmetric hold.** Those were never capability problems. A party that chooses not to compute an honest number will not be compelled to by a better model, and a platform that withholds a measurement from a worker is not withholding it for want of technique. The vault's Phase 2 notes were right to say so, and any episode on this wave must say so too — otherwise it becomes the marketing it should be examining.

## The Competitive Fight

Genuinely unresolved, which is why this wave gets the shortest section and no confident claims.

The visible contests: whether value accrues to model providers or to the application layer above them; whether proprietary data moats survive models that are already competent without them; whether inference cost falls fast enough to make per-task economics work; and whether the labelling industry this vault documents (data labelling, synthetic data, model evaluation, red teaming) is a durable sector or scaffolding for a building that will not need it.

**Write this wave with dates and mechanisms and without predictions.** Everything in the eleven waves above is settled enough to teach. This one is not, and the honest treatment of a live question is itself the lesson — an FDE's most transferable skill is distinguishing what is known from what is merely asserted confidently.

## What It Broke

Ask again in five years. Recording that this section is deliberately empty is more useful than filling it.

## Children in This Vault

**Primary:**
- [[industries/ai-agent-platforms|AI Agent Platforms]]
- [[industries/ai-inference-providers|AI Inference Providers]]
- [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
- [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
- [[industries/data-labeling-services|Data Labeling Services]]
- [[industries/llm-application-tooling|LLM Application Tooling]]
- [[industries/synthetic-data-providers|Synthetic Data Providers]]
- [[industries/vector-search-vendors|Vector Search Vendors]]

**Secondary:**
- [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
- [[industries/mlops-platforms|MLOps Platforms]]
- [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
- [[industries/software-supply-chain-security|Software Supply Chain Security]]
- [[industries/localization-services|Localization Services]]
- [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
- [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
- [[industries/brand-protection-firms|Brand Protection Firms]]
- [[industries/content-moderation-services|Content Moderation Services]]
- [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]

**Sources:** Vaswani et al., *Attention Is All You Need*, arXiv:1706.03762 (June 12 2017), NeurIPS 2017; OpenAI, ChatGPT release (Nov 30 2022); this vault's Phase 2 Stage A findings (`_phase2-plan.md`).
