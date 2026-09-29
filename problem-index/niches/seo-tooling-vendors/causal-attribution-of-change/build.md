# A Decade of Natural Experiments Drawing a Line Chart

**Niche:** [[niches/seo-tooling-vendors/causal-attribution-of-change/profile|Causal Attribution of Visibility Change]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendors hold what changed on millions of sites, when, and what happened afterwards, across every algorithm update of the last decade — and use it to draw a line chart.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #evaluation-metrics #monte-carlo-methods #time-series-forecasting #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to answer whether what a site did worked or whether the algorithm moved — and whoever does it owns the only dataset capable of settling the customer's recurring question.

## The Problem
A customer restructured their category pages in March. Visibility rose in April. Did the restructure work? There was also an algorithm update in late March, a competitor who stopped publishing, and a seasonal pattern. The vendor's answer is a chart with a vertical line marking the update. Meanwhile the vendor's database contains thousands of other sites that did the same restructure and thousands that did not, before and after the same update — which is a natural experiment with a control group already assembled, sitting unused while the customer is shown a correlation.

## Why Nobody Has Built This
The corpus was assembled to power rank tracking and its research value was never the point — the asset exists as a by-product and nobody has been asked to exploit it. Causal inference requires statistical capability the product teams were not hired for. Publishing what actually works risks contradicting the vendor's own advice and the profession's received wisdom. And customers ask for charts, so charts are what ships.

## What to Build
Use the corpus as the experiment it is. Construct control groups from comparable sites that did not make a given change, which is the core method and is available immediately because the corpus already contains both arms. Estimate the effect of a specific change with a stated interval, rather than reporting that visibility moved, since the customer's question is whether their action worked and only a comparison answers it. Separate algorithm effects from site effects by observing how sites that changed nothing behaved through the same update, which is the cleanest natural control available anywhere in this discipline. Estimate per-site counterfactuals — what would have happened without the change — which is the form of the answer a customer needs to defend a decision. Handle the obvious confounding, since sites that make a change are not random and naive comparison will attribute selection to treatment. Accumulate findings into a body of evidence about what works, which is the compounding asset and the thing the profession has never had. Report effects by site type and sector, because an effect that holds for large publishers and not for small commerce sites is two findings. Detect update effects as they happen from the cross-site panel, which is faster than any individual customer can and is genuinely valuable in the first days. Publish methodology and let it be criticised, since credibility is the product here. And state uncertainty plainly, because a causal claim presented with false confidence in a discipline built on folklore would be a serious setback.

## Target Customer
SEO tooling vendors sitting on unexploited corpora, enterprise SEO teams needing to justify investment, and the agencies whose recommendations currently rest on assertion.

## Impact If Built
The corpus contains both arms of thousands of natural experiments and was assembled as a by-product nobody was asked to exploit. Sites that changed nothing through an update are the cleanest control group this discipline will ever have, and using them converts a correlation into an answer.
