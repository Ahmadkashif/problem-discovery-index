# History: AI Inference Providers

**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Primary Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** omitted — a native birth, see below
**Episode Tier:** 1
**Transferable Pattern:** A faster kernel lowers the cost of serving a model. It does not tell a customer their true marginal cost, and a provider holding that number has no commercial reason to publish it. Distinguish the engineering problem, which this wave keeps solving, from the disclosure problem, which no engineering solves.

> **Origin Parent — genuinely absent, not merely unclaimed.** A grep of every `origins/*/legacy.md` file returns nothing for this industry. That is the correct finding rather than a gap in research: renting metered compute for interactive language-model inference at consumer latency and volume did not exist as a demand shape before Wave 12, so there is no 20th-century industry to inherit it from. It is a native birth of this wave, the same way [[history/crowdsourcing-platforms|Crowdsourcing Platforms]] is a native birth of Wave 5.

## Before the Meter Ran on Tokens

Renting compute by the hour is not new — Wave 6 (cloud and SaaS) had already turned the server into a meter two decades earlier. What that era metered was general-purpose CPU time for applications with comparatively predictable, steady load. GPU rental for machine learning existed before Wave 12 too, but overwhelmingly for **training**: long-running, scheduled, batchable jobs where a burst of demand was a planning problem, not an operational crisis.

What did not exist was a market for **interactive, latency-bound inference over unstructured text, at a volume that could 10x overnight because a consumer product went viral.** That demand shape is the whole industry, and it appeared essentially without warning.

## The Origin Event — a release date, not a founding

**"Attention Is All You Need" posted to arXiv 12 June 2017** made the underlying model architecture possible; NeurIPS presented it that December. Nothing resembling a commercial inference-serving industry followed immediately, because for five years the models capable of running on this architecture were mostly research artefacts or narrow production deployments with predictable load.

**ChatGPT's release as a free public research preview on 30 November 2022** is the actual trigger. It did not change the model architecture at all — it changed who was making requests and how many of them arrived per second, with no warning and no contract negotiated in advance. The serving-infrastructure problem this industry exists to solve is a **demand-shape problem created by a product launch**, not a technology unlocked by a paper. Five years separate the two events, and the gap is itself the lesson: a capability can exist for years before the economics around it become a business.

## How It Was Actually Solved — PagedAttention and the memory problem underneath the cost problem

The concrete engineering answer to bursty, latency-bound serving is well documented and worth stating precisely, because it is the part of this file that is not contested. **Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention," posted to arXiv 12 September 2023, presented at SOSP 2023**, identified that each request's key-value cache grows and shrinks dynamically and was, before this work, managed in a way that wasted memory through fragmentation and duplication — which in turn constrained how many requests could be batched together, which is the main lever for utilisation. PagedAttention borrows the paging concept from operating-system virtual memory, achieves near-zero KV-cache waste, and the resulting **vLLM system reported a 2–4x throughput improvement at the same latency** against the prior state of the art. SGLang followed with a comparable open serving engine; TensorRT-LLM serves the NVIDIA-optimised path. Continuous batching, 8-bit and 4-bit quantisation, speculative decoding and prefix caching are now standard techniques layered on top.

This is a genuine technical achievement and it is worth being precise about what it did and did not fix. It made a given accelerator serve more requests per hour. It did not change who bears the cost of an accelerator sitting idle between bursts, and it did not create any obligation for a provider to say what fraction of the fleet that idle accelerator represents.

## The Binding Constraint — capital that depreciates against demand nobody can forecast

Accelerators are procured on long commitments — reserved instances, multi-year leases, direct purchase — and depreciate quickly against a hardware roadmap that keeps moving. Demand arrives in spikes driven by a customer's product launch, a viral moment, or an unannounced batch job. **Overprovision and the margin disappears into idle hardware; underprovision and the latency guarantee — the one thing a customer is actually buying — fails.** Hardware is overwhelmingly NVIDIA, with meaningful alternatives from AMD and specialised inference silicon occupying a latency niche.

