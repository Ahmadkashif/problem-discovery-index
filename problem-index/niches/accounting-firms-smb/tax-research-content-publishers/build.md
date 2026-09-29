# Authority-to-Content Dependency Graph and Staleness Engine

**Niche:** [[niches/accounting-firms-smb/tax-research-content-publishers/profile|Tax Research Content Publishers]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that maintains a live dependency graph between primary tax authority and every piece of derived editorial content, so that within minutes of a new ruling the managing editor sees exactly which documents are now wrong, which are merely affected, and who owns each one.
**Tags:** #transformers #bert #large-language-models #graph-neural-networks #transfer-learning #evaluation-metrics #data-integration #tacit-knowledge-ml #revenue-impact

## The Problem
A tax research publisher maintains tens of thousands of explanatory documents, each of which rests on primary authority: statute sections, regulations, revenue rulings, notices, and case law. When the authority changes, the derived content silently becomes wrong. Today the mapping between the two lives in analysts' heads and in subject-matter assignment lists. When the SECURE 2.0 Act passed, or when a Tax Court decision reversed a long-standing position, editorial leadership had no systematic way to answer the only question that mattered: what do we now have to fix, and in what order? The practical consequence is that publishers triage by guesswork and by subscriber complaint — meaning the error is discovered by the accountant who relied on it, which is precisely the failure the subscription exists to prevent.

## Why Nobody Has Built This
The mapping is not a citation list. Editorial content cites authority explicitly in some places, paraphrases it without citation in others, and depends on it implicitly in worked examples and decision trees where the authority is never named at all. Extracting the true dependency requires reading the prose the way a tax attorney would — recognizing that a paragraph about the deductibility of a business meal depends on a code section it never cites. Building that graph across a corpus of 40,000+ documents was not tractable with keyword or citation-parsing approaches, and publishers were unwilling to fund a multi-year NLP effort against an uncertain outcome. The corpus is also proprietary and legally sensitive, which ruled out the obvious path of outsourcing the problem to a vendor who would need to ingest it.

## What to Build
A dependency engine that ingests the publisher's full editorial corpus and the primary authority it rests on, and constructs a typed graph linking each content unit to the authorities it depends on — distinguishing explicit citation, paraphrase, and implicit dependency, each with a confidence score. A monitoring layer watches primary sources (Federal Register, IRS releases, Tax Court and appellate dockets, state revenue departments) and, on each new authority, traverses the graph to produce a ranked impact list: documents that are now incorrect, documents whose examples need renumbering, documents merely worth reviewing. For high-confidence mechanical updates — a rate change, an inflation adjustment, a renumbered section — the system drafts the revision and routes it to the responsible analyst as a diff to approve rather than a document to rewrite. Everything else becomes a prioritized editorial queue item with the affected passage highlighted and the triggering authority attached.

## Target Customer
VP of Content or Managing Editor at a tax research publisher running 100-400 analysts and editors, and — as a smaller but faster-closing variant — the knowledge management lead at a 200+ person accounting firm maintaining an internal technical library.

## Impact If Built
Collapses the interval between a new authority landing and the content being correct from weeks or months to hours. Removes the category of failure that most damages a research subscription's credibility: the subscriber discovering the error first. Editorial capacity redirects from scanning and triage — which consumes a large share of senior analyst time — toward the judgment work that only credentialed analysts can do, letting the publisher expand coverage into state and specialty areas without proportional hiring.
