# Quantisation Quality Accounting

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to state what a quantisation actually costs in quality on the customer's own task — and whoever does that takes the account, because the trade is being made on everyone's behalf and measured by almost nobody.

## Profile
**Market Size:** ~$340M US
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — routine practice, inconsistent measurement
**Target Buyer:** Anyone buying a quantised deployment, which is nearly everyone
**Automation Potential:** Very High — the measurement is a mechanical comparison

## What Makes This a Distinct Niche
Quantising weights and activations to eight or four bits is routine, because it is the largest single lever on cost and throughput. Its quality cost is real, task-dependent, and inconsistently measured: a quantisation that is invisible on general benchmarks can degrade structured output, long-context reasoning, or a specific domain's vocabulary noticeably. Providers frequently serve a quantised model under the same name as the original, sometimes without saying which scheme, and the customer has no way to know what they are getting or what it cost them. The measurement is a mechanical comparison the provider is best placed to run, and the commercial incentive points against running it.

## Current Tools & Gaps
Quantisation toolkits with several schemes, published perplexity comparisons, and occasional benchmark spot checks. The gaps: no per-task quality measurement, so the number that matters is never produced; no disclosure of which scheme is in use; degradation concentrated in specific capabilities is invisible to aggregate benchmarks; and no option for the customer to choose a point on the cost-quality curve.

## Problems
- [[niches/ai-inference-providers/quantisation-quality-accounting/build|🔨 Build: A Quality Cost Asserted Rather Than Measured]]
- [[niches/ai-inference-providers/quantisation-quality-accounting/buy|🛒 Buy: Numerical Analysis and Approximation Error Practice]]
- [[niches/ai-inference-providers/quantisation-quality-accounting/fix|🔧 Fix: Served Under the Same Name]]
