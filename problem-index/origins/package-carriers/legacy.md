# Legacy: What Package Carriers Bequeathed

**Origin:** [[origins/package-carriers/profile|Package Carriers]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/last-mile-delivery|Last-Mile Delivery]] | ORION's actual product, sold downmarket: Route4Me, OptimoRoute and Circuit are this origin's sequencing-and-reoptimisation logic, packaged for operators far smaller than UPS. The tracking number COSMOS invented as a customer-facing product in 1979 is now the baseline expectation for every DSP and independent courier in this vault's note for the industry. |
| [[industries/freight-brokerage|Freight Brokerage]] | The half of this origin that didn't transfer: package-level visibility, solved in 1979, has no equivalent at the pallet or truckload level here. This vault's own note for the industry describes load boards and spot-rate data with no comparable real-time tracking layer — the parent solved this problem for parcels forty-plus years before the child solved it for freight, and in many respects still hasn't. |
| [[industries/warehouse-3pl|Warehouse & 3PL]] | The barcode-scan lineage directly: SuperTracker's 1986 handheld scan-at-every-handoff logic is the ancestor of every pick-scan step in a modern WMS (3PL Central, ShipBob, Manhattan Associates). The scanning hardware changed; the principle — read the item at every state transition, write it back to one authoritative system — did not. |
| [[industries/owner-operator-trucking|Owner-Operator Trucking]] | The starkest contrast in this file: ORION solves, at national scale and for UPS's own employees, exactly the problem — which stops to take, in which order, at what true cost — that this vault's note for owner-operators describes individual drivers solving by "intuitive feel," on spreadsheets, load by load. The optimisation this origin proved works at scale has never reached the atomised, single-truck segment of the same industry. |
| [[industries/ecommerce-sellers|E-Commerce Sellers]] | The tracking number as an inherited customer expectation, not an inherited economic view: this vault's note for the industry describes sellers unable to calculate true per-SKU profitability because freight and fulfilment costs are fragmented across carriers. COSMOS solved "where is it" in 1979; nobody in this chain has solved "what did it actually cost to get there," which is the same missing-join pattern this vault's retail-banking origin describes for payments. |

## The Second Inheritance: publicity is not superiority

FedEx and UPS run comparable internal optimisation; ORION is publicly documented chiefly because UPS pursued the INFORMS Edelman Award process and FedEx, as a rule, does not publicise its equivalent systems to the same degree. **An FDE reading the trade press should not conclude UPS's routing is better than FedEx's — only that UPS's is better advertised.** The same caution applies broadly: public case studies are a biased sample of what companies are willing to say, not a ranking of what companies actually do.

## What an Episode Should Take From This

1. **The network topology came before the tracking system, and the tracking system came before the optimisation — each one waited for the one before it to become ordinary first.** Hub-and-spoke (1973) is not COSMOS (1979) is not ORION (2013): forty years separate the founding bet from the fully realised optimisation built on top of it.
2. **A famous heuristic and the real system are frequently not the same thing**, and the gap between them is where a good episode lives — "no left turns" predates ORION and is a minor input into it, not its core.
3. **This origin's fight ended in a duopoly, not a corpse, and that itself is the lesson**: capital can replicate a network design in a way it structurally cannot replicate an algorithmic capability gap. Compare directly against [[origins/airlines/the-fight|Airlines' fight]], where it could not.

**Sources:** See [[origins/package-carriers/the-mechanism|The Mechanism]] and [[origins/package-carriers/the-fight|The Fight]] for full citations; this vault's `industries/last-mile-delivery.md`, `industries/freight-brokerage.md`, `industries/warehouse-3pl.md`, `industries/owner-operator-trucking.md`, `industries/ecommerce-sellers.md` and their problem notes.
