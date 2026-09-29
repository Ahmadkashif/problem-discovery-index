# One Model, Chosen Once, for Everything

**Niche:** [[niches/llm-application-tooling/model-routing-and-cost/profile|Model Routing & Cost]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Gateways that route across providers are widely available and the routing rule is almost always the same one: use the model we picked at the start, for everything.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #convex-optimization #confidence-intervals #revenue-impact #hypothesis-testing #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to send each request to the cheapest model that will answer it well enough — and whoever does that takes the account, because the spread across models is an order of magnitude and the current rule is to ignore it.

## The Problem
An application classifies support messages, extracts a few fields, and occasionally answers a genuinely complex policy question. All of it goes to the most capable model, because that is what was chosen during the prototype when nothing else mattered. Nine in ten requests would be answered identically by a model costing a fraction as much and returning in a third of the time. Nobody has measured that, because measuring it requires running both and comparing quality, which requires the evaluation machinery the team does not have. The bill is several times what it needs to be and the latency is worse than it needs to be, permanently.

## Why Nobody Has Built This
Routing on difficulty requires predicting difficulty, and nobody framed it as a prediction problem despite the labels being available in every deployment's history. Comparing models on the customer's own traffic requires an evaluation capability the category has not built, so the two gaps hold each other in place. Gateways sold provider abstraction and fallback, which are easier features. And the cost is tolerable until it is not, at which point the response is to shorten prompts.

## What to Build
Route each request to the cheapest model that will do. Predict per-request difficulty from features available before the call — input length, task type, structural complexity, whether retrieval returned strong matches, historical difficulty of similar inputs — which is a standard classification problem with labels derivable from the deployment's own history, and is the whole build. Measure each candidate model's quality on the customer's own traffic by clusters, which produces the quality floor the routing decision needs and which no team currently has. Route with a quality constraint rather than a cost target, so the team states the floor and the router minimises cost beneath it — this framing is what makes the change safe to adopt. Cascade where it helps: answer with a cheap model, check the result, escalate only when the check fails, which captures much of the saving at a small quality cost and is underused. Re-evaluate automatically when a new model appears, since the frontier moves and a routing decision frozen six months ago is stale. Report the realised saving and the quality delta together, since a saving with an unmeasured quality cost is not a saving. Use the same machinery for latency-sensitive paths, where a faster model within the floor is worth more than a cheaper one. And expose the routing decision in the trace, so a quality investigation can see which model answered.

## Target Customer
Engineering teams running production LLM applications, the finance functions holding the bill, and the gateway vendors whose products currently route only on failure.

## Impact If Built
Difficulty prediction is a standard classification problem with labels sitting in every deployment's own history and nobody has framed it as one. Routing under a stated quality floor rather than to a cost target is what makes the saving safe to take.
