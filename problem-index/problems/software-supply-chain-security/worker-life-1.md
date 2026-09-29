# Security Engineer Triaging Noise

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Type:** Worker Life Changing
**One-liner:** Application security engineers spend their weeks establishing that findings do not apply, one at a time, in a queue the scanner regenerates every night.
**Tags:** #graph-theory #gradient-boosting #bert #k-means-clustering #confidence-intervals #evaluation-metrics #automation #worker-facing

## The Problem
An application security engineer supports many development teams and receives the output of scanners run across all of them.

The work is triage, and most of it is refutation. Determine whether this finding is reachable in this application. Determine whether the deployment makes it exploitable. Determine whether the affected version range is accurate, since it often is not. Determine whether it duplicates a finding already assessed under a different identifier. Determine whether upgrading is feasible or would break something.

Most findings end in a dismissal, documented for audit. Then the scan runs again and returns the same findings, and unless the dismissal was recorded in a form the scanner respects, they arrive again.

The ratio is what makes it demoralising. An engineer may assess many findings to identify a handful worth acting on, and every one of the many required real technical judgement about someone else's codebase.

Meanwhile the work they were hired for — threat modelling, secure design review, building guardrails, incident response — waits.

## Why It Matters to the Worker
Application security is a specialism with genuine depth, and the triage queue exercises almost none of it. The judgement required is real and repetitive, which is a specific kind of fatigue: not mindless, but endlessly the same.

The engineer also carries an asymmetric risk. Dismissing a finding that is later exploited is a career-relevant failure, so the incentive is to escalate rather than dismiss — which pushes more work onto development teams and worsens the relationship the security function depends on.

That relationship is the other cost. Security is experienced as the source of tickets about dependencies developers did not choose, and the engineer spends real effort maintaining credibility that the tooling erodes on their behalf.

And the queue regenerates. There is no completion, only a nightly refill, which is exactly the shape of work most associated with burnout.

## What a Solution Looks Like
Automated refutation for the cases that are mechanically determinable. Unreachable code paths, versions outside the affected range, findings duplicated under another identifier, and components not present in the deployed artefact are all determinable without human judgement, and they constitute a large share of the queue.

Dismissals that persist and propagate. An assessment made once should apply to every subsequent scan and, where the reasoning is structural, to every other application in the same situation — which is the difference between a queue and a treadmill.

Deployment context joined automatically, so the engineer is not manually establishing whether a service is internet-facing for the four-hundredth time.

Remediation effort estimated, so the conversation with a development team is a specific proposal — this upgrade is a version bump, that one is a breaking change requiring a day — rather than a ticket.

And the reachability tool's error rate published, because an engineer cannot rely on an automated refutation whose false negative rate is unknown, and that unknown is why most teams still triage manually.

## Impact If Solved
Application security engineers are scarce and spend their capacity refuting findings that a better model would have suppressed. Mechanical refutation with persistent dismissals converts a regenerating queue into a finite list, and returns the specialism to the design and guardrail work that prevents vulnerabilities rather than cataloguing them.
