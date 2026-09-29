# The Firm's Own Submission History Is a Folder Tree

**Niche:** [[niches/hair-salons-independent/cosmetic-regulatory-consulting/profile|Cosmetic Regulatory & Safety Substantiation Consulting]]
**Industry:** [[industries/hair-salons-independent|Hair Salons (Independent)]]
**Type:** Fix (Pain Point)
**One-liner:** Everything the firm has learned about what regulators accept is in documents nobody can search by question.
**Tags:** #word-embeddings #large-language-models #tacit-knowledge-ml #named-entity-recognition #worker-facing

## The Problem
The most valuable thing a regulatory consultancy owns is knowing what gets through. Which substantiation approach an agency accepted, which one drew a question, how a particular ingredient at a particular concentration was justified last time, what a reviewer objected to three years ago and how the firm answered it.

All of that exists — in submitted dossiers, in correspondence files, in email threads. None of it is retrievable by the question anyone actually has. A toxicologist facing a novel preservative concentration wants to know whether this firm has justified anything similar before and how it went. Answering that means remembering which client, finding the folder, and opening documents. So mostly it means asking whoever has been there longest, and if that person is busy or gone, rebuilding the reasoning from scratch.

## Why It's Still Broken
Regulatory work is organized by client and by submission, because that is how it is billed and how confidentiality is managed. The folder tree mirrors the engagement structure perfectly and the knowledge structure not at all: every question a practitioner has cuts across clients, and every storage decision the firm has made cuts along them.

Confidentiality is the reason the obvious fix has never been attempted. Client A's dossier cannot be shown to the team working on Client B. But the useful abstraction almost never requires the dossier — "this preservative at this concentration in a rinse-off product was substantiated using this argument and accepted" is a fact about the regulatory landscape, not about the client. Nobody has drawn that line, so the whole corpus stays locked at the engagement level.

The other reason is that it has always been survivable. Firms were small, tenure was long, and the person who remembered was down the corridor. MoCRA broke that: volume rose, hiring followed, and a practice with a dozen new assessors cannot run on institutional memory held by three people.

## What a Fix Looks Like
Extract the reusable layer and leave the client layer alone.

**Precedent records, not documents.** Ingredient, concentration, product type, exposure route, the justification approach used, the outcome, the date. Structured, client-anonymized, and searchable by the question a toxicologist actually asks. Populating these from existing dossiers is largely extraction work, and the documents are formulaic enough that it is tractable.

**Agency interaction logged as outcomes.** Every question a regulator asked and every response that resolved it is the firm's most direct evidence of what scrutiny looks like. Recorded as structured pairs rather than buried in correspondence, they become a checklist for the next submission of that type.

**Retrieval at the point of drafting.** When an assessor opens a new assessment, the relevant precedents should already be beside them. Not a search box they must think to use — the system knows the formula and knows what resembles it.

**Confidentiality as a boundary, not a blanket.** The precedent layer holds no client identity and no proprietary formula. It holds regulatory facts the firm learned by doing the work, which is precisely the asset the firm should be compounding.

## Who Feels the Pain
New assessors, who take a year to become productive because the knowledge is in a folder tree organized by billing. Senior toxicologists, who are the retrieval system and are the constraint on the practice. And the firm, whose accumulated regulatory learning currently walks out at retirement.

## Impact If Fixed
Onboarding compresses from a year to a quarter, which in a market where qualified assessors are the binding constraint is the whole growth story. Consistency improves, because two assessors facing the same question see the same precedents. And the firm finally owns its experience as an asset rather than as a set of people.
