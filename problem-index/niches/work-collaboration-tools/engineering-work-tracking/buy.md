# Cycle Time Analytics Instead of Estimates

**Niche:** [[niches/work-collaboration-tools/engineering-work-tracking/profile|Engineering Work Tracking]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Forecasting from historical cycle time distributions is a well-documented practice with published methods and free tooling, and engineering organisations spend hours in estimation meetings producing numbers that are worse.
**Tags:** #survival-analysis #monte-carlo-methods #probability-distributions #confidence-intervals #evaluation-metrics #time-series-forecasting #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in engineering work tracking is fighting to make the tracker reflect what the code actually shows — and whoever connects the ticket to the commit, the review and the deployment most completely takes the engineering organisation.

## The Problem
A team spends two hours estimating a backlog in abstract units, converts the total into a duration using a velocity figure, and commits to a date. The same team's tracker holds the actual cycle time of every item it has completed over two years, from which a probabilistic forecast can be produced in seconds with better accuracy and an honest interval. The estimation meeting persists because it is the practice, and its output is treated as a plan while the historical distribution — which is the evidence — is used for a burndown chart.

## What Already Exists
Probabilistic forecasting from cycle time distributions, Monte Carlo simulation over historical throughput, and the associated practice literature are well established in the software delivery community, with free tools and published methods. Cycle time, throughput and work-in-progress analytics are available in every tracker or as inexpensive add-ons. The statistical content is elementary and the practice is documented in detail. Nothing needs inventing.

## The Customization Gap
The adaptation is to make the forecast usable and trusted in place of an established ritual. It requires: (1) cycle time measured from a defined start that reflects when work genuinely began rather than when a ticket was created, since backlog age dominates any measure that starts at creation and makes the distribution meaningless; (2) segmentation by work type, because a bug fix and a feature have different distributions and pooling them produces an interval so wide nobody uses it; (3) the forecast expressed as a probability of a date rather than a date, which is both the honest form and the one that lets a team have a useful conversation about scope; (4) dependency and blocking time reported separately, since a team whose cycle time is dominated by waiting on another team has a coordination problem rather than an estimation problem and a single distribution hides that; and (5) the forecast presented alongside the team's own historical accuracy, because the ritual persists partly because people distrust a number that arrives without provenance.

## Target Customer
Engineering leadership, delivery and programme functions, and the tracker vendors whose reporting is built around estimates their own data could replace.

## Impact If Solved
Probabilistic forecasting from cycle time is better evidenced than estimation, takes no meeting time, and produces an interval rather than a false point — and the practice is documented well enough that adopting it is a decision rather than a project. Separating blocked time is the finding that most often changes what a team actually does, because it relocates the problem from estimation to dependency.
