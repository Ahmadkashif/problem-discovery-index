# Entity Resolution and Schema Mapping Off the Shelf

**Niche:** [[niches/agtech-platforms/machine-data-interoperability/profile|Machine Data Interoperability]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reconciling records that describe the same thing under different names and schemas is a solved data engineering discipline, and agricultural machine data is reconciled by a person opening files.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #contrastive-learning #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in mixed-fleet farm software is fighting to assemble one coherent field record from equipment of different brands — and whoever makes a mixed fleet's data reconcile without manual repair takes the account.

## The Problem
Three files describe applications of the same product under three names, with rates in different units, on fields identified by three different naming conventions and three different boundary geometries. Every element of that is a standard data integration problem with mature tooling, and in agriculture it is solved by a person who knows that "Roundup PowerMAX" and the generic glyphosate entry and the custom operator's shorthand are the same thing.

## What Already Exists
Entity resolution, schema matching, record linkage and unit normalisation are mature disciplines with extensive open tooling. Spatial libraries handle boundary geometry, overlap and reconciliation trivially. Product reference data for agricultural chemicals is available from regulatory registration databases, which provide a canonical identity per product with its active ingredients. The ADAPT framework provides a format-level foundation. Every component exists and most are free.

## The Customization Gap
The adaptation is to agriculture's specific entities. It requires: (1) a canonical input catalogue built from regulatory registration data with brand, generic and shorthand aliases, which is the reference set that makes product resolution tractable and which nobody has assembled for this purpose; (2) spatial field reconciliation with agricultural tolerance, since boundaries legitimately differ by a few feet between a GPS-recorded pass and a surveyed boundary and a strict geometric match fails on every field; (3) operation matching across sources using time, location, implement and operation type together, since any one of them alone produces false matches — a fertiliser pass and a spray pass over the same acres on the same day are different operations; (4) unit and rate normalisation with the original preserved, because a conversion error in a rate is a silent and consequential defect; and (5) confidence-gated automation with an exception queue, so the farm office reviews the ambiguous minority rather than reconciling everything.

## Target Customer
Farm management platform vendors, agricultural data service providers, and the larger operations and custom operators who currently employ someone to do this.

## Impact If Solved
The canonical input catalogue is the single highest-leverage piece and is buildable once from public registration data, after which product resolution stops being a per-farm exercise. The rest is standard tooling applied to a domain that has treated a data integration problem as a standards negotiation for twenty years.
