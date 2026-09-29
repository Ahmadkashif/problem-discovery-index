# Three Thousand Recorders Who Never Agreed on What a Property Is

**Niche:** [[niches/real-estate-appraisers/avm-collateral-valuation-analytics/profile|Automated Valuation Models & Collateral Analytics]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The moat is a national property database assembled from thousands of counties with no shared identifier, and it is maintained by people writing rules.
**Tags:** #transformers #graph-neural-networks #word-embeddings #evaluation-metrics #data-integration

## The Problem
There is no national property register. Ownership and transactions are recorded county by county, in thousands of offices with different document types, different formats, different fields and different conventions. Assessor files, which supply characteristics, are maintained by a different set of offices on different cycles with different definitions — one county's finished square footage includes a basement, the next county's does not. Listing data arrives from hundreds of separate MLSs under separate schemas.

Every one of these sources describes properties, and none of them shares an identifier with the others. Building the national picture means resolving them: this deed, this tax parcel, this listing, and this prior sale are the same physical property.

That resolution is the moat and it is done with rules — address standardisation, parcel number matching, fuzzy name comparison, geospatial overlap — maintained by teams that grow with coverage. The rules break constantly, because a county changes its system, renumbers parcels, splits a subdivision, or annexes an area.

The failure modes are quiet and expensive. A missed link loses a property's sale history, so the model values it without knowing what it last sold for. A false link merges two properties, so the model values one house using another's characteristics. Neither announces itself; both simply appear as an inaccurate valuation.

## What Already Exists
Entity resolution and record linkage are mature, with strong open tooling and modern embedding-based approaches that handle textual variation far better than the string-similarity heuristics most of these pipelines were built on. Geospatial matching libraries are excellent. Commercial master data management platforms address the abstract problem.

None fits. Generic entity resolution assumes reasonably consistent record structures and a stable schema. Property records offer neither: the informative content is often in unstructured legal descriptions, the available fields vary by county, and the correct answer depends on how the physical parcel changed over time — a subdivision split is not an error to be reconciled but a real event to be represented.

## The Customization Gap
**Properties have histories, not just identities.** Parcels split, merge, get renumbered, and change address. The right object is a temporal chain, not a single record, and resolving requires deciding whether two records are the same property, a predecessor, or a successor. No general tool models this.

**Legal descriptions are the ground truth and they are prose.** Metes and bounds, lot and block, and subdivision references carry the definitive identity where parcel numbers fail, and extracting structure from them is domain-specific language work over a genre nobody else processes.

**The graph is the disambiguator.** Parcels, addresses, owners, documents, listings and geographies form a graph, and resolution on it is far stronger than field-by-field comparison. Generic products do not model the graph because their domains do not have one.

**Errors must be scored by valuation impact.** Ten thousand unresolved links are not equal; the ones that matter are those on properties being valued, in markets with thin comparables. Ranking by effect on the model's output requires running the model, which only this firm can do.

**County change is the permanent operating condition.** A recorder migrating systems silently changes formats, and a rules pipeline fails without complaint. Drift detection on ingestion, per county, is an operational necessity rather than a refinement.

**Every link must be explainable and reversible.** Valuations support lending decisions that are examined by auditors and regulators, so a resolution decision must be traceable and correctable, which rules out an opaque matching service.

## Target Customer
VP of Data Operations or Head of Property Data at a valuation analytics provider, running a normalisation function whose headcount scales with coverage.

## Impact If Solved
Data assembly is the largest recurring cost in this business and the direct determinant of model accuracy, because a valuation built on a broken sale history or a merged property is wrong for reasons no modelling improvement can fix. Breaking the linear relationship between coverage and headcount is what allows expansion into the thinner counties where competitors' coverage is weakest.
