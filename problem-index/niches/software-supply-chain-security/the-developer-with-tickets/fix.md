# The Transitive Dependency You Cannot Upgrade

**Niche:** [[niches/software-supply-chain-security/the-developer-with-tickets/profile|The Developer With Tickets]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** The ticket names a package four levels down the dependency tree, the developer's direct dependency pins it, and nothing tells them which of their own dependencies to upgrade or whether a fixed version exists at all.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to give a developer a finding they can act on — what it means, whether it matters here, and exactly how to fix it — and whoever does that takes the remediation rate, because the current output is a ticket about code they did not write.

## The Problem
The finding names a package the developer has never added. It arrived four levels deep, pulled in by a framework whose own dependency declaration constrains it to a range that excludes the fixed version. The developer's options are to upgrade the framework if a version exists that resolves it, to override the transitive version if their package manager supports it and accept the compatibility risk, to wait for the framework maintainer to update, or to do nothing. Establishing which of those applies takes half an hour of dependency tree reading. The tool that reported the finding resolved the tree to find it and did not say any of this.

## Why It's Still Broken
The scanner's job ends at identifying the vulnerable component, and the remediation path is a further computation nobody added — despite the scanner already holding the resolved dependency graph, which is what it used to find the component. Override mechanisms differ by ecosystem and carry compatibility risk, which makes recommending one require judgement the tools have avoided. And the no-fix-available case, where no version of the framework resolves it, is common and is reported identically to the fixable case.

## What a Fix Looks Like
Compute the path and state it. Walk the resolved graph from the vulnerable package back to the direct dependencies that pull it in, which is the computation the scanner has already performed and does not report, and name them. Determine whether a version of each direct dependency exists that resolves the vulnerability, which is a query over the registry and is the answer the developer needs first. State the override option where the ecosystem supports it, with its compatibility implications, since it is frequently the fastest remediation and is avoided because nobody explains it. Report the no-fix case as a distinct outcome with the available mitigations — configuration changes, feature disablement, network controls — rather than as a remediation instruction that cannot be followed, since this is where the current ticket is most useless. Identify when the fix requires an upstream maintainer to act, and say so, since the developer is then not the person who can resolve it and treating them as such is the source of considerable frustration. Group findings by the direct dependency that would resolve them, since one framework upgrade frequently closes a dozen findings and the instance-level ticket hides that. And track the ones blocked upstream, since they will remain open and should not count against the team.

## Who Feels the Pain
Developers reading dependency trees to work out what they are being asked to do; security teams whose tickets age because the action is unclear; and organisations whose remediation rate reflects the difficulty of the instruction rather than the willingness to act.

## Impact If Fixed
The remediation path is a walk over a graph the scanner already resolved and is the answer the developer needs first. Grouping by the resolving direct dependency turns a dozen tickets into one upgrade, and stating the no-fix case honestly stops asking people to do something impossible.
