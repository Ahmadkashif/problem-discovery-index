# Instrumentation Shipped by Default

**Niche:** [[niches/internal-developer-platforms/platform-usage-telemetry/profile|Platform Usage Telemetry]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product analytics software development kits make instrumenting a product a matter of a few lines, and no platform tooling ships with any instrumentation at all.
**Tags:** #descriptive-statistics #survival-analysis #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation #compliance
**Contested on:** Every serious competitor here is fighting to give a platform team the usage instrumentation any product team would consider essential — and whoever ships it by default takes the category, because the signals all exist and nobody collects them.

## The Problem
Instrumenting a product for analytics is a solved, low-effort exercise: a client library, an event schema, a few lines per interaction, and a dashboard. Every consumer product does it as a matter of course. Internal platform tooling ships with none of it, so a platform team that wants to know whether anybody uses a feature must add the instrumentation themselves across several components they did not write.

## What Already Exists
Product analytics client libraries and platforms; open event schemas and collection standards; the telemetry collection standard already used for operational data, which the platform components frequently emit to already; funnel and cohort analysis tooling; and the whole product analytics practice.

## The Customization Gap
The adaptation is to internal tooling with identifiable colleagues as users. It requires: (1) emitting on the existing operational telemetry pipeline rather than adding a separate analytics stack, since the platform already collects telemetry and a second pipeline is a second thing to operate — which is the practical route to shipping it by default; (2) an identity model that joins across components while being transparent about measuring colleagues, since this is individual usage data about identifiable employees and the ethical posture should be stated rather than assumed, with aggregate reporting as the default; (3) a standard schema for platform events, since every platform has substantially the same interactions and a shared vocabulary would make the analysis portable and the vendors' aggregate view possible; (4) defaults that produce a useful dashboard with no configuration, because a platform team will not do the configuration and the point is that the measurement exists without a project; and (5) an opt-out for organisations whose policy prohibits it, which is a real constraint in some regulated environments and should not block the default everywhere else.

## Target Customer
Platform tooling vendors, the open platform framework community, product analytics vendors for whom internal tools are an unserved segment, and platform engineering teams.

## Impact If Solved
Instrumentation is a solved, cheap exercise and the category ships none of it, which is why the measurement that would prevent the category's defining failure does not exist. Emitting on the existing telemetry pipeline is what makes shipping it by default practical.
