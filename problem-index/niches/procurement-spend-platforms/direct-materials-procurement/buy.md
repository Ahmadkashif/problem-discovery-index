# Should-Cost Modelling Brought Below the Enterprise Tier

**Niche:** [[niches/procurement-spend-platforms/direct-materials-procurement/profile|Direct Materials Procurement]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Computing what a manufactured part ought to cost from its material, geometry, process and volume is an established discipline with commercial tooling, and it is available to large manufacturers and to nobody else.
**Tags:** #linear-regression #gradient-boosting #numerical-methods #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact #feature-engineering
**Contested on:** Every serious competitor in direct materials software is fighting to get an engineering change into sourcing before it reaches production — and whoever closes the loop between design and supply takes the manufacturer.

## The Problem
A buyer receives a quote for a machined component. Whether it is a good price depends on the material cost, the machine time the geometry implies, the setup and tooling amortisation at the quoted volume, the finishing operations and a reasonable margin — which a should-cost model computes and which most buyers do not have. Without it the negotiation reference is the previous price or the second quote, both of which may be equally high. Large manufacturers run should-cost teams; everyone else negotiates on comparison.

## What Already Exists
Should-cost and design-for-cost modelling is an established discipline with commercial software — the cost engineering tools used in automotive and aerospace — and a substantial methodology literature. Material price indices are published and commercially available. Machining time estimation from geometry is a developed capability within manufacturing simulation and quoting software. Contract manufacturer quoting platforms compute something very like this to price their own work. Every component exists, packaged for large organisations or for the supply side rather than for the buy side.

## The Customization Gap
The adaptation is to a buyer without a cost engineering function. It requires: (1) cost model construction from the part's own data — material, mass, geometry where a model is available, process route — rather than from a cost engineer's build-up, which is what makes it usable without a specialist; (2) regional and supplier-tier factors, since the same part costs differently by geography and by the kind of supplier making it, and a single global estimate is not a negotiating position; (3) live material indices so the estimate moves with commodity prices, which is also the basis for a material-linked price adjustment clause that many buyers should have and do not; (4) uncertainty stated plainly, because a should-cost estimate presented as precise will be discredited by the first supplier who explains why their process differs, and a range with the assumptions listed is both more honest and more defensible in a negotiation; and (5) the output framed as a conversation opener rather than a target, since the productive use is asking a supplier why their price differs from the model rather than demanding the model's number.

## Target Customer
Mid-market manufacturers without cost engineering functions, procurement platforms serving direct materials, and the contract manufacturers who already compute this from the other side.

## Impact If Solved
Should-cost transforms a direct materials negotiation from a comparison of quotes into an examination of cost structure, which is the difference between buying the lowest offer and understanding the price. Bringing it below the enterprise tier is a packaging problem, and the material-index linkage is a second benefit that most mid-market buyers have never had access to.
