# One Field Record From Every Colour of Machine

**Niche:** [[niches/agtech-platforms/machine-data-interoperability/profile|Machine Data Interoperability]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every equipment brand exports its data and several standards exist to unify it, and a farm running mixed colours still cannot assemble one coherent field record without somebody repairing it by hand.
**Tags:** #graph-theory #bert #word-embeddings #k-nearest-neighbors #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in mixed-fleet farm software is fighting to assemble one coherent field record from equipment of different brands — and whoever makes a mixed fleet's data reconcile without manual repair takes the account.

## The Problem
The planter is one brand, the sprayer another, the combine a third, and a custom operator did the fertiliser application with their own equipment and sent a file. Four data sources describing one field's season. The field boundaries do not match — one system has the field as 78 acres and another as 81, with different shapes. The product applied is named three ways. The operation the custom operator recorded does not join to anything. Assembling the season's record is a person in an office reconciling files across a winter, which is exactly the job the farm's records manager describes as their year.

## Why Nobody Has Built This
The manufacturers' commercial interest runs against it: each platform is better with its own equipment and a competitor's data working perfectly inside it removes a reason to standardise on one colour. The standards that exist address the format and leave the semantics — boundaries, product identity, operation matching — to implementers, which is where the actual difficulty lives. And the problem has been framed as a standards problem for two decades, which has kept effort directed at agreement rather than at reconciliation, and agreement has not arrived.

## What to Build
A reconciliation layer that works without the manufacturers' cooperation. Field identity is resolved geometrically, matching boundaries across systems by spatial overlap with a canonical boundary maintained per farm and the discrepancies reported rather than silently resolved. Product identity is resolved against a canonical input catalogue, since the same chemical under three brand names is an entity resolution problem with abundant reference data. Operations are matched across sources by time, location, equipment and operation type, so a pass recorded twice becomes one event and a custom operator's record joins to the farm's field. Units and rates are normalised with the conversion recorded. Every reconciliation carries a confidence, and the output includes a data quality report per field per season — what reconciled cleanly, what was inferred, what remains unmatched — which is the artefact that tells a grower how much of their record they can actually rely on and which nobody currently provides.

## Target Customer
Growers running mixed fleets, which is the majority of substantial operations; the brand-independent platforms for whom this is the core value proposition; and the custom operators and agronomists who exchange data with many farms.

## Impact If Built
A coherent field record is the precondition for every analytical capability in this industry — the on-farm trials, the input effect estimates, the sustainability reporting — and it is currently assembled by hand or not at all. Removing the winter reconciliation is a direct labour saving for the farm office and, more importantly, it converts a partial record into one that supports analysis.
