# Assignment Fitted to Who Actually Converts What

**Niche:** [[niches/crm-platforms/lead-routing-territory-design/profile|Lead Routing & Territory Design]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Representatives differ substantially in which kinds of opportunity they convert, the organisation has thousands of assignments with outcomes attached, and leads are allocated by a geographic rule and a round robin.
**Tags:** #gradient-boosting #logistic-regression #optimization-fundamentals #confidence-intervals #evaluation-metrics #causal-inference #cross-validation #revenue-impact
**Contested on:** Every serious competitor in routing and territory software is fighting to assign a lead or an account to the representative who will actually convert it — and whoever can evidence that a design outperforms the incumbent one takes the account.

## The Problem
A lead arrives from a healthcare organisation of two thousand employees evaluating a compliance use case. It routes to whoever owns that state in the round robin. One representative on the team has closed eleven healthcare deals and knows the regulatory objections; another has closed none and will spend three weeks learning them. The organisation has the record of both. The rule sees a postcode.

## Why Nobody Has Built This
The obstacle is political rather than technical, which is why it has persisted through several generations of perfectly capable routing engines. Assignment determines compensation, so changing it redistributes income, and a system that assigns by fit rather than by territory takes leads away from representatives who currently receive them. Revenue operations will not make that change without evidence, and no product produces the evidence, which is a circularity the category has lived inside for a decade. There is also a genuine fairness dimension: a model that routes by past conversion will concentrate good leads on already-successful representatives, which is both self-reinforcing and unfair to newer people, and needs to be designed against rather than ignored.

## What to Build
A conversion model per representative per opportunity type, and an assignment that optimises against it under explicit fairness and capacity constraints. Fit is estimated from the organisation's own history — which representatives convert which segments, sizes, industries and use cases, with appropriate shrinkage for small samples so a representative with four deals is not credited with a specialism. Capacity enters as a real effect rather than a cap, since conversion degrades with load and the degradation is measurable. Fairness constraints are explicit and configurable: a floor on lead volume per representative, deliberate allocation to developing representatives, and a limit on how concentrated assignment can become — all stated rather than emergent. And the whole thing is evaluated by holding out a portion of assignments to the existing rules, which is the only way to produce the evidence that makes the political change possible and is the reason this must be built as an experiment rather than as a switch.

## Target Customer
Revenue operations organisations at companies with enough lead volume to measure, routing vendors competing on matching sophistication, and the CRM incumbents whose routing is a decision tree.

## Impact If Built
Conversion differences between representatives on the same lead type are large and measurable, and current assignment ignores them almost entirely. The holdout evaluation is the load-bearing part: it produces the number that allows a revenue operations leader to propose a change to a territory settlement, which is the actual blocker and has never had evidence behind it.
