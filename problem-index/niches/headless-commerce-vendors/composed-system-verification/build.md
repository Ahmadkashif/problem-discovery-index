# Correctness Distributed Across Six Vendors

**Niche:** [[niches/headless-commerce-vendors/composed-system-verification/profile|Composed System Verification]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Composable architecture distributes correctness and performance across six vendors and leaves the customer-visible outcome as nobody's responsibility, which is why every incident begins as a conference call.
**Tags:** #evaluation-metrics #automation #workflow-orchestration #data-integration #confidence-intervals #compliance #graph-theory #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to verify continuously that a system assembled from six vendors produces correct prices, consistent inventory and acceptable performance — and whoever does that takes the category, because the architecture removed the guarantee and nobody replaced it.

## The Problem
A customer sees a price on a product page and is charged a different one at checkout. The product page took its price from the search service's index; the cart took it from the pricing engine; a promotion applied in one and not the other. Six vendors are involved and each of their systems is behaving correctly according to its own contract. The retailer discovers it from a customer complaint, opens a conference call, and spends two days establishing where the divergence arose. Nothing in the architecture was checking that the composition produced a consistent answer, because checking that is nobody's product.

## Why Nobody Has Built This
Verifying a composition means asserting things about components you do not own and cannot fix, which every vendor has treated as a reason not to. The retailer would have to build it and lacks the incentive to build assurance for somebody else's software. The integrator is paid to deliver a working system rather than an assurance capability. And the gap is a consequence of the architecture's central virtue, which makes naming it uncomfortable for the category's advocates.

## What to Build
Verify the composition continuously from the customer's position. Run synthetic customer journeys continuously against production — browse, search, view a product, add to cart, apply a promotion, check out — and assert that the answers agree at every step, which is the verification the architecture removed and is the build; it observes the system as a customer does and therefore owns the outcome nobody else does. Assert consistency explicitly: the price shown equals the price charged, the stock shown is the stock reserved, the promotion applies identically in every surface — since these are the divergences that produce complaints and they are checkable. Contract-test every vendor boundary and run it on every change on either side, which is the preventive half and is standard practice one field over. Measure performance along the customer journey rather than per service, so a slow page has an attributable stage. Detect divergence at the data level by comparing each service's copy of the catalogue and prices, which the consistency niche develops. Attribute failures to a service boundary, which is what turns a conference call into a ticket. Position the verification as independent of any component vendor, since a verifier owned by one participant will not be trusted by the others and independence is the commercial position here. And report a composition health score the retailer can act on, because the retailer is the party who carries the outcome and currently has no instrument.

## Target Customer
Retailers running composable stacks, the vendors in them, the integrators assembling them, and the independent assurance position nobody occupies.

## Impact If Built
The architecture's central virtue produced an accountability vacuum and no participant will fill it because filling it means asserting things about somebody else's software. A continuous synthetic customer journey owns the outcome from the customer's position, which is the only position from which the composition can be judged.
