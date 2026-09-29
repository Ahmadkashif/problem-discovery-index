# Edge Compute Placement Economics

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every provider now offers edge compute and none can tell a customer whether moving a given piece of logic to the edge would actually improve anything or merely relocate the cost.
**Tags:** #gradient-boosting #time-series-forecasting #causal-inference #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
Edge compute lets application logic run in the provider's network close to users. The pitch is latency: do the work near the user instead of at a distant origin.

Whether it helps depends entirely on what the work is. Logic that needs no origin data — a redirect, a header rewrite, a personalisation decision from a cookie, an A/B assignment — genuinely improves. Logic that must reach back to a database in one region has added a network hop and made things worse. Logic that fans out to several origin services at the edge may be far worse, since each call now traverses the long path.

Customers decide by intuition and by whatever the provider's marketing suggested. There is rarely a measurement afterwards, so a migration that made latency worse frequently stays, and one that would have helped is never attempted.

The cost side is equally opaque. Edge compute is billed on requests and execution time, origin compute on instances or invocations, and the two are not comparable without careful modelling. Customers routinely discover the economics after the invoice.

## What Already Exists
Edge runtimes are available from Cloudflare, Fastly, Akamai, AWS and Vercel with differing programming models and constraints. Observability for edge functions exists at a basic level. Real user monitoring measures actual client latency. Origin performance monitoring is standard. Some providers offer regional data stores at the edge to address the data locality problem.

## The Customisation Gap
Placement analysis is entirely absent. Given a piece of logic, its data dependencies and the geographic distribution of the traffic that invokes it, whether the edge helps is computable — and no provider computes it, so the decision is made from a blog post.

Data dependency detection is the crux. Logic that touches origin data behaves completely differently from logic that does not, and identifying which is which from the code and from observed call patterns is what makes placement advice possible.

Counterfactual latency estimation is what would make the decision measurable in advance: given this traffic distribution and these dependencies, the expected real user latency at the edge versus at the origin, with an interval.

Cost comparison across the two billing models, expressed per request at realistic volumes, is a straightforward calculation that customers consistently get wrong.

And after-the-fact measurement, since a migration to the edge is a change that should be evaluated on real user latency and origin load — and providers currently offer the deployment without the evaluation.

## Impact If Solved
Edge compute is a genuinely new capability sold on a latency claim that is true for some workloads and false for others, decided by intuition and rarely measured. Placement analysis grounded in data dependencies and traffic geography would tell customers what to move, which is the difference between a platform and a runtime.
