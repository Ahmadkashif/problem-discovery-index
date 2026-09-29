# Numerical Analysis and Approximation Error Practice

**Niche:** [[niches/ai-inference-providers/quantisation-quality-accounting/profile|Quantisation Quality Accounting]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Numerical analysis has two centuries of practice on error propagation, conditioning and mixed precision, and quantisation is discussed as though it were a compression setting.
**Tags:** #numerical-methods #matrix-decompositions #evaluation-metrics #hypothesis-testing #entropy-cross-entropy-kl-divergence #confidence-intervals #probability-distributions #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to state what a quantisation actually costs in quality on the customer's own task — and whoever does that takes the account, because the trade is being made on everyone's behalf and measured by almost nobody.

## The Problem
Understanding how a reduction in numerical precision propagates through a computation, which operations are ill-conditioned, where error accumulates and how to allocate precision where it matters is the subject matter of numerical analysis, with well-developed theory and a mature practice in scientific computing where mixed precision has been deployed carefully for years. Quantisation in serving is largely treated as a configuration choice with an empirical benchmark attached.

## What Already Exists
Error analysis and condition number theory for numerical computations; mixed-precision practice from scientific computing with established guidance on where precision matters; stochastic rounding and error compensation techniques; interval arithmetic for bounding propagated error; and the numerical stability literature for iterative and accumulative computations.

## The Customization Gap
The adaptation is to a computation whose output is a distribution over tokens sampled autoregressively. It requires: (1) error analysis of the autoregressive loop, where a small per-step perturbation compounds across a long generation in a way single-pass error analysis does not capture — this compounding is the mechanism behind long-context and multi-step degradation and is essentially unanalysed; (2) sensitivity analysis per layer and per operation to allocate precision non-uniformly, which mixed-precision practice does routinely and quantisation schemes do crudely; (3) conditioning analysis to identify which decisions are fragile, since the tokens most affected are those where the top candidates are close — which explains why structured output degrades first and suggests a targeted remedy; (4) error bounds rather than empirical averages, since a bound on the output distribution's divergence is a much stronger statement than a benchmark score; and (5) error compensation techniques from the numerical world, which are largely unexplored in this setting.

## Target Customer
Inference providers, quantisation toolkit authors, model publishers, and the numerical analysis community for whom this is a large and unclaimed application.

## Impact If Solved
Two centuries of error analysis exists and quantisation is treated as a compression setting. Analysing how per-step error compounds through the autoregressive loop is what would explain the long-context and structured-output degradation the field currently observes without understanding.
