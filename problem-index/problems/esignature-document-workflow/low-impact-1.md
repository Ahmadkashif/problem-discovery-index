# Template and Clause Library Maintenance

**Industry:** [[esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Template management and clause libraries ship in every platform, and after three years a company has four hundred templates, several of which contain terms legal retired eighteen months ago.
**Tags:** #bert #word-embeddings #large-language-models #dbscan #k-means-clustering #evaluation-metrics #compliance

## The Problem
Companies send the same agreements repeatedly, so every platform supports templates and clause libraries. Sales sends order forms and quotes, HR sends offer letters and policy acknowledgements, procurement sends purchase agreements and NDAs, each with variable fields and standard terms.

The libraries decay in a familiar pattern. A template is created for a situation. Someone else creates a near-duplicate because they could not find it or needed a small change. Legal updates the limitation of liability clause and updates it in the two templates they know about. A product is renamed. A regulation changes. Three years later there are hundreds of templates, several contain retired clauses, and nobody can say which are current.

The exposure is different from the equivalent problem in support. A stale help article confuses a customer. A stale contract template creates a binding obligation the company's legal team believed it had removed, executed by a salesperson who had no way to know.

## What Already Exists
Template management with variable fields is standard everywhere. Clause libraries with approved language exist in the more sophisticated platforms and in every CLM product. Version control and audit trails are built in. Permission models restrict who can edit templates. Some platforms support clause-level approval workflows.

## The Customisation Gap
Nothing detects that a template contains an outdated clause. Clause libraries hold approved language; templates hold copies of it; and nothing compares the copies against the library, so divergence is invisible. That comparison is semantic rather than textual, since a clause may have been lightly edited when it was pasted, and it is exactly the check a legal team would want and cannot perform manually across four hundred documents.

Duplicate and near-duplicate template detection is straightforward text similarity and is absent, so the library's redundancy compounds.

Usage-weighted risk is the prioritisation nobody computes. A stale clause in a template used twice a year is a minor problem; the same clause in the template sales sends four hundred times a month is a material exposure. The platform knows the send volumes and never joins them to the clause content.

Induction from what is actually sent is the constructive direction. Users editing the same template the same way repeatedly are demonstrating that the template is wrong, and clustering the actual sent documents reveals the template that should exist.

## Impact If Solved
Template libraries are how companies execute their standard terms at volume, and they drift into containing language the legal department believes it retired. Semantic comparison against the approved clause library, weighted by send volume, turns an unauditable sprawl into a managed risk surface.
