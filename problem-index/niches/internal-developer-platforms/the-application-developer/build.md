# Discovering the Boundary by Hitting It

**Niche:** [[niches/internal-developer-platforms/the-application-developer/profile|The Application Developer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Application developers learn what the platform supports by attempting something and failing, because the abstraction hides the underlying system right up until the moment it leaks.
**Tags:** #graph-theory #bert #descriptive-statistics #large-language-models #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a developer find out what the platform supports before they build on the assumption that it does — and whoever does that takes the adoption, because discovery by failure is why developers route around.

## The Problem
A developer designs a service that needs a scheduled job with a particular concurrency behaviour. The platform's documentation covers scheduled jobs. They build it, deploy it, and discover that the platform's scheduler does not support the behaviour they need — a fact that was known to the platform team, is not written anywhere, and was discoverable only by attempting it. They have now spent two days on a design that does not work. Their next service will be built without the platform, and they will tell their colleagues, and the platform team will record two fewer adoptions with no reason attached.

## Why Nobody Has Built This
Documentation is written to describe what the platform does, which is the natural framing and omits the boundary — and the boundary is the information a developer needs before committing. The capability set is known to the platform team implicitly and has never been enumerated, because enumerating it means writing down limitations, which is uncomfortable and feels like advertising weakness. Errors are written by engineers debugging their own system rather than for a developer encountering a wall. And the platform has no mechanism to answer a hypothetical question, which is what a developer actually wants to ask.

## What to Build
State the boundary and let it be queried. Enumerate the capability surface explicitly — what the platform supports, with what parameters, within what limits, and what it does not support — which is the artefact that does not exist and is the whole niche. Publish the limitations as prominently as the capabilities, since a developer who knows what the platform cannot do will design around it rather than discovering it, and the honesty is what earns the trust that produces adoption. Let a developer ask before building: a query interface, in the portal and in the tooling, that answers whether a described need is supported and what the alternative is — which is the support channel's most common question answered without a human. Validate a proposed design against the capability surface, which catches the mismatch at design time rather than at deployment. Tell the developer at the point of attempt rather than at the point of failure, which is a check in the tooling rather than an error at runtime. Record every question the boundary could not answer and every attempt that hit it, feeding the gap capture from the provisioning niche. And treat the boundary as a published contract that changes with notice, since a capability that disappears silently is worse than one that was never offered.

## Target Customer
Platform engineering teams, platform tooling vendors, and the application developers currently routing around a platform they cannot predict.

## Impact If Built
Discovery by failure is the mechanism by which developers decide to route around, and the information required to prevent it is known to the platform team and written nowhere. A queryable capability surface answers the support channel's most common question and catches the mismatch at design time.
