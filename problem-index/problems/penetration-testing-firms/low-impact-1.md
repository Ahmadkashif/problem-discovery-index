# Scoping Against an Unknown Attack Surface

**Industry:** [[penetration-testing-firms|Penetration Testing Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The engagement is scoped and priced before anyone has looked, from an asset list the client compiled by asking around.
**Tags:** #graph-neural-networks #gradient-boosting #bert #k-nearest-neighbors #confidence-intervals #evaluation-metrics #feature-engineering #change-point-detection

## The Problem
Scoping happens first. The client describes the system, provides an asset inventory and a rough sense of complexity, and the firm quotes days. Both parties then discover during the engagement that the inventory was incomplete — a forgotten subdomain, an acquired company's infrastructure, a third-party integration nobody mentioned, an API with more endpoints than documented.

Client inventories are unreliable for structural reasons rather than negligence. Cloud resources are created by teams outside any central register, acquisitions bring estates nobody has mapped, and the boundary between what the organisation owns and what a supplier runs is frequently unclear to the people answering the question.

The estimation error runs both ways. An under-scoped engagement means the tester runs out of time with the interesting parts unexamined, which is exactly the coverage problem. An over-scoped one means the client pays for days spent on a smaller surface than expected, which erodes trust.

And the scoping conversation is conducted by salespeople and engagement managers rather than by testers, which introduces a further gap between the estimate and the reality.

## What Already Exists
Attack surface management vendors — external asset discovery, subdomain enumeration, certificate transparency monitoring, cloud asset inventory — are a mature adjacent category. Reconnaissance tooling is standard in the tester's own kit and is used after the engagement starts. Asset inventories exist in configuration management databases of variable accuracy. Some testing firms run a short discovery phase before quoting, usually unpaid. Penetration testing as a service platforms have structured scoping templates.

## The Customisation Gap
Discovery belongs before the quote and is currently done after the contract. Running external attack surface discovery at scoping time — passively, from public sources, before any engagement — gives both parties a real picture of the surface and turns a negotiation over an asset list into a conversation about a map. The tooling exists and is sold to defenders rather than used by testers at the point where it would change the commercial outcome.

Effort estimation from surface characteristics is the second gap and is the same shape as estimation problems across every services business in this vault. A firm with thousands of completed engagements can relate measurable surface properties — endpoint counts, technology stack, authentication complexity, integration count, framework and version profile — to the days actually consumed and the findings actually produced, and nobody has built it.

Estimating what a given scope will find is the more interesting version. If the firm can say that engagements against this kind of surface typically yield a given number of findings at given severities, then the quote is a conversation about expected value rather than about days, which changes what the client is buying.

And drift matters between engagements. A client tested annually has a surface that changed all year, and detecting what is new since the last engagement is the natural basis for scoping the next one — a continuity no annual-engagement model currently provides.

## Impact If Solved
Scoping error produces both the coverage failures that make reports misleading and the trust failures that make clients feel oversold. Discovery before quoting, effort estimation from measured surface characteristics, and a finding-yield expectation would make the commercial conversation honest — and surface drift detection between engagements turns a series of disconnected annual tests into something closer to continuous assurance.
