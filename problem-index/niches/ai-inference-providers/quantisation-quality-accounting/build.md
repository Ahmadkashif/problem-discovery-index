# A Quality Cost Asserted Rather Than Measured

**Niche:** [[niches/ai-inference-providers/quantisation-quality-accounting/profile|Quantisation Quality Accounting]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Quantisation is the largest cost lever in the business and its quality cost is asserted as negligible on general benchmarks while landing unevenly on specific capabilities nobody measures.
**Tags:** #numerical-methods #evaluation-metrics #hypothesis-testing #confidence-intervals #entropy-cross-entropy-kl-divergence #descriptive-statistics #cross-validation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to state what a quantisation actually costs in quality on the customer's own task — and whoever does that takes the account, because the trade is being made on everyone's behalf and measured by almost nobody.

## The Problem
A customer builds a structured extraction pipeline against a model endpoint. It works. Two months later the provider moves the deployment to a four-bit quantisation to improve throughput, which is invisible on general benchmarks and costs a fraction of a point of perplexity. The customer's extraction accuracy falls several points, because quantisation error concentrates in exactly the low-probability token decisions that structured output depends on. The provider's quality dashboard shows nothing. The customer spends three weeks investigating their prompts and their parsing, because they do not know anything changed.

## Why Nobody Has Built This
Measuring quality per task requires a task, which the provider does not have and has not asked for. General benchmark deltas are small and easy to report as negligible, which is true on average and misleading in the specific. The cost saving is immediate and the quality cost is diffuse and deniable. And disclosing a quantisation invites a customer to ask for the unquantised version at a higher price, which is a conversation providers have chosen not to open.

## What to Build
Measure the trade and let the customer choose a point on it. Build per-capability quality measurement comparing quantised against full-precision output across the axes where degradation concentrates — structured and constrained output, long-context retention, arithmetic and code, rare vocabulary, and multi-step reasoning — because the aggregate benchmark is the wrong instrument and these axes are where the damage actually lands. Report the cost-quality curve per model and per scheme, so the customer chooses rather than inherits, which is the product change and is available to any provider willing to make it. Let customers supply their own evaluation set and report the delta on it, which is the only fully convincing answer and is cheap to run. Offer explicit precision tiers at different prices, since many customers would happily take a cheaper quantised tier knowingly and some cannot, and serving both the same way serves neither. Compare quantisation schemes on the customer's task rather than in general, because they differ in where they degrade and the best choice is task-dependent. Detect degradation in production by shadowing a sample against full precision, which is a small continuous cost and the only ongoing assurance available. Report distributional divergence alongside task metrics, since it catches degradation on axes the task set does not cover. And publish the methodology, because a quality claim about your own cost-saving measure needs to be checkable.

## Target Customer
Every customer of a quantised deployment, the providers making the trade, and the model publishers whose reputation absorbs a degradation they did not cause.

## Impact If Built
Aggregate benchmarks are the wrong instrument for a degradation that concentrates in structured output, long context and rare vocabulary. A published cost-quality curve with explicit precision tiers turns an inherited trade into a customer choice.
