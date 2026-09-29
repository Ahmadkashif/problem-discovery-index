# Scope Determination as a Maintained Model, Not a Consulting Opinion

**Niche:** [[niches/food-distributors/food-traceability-compliance-services/profile|Food Traceability Compliance Services]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a given product at a given step falls under the traceability rule is a judgment made per client by a specialist, and the same judgment is being made independently thousands of times across the industry.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #evaluation-metrics #feature-engineering #compliance #data-integration #revenue-impact

## The Problem
The rule applies to a defined list of foods and to specified events in their handling, and neither the list nor the events map cleanly onto how a distributor's catalogue is actually organized. Whether a particular item is in scope depends on its composition, its form, and what happens to it at each step — and the answer changes when a product is transformed, commingled, or repacked. Specialists work it out per client, product family by product family, from the regulation and from accumulated interpretation. The reasoning lives in engagement deliverables. So the same determinations are made independently across every client, the firm cannot say whether its own specialists reach consistent answers on comparable products, and when a regulator questions a scope decision the defence is reconstructed.

## Why Nobody Has Built This
The rule is recent and interpretation is still settling, which has made everyone reluctant to codify what is genuinely unsettled. Scope determination is also a professional judgment carrying liability, and firms have been careful to keep it as advice rather than as a system output. And engagements are delivered under compliance-date pressure, where building reusable structure loses to shipping the current client.

## What to Build
A scope model expressed as structured rules over product attributes and handling events, rather than as prose per engagement. Each determination records the product characteristics relied on, the events in the flow, the rule provisions applied, and the specialist's confidence — captured as the work is done. Across clients that produces a maintained interpretation layer: a new client's catalogue is scoped against accumulated determinations rather than from the regulation, with genuinely novel products routed to a specialist and everything resembling a prior determination proposed with its precedent attached. Where regulators or investigators have accepted or challenged a scope position, that outcome attaches to the determination — which is the highest-value field, because it is the only evidence anyone has about what the rule means in practice. Consistency becomes measurable for the first time, which matters in a service whose value is that the answer is defensible.

## Target Customer
VPs of regulatory services at traceability providers running 50-300 specialists, and the food safety leaders at distributors who receive scope opinions they cannot themselves verify.

## Impact If Built
Turns per-engagement judgment into a maintained interpretation asset in a domain where the interpretation is still forming — which is exactly when accumulating it is most valuable and least contested. It also makes the service scale past specialist headcount, which is the current constraint as compliance dates arrive.
