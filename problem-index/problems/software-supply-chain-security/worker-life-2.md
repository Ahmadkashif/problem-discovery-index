# The Developer Handed Someone Else's Vulnerabilities

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Type:** Worker Life Changing
**One-liner:** A developer receives tickets about vulnerabilities in transitive dependencies they never chose, with no context on whether it matters and no clear way to fix it.
**Tags:** #graph-theory #gradient-boosting #large-language-models #confidence-intervals #k-nearest-neighbors #evaluation-metrics #automation #worker-facing

## The Problem
A developer is assigned a ticket: a critical vulnerability in a package their service depends on. They did not choose it — it arrived four levels deep through a dependency they did choose, which is normal in every modern ecosystem.

The ticket contains an identifier, a severity score and a version range. It does not say whether their code reaches the vulnerable function, whether their deployment is exposed, or what fixing it requires.

Fixing it is frequently not straightforward. The vulnerable package is transitive, so upgrading it means upgrading the intermediate dependency, which may not have a version that pulls the fixed one, which may require a major version bump with breaking changes, which may require code changes across the service.

So the developer spends a day on it, or overrides the version and hopes, or asks for an exception. None of these feel like security work and none produce confidence.

Then more tickets arrive, because the scanner runs nightly and the ecosystem publishes advisories continuously.

## Why It Matters to the Worker
Being handed responsibility for something you did not choose, cannot easily evaluate and may not be able to fix is a recognisable and demoralising pattern, and it recurs throughout modern software work.

The lack of context is the specific irritation. A developer asked to interrupt feature work for a security issue will do it willingly if they understand why it matters. Given only a severity score and an identifier, they cannot form that judgement, and over time they learn to treat the tickets as noise — which is exactly the wrong outcome and is entirely the tooling's doing.

The relationship damage compounds. Security becomes the function that generates unactionable work, and the next genuinely urgent request arrives with credibility already spent.

And the effort is frequently wasted. Much of what developers are asked to fix is not exploitable in their context, so real engineering time is spent on upgrades that changed nothing about the application's actual risk.

## What a Solution Looks Like
Context in the ticket. Whether the vulnerable code is reachable from this service, whether the deployment is exposed, and what the realistic exploitation path would be — so the developer can judge urgency rather than accept an assertion.

An upgrade path, not an instruction. The dependency tree determines what actually has to change, and computing the minimal set of upgrades that resolves the finding — with the breaking changes identified — is the difference between a ticket and a solution.

Automated pull requests where the change is safe, which the dependency update tools already do well for version bumps and do not do for transitive resolution, which is the harder and more common case.

Batching, so a developer addresses a set of related upgrades once rather than receiving them individually across weeks.

And honest deprioritisation, so unreachable findings do not become tickets at all — because the fastest way to restore credibility is to stop sending work that does not matter.

## Impact If Solved
Developers receive a continuous stream of tickets about code they did not write, without the context to judge them or the path to fix them, which teaches them to ignore security tooling. Reachability context and computed upgrade paths make each ticket actionable, and suppressing the unreachable ones is what restores the credibility the category has spent.
