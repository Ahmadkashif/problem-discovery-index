# A Selection Model Instead of a Threshold

**Niche:** [[niches/mobile-game-publishers/prototype-selection/profile|Prototype Selection]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retention number from a few thousand installs decides whether a concept continues, and the threshold it is compared against was inherited rather than derived.
**Tags:** #survival-analysis #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #causal-inference #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to decide which of dozens of prototypes a month deserves to continue, on evidence that is three days long and drawn from a population that was itself filtered by the same rule — and whoever gets the selection right takes the account.

## The Problem
Day-one retention on a small test campaign is compared to a number, and a team's three weeks of work either continues or does not. The number came from the hypercasual era, survived a structural change in how mobile games are acquired and monetised, and is applied across genres whose retention curves have different shapes entirely. The relationship between that signal and a 180-day outcome is weak, genre-dependent and unquantified, and the decision carries no stated uncertainty at all.

## Why Nobody Has Built This
The threshold works well enough to run a business on, which removes the urgency. The publisher's own outcome history is small in the tail that matters — few games reach scale. The evidence is contaminated by the funnel, since only survivors have outcomes. And a model that says "uncertain" is harder to operate than a number that says "kill".

## What to Build
Replace the threshold with a prediction and an interval. Model eventual performance from early behavioural telemetry conditioned on genre and mechanic, which is the core — retention curves have different shapes across genres and a single threshold is simply wrong for most of them. Attach an honest confidence interval to every prediction, since a decision made on a few thousand installs has uncertainty that dominates the point estimate and hiding it is the central error. Use richer early signal than day-one retention alone — session structure, progression pace, early engagement depth — as the day-one number discards nearly everything the test collected. Control for the acquisition conditions the test ran under, because a concept tested into an expensive audience looks worse than the same concept tested cheaply. Express the output as expected portfolio value rather than pass or fail, which is what leadership is actually optimising. Recommend continue, extend the test, or kill, since "run it another week" is the correct answer surprisingly often and the binary rule cannot produce it. Calibrate against the publisher's own realised outcomes rather than industry convention, which is the whole asset. Report how often the model and the threshold disagree, as that is how it earns trust. Track decision quality over time rather than only model accuracy. And make the kill decision auditable, because teams deserve to know what ended their project.

## Target Customer
Mobile publishers, hypercasual and hybridcasual studios, publishing partners evaluating third-party concepts, and games analytics vendors.

## Impact If Built
Retention curves have different shapes across genres and a single threshold is simply wrong for most of them. A genre-conditioned prediction with an honest interval turns the highest-leverage decision in the business into one that can be evaluated.