**Groq** is the sharpest illustration of how mismatched the original hardware bet could be to the wave that ended up needing it. **Founded in 2016 by Jonathan Ross and Douglas Wightman** — Ross had designed Google's original Tensor Processing Unit — the company built the **Tensor Streaming Processor**, codenamed "Alan," as a general AI accelerator aimed at workloads including image classification, years before ChatGPT existed. Only after ChatGPT's release did Groq rebrand the same architecture as the **LPU — "Language Processing Unit"** — to make its fit for LLM inference legible to buyers who had not been the original target market. The chip did not change; the wave it was pitched into did.

## The Declined Join — a number the providers hold and do not publish

This is the section worth making central, because it is easy to mistake for an engineering gap and it is not one. The vault's own hub note is explicit that these providers hold **the most detailed record anywhere of what inference actually costs** — request-level latency, token counts, batch composition, memory pressure and utilisation across millions of requests. That corpus would answer the question every buyer actually wants answered: what does a request truly cost this provider to serve, and how much of the list price is margin against idle capacity versus margin against genuine scarcity.

**No provider publishes this.** This session's research turned up extensive technical detail on serving engines and none on public utilisation rates, true marginal cost per token, or margin structure at any named provider — a negative finding worth stating rather than papering over. That absence is not evidence of secrecy for its own sake; it is the ordinary commercial logic of not handing a customer the leverage a real cost number provides. **This is the same shape the wave-12 era file names directly: the missing join — normalising data that used to require bespoke work — is exactly what got cheap. The declined join, where a party holding a number chooses not to disclose it, is untouched, because it was never a capability problem.** A model that computes utilisation perfectly does not create a market incentive for a provider to show a customer that number.

## What's Still Open

- [[problems/ai-inference-providers/high-impact|🔴 Capacity Economics Against Bursty Demand]]
- [[problems/ai-inference-providers/low-impact-2|🟡 Multi-Tenant Isolation on Shared Accelerators]]
- [[problems/ai-inference-providers/worker-life-1|🟢 SRE During a Capacity Event]]
- [[problems/ai-inference-providers/worker-life-2|🟢 Performance Engineer Chasing Regressions]]
- [[niches/ai-inference-providers/capacity-and-utilisation/profile|Capacity & Utilisation]]
- [[niches/ai-inference-providers/inference-cost-corpus/profile|Inference Cost Corpus]]
- [[niches/ai-inference-providers/quantisation-quality-accounting/profile|Quantisation Quality Accounting]]
- [[niches/ai-inference-providers/multi-tenant-isolation/profile|Multi-Tenant Isolation]]

## The Transferable Pattern

> **Ask which half of the problem you are looking at. If the number does not exist yet, build the tool that computes it. If the number exists and is not shared, no tool changes that — only a contract term, a regulator, or a competitor willing to publish theirs does.**

Model optimisation, quantisation quality and multi-tenant isolation are all genuinely open engineering problems where a better model or a better kernel moves the needle — the vault's own hub note calls the tooling world-class and the economics underneath it unsolved, and that split is the finding. An FDE walking into a capacity crisis should expect to be handed the SRE's problem, not the provider's balance sheet, and should not assume that a faster serving engine is the same kind of fix as a transparent invoice.

**The competitive fight — genuinely unresolved, stated without a prediction.** Whether value accrues to model providers or to the inference layer running on top of them, whether proprietary optimisation work remains a moat as serving engines commoditise, and whether inference cost falls fast enough to make thin-margin, high-volume serving durable are all open, per the wave-12 era file's own instruction to write this wave with dates and mechanisms and no forecast. Ask again in a few years.

**Sources:** Vaswani et al., *Attention Is All You Need*, arXiv:1706.03762 (12 June 2017); OpenAI, ChatGPT release (30 November 2022); Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv:2309.06180, SOSP 2023; Wikipedia, *Groq*; this vault's `industries/ai-inference-providers.md`, `problems/ai-inference-providers/*.md`, and `series/eras/wave-12-transformers.md`. No public source for provider-level utilisation rates or true marginal cost per token was located during this research; that absence is recorded rather than filled with an estimate.
