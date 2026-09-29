# State Reporting Is Rebuilt Per State, Every Year, By Hand

**Niche:** [[niches/childcare-centers/early-childhood-assessment-publishers/profile|Early Childhood Assessment Publishers]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Fix (Pain Point)
**One-liner:** Forty state contracts each specify their own aggregations, cut points, and file formats, every one is implemented as bespoke reporting code, and a change in one state's rules sends an engineer to find out what else it breaks.
**Tags:** #workflow-orchestration #data-integration #automation #evaluation-metrics #descriptive-statistics #compliance #feature-engineering #bert #transformers #worker-facing

## The Problem
Accountability reporting is a large share of what the publisher actually delivers, and it is delivered as bespoke work. Each state defines its own outcome bands, its own subgroup breakdowns, its own inclusion rules for which children count, its own submission format, and its own deadline — and each is implemented separately, largely by hand, by people who have accumulated the state's quirks in their heads. When a state adjusts a cut point or adds a subgroup, someone traces what depends on it through reporting code that was written for that state alone. Reporting season is therefore a recurring crisis with a fixed date, and the cost scales linearly with every new state contract won, which quietly caps how many the company can take.

## Why It's Still Broken
Each state contract was won separately and implemented under its own deadline, so the fastest path was always another bespoke pipeline, and forty of those decisions compound into an architecture nobody chose. The requirements themselves arrive as prose in contracts and state guidance documents, not as specifications, so there has never been a structured artifact to build a general system against. And because reporting is delivery rather than product, it is staffed as an operational cost centre with no mandate to rebuild itself, which is precisely why it never has been.

## What a Fix Looks Like
State reporting expressed as configuration over a common model rather than as code per state. The reporting requirements become structured declarations — population inclusion rules, aggregation levels, subgroup definitions, cut points, output format, deadline — evaluated by one engine, so a state's rules live in a readable specification a domain expert can check rather than in a pipeline only an engineer can read. Each specification is versioned against the contract period it applies to, which is what makes a prior year's submission reproducible when a state audits it — currently a reconstruction exercise. A dependency view answers, before a change, which reports and which states are affected. Validation runs against each state's own rules before submission rather than after rejection, and a shared library of common definitions makes visible how much of what looks like forty unique requirements is actually five patterns with variations, which is the finding that makes the next contract cheap instead of expensive.

## Who Feels the Pain
Engineers reverse-engineering state requirements under a fixed deadline every year; the delivery organization whose cost scales with contracts won; state administrators receiving late or rejected submissions; and the growth strategy, since the marginal cost of a new state contract is what limits how many the company pursues.

## Impact If Fixed
Turns the constraint on expansion into a configuration exercise. Reporting season stops being a recurring crisis, prior submissions become reproducible under audit, and the structured requirement library is itself an asset — a documented, comparable picture of how forty states define early childhood outcomes, which nobody else holds and which is directly useful in the policy conversations the publisher is already part of.
