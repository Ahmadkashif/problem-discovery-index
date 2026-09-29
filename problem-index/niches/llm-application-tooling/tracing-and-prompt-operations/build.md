# A Trace Viewer for a Question Nobody Asks One at a Time

**Niche:** [[niches/llm-application-tooling/tracing-and-prompt-operations/profile|Tracing & Prompt Operations]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These products let an operator read one trace beautifully, and the questions they actually have — what changed, which inputs get worse answers, is this version better — are all aggregate questions.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #change-point-detection #confidence-intervals #hypothesis-testing #large-language-models #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to let an operator explain a production failure and change a prompt without breaking anything — and whoever does that takes the account, because the buyer already has the application running and those are the only two things they need.

## The Problem
Something got worse this week. The operator opens the tracing product and sees a list of traces, a filter bar and a detail view that renders one conversation elegantly. To answer their question they would need to know which categories of input degraded, whether the degradation coincides with a prompt version, a model change or a traffic shift, and what the bad responses have in common. The product offers none of those; it offers a search. They export a sample to a notebook, which is what the product was bought to avoid.

## Why Nobody Has Built This
Trace viewing was inherited from distributed tracing, where reading one trace really is the primary workflow. Aggregate quality analysis requires grading, which requires a judge and a rubric the product does not have. Clustering free-text inputs and outputs is a modest amount of work that looks like a research feature. And the single-trace view demos well, which is where product effort goes in a fast-moving market.

## What to Build
Answer the aggregate questions directly. Cluster production inputs and report quality, cost and latency per cluster, so degradation is attributable to a kind of request rather than to a vague sense — this is the core view the category lacks and it is the one operators construct by hand. Join every trace to the prompt version, model version and configuration that produced it, so a change point in a metric can be attributed to a specific change rather than correlated by eye. Provide a two-version comparison view on the same input clusters, which is the question behind every prompt deployment. Grade a continuous sample automatically with a calibrated judge, so quality is a first-class dimension alongside latency and cost rather than something a team measures occasionally. Detect and alert on quality change points, since that is the failure this category has and no generic observability product can see. Surface exemplars from each cluster, so the aggregate view leads directly to the traces worth reading. Summarise what the failing responses have in common in plain language, which is the step operators spend the longest on. And make the whole thing answer the question from the on-call engineer's starting point — something got worse — rather than from a trace identifier they do not have.

## Target Customer
Teams operating LLM applications, their on-call engineers, and the observability vendors whose generic products cannot express quality.

## Impact If Built
Every question an operator actually has is aggregate and the product offers a search. Per-cluster quality with traces joined to prompt and model versions turns a vague degradation into an attributable change, which is what these teams currently rebuild in notebooks.
