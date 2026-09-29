# Four Hundred Templates and Three Retired Clauses

**Niche:** [[niches/esignature-document-workflow/template-and-clause-sprawl/profile|Template & Clause Sprawl]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Legal retires a clause and updates the clause library, and the copy of it embedded in ninety templates keeps going out to customers for the next eighteen months.
**Tags:** #word-embeddings #bert #transformers #dbscan #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in agreement content is fighting to guarantee that the clause in the document going out today is the one legal currently approves — and whoever can prove that across a whole library takes the legal operations account.

## The Problem
Legal revises the limitation of liability clause in March. They update the approved clause in the clause library and send a note. The clause is also embedded — as text, copied at creation time — in ninety-odd templates built over three years by sales operations, deal desk and regional teams. Nothing connects the library entry to those copies. The old cap continues to go out on real agreements, gets signed, and is discovered in a dispute two years later, at which point somebody asks how many other agreements contain it and nobody can answer without reading four hundred templates and an archive of executed documents.

## Why Nobody Has Built This
Templates were built as documents rather than as compositions of referenced components, so a clause in a template is a copy and not a reference — a modelling decision made early and now embedded in every product in the category. Retrofitting a reference model onto a library of documents means identifying which passages are instances of which approved clause, which is a similarity problem nobody has framed. Ownership is also split: legal owns the language, operations owns the templates, and neither owns the join. And the failure surfaces years later in a dispute, which is when it is a legal problem rather than an operations one.

## What to Build
A clause-aware view of the template estate. Identify clause instances across all templates by semantic similarity to the approved library, which recovers the reference structure that was never modelled and does so retrospectively over an existing library. From that: currency checking, so every template reports which of its clauses are current, which are superseded and which do not match any approved clause at all — the last category being the interesting one, since it is where unreviewed language lives. Propagation on change, so revising an approved clause produces the list of affected templates and a proposed edit for each, reviewed rather than applied blindly. Drift detection for clauses that were modified after being copied, which is common and invisible. And the retrospective audit that is asked for in a dispute: which executed agreements contain a given superseded clause, computed over the archive, which the platform holds in full and which is currently answered by reading.

## Target Customer
Legal operations and template administrators at companies with meaningful agreement volume, and the signature and contract lifecycle vendors whose libraries rot the same way at every customer.

## Impact If Built
The copy-not-reference modelling decision is universal in the category and guarantees this failure everywhere, which makes it structural rather than a matter of diligence. Semantic clause matching recovers the missing structure without re-authoring anything, and the retrospective audit answers the one question that is asked when it matters.
