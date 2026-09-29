# Repositories That Nothing Is Ever Retrieved From

**Industry:** [[ux-research-agencies|UX Research Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every research team now has a repository holding years of transcripts and tagged findings, and the most common thing anyone says about it is that nobody searches it.
**Tags:** #bert #word-embeddings #contrastive-learning #large-language-models #k-nearest-neighbors #dimensionality-reduction #evaluation-metrics #data-integration

## The Problem
Research repositories became standard practice on a reasonable premise: studies are expensive, findings recur, and an organisation should be able to answer a question from work it has already done rather than commissioning it again. Teams have invested substantially — tagging taxonomies, nugget-level annotation, curated insight pages.

The retrieval never materialises. The common experience is that a product manager with a question does not think to look, and if they do, the search returns transcripts rather than answers. Tagging decays because it is manual and expensive and the person doing it is under deadline. The taxonomy that made sense at fifty studies is unusable at five hundred. Repositories fill and are not read, which is the outcome practitioners describe openly at conferences and in their own communities.

The consequence is duplicate research. Organisations regularly commission a study whose core question was answered eighteen months earlier by a team that has since reorganised.

## What Already Exists
Dovetail, Condens, Marvin and EnjoyHQ provide repository tooling with transcription, tagging, clipping and insight pages, and they are competent products. Automatic transcription is solved. Several have added semantic search and generative summarisation over the corpus. Some organisations run a research operations function specifically to maintain the repository, which is the intervention that works and is affordable at very few companies.

## The Customisation Gap
The repository is organised around studies and tags; the question arriving is about a decision. Somebody wants to know whether users understand a particular concept, or whether a workflow assumption holds, and the relevant evidence is three clips from two studies eighteen months apart plus a contradicting finding from a third. Retrieval has to work at the level of the claim rather than the document, and it has to surface disagreement rather than picking one answer — because the most valuable thing a repository can say is that two studies found different things and here is why they might have.

The second gap is currency. A finding from three years ago about a product that has since changed twice may be obsolete, and nothing in these systems models staleness. Weighting evidence by how much the relevant product surface has changed since the study is computable where the repository is connected to release history and is done nowhere.

The third is that the taxonomy should be derived rather than maintained. Tags are manual, decay predictably, and differ between researchers; inducing structure from the corpus itself and using the tags as a weak signal rather than the primary index removes the maintenance burden that kills these systems.

And the interface should meet the asker where the question is asked — in a product discussion, not in a research tool that a product manager has no habit of opening.

## Impact If Solved
Organisations pay for the same research repeatedly and hold the answers already, which is a direct and measurable waste in a function under constant budget pressure. Claim-level retrieval that surfaces contradiction, staleness weighting, and derived rather than maintained structure address the reasons repositories fail — and delivering answers into the tools where questions actually get asked addresses the reason nobody opens them.
