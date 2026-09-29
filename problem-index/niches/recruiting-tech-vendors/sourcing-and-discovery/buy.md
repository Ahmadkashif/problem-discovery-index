# Buy: Search Infrastructure Adapted to Careers Described Differently

**Niche:** [[niches/recruiting-tech-vendors/sourcing-and-discovery/profile|Sourcing & Candidate Discovery]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Semantic search and retrieval infrastructure is commodity; the domain problem is that two people with identical capability describe it with no overlapping words.
**Tags:** #word-embeddings #transformers #large-language-models #evaluation-metrics #confidence-intervals #data-integration #automation #k-nearest-neighbors
**Contested on:** Whether general semantic retrieval closes a vocabulary gap this specific without domain modelling.

## The Problem

Search infrastructure is abundant and good. Vector databases, embedding models, hybrid retrieval combining lexical and semantic matching, reranking and query understanding are all available, cheap and well documented, and a sourcing vendor can deploy a competent semantic search quickly.

Applied to resumes and profiles it improves on boolean matching and does not solve the problem. General-purpose embeddings place a profile near text that resembles it, and the whole difficulty is that equivalent capability frequently resembles nothing — a military logistics role and a warehouse operations role, a teacher and a corporate trainer, an academic and a data scientist, described in vocabularies with almost no lexical or semantic overlap in a general model.

## What Already Exists

Vector databases and embedding models. Hybrid retrieval frameworks. Reranking models. Resume parsing and entity extraction. Occupational taxonomies — O*NET, ESCO and their skill mappings. Profile data aggregators. Job description parsing. All of it deployable.

## The Customization Gap

**Equivalence is a domain fact, not a semantic similarity.** Two roles requiring the same capability with no vocabulary overlap need a capability layer between them — extraction into a shared representation — rather than a better embedding. Occupational taxonomies partially encode this and are too coarse for real matching, so the mapping is domain work.

**The profile is a self-presentation, not a description.** Resumes are marketing documents with inflation, omission and convention baked in, varying by culture, seniority and industry. Retrieval treats text as evidence; here the text is a claim, and a capability extraction has to account for the conventions of how people write about themselves.

**Recall is what matters and every evaluation measures precision.** Search infrastructure is tuned and evaluated on returning good results at the top. The sourcing problem is the people never returned at all, which requires a recall-oriented evaluation against a reference population that does not exist in the index — a fundamentally different evaluation design.

**The corpus is incomplete in a biased way.** Profile databases over-represent certain industries, geographies, seniorities and demographics. Retrieval quality metrics computed on the index are silent about everyone absent from it, and the coverage question sits outside the search stack entirely.

**Freshness and provenance matter legally.** Aggregated profile data has consent, accuracy and jurisdiction implications, and increasingly regulation reaches how candidate data is collected and used in sourcing. The retrieval stack has no concept of provenance constraints on what may be indexed or contacted.

## Target Customer

Sourcing platform vendors upgrading from boolean to semantic and finding the vocabulary gap persists. Also employers building internal talent search over their own applicant databases — frequently the largest and most neglected sourcing pool they have.

## Impact If Solved

The vector infrastructure, embedding models and reranking get reused, and the capability extraction layer, self-presentation handling, recall-oriented evaluation, coverage measurement and provenance constraints get built. Concretely: a search that returns the person whose experience matches and whose words do not.
