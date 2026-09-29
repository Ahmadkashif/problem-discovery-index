# Nobody Knows Their Own Single-Maintainer Exposure

**Niche:** [[niches/open-source-commercial-vendors/long-tail-critical-dependencies/profile|Long-Tail Critical Dependencies]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An enterprise's production systems depend on dozens of packages maintained by one person each, the list is computable from their own dependency files in an afternoon, and no enterprise has it.
**Tags:** #graph-theory #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to identify which unfunded projects the software economy actually depends on and get resources to them before they fail — and whoever does that takes the funding function, because the current allocation is driven by visibility rather than by dependence.

## The Problem
An enterprise runs a risk programme covering its suppliers, its cloud providers and its major software vendors. Its production systems also depend, transitively, on several hundred open-source packages, of which a few dozen have a single maintainer, several have had no release in over a year, and a handful are controlled by a single publishing credential with no second party. None of this is on any risk register. The computation — take the dependency files, resolve transitively, look up maintainer counts and activity — is an afternoon's work with public data and has not been done.

## Why It's Still Broken
Third-party risk management covers entities the organisation has a contract with, and an open-source maintainer is not one — the framework's boundary excludes exactly the dependencies that cannot be managed by contract. Composition analysis tools report licences and vulnerabilities rather than sustainability, so the tooling that scans the dependency graph does not ask this question. The risk has no owner: security looks at vulnerabilities, procurement at suppliers, and engineering at whether things work. And the failure mode is rare enough that it has not forced the question, though the instances that have occurred were expensive.

## What a Fix Looks Like
Compute the exposure and put it on the register. Resolve the full transitive dependency graph for production systems, which composition analysis tools already do, and join it to maintainer and activity data from the public ecosystem metadata — which is the missing step and requires no new tooling. Flag the combination that matters: a package that is depended on by something important, has one maintainer, and shows declining activity. Include publication control as a distinct risk, since a single credential with no second approver is how several supply chain compromises happened and is separately observable. Prioritise by the importance of what depends on it rather than by the package's popularity, since the enterprise's risk is about their systems. Then act, with the options being to fund, to contribute a maintainer, to vendor the code, or to accept the risk knowingly — all of which are reasonable and none of which is available while the exposure is unknown. Re-run continuously, because dependencies change with every build and a maintainer's circumstances change without notice. And share the findings upstream where funding or contribution is the chosen response, since the maintainer frequently does not know an enterprise depends on them.

## Who Feels the Pain
Enterprises with an unmeasured concentration of risk in unpaid individuals; maintainers carrying critical infrastructure without support; and security functions whose supply chain programme stops at the entities with contracts.

## Impact If Fixed
The computation is an afternoon over data the enterprise already has and produces a risk list that currently exists nowhere. Prioritising by the importance of the dependent rather than by package popularity is what makes the list specific to this organisation and therefore actionable.
