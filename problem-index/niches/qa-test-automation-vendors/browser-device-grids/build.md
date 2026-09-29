# Thousands of Combinations, None of Them Evaluated

**Niche:** [[niches/qa-test-automation-vendors/browser-device-grids/profile|Browser & Device Grids]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Device and browser grids are mature commercial services offering thousands of combinations, and nobody can tell a customer which ones are actually earning their cost.
**Tags:** #optimization-fundamentals #gradient-boosting #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to offer the combinations that actually matter, on environments that behave like real ones, at a price per parallel session that beats running a lab — and whoever does that takes the grid account, because the alternative is self-hosting.

## The Problem
A team runs its suite against fourteen browser and device combinations. The list was chosen three years ago from market share statistics and has grown when somebody worried about a platform. Of the fourteen, three have never produced a failure that the primary combination did not also produce, two cover a browser version with a negligible share of this product's actual users, and one covers a device that is genuinely different and catches things — and nobody knows which is which. The cost is fourteen times the primary combination, the suite takes fourteen times as long, and the selection has never been evaluated.

## Why Nobody Has Built This
Grids are billed per session, so a larger matrix is more revenue and nobody has an incentive to prune it. The evaluation requires joining failures to combinations and determining which failures were unique to a combination, which is straightforward and has not been packaged. Matrix selection is made defensively — the cost of missing a platform-specific defect feels larger than the cost of running the combination — which is a reasonable instinct in the absence of evidence and produces monotonic growth. And the customer's own analytics, which show what their users actually use, are in a different system from the grid configuration.

## What to Build
Select the matrix from evidence. Join the customer's own user analytics to the combination choice, so the matrix reflects what their users actually run rather than global market share, which is the most obvious correction and is currently not made. Report unique failures per combination: which combinations have produced a failure that no other combination produced, over a period, which is the direct measure of whether a combination earns its cost and is a straightforward analysis over execution history. Cluster combinations by behavioural similarity, since browsers sharing an engine version rarely diverge and a matrix containing several near-identical environments is paying repeatedly for the same coverage. Recommend a matrix that maximises defect-finding per unit of cost, which is a selection optimisation with an empirical objective. Run the full matrix periodically and the reduced one continuously, which is the standard compromise everywhere else in testing and is rarely applied here. Report user exposure for combinations not covered, so the risk of omitting one is stated rather than feared. And measure the outcome, since a matrix reduction that later misses a defect should be visible and correctable.

## Target Customer
Quality and device operations teams running large matrices, and the grid vendors willing to compete on effectiveness rather than on matrix size.

## Impact If Built
The matrix is chosen defensively and grows monotonically because nothing evaluates it, and the evaluation is a straightforward analysis over execution history. Joining to the customer's own user analytics is the most obvious available correction and is not made anywhere.
