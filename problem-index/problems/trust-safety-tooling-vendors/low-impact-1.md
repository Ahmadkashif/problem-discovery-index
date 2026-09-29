# The Threshold Is Where the Policy Actually Lives

**Industry:** [[trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The product ships a confidence score and the customer picks a number, which is where the trade between missing harm and removing legitimate speech is actually made.
**Tags:** #confidence-intervals #bayesian-inference #evaluation-metrics #gradient-boosting #hypothesis-testing #probability-distributions #compliance #transfer-learning

## The Problem
A classifier outputs a score and the customer sets a threshold above which content is actioned, below which it is reviewed or ignored. That single number determines the balance between content that should have been removed and was not, and content that should have stayed and was removed.

Those two errors are not commensurable and the product treats them as though they are. Missing a credible threat and removing a piece of journalism are both errors; they are not the same kind of thing, their costs fall on different people, and the correct operating point depends on the category, the platform, the audience and the legal context. The tooling supplies one score and one threshold.

Customers set it by trial. A number is chosen, the review queue is too large or too small, the number is adjusted, and it settles where the operational load is tolerable — which means the balance between harms is being determined by staffing capacity rather than by any assessment of the costs.

Category-specific operating points are rare. The threshold appropriate for child safety content, where a miss is catastrophic and review capacity should absorb false positives, is entirely different from the one appropriate for spam — and many deployments apply similar thresholds across categories because that is how the product is configured.

And the customer's own policy is a document that has no formal relationship to the threshold at all. The translation from policy prose to a number happens in someone's head.

## What Already Exists
Vendors supply confidence scores and configurable thresholds, and the better products support per-category configuration. Some provide guidance on threshold selection based on typical customer choices. Human review routing by confidence band is a common pattern and is the right structure. Precision-recall curves are supplied to sophisticated customers. Platform policy documents exist and are entirely disconnected from classifier configuration.

## The Customisation Gap
The operating point should follow from stated costs rather than from queue capacity. A customer that can express the relative cost of a miss and a false positive per category — even coarsely, even as an ordering — has enough for the threshold to be derived rather than tuned, and the exercise of stating those costs is itself valuable because it surfaces decisions the organisation has been making implicitly.

Review capacity should be a constraint, not the objective. The correct framing is maximising harm reduction subject to available review capacity, which is a well-formed allocation problem across categories — and it produces a very different configuration from tuning each category until the queue looks manageable.

Policy-to-configuration mapping is the unbuilt translation layer. A customer's written policy describes what is and is not acceptable, and mapping that to category selection, thresholds and routing is currently a solutions engineer's interpretation. Making it explicit, versioned and reviewable means the configuration can be checked against the policy it is meant to implement.

And uncertainty should reach the decision. A score near the threshold is a different situation from one far above it, and routing by distance from the boundary rather than by a binary comparison puts human attention where the classifier is least certain — which is where the errors are.

## Impact If Solved
The threshold is where trust and safety policy is actually implemented, and it is set by trial against queue capacity with no stated relationship to the costs involved. Cost-derived operating points, capacity as a constraint rather than an objective, explicit policy-to-configuration mapping and confidence-aware routing would make the most consequential configuration in a moderation system a deliberate decision rather than an operational accident.
