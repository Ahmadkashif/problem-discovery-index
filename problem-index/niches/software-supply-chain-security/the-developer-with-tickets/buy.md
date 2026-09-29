# Automated Remediation That Already Works

**Niche:** [[niches/software-supply-chain-security/the-developer-with-tickets/profile|The Developer With Tickets]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated dependency update tooling opens tested pull requests across an estate and is widely deployed, and security findings are delivered as tickets that ask a human to do the same thing by hand.
**Tags:** #graph-theory #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #cross-validation
**Contested on:** Every serious competitor that takes this seriously is fighting to give a developer a finding they can act on — what it means, whether it matters here, and exactly how to fix it — and whoever does that takes the remediation rate, because the current output is a ticket about code they did not write.

## The Problem
Automated dependency update tools resolve a version, open a pull request, run the tests and report the result — across hundreds of repositories, unattended, and they are widely deployed. Security findings arrive as tickets asking a developer to perform the same operation manually, frequently in the same repository where the update tool is already running. The two mechanisms are not connected, so a developer receives a ticket about a vulnerability and, separately, a pull request that would fix it, with nothing relating them.

## What Already Exists
Automated dependency update tooling with cross-repository operation, grouping and test integration; dependency resolution engines in every package manager; the update tools' own security advisory integration, which exists and is shallow; and pull request automation frameworks.

## The Customization Gap
The adaptation is to a security-driven update with a constrained target. It requires: (1) resolving the minimum change that fixes the vulnerability, since the update tool's default is the latest version and the security requirement is the earliest version that resolves it — which is a much smaller and safer change and is frequently available; (2) transitive resolution, because the vulnerable package is usually not a direct dependency and the fix is an upgrade to something that depends on it, which requires walking the graph and is the computation the ticket omits; (3) linking the change to the finding, so a merged pull request closes the ticket and the remediation is recorded automatically — which is plumbing and is what stops the two mechanisms operating independently; (4) risk assessment attached to the proposed change, since the developer's reluctance is about breakage and an unannotated upgrade proposal does not address it; and (5) handling the no-fix-available case explicitly, which is common and where the ticket is currently most useless — the honest output is the available mitigations rather than an upgrade instruction that cannot be followed.

## Target Customer
Supply chain security vendors, the dependency update tooling projects, and the application security functions whose remediation rate depends on this connection.

## Impact If Solved
The automation that performs the remediation is already running in the same repository and is not connected to the finding that requires it. Minimum-version resolution and transitive path computation are what turn a ticket into a mergeable change.
