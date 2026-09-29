# Extensibility as Both the Feature and the Burden

**Niche:** [[niches/internal-developer-platforms/platform-tooling-market/profile|Platform Tooling Market]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The portal framework is chosen for its extensibility, the organisation writes eleven plugins, and upgrading becomes a project because every plugin depends on internals that moved.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to be the tooling an organisation builds its platform on — and that contest is a portal decision in one market and an abstraction decision in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
An organisation adopts the portal framework specifically because it can be extended to fit their estate, and extends it: eleven plugins, several forks of core components, and a substantial amount of glue. Eighteen months later an upgrade is needed for a security fix. Six plugins depend on interfaces that changed, two forks have diverged too far to rebase, and the upgrade takes a quarter. The organisation stops upgrading, runs an increasingly old version, and eventually concludes the framework is expensive to operate — which is true and is a consequence of the property they chose it for.

## Why It's Still Broken
Extensibility through internal interfaces is easy to offer and hard to support: a stable public extension interface requires deciding what is public, which constrains the project, and the path of least resistance is to let people reach into internals. The maintenance consequence lands on the adopter eighteen months later. Nobody measures the upgrade burden across the adopter population, though the framework's maintainers could. And the forks are invisible to everyone including, frequently, the organisation that made them.

## What a Fix Looks Like
Make the extension surface explicit and the upgrade cost visible. Define a supported extension interface with a stability commitment, distinct from internals, so an adopter knows which extensions will survive an upgrade — which is the structural fix and constrains the project usefully. Detect extensions that reach past the supported surface and warn at build time, since an organisation building a plugin on an internal interface is creating a future upgrade problem they cannot see. Measure the upgrade burden across adopters, which the maintainers can do from public deployments and issue reports and which would prioritise interface stability where it actually hurts. Provide migration tooling for interface changes, which is standard practice in mature frameworks and reduces the burden more than any amount of documentation. Track fork divergence within an organisation, so the cost of a fork is visible while it is small. Report the organisation's own extension inventory and its upgrade exposure, which is a straightforward analysis and is the number that would inform whether to extend or to contribute upstream. And make contributing upstream the easier path for extensions that many organisations need, since the same plugin is written repeatedly across adopters.

## Who Feels the Pain
Platform teams whose upgrade is a quarter; organisations running old versions with known vulnerabilities because upgrading is too expensive; and framework maintainers whose extensibility is producing the complaint about operational cost.

## Impact If Fixed
A supported extension interface with a stability commitment is a project decision that eliminates most of the upgrade burden structurally. Detecting extensions that reach past it at build time makes the future cost visible while it is still avoidable.
