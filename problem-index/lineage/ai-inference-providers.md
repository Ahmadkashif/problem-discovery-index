# Lineage: AI Inference Providers

**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** vLLM and its PagedAttention algorithm — an open-source LLM serving engine that stores each request's attention key-value cache in fixed-size blocks mapped through a block table, like pages of virtual memory; released 20 June 2023
**Builder:** University of California Berkeley
**Builder in vault:** **ABSENT**
**Verification:** verified — dates and figures from primary sources; see Sources for one gap

## The Problem That Came First

Serving a large language model is not limited by arithmetic. It is limited by memory, and specifically by memory that grows while you use it.

A transformer generating text keeps the attention keys and values of every earlier token — the **KV cache**. The vLLM paper's worked example: a 13-billion-parameter model on a 40 GB NVIDIA A100 spends about 65% of memory on weights, which never change, and close to 30% on KV cache, which changes with every request. The launch post put it at up to 1.7 GB for one LLaMA-13B sequence, sized by an output length nobody knows in advance.

Serving systems handled that uncertainty cautiously: reserve a contiguous chunk big enough for the longest possible output. **The authors profiled existing systems and found only 20.4%–38.2% of KV cache memory held actual token state.** The rest was reserved-but-empty space and fragmentation between differently sized chunks.

For anyone renting GPUs by the hour, fewer concurrent requests per card means more cards per unit of demand.

## What Got Built

vLLM, whose core is **PagedAttention**. Instead of one contiguous buffer per request, the KV cache is cut into fixed-size blocks allocated on demand. The launch post's own analogy: "blocks as pages, tokens as bytes, and sequences as processes," with a block table mapping each sequence's logical blocks to non-contiguous physical ones.

Two things follow. Waste drops to the last partly filled block — the post claims "under 4%" against "60% – 80%" in existing systems. And sequences can share physical blocks, so several samples from one prompt store the prompt's cache once, the way processes share pages.

The measured result was throughput: up to 24x Hugging Face Transformers and up to 3.5x Text Generation Inference in the launch post, and 2–4x FasterTransformer and Orca at equal latency in the paper, presented at SOSP in October 2023. Installation was `pip install vllm`.

## Who Built It, And Why Them

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang and Ion Stoica — a group anchored at UC Berkeley, with co-authors listed at Stanford, UC San Diego and as an independent researcher. The launch post states plainly that vLLM "has been developed at UC Berkeley."

**The reason it was them is that they were running an inference service with an academic budget.** The post says vLLM was deployed behind LMSYS's Chatbot Arena and Vicuna demo, where from mid-April 2023 it served an average of 30K requests a day with a peak of 60K, and that it let LMSYS "cut the number of GPUs used for serving the above traffic by 50%." A free public demo could not price its waste in.

The second reason is disciplinary. The fix is an operating-systems idea — paging, from decades of virtual-memory design — applied to a GPU tensor. It came from a systems group whose venue was SOSP, not a machine-learning conference.

## What It Cost

**Indirection.** A contiguous buffer can be read by a standard attention kernel; a paged one needs a custom kernel that follows the block table. The paper concedes 20–26% higher attention-kernel latency than FasterTransformer's; the throughput gains come from batching more requests, not from faster attention per request.

And **higher utilisation makes load harder to reason about.** Packing more sequences into the same memory means admission, preemption and eviction decisions that a one-chunk-per-request design never had to make.

## What You Still Touch

A provider's price per million tokens is largely a statement about how many sequences it can pack onto one accelerator. vLLM made that packing a free, open default — which turned serving efficiency from a moat into table stakes and moved competition onto capacity planning and isolation.

- [[problems/ai-inference-providers/high-impact|🔴 Capacity Economics Against Bursty Demand]] — where the margin went once memory stopped being the bottleneck
- [[problems/ai-inference-providers/low-impact-2|🟡 Multi-Tenant Isolation on Shared Accelerators]] — the cost of packing strangers' sequences onto one card
- [[problems/ai-inference-providers/worker-life-2|🟢 Performance Engineer Chasing Regressions]]
- [[niches/ai-inference-providers/model-serving-platforms/profile|Model Serving Platforms]]
- [[niches/ai-inference-providers/capacity-and-utilisation/profile|Capacity & Utilisation]]

**Sources:** Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention," arXiv:2309.06180 (submitted 12 September 2023; SOSP '23, Koblenz, 23–26 October 2023) — author affiliations, the 65%/30% memory split and the 20.4%–38.2% utilisation figure and the 20–26% kernel-latency overhead read from the PDF; vLLM launch post, vllm.ai/blog/2023-06-20-vllm (20 June 2023), for the paging analogy, the 60–80% / under 4% waste figures, the throughput multiples, the LMSYS deployment and "developed at UC Berkeley"; GitHub API for `vllm-project/vllm` (repository created 9 February 2023). WebSearch was unavailable this session (budget exhausted). ⚠️ **Not established:** who funded the LMSYS serving GPUs, and whether any earlier serving system paged its KV cache — not searched, so "first" is not claimed. The builder is keyed to the university because the post names it; no firm existed at release.
