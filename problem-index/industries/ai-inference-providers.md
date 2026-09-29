# AI Inference Providers

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$6B US model inference and GPU cloud services, growing fast on thin and contested margins
**Tech Maturity:** World-class kernel engineering on top of an unsolved economics problem — Together, Fireworks, Baseten, Modal, Replicate, Anyscale, Groq and Fal have made serving open models fast and simple. The business underneath is renting depreciating hardware against demand that arrives in bursts, and nobody has made that work reliably.
**Workforce:** Performance and kernel engineers, capacity planners, site reliability engineers, solutions architects, hardware procurement specialists, support engineers

## Key Pain Themes
This is a capital-intensive business with a utilisation problem that no amount of engineering fixes. Accelerators are bought or leased on long commitments and depreciate quickly; demand arrives in spikes driven by a customer's product launch, a viral moment, or a batch job someone scheduled without warning. Overprovision and the margin disappears into idle hardware; underprovision and the latency guarantee fails, which is the one thing customers actually buy. Below that sit two engineering burdens that never end: model optimisation, where every new architecture must be re-optimised for every hardware target and the work is redone with each release; and multi-tenant isolation, where sharing accelerators across customers is the only route to acceptable utilisation and the noisy neighbour problem is severe on hardware not designed for it. Site reliability engineers absorb the capacity events, and performance engineers chase regressions across a stack that changes underneath them constantly.

## Current Tech Landscape
vLLM and SGLang have become the dominant open serving engines, with continuous batching and paged attention as standard techniques. TensorRT-LLM serves NVIDIA-optimised deployments. Quantisation to eight and four bits is routine with quality trade-offs that are inconsistently measured. Speculative decoding and prefix caching are widely deployed. Hardware is overwhelmingly NVIDIA with meaningful alternatives from AMD, and specialised inference silicon from Groq and Cerebras occupying a latency niche. Capacity is procured through a mix of long-term commitments, reserved cloud instances and spot markets, and the spread between them is where the margin lives.

## Problems
- [[problems/ai-inference-providers/high-impact|🔴 High Impact: Capacity Economics Against Bursty Demand]]
- [[problems/ai-inference-providers/low-impact-1|🟡 Low Impact: Per-Architecture Optimisation Work]]
- [[problems/ai-inference-providers/low-impact-2|🟡 Low Impact: Multi-Tenant Isolation on Shared Accelerators]]
- [[problems/ai-inference-providers/worker-life-1|🟢 Worker Life: SRE During a Capacity Event]]
- [[problems/ai-inference-providers/worker-life-2|🟢 Worker Life: Performance Engineer Chasing Regressions]]
- [[problems/ai-inference-providers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ai-inference-providers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These providers hold the most detailed record anywhere of what inference actually costs: request-level latency, token counts, batch composition, memory pressure and hardware utilisation across millions of requests, thousands of models and every accelerator generation. That corpus answers questions the whole industry guesses at — what a given quantisation actually costs in quality, which architectures serve efficiently at which batch sizes, how much of the fleet is genuinely necessary. It is used to generate invoices.
