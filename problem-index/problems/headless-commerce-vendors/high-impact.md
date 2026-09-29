# Nobody Owns the Composed Outcome

**Industry:** [[headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** High Impact
**One-liner:** Composable architecture distributes correctness and performance across six vendors and leaves the customer-visible outcome as nobody's responsibility, which is why every incident begins as a conference call.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #graph-theory #workflow-orchestration #revenue-impact

## The Problem
A composable commerce stack assembles a storefront from independent services: commerce engine, content management, search, pricing, inventory, personalisation, tax, payments, front-end delivery. Each is a separate product with its own vendor, contract, release cycle and support organisation.

The architecture works and the accountability does not. When a product page is slow, the cause is in one of those services or in the composition between them, and each vendor's own monitoring shows their component healthy. When the displayed price differs from the charged price, several services hold pricing information and any could be stale. When inventory shows available and the order fails, the same is true.

The customer sees one experience and there is no party responsible for it. The retailer's own engineering team is nominally accountable and has visibility into their integration code and not into the services beneath it.

Incidents are therefore slow. A peak-traffic failure produces a call with representatives from several vendors, each with partial information, and root cause analysis takes hours during which revenue is lost. Afterwards the finding is frequently an interaction between two services rather than a fault in either, which means no vendor accepts it and it is not fixed.

## Why It's Unsolved
No vendor can own the composed outcome without taking responsibility for components they do not control, and none will. This is a commercial reality rather than a technical gap, and it is why the category has produced better architecture without producing better operations.

Observability stops at vendor boundaries. Distributed tracing exists and requires every participant to propagate context, and vendors implement it inconsistently, so a trace goes dark at the edge of the component you most need to see into.

Correctness verification is genuinely hard in this shape. Determining that the price a customer sees equals the price they are charged requires reasoning across services that each believe they are authoritative, and there is no shared source of truth to check against.

The integrator gap compounds it. Implementation is delivered by systems integrators whose engagement ends, leaving a retailer operating a bespoke composition nobody currently understands well.

And the failure mode is silent for the most damaging class. A price inconsistency does not error; it charges a customer a different amount than they agreed, which surfaces as a complaint or a chargeback rather than as an alert.

## What a Solution Looks Like
Outcome-level synthetic verification, continuously. Automated journeys that browse, add to cart, apply a promotion and reach payment — running constantly against production, checking that prices are consistent at every step, that inventory claims hold, and that pages meet performance thresholds — measure the composed system as a customer experiences it, which is the only level at which it is meaningfully correct.

Cross-service consistency checking on real traffic. Comparing what each service asserted about the same product, price and inventory position at the same moment finds divergence directly, and this is available to whoever sits in the composition layer.

Attribution across boundaries. When outcome-level latency degrades, identifying which service's contribution moved is a straightforward decomposition given trace data, and it converts a six-party call into a routed ticket.

Change correlation. Every vendor releases independently, and correlating outcome degradation against the change log of every component is the single most useful diagnostic in this architecture and requires only that release events be collected.

Contract testing between services, so an upstream change that breaks a downstream assumption is caught before it reaches production.

## Impact If Solved
Composable architecture is the right direction for large retailers and its operational cost is currently paid in slow incidents and silent correctness failures. Verification at the outcome level, with attribution across vendor boundaries, restores what the monolith provided implicitly and is the missing layer that would make the architecture safe to run.
