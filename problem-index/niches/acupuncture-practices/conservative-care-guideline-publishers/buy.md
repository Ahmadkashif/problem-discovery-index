# Evidence Surveillance Adapted to Guideline Dependency

**Niche:** [[niches/acupuncture-practices/conservative-care-guideline-publishers/profile|Conservative-Care Treatment Guideline Publishers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Living-guideline platforms track whether evidence has changed; none of them track which of the four hundred places a guideline says something about acupuncture depend on the study that just got retracted.
**Tags:** #transformers #bert #large-language-models #graph-neural-networks #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration #compliance

## The Problem
Guidelines are dependency structures pretending to be documents. A single systematic review can underpin the visit ceiling in one care pathway, the documentation standard in another, and a contraindication in a third, written by different authors in different years. When that review is superseded, retracted, or reanalyzed, the publisher needs to know every place it load-bears. Today that is answered by full-text search for the citation, which finds the explicit references and misses everything that inherited the conclusion without citing the source — a pathway that adopted a visit ceiling from a sibling pathway, a documentation requirement copied forward through three editions. Annual edition planning therefore proceeds on a chapter rotation rather than on where evidence has actually moved, and clauses in unrotated chapters can rest on superseded evidence for years.

## What Already Exists
Guideline development tooling is real and improving. MAGICapp, GRADEpro, and the living systematic review platforms handle evidence-to-decision frameworks, recommendation authoring with attached certainty ratings, structured citation management, and multi-reviewer workflow. Several offer alerting when a cited study is updated or retracted. Reference managers and CTSU-style surveillance services cover the literature monitoring half competently.

## The Customization Gap
These tools model the guideline as a set of recommendations each carrying its own evidence profile — a tree. The commercial reality is a graph: recommendations reference each other, inherit thresholds, and share evidentiary foundations across chapters that no explicit citation records. Nothing in the existing stack represents inheritance, so impact analysis stops at direct citation and the transitive consequences stay invisible. The adaptation needed is a dependency layer over the corpus that captures both explicit citation and inherited reasoning, built once by mining the existing guideline text and then maintained as authors work. With that in place, a retraction alert stops being a notification and becomes a scoped work order: these nine clauses across four pathways rest on this study, three of them directly and six by inheritance, and here is each one's current wording. The second adaptation is regulatory: several states adopt specific guideline editions into statute, so the same dependency layer has to answer which adopted editions are affected and what the notification obligation is.

## Target Customer
Editorial directors and evidence leads at guideline publishers, and the clinical content teams inside large payers who maintain internal medical policy derived from licensed guidelines and face the identical problem one layer down.

## Impact If Solved
Edition planning moves from calendar rotation to evidence-driven prioritization, which is the difference between a guideline that is defensibly current and one that is merely recently reviewed. Retraction response drops from a multi-week manual sweep to a scoped list. And because state-adopted editions are tracked in the same structure, the compliance question that currently requires a lawyer and a spreadsheet gets answered by the system that already knows the answer.
