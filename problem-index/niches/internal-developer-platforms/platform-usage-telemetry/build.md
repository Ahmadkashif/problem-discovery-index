# Every Signal Available, None Collected

**Niche:** [[niches/internal-developer-platforms/platform-usage-telemetry/profile|Platform Usage Telemetry]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An internal platform team is a product team whose users sit in the same building and whose usage it does not measure, and the instrumentation that would fix that ships with no product in the category.
**Tags:** #survival-analysis #k-means-clustering #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to give a platform team the usage instrumentation any product team would consider essential — and whoever ships it by default takes the category, because the signals all exist and nobody collects them.

## The Problem
A platform team wants to know where developers abandon the onboarding path. The portal knows who visited; the scaffolding tool knows who generated; the pipeline knows who deployed; the catalogue knows who registered. Four systems, four logs, no shared identifier, no join. Constructing the funnel is a fortnight of data engineering competing against the platform roadmap, so it does not happen, and the team continues to make product decisions from anecdote. Every platform team in the industry is in the same position, and the tooling they all use could have shipped the join.

## Why Nobody Has Built This
The tooling was built by infrastructure engineers for infrastructure engineers, and product instrumentation was not part of the mental model — the same category error the first niche describes, expressed in what the products ship. Each component logs for its own operational purposes with its own identifiers, and nothing was designed to be joined. The vendors also do not instrument their own products' usage, so they have no internal practice to export. And every platform team rebuilds the same thing or does without, which means the cost is paid hundreds of times.

## What to Build
Ship the instrumentation as a default. Establish a consistent identity across the platform's components — the developer, the team, the service — so that an action in the portal, the scaffold, the pipeline and the deployment can be joined, which is the enabling decision and is trivial at design time and awkward afterwards. Emit a standard event stream from every component with a shared schema, which turns four logs into one product analytics dataset. Define the standard funnel — aware, attempted, onboarded, deployed, retained — and compute it out of the box, since every platform has substantially the same funnel and each team currently defines it from scratch. Measure elapsed time per step as well as conversion, because the developer's experience is duration and the conversion rate alone hides it. Record feature-level usage within the platform, so a capability nobody uses is visible. Report it to the platform team as their product dashboard, arriving by default rather than requiring a project. And let the vendors use the aggregate across customers to see which of their own features are used, which is the same measurement pointed at themselves and is equally absent.

## Target Customer
Platform tooling vendors, who could differentiate enormously by shipping this; and platform engineering teams, who currently build it or do without.

## Impact If Built
Every platform team in the industry needs the same instrumentation and none of the tooling provides it, so the cost is paid hundreds of times or the measurement is skipped. A consistent identity and a shared event schema are design decisions rather than features, and they make the whole product-analytics practice available by default.
