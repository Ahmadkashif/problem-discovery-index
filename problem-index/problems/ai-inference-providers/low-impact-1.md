# Per-Architecture Optimisation Work

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Serving engines, quantisation and kernel libraries are mature and open, and every new model architecture still means weeks of hand optimisation per hardware target that is redone with the next release.
**Tags:** #optimization-fundamentals #bayesian-optimization #gradient-boosting #evaluation-metrics #hypothesis-testing #confidence-intervals #transfer-learning

## The Problem
A new open model is released and customers want it served, fast, that week. Making it fast means work: selecting and tuning a kernel implementation for the attention variant it uses, choosing a quantisation scheme and validating that quality survives it, setting tensor and pipeline parallelism for the target hardware, tuning batch size and sequence length policies, and configuring the serving engine's memory management.

Every step is hardware-specific. The optimal configuration on one accelerator generation is wrong on the next and wrong again on a different vendor's silicon. So the work multiplies across the fleet.

Then the model is superseded, a new architecture appears with a slightly different attention mechanism or a mixture-of-experts routing scheme, and it begins again. Performance engineering teams at these providers are permanently behind, and the differentiation between providers is largely how quickly they get through this.

Quantisation quality is the least rigorous part. Providers serve quantised weights because the economics demand it, validate quality with a handful of benchmarks, and the customer's actual workload is not among them.

## What Already Exists
vLLM and SGLang provide production-grade serving with continuous batching and paged attention, and are open source with active communities. TensorRT-LLM offers deep NVIDIA optimisation. Quantisation toolkits are mature. Triton and CUTLASS make custom kernel development tractable. Compilers including torch.compile and XLA automate some of the work. Model architectures are increasingly variations on a small number of patterns.

## The Customisation Gap
Configuration search is manual. Parallelism strategy, batch policy, memory allocation and quantisation scheme form a large search space with strong interactions, and it is explored by engineers running benchmarks and applying intuition. It is a textbook case for automated search — the objective is measurable, the evaluation is cheap relative to the search, and the space is structured — and providers do it by hand.

Transfer across models is the second gap. Architectures share components, and the optimal configuration for a new model of a familiar family is close to the configuration for its predecessor. Nobody has built the mapping, so each model starts from defaults.

Quantisation quality assessment is the most consequential absence. What a given quantisation costs on a given model for a given workload is directly measurable, is rarely measured beyond a benchmark score, and is exactly what determines whether the customer is getting what they think they are. Task-conditioned quality measurement would let providers offer an honest quality-price choice rather than an implicit one.

## Impact If Solved
Time to serve a new architecture is a primary differentiator in this market and the work is redone per model per hardware target by scarce engineers. Automating configuration search and transferring across architecture families converts weeks of manual tuning into hours, and honest quantisation quality measurement turns an implicit trade-off into a product decision the customer can make.
