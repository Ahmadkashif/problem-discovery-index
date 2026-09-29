# Retyping Facts the Template Already Knew

**Niche:** [[niches/esignature-document-workflow/post-signature-administration/profile|Post-Signature Administration]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A contract administrator reads an executed PDF to type in the effective date, term and notice period, for a document the platform generated from a template with those exact fields in it.
**Tags:** #bert #transformers #large-language-models #graph-theory #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor moving from signature to agreement platform is fighting to turn the executed document into structured obligations that drive a calendar and a system of record — and whoever does that stops being a signature vendor, which is the whole strategic question in the category.

## The Problem
An agreement is generated from a template. The template has merge fields for the counterparty, the effective date, the term length, the fee and the notice period, populated from a deal record. It is executed. The platform stores a flattened PDF. A contract administrator opens that PDF, reads it, and types the effective date, term, renewal type and notice period into a spreadsheet — facts that were structured data forty minutes earlier, inside the same system, and were thrown away at the moment of signing. Where the agreement was negotiated, some of those terms changed in redline, which is the only part that genuinely requires reading.

## Why Nobody Has Built This
The product boundary is the signature, and everything past it was designed to be somebody else's category — contract lifecycle management, sold separately and mostly to enterprises. Flattening to PDF at execution is a legal-integrity convention that is correct as far as it goes and has been allowed to destroy the structured layer alongside it, when both could be retained. And the administrators doing the retyping are not the buyers, so the work is invisible in the procurement conversation.

## What to Build
Carry the structure through execution. Merge-field values retained as structured data alongside the executed document, with the PDF remaining the legal artefact — the two are not in conflict and treating them as if they were is the mistake. Negotiated changes detected by comparing the executed document against the generated one, which isolates precisely the terms that require reading and reduces the administrator's work to the genuinely variable part. Extraction applied only to documents that did not originate in the platform, which is the minority. From the resulting obligation set: a renewal and notice calendar that belongs to the organisation rather than to an individual, non-date obligations tracked as work items with owners, and an amendment chain that computes the current operative terms rather than storing five documents and leaving the reader to work it out. Push to the systems that need the facts — finance for the payment schedule, procurement for the supplier record — which is where the retyping actually terminates today.

## Target Customer
Contract administration and legal operations teams, finance functions dependent on contract terms, and the signature vendors whose stated strategy is to become agreement platforms and who need a reason beyond the signature to be one.

## Impact If Built
This is the clearest case in the industry of information being destroyed and then manually reconstructed inside a single system. Retaining the structured layer eliminates most of the work outright rather than automating it, and the executed-versus-generated comparison reduces the remainder to the part that genuinely needs a person.
