# The Mechanism: What MRP Computes, and What Kanban Refuses To

**Origin:** [[origins/auto-oems/profile|Auto OEMs]]
**Tags:** #optimization-fundamentals #matrix-algebra #time-series-forecasting #dynamic-programming #workflow-orchestration #automation #data-integration #evaluation-metrics

## MRP: Explode the Plan

MRP takes three inputs and produces one output: a dated list of what to order or make, and when.

1. **The master production schedule** — how many finished vehicles, of which configuration, on which date. This part is, unavoidably, a forecast.
2. **The bill of materials (BOM)** — the exact parts tree for each configuration: this vehicle needs four of this bracket, one of this harness, which itself needs three of this connector.
3. **Inventory and open-order records** — what is already on hand or already ordered, to be netted off.

The computation — **BOM explosion** — multiplies the schedule down through the parts tree (structurally, a matrix multiplication against the bill-of-materials relationships) and nets against on-hand inventory, then offsets each resulting requirement backward by the part's lead time to get an order-release date. Run this for every part, every level of the tree, every week, and you have a plan. This is why it needed a computer: not because the arithmetic is hard, but because a mid-sized vehicle's BOM has tens of thousands of lines and the plan must be re-exploded every time the schedule, the BOM or the inventory changes — which is constantly.

**MRP II (1983)** closed a loop the original method left open: capacity. A materials plan that ignores whether the machine or the labour hour actually exists to execute it is a wish, not a plan. Wight's extension added capacity requirements planning, rough-cut capacity checks against the schedule, and eventually financial integration, turning MRP from a parts-ordering tool into what a modern ERP system still resembles.

## Kanban: Let the Floor Decide

Kanban has no forecast step at all. A card (or, today, an electronic signal) represents authorisation to produce or move exactly one standard container of parts. A station produces only when it receives a card; a card is only issued when the downstream station consumes a container. **Work-in-process is capped by the number of cards in circulation**, full stop — there is no plan to be wrong about, because nothing is planned more than one container ahead.

## Why "They're the Same Idea" Is Wrong

They optimise for different things and fail in different ways:

- **MRP is confidently wrong at scale.** A bad forecast propagates through the entire exploded plan and produces a large, precisely calculated, incorrect order list — the software will not tell you it is wrong, because from its own inputs it isn't. This is the classic **bullwhip effect**: small forecast error at the top of the tree becomes large inventory swings further down it.
- **Kanban is locally self-correcting but structurally rigid.** It has no bullwhip because it has no forecast to be wrong about — but it assumes stable, low-mix, low-variability production with reliable suppliers close enough to replenish fast. It does not natively handle a build schedule that swings wildly between configurations, and it depends on **jidoka** — stopping the line the instant a defect appears — which is an organisational commitment, not a software feature.

**The algorithm was never the scarce resource in either lineage. The scarce resource was the willingness to run the floor the way the method required** — continuous re-exploded planning discipline for MRP, or stop-the-line authority for every worker under kanban. Both are organisational costs disguised as technical ones.

## The Transferable Pattern

> **A push system computes an answer from a belief about the future and commits resources to it before reality arrives. A pull system commits nothing until reality asks for it.** Every planning problem in this vault — staffing, procurement, capacity, even model retraining cadence — is one or the other, and the two require different failure-handling entirely: a push system needs to detect when its forecast has gone stale; a pull system needs enough slack in the chain to actually respond in time.

**Sources:** Wikipedia, *Material requirements planning*; QAD, *Joseph Orlicky: Hero of Material Requirements Planning*; Toyota Global, *75 Years of Toyota*; ProjectManager, *Kanban History*.
