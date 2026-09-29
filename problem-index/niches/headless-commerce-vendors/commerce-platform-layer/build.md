# An Architecture Committee and a Developer

**Niche:** [[niches/headless-commerce-vendors/commerce-platform-layer/profile|Commerce Platform Layer]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One product is sold to an architecture committee on a multi-year licence and adopted for free by a developer choosing a stack, and almost nothing that wins one purchase matters to the other.
**Tags:** #workflow-orchestration #data-integration #evaluation-metrics #compliance #automation #revenue-impact #graph-theory #descriptive-statistics
**Contested on:** Not terminal — the contest differs by whether the buyer is an architecture committee or a developer, and the decomposition is recorded in the profile.

## The Problem
A vendor presents to a retailer's architecture committee and to a development team evaluating options for a smaller build. The committee asks about the data model's extensibility across twelve business units, the scale characteristics under peak, the partner ecosystem's depth in their region, and the contractual position on availability. The developers ask how long it takes to get a storefront running, whether the documentation is any good, and whether they can drop to the raw interface when the abstraction gets in the way. The same product answers both sets partially, and the sales motion that reaches one cannot reach the other.

## Why Nobody Has Built This
The commerce engine genuinely is common, which makes one product look efficient. The enterprise business has revenue per account and the developer business has adoption, and both are attractive. But an enterprise sales motion cannot economically reach a developer, developer-led adoption produces contracts that do not fit an enterprise procurement, and a product designed to satisfy an architecture committee accumulates configuration surface that makes the developer experience worse.

## What to Build
Build the engine properly and let the go-to-market diverge. The genuinely shared substrate is the commerce domain model and its correctness — carts, orders, pricing, promotions, inventory reservation, tax points, currency, returns — and getting that model right is what both buyers actually depend on and what neither evaluates directly. Make the extensibility mechanism first-class rather than a set of hooks, since both audiences need to add behaviour and the current mechanisms are where deployments become unmaintainable — this is the fix note's subject. Keep the interface honest about eventual consistency and transactional boundaries, because both audiences build incorrect assumptions and the resulting bugs are the expensive ones. Version and deprecate properly, since an enterprise deployment lives for years and a developer expects modern cadence, and the same discipline serves both. Expose the domain model's constraints explicitly, so an integrator cannot configure an invalid state. Provide a reference composition and a verified upgrade path, which is the artefact enterprise buyers ask for and developers benefit from. Be explicit about which business the vendor is in, since the mismatch surfaces at renewal for one and at production for the other. And measure developer time-to-first-order and enterprise time-to-go-live separately, because those are the two products' real metrics.

## Target Customer
Platform vendors deciding which business they are in, architecture committees, and the developers who will implement whatever is chosen.

## Impact If Built
The shared substrate is the commerce domain model's correctness, which both buyers depend on and neither evaluates. Making extensibility first-class rather than a hook set is what stops deployments becoming unmaintainable, which is where both businesses actually lose customers.
