# Lineage: Technical Content Agencies

**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** DITA, the Darwin Information Typing Architecture — an XML vocabulary in which documentation is written as small typed topics (concept, task, reference), assembled into deliverables by DITA maps, reused by content reference (conref), and extended by specialization
**Builder:** IBM
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A software company's documentation was written as books, and the product was no longer shipped as one.

A large vendor produced the same facts many times over: in a printed manual, in online help, in training material, in a second product that shared a component with the first, and in every language it sold into. When the facts lived inside chapters, each deliverable was a separate copy. A parameter renamed in the software had to be found and fixed in every book that mentioned it, then re-sent to every translator who had already been paid to translate the old sentence.

The cost scaled with products times formats times languages.

## What Got Built

A way to stop writing books.

DITA's unit is the **topic**: a short, self-contained piece of information with a declared type. A *task* is a procedure with steps; a *concept* explains; a *reference* holds syntax and facts. Because each type has a fixed structure, a task cannot quietly turn into an essay, and a machine knows which part of it is a step.

Books become **DITA maps** — ordered lists of pointers to topics. The same topic can appear in a user guide, a help system and a training module without being copied. Below the topic, a **conref** pulls a single element — one warning, one parameter description — from a canonical source into every place that needs it.

The name carries the extension mechanism. "Darwin" refers to **specialization**: an organisation can derive new topic types from the base ones, inheriting their processing, so a company-specific "API reference" type still renders with standard tools.

The dates: IBM introduced DITA in **March 2001** as DTD and XML Schema files with introductory material; submitted it to OASIS in **April 2004**, when the DITA Technical Committee formed; and DITA 1.0 was approved as an OASIS standard in **June 2005**, followed by 1.1 (August 2007), 1.2 (December 2010) and 1.3 (December 2015).

## Who Built It, And Why Them

IBM, from inside its own documentation operation. The introductory paper, "Introduction to the Darwin Information Typing Architecture: Toward Portable Technical Information," was written by IBM's Don R. Day, Michael Priestley and Dave A. Schell.

**Why IBM:** it had the problem at a scale almost nobody else did — a vast product line, documentation in many languages, and an existing SGML publishing stack (IBMIDDoc) that already treated documentation as structured data. A later IBM account of the migration describes the aim as "topic-based authoring through rich, semantic markup" to support "single sourcing across books, help files, training, and multimedia." A company paying to translate the same sentence across dozens of manuals is the company that gains most from writing it once.

Giving it to OASIS served the same interest. A proprietary format would have left IBM maintaining its own tool chain alone; a standard meant authoring and publishing tool vendors would build for it.

## What It Cost

Writers stopped writing prose and started writing components. The topic model forbids the connective tissue — "as described in the previous chapter" — that makes a book readable, and a reader landing on one topic from search may get a fragment without its context.

It moved the work into a pipeline. Maps, conrefs, specializations and publishing transforms have to be built and maintained by someone, and reuse means a single broken reference fails every deliverable that includes it.

And it modularised the text, not the truth. DITA makes a parameter description reusable; it does not know when the code renamed the parameter.

## What You Still Touch

Every docs site split into "Concepts," "How-to guides" and "Reference," and every docs-as-code repository assembling pages from shared snippets, works in the grammar DITA standardised — topic types, maps, single-sourcing.

- [[problems/technical-content-agencies/low-impact-1|🟡 Documentation Drift From the Software It Describes]] — reuse made copies consistent with each other, not with the code
- [[problems/technical-content-agencies/worker-life-2|🟢 The Docs Engineer Maintaining the Pipeline Nobody Funds]] — the pipeline topic-based authoring created
- [[niches/technical-content-agencies/corpus-structure/profile|Corpus Structure & Disambiguation]]
- [[niches/technical-content-agencies/reference-generation/profile|Reference Generation & Build Tooling]]

**Sources:** Wikipedia, *Darwin Information Typing Architecture* (IBM introduction March 2001; OASIS TC formed April 2004; OASIS standard dates 1.0–1.3; topic types; meaning of "Darwin"); Robin Cover, xml.coverpages.org/dita.html (authors of the introductory paper; IBM submission to OASIS April 2004; a December 2005 IBM migration account quoting IBMIDDoc and the single-sourcing aim); OASIS DITA TC charter page (no origin history). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs only. ⚠️ **Not established:** the exact first-publication date of the Day–Priestley–Schell paper — the Cover Pages entry is ambiguous between 2001 and a revised October 2003 version; which IBM division or lab did the work; the DITA Open Toolkit's release date; the translation-cost motive is inferred from IBM's single-sourcing statement, not quoted from an IBM source.
