# The Engineering Change Loop Closed Into Sourcing

**Niche:** [[niches/procurement-spend-platforms/direct-materials-procurement/profile|Direct Materials Procurement]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engineering change to a part has consequences for inventory, supplier qualification, tooling and cost, and it reaches the sourcing team as an email with a revised drawing attached.
**Tags:** #graph-theory #data-integration #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #revenue-impact #compliance
**Contested on:** Every serious competitor in direct materials software is fighting to get an engineering change into sourcing before it reaches production — and whoever closes the loop between design and supply takes the manufacturer.

## The Problem
An engineer revises a part to correct a fit problem. The change is approved in the engineering system and released. Sourcing learns about it when the buyer notices a new revision on a drawing, by which time eleven thousand units of the previous revision are on order or in stock, the supplier's tooling produces the old geometry, the requalification will take six weeks, and the change was scheduled to take effect in production in three. Somebody now manages an obsolescence write-off, an expedited requalification and a temporary dual-running arrangement, all of which were avoidable with two weeks of notice.

## Why Nobody Has Built This
The engineering system and the procurement system have different owners, different data models and frequently different vendors, and the change process was designed around engineering release rather than around supply consequence. Connecting them requires modelling the dependency from a part revision to every downstream commitment — open orders, inventory, tooling, qualification, supplier agreements — which crosses three systems. And the organisational structure reinforces it: engineering's change board assesses technical and regulatory impact, and supply impact is represented by whoever from operations happens to attend.

## What to Build
A supply impact assessment generated automatically at change proposal, before approval. The moment a change is proposed, the system computes what it touches: open purchase orders and their cancellation terms, inventory on hand and in transit with its obsolescence exposure, tooling affected and who owns it, supplier qualification status and requalification lead time, and the cost delta from a should-cost comparison. That assessment goes to the change board as a document rather than as a person's recollection, which is the whole point — the decision to approve a change is currently made with the engineering consequence quantified and the supply consequence estimated. On approval it becomes a sourcing work plan with the requalification, tooling and phase-out sequenced against the production effective date, which is what determines whether the change lands cleanly. And the effective date itself becomes negotiable on evidence: an engineering change board that can see a six-week requalification will set a date that accommodates it.

## Target Customer
Manufacturers of any scale with engineered products, product lifecycle management and procurement vendors on either side of the gap, and the contract manufacturers who absorb the consequences of their customers' changes.

## Impact If Built
Engineering change is the largest recurring source of obsolescence, expedite cost and supply disruption in discrete manufacturing, and the supply consequence is currently assessed after the decision rather than before it. Producing the impact assessment at proposal changes what the change board is deciding on, which is the intervention point, and it is computable from systems the manufacturer already runs.
