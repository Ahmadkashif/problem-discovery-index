# Machine Data Interoperability

**Parent Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in mixed-fleet farm software is fighting to assemble one coherent field record from equipment of different brands — and whoever makes a mixed fleet's data reconcile without manual repair takes the account.

## Profile
**Market Size:** ~$410M US spend attributable to data integration within farm management platforms
**Share of Parent Industry:** ~10% of agtech revenue, gating most of the rest
**Digital Adoption:** Medium — data is collected universally and reconciled partially
**Target Buyer:** Product leads at the platforms; growers running equipment from more than one manufacturer, which is most of them
**Automation Potential:** Very High — this is schema and entity reconciliation with published standards available

## What Makes This a Distinct Niche
A farm running a green combine, a red tractor and a third brand's sprayer generates three data streams that do not reconcile. Field boundaries differ between systems. Product names differ. Units differ. Operations recorded by one machine do not join to operations recorded by another on the same acres. The consequence is that the farm cannot assemble a coherent record of what happened on a field in a season without somebody fixing it by hand, which is the winter work of the farm office described in this industry's own problem notes. Standards exist — ISOBUS and ADAPT among them — and are implemented partially and inconsistently, and the manufacturers have limited commercial interest in making a competitor's data work well inside their own platform. Two decades of this have produced an industry where the best-instrumented farms have the least usable records.

## Current Tools & Gaps
John Deere Operations Center, Climate FieldView, Trimble and AGCO all import competitor data with varying fidelity. Third-party translation services and consultants exist. The ADAPT framework was created specifically for this problem and has partial adoption. The gaps: field boundary reconciliation across systems is manual, which is the foundational join and the one that breaks everything downstream; product and input naming has no canonical vocabulary, so the same chemical appears under several names; unit and rate conventions differ; and operation matching — recognising that the same pass is recorded twice by two machines, or that a custom operator's record and the farm's own record describe one event — is entirely manual. Nobody reports the reconciliation quality, so a grower does not know how much of their record is sound.

## Problems
- [[niches/agtech-platforms/machine-data-interoperability/build|🔨 Build: One Field Record From Every Colour of Machine]]
- [[niches/agtech-platforms/machine-data-interoperability/buy|🛒 Buy: Entity Resolution and Schema Mapping Off the Shelf]]
- [[niches/agtech-platforms/machine-data-interoperability/fix|🔧 Fix: Field Boundaries That Disagree Between Systems]]
