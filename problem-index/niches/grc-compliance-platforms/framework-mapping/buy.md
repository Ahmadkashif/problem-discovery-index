# Buy: Common Control Frameworks, Made Live

**Niche:** Framework Mapping & Crosswalks
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Common control frameworks already provide a canonical control set with mappings to everything, as documents and spreadsheets that no platform consumes as live data.
**Tags:** #bert #word-embeddings #large-language-models #graph-theory #data-integration #compliance #automation
**Contested on:** Whether an organisation pursuing several frameworks implements one control set once, or implements substantially the same things repeatedly.

## The Problem

The canonical control set already exists, several times over. The Secure Controls Framework maintains a large control catalogue mapped to dozens of authority documents. The Unified Compliance Framework has done similar work commercially for years. NIST publishes mappings between its own publications and several external frameworks. Standards bodies publish crosswalks at revision.

All of it ships as documents and spreadsheets. A platform wanting to use it downloads a file, imports it, and maintains a fork that drifts from the source. There is no live interface, no versioning discipline a consumer can rely on, no machine-readable change notification at revision, and no shared representation of mapping strength.

So the mapping problem is solved in substance and unsolved in distribution. Every platform and every consultancy maintains its own copy of substantially the same knowledge, each going stale independently, and the expert effort that produced the mappings is replicated across the industry many times over.

## What Already Exists

Common control frameworks: the Secure Controls Framework, with broad coverage and an open licence; the Unified Compliance Framework, commercial and long established; NIST's own mapping publications and the OSCAL format.

OSCAL is the most important item here: a NIST-developed machine-readable format for catalogues, profiles, control implementations and assessment results, designed precisely to make this content consumable as data rather than as documents. Adoption is growing and remains thin outside the federal ecosystem.

Framework sources: ISO, AICPA, PCI SSC and the sector regulators, publishing as documents with revision cycles.

Platform-internal: the mapping tables every GRC platform maintains privately.

## The Customization Gap

**OSCAL solves the format and has not solved distribution.** A machine-readable representation exists and most frameworks are not published in it, so the first step is still parsing a document. Framework bodies publishing in OSCAL natively would change the category more than any product.

**Mappings are untyped.** Existing crosswalks assert that a control relates to a requirement without saying whether it satisfies it fully, partially or conditionally. Adding typed strength to existing mappings is a modest enrichment with a large practical effect.

**Nothing carries evidence expectations.** Common control frameworks map requirements. What evidence each framework expects, and whether one artefact serves both, is where the duplicated work is and is absent from every crosswalk.

**Revision handling is manual everywhere.** No mapping source publishes a structured diff at revision, so every consumer re-derives what changed. Computing that diff over a machine-readable corpus is straightforward and nobody does it.

**Licensing fragments adoption.** Some catalogues are open, others commercial. A platform building on a commercial mapping inherits a dependency; one building on an open catalogue inherits a resourcing risk. Neither has produced a default.

**Confidence is not expressed.** Mappings are asserted by experts with no indication of certainty, and the uncertain ones are exactly where an organisation should not rely on the mapping without checking.

## Target Customer

The compliance platforms, who should be consuming these catalogues as live data rather than maintaining private forks — the maintenance they each perform separately is close to pure waste.

The catalogue maintainers, particularly the Secure Controls Framework, for whom OSCAL-native publication, typed mappings and structured revision diffs would make their work far more usable and would consolidate the fragmented adoption.

Framework bodies as the highest-leverage actors: publishing the frameworks themselves in a machine-readable format would remove the parsing step every downstream consumer currently repeats.

## Impact If Solved

The industry stops maintaining the same mapping knowledge many times over in private forks that each go stale on their own schedule.

Typed mapping strength and evidence expectations are modest enrichments to existing catalogues that would convert an indicative crosswalk into something an organisation can actually rely on.

And machine-readable framework publication with structured revision diffs would remove the single most recurrent manual burden in this niche, which is a small team reading two long documents every time a standard updates.
