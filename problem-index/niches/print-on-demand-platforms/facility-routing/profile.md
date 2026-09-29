# Facility Routing

**Parent Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to send each order to the facility that will produce it well rather than the one that is nearest — and whoever does that takes the quality, because quality is the variable the routing decision currently omits.

## Profile
**Market Size:** ~$620M US
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Low — distance and capacity, not quality
**Target Buyer:** Network operations
**Automation Potential:** Very High — this is a multi-objective assignment problem

## What Makes This a Distinct Niche
Routing engines that assign orders to facilities by distance and capacity are standard, and the variable that determines whether the customer is happy — which facility prints this kind of work well — is not in the routing decision. The platform knows, from its own history, that facility A produces dark-substrate direct-to-garment work with a two percent reprint rate and facility B with nine percent, and routes by whichever is closer to the customer. The routing decision is the single lever that connects the platform's accumulated quality knowledge to the individual order, it is made hundreds of thousands of times a day, and it uses two of the four variables that matter.

## Current Tools & Gaps
Rules and optimisation on distance, capacity, capability flags and cost. The gaps: facility quality by work type is not a routing input despite being recorded; capability is a binary flag rather than a measured competence; the trade-off between shipping speed and reprint probability is not quantified; routing does not learn from outcomes; and no facility receives quality-based volume consequences.

## Problems
- [[niches/print-on-demand-platforms/facility-routing/build|🔨 Build: Routing on Distance, Not on Who Prints It Well]]
- [[niches/print-on-demand-platforms/facility-routing/buy|🛒 Buy: Assignment Optimisation and Supplier Scorecards]]
- [[niches/print-on-demand-platforms/facility-routing/fix|🔧 Fix: Capability as a Checkbox]]
