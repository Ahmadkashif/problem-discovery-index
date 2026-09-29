# Work Identity Across Editions, Formats and a Century of Records

**Niche:** [[niches/independent-publishers/permissions-rights-licensing-agencies/profile|Permissions & Rights Licensing Agencies]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A licence has to attach to a work, and a work exists as a dozen identifiers, several editions, and a title that changed between territories.
**Tags:** #named-entity-recognition #word-embeddings #graph-ml #data-integration #ocr

## The Problem
Everything the organization does starts with identifying what is being licensed. A user submits a citation, a scanned page, an article reference, or a chapter title. The system must decide which work that is — and then which manifestation of it, because rights can differ between the hardcover, the paperback, the ebook, the UK edition, and the anthology reprint.

Identifiers help and do not solve it. Every edition carries its own ISBN; articles carry DOIs that may or may not be recorded; older works predate both. Titles change between territories, are translated, are abbreviated in citation, and are shared by unrelated works. Author names appear with initials, full names, transliterations, and pseudonyms.

Matching is a mix of identifier lookup, fuzzy title comparison, and analyst review, and the failures go both ways: an unmatched request is a declined licence, and a wrong match is a licence granted against the wrong rights holder.

## What Already Exists
Master data management and entity resolution platforms — Informatica, Reltio, Senzing, and the open-source record linkage libraries — are mature and handle fuzzy matching, survivorship, and hierarchy at scale. Bibliographic matching tools exist in the library sector.

## The Customization Gap
Generic entity resolution matches records describing the same thing. Here the hard part is deciding what "the same thing" means for the question being asked.

**Work, expression, and manifestation are different objects with different rights.** A translation is a separate copyrightable work with its own rights holder. A revised edition may or may not be. An anthology chapter carries rights distinct from the same text in the author's own collection. Generic MDM has one notion of an entity; this domain needs a layered model where the correct resolution level depends on the use being licensed.

**The identifier space is fragmented and historically incomplete.** ISBNs are per-edition and post-date most of the backlist; DOIs cover part of the article literature; nothing covers everything. Resolution has to work across a mixed regime where some records are identified and most are described.

**Multilingual and transliterated at the core.** Titles and author names cross scripts and conventions, and the same work appears under several. This is not an edge case in a rights corpus; it is a large fraction of it.

**The input is a citation, not a record.** Users submit informal references, page scans, and partial descriptions. Parsing that into something matchable is a document and text problem sitting in front of the resolution problem, and generic MDM assumes structured input.

**Asymmetric error costs.** A false match creates a legal exposure; a missed match loses a fee. Those should not be traded off at the same threshold, and the trade-off differs by use type and by licence value — which means calibrated confidence and cost-aware routing rather than a single similarity cutoff.

## Target Customer
Head of Data or VP of Rights Operations at a collective licensing organization, where match rate is simultaneously the revenue lever and the risk exposure.

## Impact If Solved
Match rate converts directly to licensed revenue for rights holders and to access for users, and every unmatched request is a use that either did not happen or happened unlicensed. Handling the work-expression-manifestation distinction properly also removes a whole class of quiet errors where a licence was granted against the right title and the wrong rights holder.
