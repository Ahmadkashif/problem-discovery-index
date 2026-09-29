# Weeks of Hand Work, Redone Every Release

**Niche:** [[niches/ai-inference-providers/model-optimisation-per-target/profile|Model Optimisation Per Target]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Serving engines, quantisation and kernel libraries are mature and open, and every new model architecture still means weeks of hand optimisation per hardware target that is redone with the next release.
**Tags:** #bayesian-optimization #convex-optimization #transfer-learning #gaussian-processes #evaluation-metrics #numerical-methods #optimization-fundamentals #automation
**Contested on:** Every serious competitor in this niche is fighting to serve a new architecture at near-peak hardware efficiency on the day it is released rather than six weeks later — and whoever does that takes the account, because the window between a model's release and its commoditisation is where the margin is.

## The Problem
A significant open model is released on a Tuesday. Demand is immediate and the price it commands is highest in the first fortnight. A provider's performance team spends three weeks getting it from a working implementation at half of achievable throughput to a tuned one at eighty percent — fusing operations, choosing layouts, selecting an attention implementation, tuning cache and batch parameters per accelerator generation. Six weeks later a variant of the same architecture is released and most of the work is repeated, because none of it was expressed in a form that transfers.

## Why Nobody Has Built This
The work sits between compiler engineering and hardware expertise, which is a rare combination held by people who are fully occupied doing it. Autotuning frameworks cover the kernel level but not the architecture-level decisions where much of the gain is. The knowledge is genuinely tacit and hardware-generation-specific, which makes people doubt it generalises. And each provider does it privately, so the field repeats the same work several times over in parallel.

## What to Build
Turn the hand work into a search with memory. Define the optimisation space explicitly — fusion choices, layouts, attention implementations, tile shapes, batch and cache parameters — since making it a structured space is what converts craft into something searchable, and it is currently implicit in people's heads. Search it with the methods built for expensive black-box objectives, using multi-fidelity evaluation so that most candidates are rejected cheaply on short benchmarks. Transfer aggressively across architectures, because most new models are variations and the configuration that worked for the nearest previous architecture is a far better starting point than a default — this transfer is where the weeks actually go and it is the highest-value piece. Maintain a durable record of configuration and achieved efficiency per architecture-hardware pair, so the third variant starts from the first two rather than from scratch. Estimate achievable peak from hardware characteristics, which the fix note develops and which tells the team when to stop. Automate across hardware targets in parallel, since the same architecture must be tuned for each generation and doing them independently is the current waste. Leave the genuinely novel cases to the engineers, which is the minority and is where their expertise is worth most. And contribute the transferable parts upstream to the open engines, since the whole industry repeating this work privately serves nobody, including the provider.

## Target Customer
Performance engineering organisations at inference providers, the open serving engine projects, and the accelerator vendors whose hardware is under-utilised during these windows.

## Impact If Built
The first fortnight of a model's life is where the margin is and it is spent hand-tuning. Transfer from the nearest previous architecture is where the weeks actually go, and a durable configuration record turns the third variant into a lookup rather than a project.
