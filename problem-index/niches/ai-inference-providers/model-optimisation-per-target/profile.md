# Model Optimisation Per Target

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to serve a new architecture at near-peak hardware efficiency on the day it is released rather than six weeks later — and whoever does that takes the account, because the window between a model's release and its commoditisation is where the margin is.

## Profile
**Market Size:** ~$420M US in engineering cost and lost first-mover margin
**Share of Parent Industry:** ~7% of category revenue equivalent
**Digital Adoption:** Very Low — hand work redone every release
**Target Buyer:** Performance engineering organisations at the providers
**Automation Potential:** High — search over a structured space with a measurable objective

## What Makes This a Distinct Niche
Serving engines, quantisation methods and kernel libraries are mature and open. What is not automated is the work of making a specific new architecture run near peak on a specific accelerator: fusing the right operations, choosing tile shapes and memory layouts, selecting attention implementations, tuning batch and cache parameters. It takes a small team weeks per architecture per hardware target, it is redone with the next release, and during those weeks a provider is either serving inefficiently or not serving the model at all — which is precisely the window when a new model commands a premium. The economics of the whole industry turn on how fast this work happens, and it is done by hand.

## Current Tools & Gaps
Open serving engines with implementations for common architectures, compiler stacks with autotuning, vendor kernel libraries, and hand-written kernels. The gaps: autotuning covers a fraction of the space and is rarely used at the level that matters; optimisations are not transferable across architectures despite most new ones being variations; no shared record of what worked for which architecture-hardware pair; and no estimate of how far a current implementation sits from achievable peak, so nobody knows when to stop.

## Problems
- [[niches/ai-inference-providers/model-optimisation-per-target/build|🔨 Build: Weeks of Hand Work, Redone Every Release]]
- [[niches/ai-inference-providers/model-optimisation-per-target/buy|🛒 Buy: Compiler Autotuning and Search]]
- [[niches/ai-inference-providers/model-optimisation-per-target/fix|🔧 Fix: Nobody Knows How Far From Peak They Are]]
