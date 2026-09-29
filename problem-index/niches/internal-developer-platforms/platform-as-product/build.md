# A Platform Nobody Uses

**Niche:** [[niches/internal-developer-platforms/platform-as-product/profile|Platform as Product]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platform teams build paved paths, developers route around them, and nobody measures where the abandonment happens — because the team thinks it is building infrastructure rather than a product with users.
**Tags:** #survival-analysis #logistic-regression #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to make a platform team behave like a product team — measuring adoption, abandonment and what developers do instead — and whoever does that takes the platform account, because the category error explains most of its failures.

## The Problem
A platform team spends a year building a paved path for new services: a template, a pipeline, standard observability, a deployment mechanism. Eleven teams adopt it, all of whom were consulted during the build. The next thirty teams do not. Nobody knows why. Some tried the template and abandoned it at a step that did not fit their language; some found the deployment mechanism did not support a pattern they needed; some never heard about it. The platform team's response is a roadshow, better documentation and a scorecard that marks non-adopting teams down — none of which addresses a cause, because no cause has been identified.

## Why Nobody Has Built This
Platform teams are staffed with infrastructure engineers and organised as infrastructure functions, so the product disciplines — user research, funnel instrumentation, adoption measurement — are absent by construction rather than by choice. The signals are available in the portal, the pipelines, the provisioning system and the repositories, and collecting them requires somebody to frame the platform as a product with users, which is a framing change rather than a technical one. And a platform that measures its own abandonment produces uncomfortable findings about work already done.

## What to Build
Instrument the platform like a product and act on it. Define the funnel explicitly — aware, attempted, completed onboarding, deployed, still using after three months — and measure conversion and elapsed time at each step, which is the foundational instrumentation and is a join across systems the platform already runs. Identify the abandonment point precisely, since a golden path is a sequence and developers stop at a specific step for a specific reason, which is observable and is the most actionable finding available. Observe what teams do instead, which is visible in their repositories and pipelines, and is the strongest evidence of what the platform is missing — a team that built their own deployment mechanism has told you something specific. Measure retention rather than onboarding, since a service that onboarded and reverted is a failure counted as a success. Segment by team characteristics, because the platform frequently works for the teams it was designed with and not for others, and the aggregate hides that. Instrument the support channel, which is the second niche below and is a direct signal of where the abstraction is confusing. And report all of it to the platform team as their own product metrics, since the change that matters is what the team optimises.

## Target Customer
Platform engineering leadership, the developer experience function where one exists, and the platform tooling vendors whose customers' deployments stall at partial adoption.

## Impact If Built
The category's defining failure is a framing error with an instrumentation remedy, and every required signal exists. Abandonment-point identification and observing what teams built instead are the two findings that turn a roadshow into a roadmap.
