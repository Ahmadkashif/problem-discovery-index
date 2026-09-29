# Buy: Pricing and Offer Engines Adapted to a Worker's Decision

**Niche:** [[niches/gig-delivery-platforms/offer-construction/profile|Offer Construction & the Accept Decision]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Dynamic pricing and incentive engines are built to move a customer's willingness to pay; here the priced party is a worker deciding whether an hour of their life is worth it.
**Tags:** #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #feature-engineering #compliance #automation #revenue-impact
**Contested on:** Whether pricing infrastructure built for demand-side elasticity can carry a supply-side offer that must also be truthful.

## The Problem

Dynamic pricing, incentive optimisation and offer personalisation are mature commercial disciplines with strong tooling — real-time feature serving, elasticity modelling, constrained optimisation, experimentation platforms and uplift modelling are all available and well understood.

Applied to the supply side of a delivery marketplace, they optimise acceptance probability per dollar of incentive, which is a coherent objective and produces exactly the current state: an offer tuned to be accepted rather than to be accurate. The engine has no representation of whether the offer's stated terms match what the work turns out to be, because in its native domain — a price shown to a customer for a defined product — that question does not arise.

## What Already Exists

Real-time pricing and incentive platforms, feature stores with low-latency serving, uplift and elasticity modelling libraries, constrained optimisation solvers for budget allocation, and experimentation infrastructure capable of running thousands of concurrent offer variants. Every large platform in this industry runs a sophisticated version of this stack and it works.

## The Customization Gap

**The offer is a representation, not just a price.** A price to a customer is an ask. An offer to a courier is a statement about work that has not happened yet, and its accuracy is checkable within the hour. The pipeline needs realised-outcome calibration as a first-class objective alongside acceptance, and no pricing engine has a concept of an offer being *wrong*.

**Net, not gross, and the cost side is the courier's.** Pricing engines optimise the amount paid. The quantity that governs the courier's decision is that amount minus vehicle cost over the actual route, per hour of engaged time. Computing it requires route distance, engaged duration including wait, and a per-courier cost assumption — three inputs the pricing stack does not hold and does not model.

**Wait time is the dominant unmodelled term.** Merchant readiness by store and hour is known to the platform's own operations systems and is typically absent from the pay model's feature set, which is why offers are systematically optimistic in exactly the conditions where they are worst. Joining the merchant-readiness signal into offer construction is an integration the incentive engine does not anticipate.

**Acceptance rate is an outcome of the offer and an input to future offers, and the loop is unmodelled.** A courier who declines bad offers may receive worse ones, which makes acceptance a poor optimisation target and a genuinely unfair one. Modelling that feedback — and deciding deliberately whether acceptance rate should influence allocation at all — is a policy question the tooling silently answers by default.

**Compliance is now a hard constraint, not a reporting layer.** Minimum earnings standards, pay composition disclosure requirements and deactivation protections exist in several jurisdictions and differ between them. The offer engine needs per-jurisdiction constraints enforced at construction time with an auditable record of what was computed and shown, which is a substantially different architecture from an unconstrained optimiser with a reporting dashboard bolted on.

## Target Customer

Marketplace pricing teams at the major platforms, and the regional and vertical delivery operators who license or build on commodity pricing infrastructure. The compliance-driven version has a clearer buyer: whoever owns jurisdictional earnings-standard conformance, who needs the constraint in the engine rather than in a report.

## Impact If Solved

The strong optimisation machinery stays and acquires the constraints that make an offer honest: calibrated against realised outcomes, stated in net terms, including wait, and bounded by jurisdictional minimums at construction time. The observable result is that offers stop being systematically optimistic in precisely the situations where couriers lose money.
