# A Literature That Never Stops Moving, Read by Hand

**Niche:** [[niches/pharmacy-independents/drug-compendia-pricing-publishers/profile|Drug Compendia & Pricing Content Publishers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical editors read the literature to find what changed, and the volume grew faster than the editorial team ever will.
**Tags:** #transformers #large-language-models #word-embeddings #transfer-learning #workflow-orchestration

## The Problem
The knowledge base has to be current, because the customers' dispensing systems block on it. New approvals, new NDCs, label changes, boxed warnings, safety communications, recalls, new interaction evidence, revised dosing in renal impairment — all of it must be found, assessed, and reflected in structured content, continuously.

Finding it is the bottleneck. Clinical editors monitor regulatory feeds, journal tables of contents, professional society guidance, and manufacturer communications, and read to work out whether anything requires a content change. Most of what they read requires none. The signal rate is low and the volume is not.

Meanwhile the corpus a change might affect is enormous and interconnected. A revised warning about one drug can implicate a whole class, several interaction pairs, and dosing content in multiple populations. Working out the blast radius of a change is manual, and missing part of it produces exactly the inconsistency customers notice.

Editorial headcount does not scale with a literature that grows every year. The team gets more selective about what it monitors, which is a coverage decision made by triage rather than by policy.

## What Already Exists
Biomedical language models are mature. Domain-adapted encoders handle clinical and pharmacological text well, retrieval over the biomedical literature is a solved engineering problem, and commercial pharmacovigilance tooling already does literature screening for adverse event case identification.

None of it produces the output needed. Pharmacovigilance screening asks whether a document describes an adverse event in a patient — a different question from whether a document requires a change to a structured knowledge base assertion. Generic literature triage returns relevance rankings over documents, and the editorial workflow needs a proposed change to a specific field of a specific record, with its evidence attached.

## The Customization Gap
**The unit of output is a content change, not a document.** The system must surface "this publication implies the severity grade on this pair should be reconsidered", not "this paper is relevant to warfarin". That mapping — from evidence to the specific assertion it bears on — requires the knowledge base's own structure as the target, and only the publisher has it.

**Blast radius must be computed.** The content is a graph: drugs, classes, ingredients, interactions, conditions, populations. Determining everything a change touches is graph traversal over that structure, and it is the part editors currently do from memory.

**Editorial policy is not literature quality.** Whether a finding is sufficient to change a graded assertion depends on the publisher's own evidence standards, which differ by content type and are stricter than journal peer review. The model must learn the house standard, and the training signal is the editorial decision history — which the publisher has and nobody else does.

**Identifier chaos is the substrate.** NDCs, RxNorm, GPI, ingredient identifiers, brand and generic naming across manufacturers and repackagers. Any extraction pipeline that cannot resolve a drug mention to the right node in the publisher's own hierarchy produces work rather than saving it.

**Provenance is mandatory.** Every assertion must trace to its evidence, because customers, regulators and courts ask. A model that proposes a change without a citable basis cannot enter this workflow at all.

## Target Customer
VP of Content Operations or Chief Clinical Officer at a drug knowledge base publisher, running an editorial team whose size determines the currency of the product.

## Impact If Solved
Editorial capacity is the binding constraint on both currency and coverage, and currency is the product. Turning literature monitoring from reading into reviewing proposed changes — each with its evidence and its computed blast radius — lets the same team cover substantially more of a literature that is growing regardless.
