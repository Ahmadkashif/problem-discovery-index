# The Prototype Factory Floor

**Niche:** [[niches/mobile-game-publishers/prototype-production-tooling/profile|Prototype Production Tooling]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A publisher testing thirty concepts a month is running a factory and the unit cost of a build is nobody's responsibility.
**Tags:** #workflow-orchestration #automation #data-integration #evaluation-metrics #optimization-fundamentals #revenue-impact #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to cut the cost and time of getting a testable prototype in front of a paid audience, because the funnel's economics are set by that number — and whoever cuts it takes the account.

## The Problem
The publishing model's arithmetic depends on prototypes being cheap. Each one still requires onboarding, tutorial scaffolding, analytics events, store metadata, build configuration, submission, campaign setup and a dashboard — almost none of which is specific to the concept being tested. Teams rebuild it each time, differently, and a meaningful share of a three-week prototype cycle is spent on work that has been done dozens of times in the same building.

## Why Nobody Has Built This
Internal tooling has no revenue line and no owner. Each team solves it for itself and the duplication is invisible in aggregate. The engine vendors build for shipped games rather than for disposable prototypes. And the cost is distributed across many small delays rather than appearing anywhere as a number.

## What to Build
Treat it as a production line and standardise the shared parts. Ship a prototype scaffold containing everything every concept needs — onboarding, analytics, store metadata, build config — so a team starts at the concept rather than at the plumbing, which is the core and is where most of the recoverable time sits. Instrument by default with a standard event set, since consistent instrumentation across concepts is also what makes cross-prototype comparison possible for the first time. Automate build, signing and store submission, as the turnaround delay is pure waiting. Template the test campaign setup so a build reaches an audience the same day. Maintain a shared component library for the mechanics that recur, because most concepts are recombinations. Standardise the reporting output rather than letting each team build a dashboard. Measure the unit cost and cycle time per prototype and report it, which nobody does and which is what justifies the investment. Version the scaffold so improvements propagate rather than forking. Keep it thin enough that teams do not route around it, which is how internal platforms die. And make the scaffold the path of least resistance rather than a mandate.

## Target Customer
Mobile publishers, hypercasual and hybridcasual studios, engine and middleware vendors, and internal platform tooling providers.

## Impact If Built
The funnel's economics are set by the unit cost of a testable build, and nobody owns that number. A default scaffold with standard instrumentation turns duplicated plumbing into cross-prototype comparability.
