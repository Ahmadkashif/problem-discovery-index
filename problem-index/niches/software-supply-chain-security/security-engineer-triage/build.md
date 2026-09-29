# Establishing That It Does Not Apply, Nightly

**Niche:** [[niches/software-supply-chain-security/security-engineer-triage/profile|The Security Engineer]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Application security engineers spend their weeks establishing that findings do not apply, one at a time, in a queue the scanner regenerates every night.
**Tags:** #graph-theory #bert #k-means-clustering #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop an application security engineer establishing that findings do not apply, one at a time, in a queue the scanner regenerates nightly — and whoever does that takes the function, because that is currently the job.

## The Problem
An engineer opens the queue on Monday. Four hundred findings. They work through them: this one is in a test-only dependency, this one requires a configuration the service does not use, this one is in a code path the application never reaches, this one is genuinely applicable and becomes a ticket. By Thursday they have made three hundred and eighty determinations, of which perhaps two hundred are identical to determinations somebody in the organisation made before, and of which most will be regenerated when the scan next runs against a patched version of the same component. The threat modelling work that would reduce next quarter's inflow was not started.

## Why Nobody Has Built This
The tooling was built around the scanner's output, which is a list, so the workflow is a list to be processed. Determinations are treated as annotations on findings rather than as knowledge about components, which is why they do not transfer to the next service or survive the next version. Nothing proposes a determination from prior identical ones, although the prior determinations exist and the components are the same. And the function is resourced against the queue, which makes headcount the response to volume and guarantees the preventive work is never reached.

## What to Build
Make determinations reusable knowledge rather than per-finding annotations. Record each determination against the component, the usage pattern and the reasoning rather than against the finding instance, so it applies to every other service using the component the same way and survives a version change where the reasoning still holds — which is the change that eliminates most of the repeat work. Propose determinations from prior identical assessments, with the reasoning shown for confirmation, which turns a forty-minute analysis into a thirty-second review for the large repeat share. Cluster the queue so identical determinations are made once across every affected service rather than per service. Detect when a prior determination no longer holds — the code path is now reached, the configuration changed — and resurface only those, which is the safety property that makes reuse acceptable. Adopt the portable exploitability exchange formats so determinations move between tools and between organisations, since the same open-source component is assessed independently by thousands of security teams. Report the queue's composition — repeat, novel, and genuinely applicable — which is the number that shows how much of the function's capacity is lookup. And protect time for the preventive work explicitly, because the queue will otherwise consume all of it.

## Target Customer
Application security leadership, the engineers carrying the queue, and the vulnerability management vendors whose products organise the queue rather than reducing it.

## Impact If Built
The determinations are expert work, are repeated across services and versions, and are discarded — which is the waste at the centre of this function. Recording them against the component and usage rather than the finding makes them reusable, and resurfacing only when the reasoning stops holding is what makes reuse safe.
