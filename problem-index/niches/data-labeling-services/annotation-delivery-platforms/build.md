# Excellent Tooling for Last Decade's Tasks

**Niche:** [[niches/data-labeling-services/annotation-delivery-platforms/profile|Annotation Delivery Platforms]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The annotation tooling is genuinely excellent for the modalities that mattered a decade ago and thin for reasoning traces, tool use and long-form comparison, which is where the demand has moved.
**Tags:** #large-language-models #transformers #bert #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to be how annotation actually gets done — and that contest is a tooling problem for teams doing it themselves and a workforce problem for those buying a result, which is why this niche is not terminal and is decomposed below.

## The Problem
A customer needs annotators to evaluate a model's multi-step reasoning where the model called three tools, revised its approach and produced a final answer. The annotator must see the trace, evaluate each step's validity, judge whether the tool use was appropriate, and assess the final answer — with the ability to mark a step as wrong while the conclusion is right, which happens constantly. No existing interface supports this, so a solutions engineer builds one over three weeks, for this customer, and a different one for the next customer whose task is nearly the same.

## Why Nobody Has Built This
The tooling matured around modalities with stable task shapes: a bounding box is a bounding box and the interface converged. The new work has no stable shape — it is judgement about structured processes, and each customer's structure differs — which defeats the per-modality product design the category is built on. Building a general task-composition capability is a substantially different product from a set of specialised editors, and the vendors' engineering is organised around the latter. And the bespoke-build cost is absorbed as solutions engineering, which is a cost line rather than a product gap.

## What to Build
The shared layer both sub-niches need: annotation as a composable task rather than a fixed interface. A task definition model expressive enough to describe the new work — a sequence of steps to assess, a comparison with structured criteria, a rationale to write, a partial judgement where one part is right and another wrong — from which an interface is generated rather than built, which is the structural change that removes the solutions engineering. Support the judgement shapes the expert tier actually needs, particularly partial and conditional assessments, which current interfaces force into a single verdict and which is where much of the information is lost. Capture the rationale as structured data rather than as a free-text field, since the reasoning is frequently the product at this tier and is currently stored as a note. Instrument the annotator's process — time, revisions, what they looked at — since that is the signal the corpus niche needs and is discarded. Keep the excellent existing modality tooling, since it works, and compose rather than replace. And measure time-to-first-label for a new task type, which is the metric this contest is actually about and which nobody reports.

## Target Customer
Annotation platform vendors, the labs commissioning new task types, and the in-house teams currently waiting for a bespoke interface.

## Impact If Built
The tooling's per-modality design was right for stable task shapes and is wrong for judgement about structured processes, which is where the market moved. Generating interfaces from a task definition removes the solutions engineering that currently precedes every new task type.
