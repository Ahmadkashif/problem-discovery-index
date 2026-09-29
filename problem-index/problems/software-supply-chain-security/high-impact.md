# Findings Nobody Can Act On

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Type:** High Impact
**One-liner:** A scan returns thousands of findings, a handful matter, and the tools report a severity score computed by someone who has never seen the application — which is why the output is filed rather than fixed.
**Tags:** #graph-theory #gradient-boosting #logistic-regression #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics #compliance

## The Problem
Scan a typical application and the tool returns hundreds to thousands of vulnerability findings across its dependency tree, most in transitive dependencies nobody chose directly.

Of those, a minority involve code paths the application ever executes. A smaller subset are exploitable given how the application actually deploys — behind authentication, without network exposure, in a configuration the vulnerability requires. A smaller subset still would justify interrupting a release.

Everyone working in the field knows this. The tools nonetheless report a count and a severity score drawn from a public database, computed by an analyst assessing the vulnerability in the abstract, with no knowledge of whether this application calls the affected function, whether the input reaches it, or what the deployment looks like.

The predictable outcome is that findings are ignored. Teams set a threshold, act on what crosses it, and file the rest, which means the genuinely critical finding is somewhere in a backlog of thousands. Security teams know this and cannot fix it, because prioritising properly would require the assessment the tool did not do.

Compliance made it worse rather than better. Because the finding count is auditable and the exploitability is not, organisations report on the count, which incentivises reporting everything.

## Why It's Unsolved
Reachability analysis is genuinely hard and is the right approach. Determining whether an application can reach a vulnerable function requires call graph analysis across language boundaries, through dynamic dispatch, reflection, dependency injection and configuration — and every one of those defeats static analysis in ordinary code. Vendors offering reachability differ enormously in rigour and rarely publish their false negative rates.

Exploitability depends on deployment, which the scanner does not see. The same dependency in a public-facing service and in a batch job that processes trusted input carries entirely different risk, and nothing joins the scan to the runtime environment.

The vulnerability data itself is a weak substrate. Severity scores are assigned inconsistently, affected version ranges are frequently wrong, and the same issue appears under multiple identifiers. Everything built on it inherits that.

And the incentives are perverse in a specific way: a vendor that reported far fewer findings would appear less thorough in an evaluation against competitors who report everything.

## What a Solution Looks Like
Reachability with honest error rates. The value is enormous — a finding in code the application never executes is genuinely not urgent — and the requirement is that vendors state how often they miss a reachable path, which none currently do.

Deployment context joined to the scan. Whether the service is internet-facing, what it processes, whether the vulnerable path is behind authentication, and whether runtime protections apply are all knowable from infrastructure and observability data and are never joined.

Exploitation likelihood rather than theoretical severity. Whether an exploit exists, whether it is being used, and whether this class of vulnerability historically gets exploited are far better prioritisation inputs than an abstract score, and probabilistic exploit prediction data exists and is under-used.

Remediation effort estimated alongside risk, because the decision is a trade-off. Whether upgrading this dependency is a version bump or a breaking migration is estimable from the ecosystem's own upgrade history across thousands of projects, and it is the missing half of every prioritisation conversation.

And a stated, defensible ranking rather than a count, so a team can work the top of a list knowing what was deprioritised and why.

## Impact If Solved
The category's output is currently unusable at the volume it generates, which means the critical finding sits alongside a thousand irrelevant ones. Reachability with honest error rates, joined to deployment context and remediation effort, is what converts a scan result into a work list — and the corpus needed to estimate upgrade risk sits in the vendors' own dependency graphs.
