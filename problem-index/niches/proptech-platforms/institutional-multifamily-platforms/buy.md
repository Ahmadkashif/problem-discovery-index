# Revenue Management Methods From Airlines and Hotels

**Niche:** [[niches/proptech-platforms/institutional-multifamily-platforms/profile|Institutional Multifamily Platforms]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines and hotels have practised single-operator revenue management for forty years using their own demand data, with a deep published literature and mature commercial systems, and multifamily reached for a competitor price feed instead.
**Tags:** #dynamic-programming #bayesian-inference #time-series-forecasting #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact #compliance
**Contested on:** Every serious competitor in multifamily revenue management is now fighting to price a unit well using only what one operator legitimately knows about its own demand — and whoever prices accurately without pooled competitor data takes the market.

## The Problem
The problem multifamily faces — perishable inventory, a booking curve, demand that varies by season and segment, and a price decision that trades revenue against the risk of the unit going unsold — is the canonical revenue management problem. Airlines solved its structure in the 1980s. Hotels followed. Both did it primarily with their own historical demand, forecasting and optimisation, with competitor rates as a minor input where available at all. Multifamily built its practice on the competitor input as the primary signal and under-developed everything else.

## What Already Exists
Revenue management is a mature academic and commercial discipline: demand forecasting under censoring, price-response estimation, dynamic pricing under capacity constraints, overbooking and displacement analysis, and unconstraining — recovering true demand from observed bookings when inventory sold out — are all thoroughly developed with published methods and mature implementations. Hospitality revenue management systems are purchasable. The transfer is unusually direct.

## The Customization Gap
The adaptation is to a lease rather than a night. It requires: (1) modelling lease term as a decision variable alongside price, since a twelve-month and a fifteen-month lease at the same rent have different values depending on when they expire relative to the operator's seasonal demand — expiration management is multifamily's version of network revenue management and is largely unexploited; (2) unconstraining applied to enquiry data, since an operator only observes enquiries at the price it set and the demand at other prices is censored, which is exactly the problem hospitality developed methods for; (3) renewal as a distinct decision from new lease pricing, with the resident's own history, tenure and prior acceptance as the evidence — there is no hospitality analogue and it is where most of the money is; (4) vacancy and turn cost as the true opportunity cost rather than a rule-of-thumb, including the turn work the unit will need; and (5) strict first-party data discipline, which is a constraint hospitality never had and which must be architectural rather than a policy.

## Target Customer
Institutional multifamily operators and the platform vendors rebuilding revenue management under a first-party constraint.

## Impact If Solved
Importing forty years of single-operator revenue management practice is far faster than rediscovering it, and it arrives with the censoring and endogeneity problems already solved. Lease expiration management in particular is a well-understood technique in hospitality that multifamily barely uses, and it improves portfolio revenue without touching price at all.
