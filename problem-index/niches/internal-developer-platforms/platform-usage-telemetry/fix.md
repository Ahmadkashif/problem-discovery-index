# The Feature Nobody Uses and Nobody Knows

**Niche:** [[niches/internal-developer-platforms/platform-usage-telemetry/profile|Platform Usage Telemetry]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A platform team maintains a set of capabilities of which several are used by nobody, and nothing in the platform tells them which.
**Tags:** #descriptive-statistics #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to give a platform team the usage instrumentation any product team would consider essential — and whoever ships it by default takes the category, because the signals all exist and nobody collects them.

## The Problem
The platform offers twenty-three capabilities. Three of them account for nearly all use. Four have never been used by anybody outside the platform team. Several were built for a team that has since reorganised. All twenty-three are maintained, documented, tested and carried through every upgrade, and the platform team's capacity is consumed partly by keeping alive things nobody uses. Nobody knows which is which, so nothing is retired, and the maintenance burden grows while the useful surface does not.

## Why It's Still Broken
Feature-level usage is not recorded because the components log operationally rather than analytically, so the question cannot be answered without building the instrumentation. Retirement carries the familiar asymmetry — removing something somebody depends on is visible and keeping something unused is not — which guarantees monotonic growth exactly as it does with dashboards, rules and templates throughout this vault. And the platform team's own maintenance burden is not attributed to specific capabilities, so the cost of carrying an unused one is invisible too.

## What a Fix Looks Like
Count the usage and give capabilities a lifecycle. Record use per capability, per team and over time, which is the enabling instrumentation and requires the event stream from the build note. Classify into active, occasional, dormant and unused, and report it — which usually produces an uncomfortable and immediately actionable list. Attribute maintenance cost where it can be estimated, since a capability with no users and a substantial upgrade burden is the clearest possible candidate and the two facts are never joined. Deprecate with notice and a reversible window rather than deleting, which is what makes the decision safe enough to take, and is the same pattern the analytics and open-source deprecation niches describe. Tell the few users of a dormant capability directly, since they exist and can be consulted, which is an advantage an internal platform has over any external product. Report capability creation alongside retirement, since a platform adding four capabilities a quarter and retiring none has the same trajectory as every other estate in this vault. And re-run it continuously rather than as an audit, because a periodic campaign will stall exactly as every other campaign in this category does.

## Who Feels the Pain
Platform teams maintaining capabilities nobody uses; developers navigating a surface larger than its useful part; and organisations whose platform capacity is consumed by carrying its own history.

## Impact If Fixed
Per-capability usage is a grouping over the event stream and immediately identifies the unused surface, which is usually larger than the team expects. Notice-and-reversible deprecation is what converts an unmakeable decision into a routine one, and consulting the few actual users is an advantage only an internal platform has.
