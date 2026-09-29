# Recommendation Under a Decision Frame

**Niche:** [[niches/bi-analytics-platforms/frontline-operational-analytics/profile|Frontline Operational Analytics]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Prescriptive analytics, decision theory and uplift modelling are all developed fields, and frontline analytics ships a line chart.
**Tags:** #causal-inference #gradient-boosting #decision-trees #bayesian-inference #monte-carlo-methods #evaluation-metrics #confidence-intervals #worker-facing
**Contested on:** Every serious competitor here is fighting to put a decision-shaped answer in front of someone standing on a shop floor in the moment they can act on it — and whoever does that takes the operations account, because a dashboard nobody on shift opens is worth nothing.

## The Problem
Turning a prediction into a recommended action under uncertainty and asymmetric costs is decision theory, which is old and settled. Estimating the effect of an intervention rather than the outcome under it is causal inference and uplift modelling, both mature. Frontline analytics products present the prediction, or more often the history, and leave the entire decision to a person with forty seconds.

## What Already Exists
Decision-theoretic frameworks with explicit loss functions; uplift and treatment-effect models with open implementations; contextual bandits for learning from deployed decisions; simulation for evaluating policies before deployment; and calibrated probability estimation. Operations research supplies the scheduling and allocation formulations for many of these decisions directly. None of it is novel and much of it is taught in a first graduate course.

## The Customization Gap
The adaptation is to a frontline decision made under time pressure. It requires: (1) an explicit and asymmetric loss function per decision, elicited from operations rather than assumed, because the cost of stopping a line unnecessarily and the cost of running it into a failure are wildly different and a symmetric objective gets every such decision wrong; (2) the action set as a first-class object, since the recommendation must be one of the things this person can actually do right now, which is a much smaller set than the abstractly optimal one; (3) explanation compressed to two or three facts, because a supervisor will not read more and an unexplained recommendation is not followed — this is a presentation constraint that determines whether the model is used at all; (4) an override path that is easy and is recorded, since the operator is often right and their override is the most valuable training signal available; and (5) evaluation against the experienced operator's decisions rather than against a naive baseline, which is the honest comparison and frequently an unflattering one at the start.

## Target Customer
Operations leadership, vertical operational software vendors, and the analytics vendors attempting to move from reporting to prescription.

## Impact If Solved
The methods are mature and the transfer has not happened because the category's products stop at presentation. The asymmetric loss function and the recorded override are the two adaptations that matter, and the second is what makes the system improve rather than stagnate.
