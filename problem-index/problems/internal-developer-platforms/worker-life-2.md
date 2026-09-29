# Discovering the Platform by Hitting Its Edges

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Type:** Worker Life Changing
**One-liner:** Application developers learn what the platform supports by attempting something and failing, because the abstraction hides the underlying system right up until the moment it leaks.
**Tags:** #large-language-models #bert #gradient-boosting #k-nearest-neighbors #evaluation-metrics #automation #workflow-orchestration #worker-facing

## The Problem
An application developer wants to do something ordinary: add a background worker, connect to a queue, run a scheduled job, expose a new endpoint, increase a memory limit.

The platform may support it directly, support it with a configuration they cannot find, support it only through a request to the platform team, or not support it at all. There is rarely a way to know in advance. So the developer tries, hits an error message written for a platform engineer, and either finds a workaround or asks in the channel.

The error messages are the specific problem. Platform abstractions leak at their edges, and when they do the developer receives a message from the underlying system — a Kubernetes admission controller, a Terraform provider, an IAM policy evaluation — that assumes knowledge of exactly the layer the platform exists to hide.

This produces a familiar reaction. Developers conclude that the platform is obstructive, and start routing around it, which the platform team experiences as poor adoption and attributes to resistance to standards.

## Why It Matters to the Worker
Being unable to determine what is possible without attempting it is a poor working experience, and it is intermittent enough to be difficult to plan around. A task estimated at an hour becomes a day because it turned out to require a platform team request with its own queue.

The error messages are actively demoralising. Receiving a low-level failure from a system you were told you did not need to understand is the abstraction breaking its promise, and it happens at the moment of highest frustration.

There is also a status dimension. Asking the platform team for something the platform does not support puts the developer in the position of requesting a favour, repeatedly, for work they consider ordinary. Over time this shapes what they attempt, which means the platform is quietly constraining engineering decisions in ways nobody has evaluated.

## What a Solution Looks Like
Capability discovery before the attempt. A developer should be able to find out what the platform supports for their service, in their environment, at their access level, without trying it — which is a documentation and interface problem the category has largely neglected in favour of provisioning.

Error translation at the boundary. When an underlying system rejects something, the message reaching the developer should be expressed in the platform's own terms with the actual remedy, and the mapping from low-level failure to platform-level explanation is a finite, learnable set.

Self-service paths for the common requests. The requests that regularly reach the platform team are enumerable, and the ones that are routine should be automated with policy checks rather than queued for a human.

Precedent surfacing: another team has almost certainly done this before, and showing how they did it is more useful than any documentation page.

And the constraint made explicit. Where something genuinely is not supported, saying so clearly with the reason and the alternative is far better than an error, and it lets the developer plan rather than discover.

## Impact If Solved
Developers experience the platform as a set of edges they discover by hitting them, which is why they route around it and why platform teams misread that as resistance. Capability discovery and error translation address the actual cause, and both are interface work on information the platform already has.
