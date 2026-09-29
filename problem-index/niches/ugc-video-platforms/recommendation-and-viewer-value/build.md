# Optimising for Glad Rather Than Long

**Niche:** [[niches/ugc-video-platforms/recommendation-and-viewer-value/profile|Recommendation & Viewer Value]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most capable ranking systems ever built optimise a proxy nobody has validated against the outcome it stands in for.
**Tags:** #markov-decision-processes #causal-inference #evaluation-metrics #confidence-intervals #policy-gradient-methods #hypothesis-testing #survival-analysis #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to optimise for a viewer who is glad they watched rather than one who watched for longer — and whoever measures that instead of assuming it holds the attention everyone else is burning.

## The Problem
Time spent is measurable, immediate and abundant, so it became the objective. Whether the viewer was glad afterwards — whether they got what they wanted, would choose the session again, or feel the platform is worth returning to next year — is none of those things and is never measured. The two diverge in known ways, the divergence compounds over time into retention and reputation, and the systems optimising the proxy are powerful enough that the divergence is a large effect rather than a rounding error.

## Why Nobody Has Built This
Engagement is the metric the business and the advertising model are built on, so an alternative objective would have to beat it on the metric it is replacing — a proxy embedded in revenue recognition cannot be displaced by an argument, only by a measurement. Satisfaction is harder to measure and slower to observe. Long-horizon experiments are expensive. And the short-horizon metric always wins a short-horizon comparison.

## What to Build
Measure satisfaction and optimise the long horizon. Measure whether viewers were glad — through direct signals, survey at scale, and behavioural proxies like deliberate return, sharing and library behaviour — which is the core and is what the objective is currently standing in for. Model long-horizon retention rather than session engagement, since the divergence between the two is where the harm and the business risk both sit. Run long-horizon experiments, because a short experiment always favours the short-horizon objective and that is why the question stays open. Detect the low-value session — long watch, no satisfaction, no return — which is directly observable and is the clearest instance of the proxy failing. Model the recommender's effect on creator exposure as an allocation, connecting to the enforcement and monetisation questions. Report exposure concentration, since the recommender determines who earns and nobody publishes its distribution. Balance the objective explicitly rather than implicitly, as multi-objective ranking is standard and the objectives chosen are a policy decision. Publish the methodology, because the credibility of any claim here is the point. Handle the regulatory attention deliberately, since this is exactly where it is arriving. And measure the business effect of the change, as the case must be made on retention rather than on virtue.

## Target Customer
Product and data leadership, viewers, creators whose exposure it allocates, regulators examining recommender effects, and recommendation platform vendors.

## Impact If Built
A proxy embedded in revenue recognition cannot be displaced by an argument, only by a measurement. Measuring satisfaction and running long-horizon experiments is the only way the question gets settled, and the divergence is large enough to matter commercially.
