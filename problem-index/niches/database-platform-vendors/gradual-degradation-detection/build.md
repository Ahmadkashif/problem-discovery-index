# Gradual and Then Sudden

**Niche:** [[niches/database-platform-vendors/gradual-degradation-detection/profile|Gradual Degradation Detection]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Databases degrade gradually and fail suddenly — a plan flips, an index stops being selective, growth crosses a threshold — and the engine exposes every diagnostic needed to see it coming and interprets none of them.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to warn a team that a database is degrading weeks before it breaks — and whoever does that takes the account, because the engines already expose everything required and interpret none of it.

## The Problem
A query that has run in four milliseconds for two years starts taking nine hundred. The table grew past the point where the planner's estimate crossed a boundary, the plan flipped from an index scan to a sequential scan, and it happened on the Monday of a promotion. The engine's statistics showed the row count growing steadily for six months, the plan stability could have been tracked, and the selectivity of the index had been declining measurably. Nobody was watching any of it, because watching it requires knowing which of several hundred catalogue views matter and what the numbers mean — which is a specialist's knowledge and the organisation does not have a specialist.

## Why Nobody Has Built This
The engines were built by people who understand the internals for people who understand the internals, and the diagnostic surface reflects that: it is complete, precise and uninterpreted. The monitoring products that emerged serve the same specialist audience and compete on presenting the same views more attractively. Interpretation requires encoding the specialist's knowledge — which indicators matter, what thresholds mean, how a trend translates into a timeline — which is tacit, engine-specific and has never been written down in an operational form. And the managed service vendors, who have the fleet-wide view that would make this easy, use it for capacity planning.

## What to Build
Track the leading indicators as trajectories and predict the break. Monitor the specific precursors rather than the symptoms: statistics staleness against table churn, plan stability per query with the alternatives the planner is close to choosing, index selectivity trends, bloat accumulation against reclamation rate, table and index growth against the thresholds where access patterns change, connection and lock contention trends, and replication lag under load. Forecast each trajectory to the point where it becomes a problem, which turns a trend into a date and is the form a team can act on — this table will cross the threshold at which this query's plan flips in approximately six weeks. Attach the remedy, since a correct diagnosis without a procedure leaves the team searching blog posts, which is the state the category's own profile describes. Rank by consequence, using query importance and workload criticality, because a database exposes hundreds of potential concerns and an unranked list is a specialist's tool again. Detect the plan flip when it happens as well as before, since some cannot be predicted and rapid attribution is the next best thing. And validate the predictions against what actually happened, because a warning system whose accuracy is never measured will be ignored within two quarters.

## Target Customer
Platform engineering teams without a database specialist, which is most of them; database monitoring vendors; and the managed service providers for whom this is the operability their engineering quality is not matched by.

## Impact If Built
The failure paths are known, gradual and fully observable, and the interpretation is the missing layer rather than the data. Forecasting a trajectory to a date converts a diagnostic into an action, and attaching the remedy is what makes it usable by a team without a specialist.
