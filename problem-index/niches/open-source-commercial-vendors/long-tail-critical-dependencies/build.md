# Everything Depends On It and Nobody Funds It

**Niche:** [[niches/open-source-commercial-vendors/long-tail-critical-dependencies/profile|Long-Tail Critical Dependencies]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The software the economy most depends on is frequently maintained by one unpaid person, the situation is discussed constantly and addressed rarely, and both the dependence and the fragility are computable from public data.
**Tags:** #graph-theory #spectral-graph-theory #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #revenue-impact
**Contested on:** Every serious competitor here is fighting to identify which unfunded projects the software economy actually depends on and get resources to them before they fail — and whoever does that takes the funding function, because the current allocation is driven by visibility rather than by dependence.

## The Problem
A utility library is a transitive dependency of a substantial fraction of the software industry. It is maintained by one person in their spare time, has not had a release in fourteen months, and has an issue queue they stopped reading. Corporate open-source funding in the same period went to well-known projects with foundations, paid staff and conference tracks — allocated by visibility, which is a reasonable proxy for importance and is not the same thing. When the library eventually fails, through abandonment or through a compromise of a maintainer account nobody was watching, the cost lands across the industry and is enormously larger than the funding that would have prevented it.

## Why Nobody Has Built This
The dependence is computable and the computation has not been made operational: dependency graphs are public, transitive dependence is a graph traversal, and nobody has joined it to maintainer health at scale and published the result as a fundable list. Funding decisions are made by people responding to what they can see, and a single-maintainer library with no marketing is invisible by construction. The maintainers themselves frequently do not know how widely their code is used and therefore do not ask. And there is no mechanism to convert a computed criticality into resources, which is the harder half.

## What to Build
Compute dependence and join it to fragility, then build the mechanism. Traverse the public dependency graphs to compute transitive dependence, weighted by the importance of the dependents rather than by raw counts, which distinguishes a package everything depends on from one with many hobbyist users. Measure fragility from public signals: maintainer count and concentration, contribution trend, release cadence, responsiveness, time since last activity, and whether a single account controls publication — all of which are observable and none of which is currently joined to dependence. Produce the ranked list of highest-dependence, highest-fragility projects, which is the artefact the funding conversation has always lacked. Tell the maintainers, since many do not know their reach and the knowledge changes both their choices and their ability to ask for support. Give enterprises their own exposure list, which is the same computation over their own dependency graph and is the version they will act on because it is about their risk. Build the funding mechanism to match the analysis, since a list without a route to resources is another report. And track succession explicitly: which projects have a single point of control, which have a documented succession plan, and which have neither, because abandonment and account compromise are the two realised failure modes and both are succession problems.

## Target Customer
Foundations and funding programmes, corporate open-source offices, enterprises quantifying their dependency risk, and the maintainers themselves.

## Impact If Built
Dependence and fragility are both computable from public data and are not joined, which leaves funding allocated by visibility. The enterprise-specific exposure list is the version that produces action, because it converts a general concern into a specific risk somebody owns.
