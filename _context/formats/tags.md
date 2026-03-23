# Canonical Tag Rules

**When you tag a file, follow these rules exactly. A wrong tag is broken output — treat it like a broken link.**

The single source of truth is `problem-index/metadata/tags.md`. This file summarizes what you need to apply tags correctly.

---

## How to Tag

1. **Use ONLY canonical tags** from `problem-index/metadata/tags.md`. If a concept isn't listed, it does not get a tag.
2. **Mix tiers** — combine algorithm/model tags with task-type tags and context tags.
3. **Be specific** — write `#gradient-boosting` + `#time-series-forecasting`, NOT just `#gradient-boosting`.
4. **Check the deprecated list below BEFORE using any tag.** If you use a deprecated tag, your output is wrong.
5. **Apply 2–5 tags** on a `**Tags:**` line immediately after `**One-liner:**`.

---

## Deprecated Tags — DO NOT USE

These tags exist in older vault files. You MUST NOT use them in new content. Use the replacement instead.

| Deprecated | Use Instead |
|---|---|
| `#cnn` | `#cnns` |
| `#lstm` | `#lstms-and-grus` |
| `#llm` | `#large-language-models` |
| `#svm` | `#support-vector-machines` |
| `#rnn` | `#rnns` |
| `#autoencoder` | `#autoencoders` |
| `#gan` | `#gans` |
| `#bayesian-network` | `#bayesian-inference` |
| `#gaussian-process` | `#gaussian-processes` |
| `#isolation-forest` | Use appropriate technique + `#evaluation-metrics` |
| `#binary-classification` | Use relevant classifier + `#evaluation-metrics` |
| `#multiclass-classification` | Use relevant classifier + `#evaluation-metrics` |
| `#regression` | Use `#linear-regression` or `#gradient-boosting` |
| `#computer-vision` | Use `#cnns` + task-specific tags |
| `#nlp` | Use `#bert` or `#transformers` or `#large-language-models` |
| `#tabular-ml` | Use specific algorithm tags |
| `#anomaly-detection` | Use `#dbscan` or `#gaussian-mixture-models` or relevant technique |
| `#reinforcement-learning` | Use specific RL tags |
| `#random-forest` | `#random-forests` |
| `#transformer` | `#transformers` |
| `#diffusion-model` | `#diffusion-models` |
| `#k-means` | `#k-means-clustering` |

---

## Context Tags — Always Valid

Apply these alongside algorithm/task tags:

| Tag | Use When |
|---|---|
| `#tacit-knowledge-ml` | **Top priority.** Expert has internalized pattern recognition through experience — ML can capture and scale it |
| `#quick-win` | Buildable in <4 weeks with available data |
| `#automation` | Replaces a fully manual, repetitive step |
| `#data-integration` | Core challenge is joining/reconciling disparate data sources |
| `#workflow-orchestration` | Core challenge is sequencing and routing work between systems |
| `#compliance` | Solution directly addresses a regulatory or legal constraint |
| `#worker-facing` | Primary beneficiary is the individual worker, not the business |
| `#revenue-impact` | Solution directly unlocks or protects revenue |
| `#ai-agent` | Opportunity for an autonomous AI agent (multi-step, tool use) |
| `#ai-platform` | Opportunity to build a vertical AI platform or workflow layer |

---

## Authoritative Source

Always defer to `problem-index/metadata/tags.md` for the complete list. This file is a quick-reference summary.
