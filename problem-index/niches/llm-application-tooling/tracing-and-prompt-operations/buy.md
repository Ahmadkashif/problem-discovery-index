# Observability Aggregation and Exemplars

**Niche:** [[niches/llm-application-tooling/tracing-and-prompt-operations/profile|Tracing & Prompt Operations]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mature observability platforms solved aggregation, exemplars and change attribution over high-cardinality telemetry, and LLM tracing products rebuilt the trace list.
**Tags:** #descriptive-statistics #change-point-detection #time-series-forecasting #evaluation-metrics #confidence-intervals #data-integration #automation #k-means-clustering
**Contested on:** Every serious competitor in this sub-niche is fighting to let an operator explain a production failure and change a prompt without breaking anything — and whoever does that takes the account, because the buyer already has the application running and those are the only two things they need.

## The Problem
Moving from an aggregate metric to the specific traces behind it, attributing a change to a deployment, and exploring high-cardinality dimensions interactively is what mature observability platforms do well after fifteen years of work. LLM tracing products have the same telemetry shape with an extra dimension — quality — and largely reimplemented a filtered list of traces, leaving the aggregation and attribution machinery on the table.

## What Already Exists
High-cardinality aggregation with interactive exploration; exemplars linking an aggregate metric to representative traces; deployment markers and change attribution; service level objectives with error budgets; anomaly detection on telemetry; and distributed trace storage and sampling strategies.

## The Customization Gap
The adaptation is to telemetry whose most important attribute is a judgement. It requires: (1) quality as a metric dimension, computed by grading a sample continuously, which is the entire difference between this and generic observability and is what justifies a dedicated product at all; (2) semantic clustering of free-text inputs as a grouping dimension, since the natural groupings here are meaning-based and no observability platform groups by meaning; (3) prompt and model versions as deployment markers, so change attribution works on the artefacts that actually change in this domain; (4) sampling that preserves the unusual, because the interesting traces are the rare bad ones and uniform sampling loses them — which is the same lesson telemetry cost management learned; and (5) payload handling for large sensitive content, which the fix note develops and which generic platforms do not have to solve at this scale.

## Target Customer
LLM tracing vendors, observability platforms for whom this is an adjacent domain, and the teams operating these applications.

## Impact If Solved
Fifteen years of aggregation and attribution machinery exists and this category rebuilt the trace list. Quality as a graded metric dimension and semantic clustering as a grouping key are the two additions that make the existing machinery answer this domain's questions.
