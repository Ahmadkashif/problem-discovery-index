# Niche Analysis — AI Inference Providers

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Capacity & Utilisation | 🔵 High Market Share | $1.6B | Low — the margin sits in an unmeasured gap | The providers themselves and their investors |
| 2 | Model Serving Platforms | 🔵 High Market Share | $1.9B | High | Product teams; separately, data teams |
| 3 | Model Optimisation Per Target | 🟠 Low Digitized | $420M | Very Low — hand work redone every release | Performance engineering organisations |
| 4 | Multi-Tenant Isolation | 🟠 Low Digitized | $380M | Very Low — primitives not designed for this | Platform and reliability teams |
| 5 | The Capacity SRE | 🟣 Underserved Audience | $260M | None — arbitration by hand under pressure | Site reliability teams and their leadership |
| 6 | The Performance Engineer | 🟣 Underserved Audience | $220M | None — bisecting an unversioned stack | Performance engineering teams |
| 7 | Quantisation Quality Accounting | ⚡ Highly Automatable | $340M | Low — routine practice, inconsistent measurement | Anyone buying a quantised deployment |
| 8 | Inference Cost Corpus | ⚡ Highly Automatable | $300M | None — used to generate invoices | The providers themselves |

## Why These Niches

This is world-class engineering on top of an unsolved economics problem. Accelerators are bought on long commitments and depreciate quickly, demand arrives in unannounced spikes, and the entire margin sits in the gap between what is provisioned and what is used. Overprovision and the margin goes to idle hardware; underprovision and the latency guarantee fails, which is the one thing the customer is buying. Capacity is therefore the largest contested surface in the industry and the one that decides who survives it.

Model serving **failed the filter as one niche**. Interactive token serving is fought over time-to-first-token and inter-token latency under concurrent load, bought by product teams whose users are waiting, priced per token with a latency guarantee attached. Batch and throughput inference is fought over cost per million tokens with no latency requirement at all, bought by data teams running offline scoring and embedding jobs, and won by exploiting exactly the interruptible capacity the interactive workload cannot touch. The scheduling, the pricing, the buyer and the hardware strategy differ completely. Decomposed below.

The two underdigitised areas are both engineering treadmills. Every new model architecture requires weeks of hand optimisation per hardware target, redone with the next release. And sharing accelerators across tenants is the only route to acceptable utilisation on hardware whose isolation primitives were not designed for it.

The two underserved constituencies are the reliability engineer deciding in real time which customer gets degraded so another does not, and the performance engineer bisecting latency regressions across a stack where the serving engine, the driver, the kernel library, the model and the hardware all move independently and none of it is pinned.

The automation niches are the quantisation whose quality cost is asserted rather than measured, and the request-level corpus that would answer what inference actually costs and which is used to generate invoices.

## Niches
- [[niches/ai-inference-providers/capacity-and-utilisation/profile|🔵 Capacity & Utilisation]]
- [[niches/ai-inference-providers/model-serving-platforms/profile|🔵 Model Serving Platforms]]
  - [[niches/ai-inference-providers/interactive-token-serving/profile|🎯 Interactive Token Serving]]
  - [[niches/ai-inference-providers/batch-and-throughput-inference/profile|🎯 Batch & Throughput Inference]]
- [[niches/ai-inference-providers/model-optimisation-per-target/profile|🟠 Model Optimisation Per Target]]
- [[niches/ai-inference-providers/multi-tenant-isolation/profile|🟠 Multi-Tenant Isolation]]
- [[niches/ai-inference-providers/the-capacity-sre/profile|🟣 The Capacity SRE]]
- [[niches/ai-inference-providers/the-performance-engineer/profile|🟣 The Performance Engineer]]
- [[niches/ai-inference-providers/quantisation-quality-accounting/profile|⚡ Quantisation Quality Accounting]]
- [[niches/ai-inference-providers/inference-cost-corpus/profile|⚡ Inference Cost Corpus]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Model Serving Platforms** is not: it names what every provider sells rather than a contest, and the two workloads inside it are run on different principles. Interactive serving is won on tail latency under concurrency and is bought by product teams whose alternative is a frontier model API. Batch inference is won on cost per million tokens with latency essentially unconstrained, is bought by data teams whose alternative is a spot-instance job they run themselves, and its whole advantage comes from using interruptible capacity that an interactive guarantee forbids. Different scheduling, different hardware strategy, different pricing model, different buyer. Decomposed into two contested sub-niches.

Two candidates were rejected. *Training and fine-tuning services* was rejected because its contest is a different business — long-running jobs with no latency guarantee and an entirely different failure model — and the adjacent problems are covered under MLOps platforms in this vault. *Specialised inference silicon* was rejected because designing and fabricating accelerators is hardware manufacturing rather than a service market, and the providers here are its customers.
