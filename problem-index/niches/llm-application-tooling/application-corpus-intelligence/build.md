# Exceptional Recording, No Inference

**Niche:** [[niches/llm-application-tooling/application-corpus-intelligence/profile|Application Corpus Intelligence]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category holds every prompt version, input, output, model and configuration change across thousands of applications, and has built exceptional recording infrastructure and stopped short of inference.
**Tags:** #causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #transfer-learning #descriptive-statistics #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn the complete record of how these applications behave into empirical answers about what actually works — and whoever does that stops selling a trace viewer and starts defining the practice.

## The Problem
Practitioners decide how to structure a prompt, whether to put instructions before or after context, whether examples help for their task, whether a model upgrade is worth taking, and whether a two-point evaluation difference is real. Every one of those is answered by a blog post, a conference talk or a colleague's intuition. The vendors those practitioners log into hold thousands of applications' worth of prompt versions with measured outcomes, which answers all five empirically, and offer them a filtered list of traces. It is the same failure the machine learning operations category made a decade ago with training runs, repeated by people who watched it happen.

## Why Nobody Has Built This
Traces are shaped for reading one at a time rather than for analysis across millions. Cross-customer work is contractually awkward and nobody has asked the narrow version of the question. Product organisations in a fast-moving market build features. And publishing findings means taking positions that could be wrong in public, which is uncomfortable — and is also exactly what would make a vendor the reference rather than a tool.

## What to Build
Turn the corpus into the field's evidence base. Start with the model upgrade question, since it is concrete, universally faced and immediately valuable: what a given model change actually cost or gained in quality and cost on real traffic, measured across many applications — nobody can answer it today and every customer wants to. Analyse prompt structure against outcomes across deployments, which produces the empirical account of prompt patterns the field has been substituting folklore for. Quantify measurement noise, so the field learns how large an evaluation difference has to be to mean anything — a finding that would change how thousands of teams work and costs nothing but the analysis. Build a cohort benchmark, so a customer can see how their application compares to similar ones on quality, cost and latency, which the fix note develops. Recommend configuration from a new application's characteristics, warm-starting from what worked in similar deployments. Establish a narrow, inspectable aggregation basis with customers, since the objection is to open-ended use. Offer per-customer analysis unconditionally, which needs no permission and demonstrates the value. And publish, because the vendor that supplies the field's empirical answers becomes the reference and is no longer competing on whose trace viewer is nicer.

## Target Customer
Tooling vendors, their customers, and the practitioner community that currently has no empirical basis for its most common decisions.

## Impact If Built
The same recording-without-inference failure happened a decade earlier with training runs, by people who watched it. Quantifying measurement noise alone would change how thousands of teams interpret their evaluations, and it costs nothing but the analysis.
