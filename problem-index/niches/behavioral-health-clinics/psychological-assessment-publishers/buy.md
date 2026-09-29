# Item Banking Adapted to Cross-Instrument Reuse

**Niche:** [[niches/behavioral-health-clinics/psychological-assessment-publishers/profile|Psychological Assessment Publishers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Item banking software is built for a single testing programme with one blueprint; a clinical publisher's catalogue is dozens of instruments that overlap heavily and share nothing.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #dimensionality-reduction #word-embeddings #bert #transformers #feature-engineering #automation #workflow-orchestration #data-integration

## The Problem
Developing an instrument starts, in practice, from a blank page. Authors write items, pilot them, discard most, and refine what survives — and a substantial fraction of those items are near-duplicates of items the publisher already owns in another instrument, with known psychometric properties from a prior sample. Nobody can find them, because items live inside the instrument that published them rather than in a catalogue-wide bank. So the publisher repeatedly pays to discover the properties of items it has already characterized, and the overlap between its own instruments — a real clinical issue when a battery administers the same construct three times in slightly different words — goes unmeasured.

## What Already Exists
Item banking and test development platforms are mature. FastTest, Concerto, TAO, and the enterprise assessment platforms handle item authoring with metadata, versioning, IRT calibration, blueprint-driven form assembly, exposure control, and adaptive delivery. Educational and certification testing programmes run large operations on them successfully.

## The Customization Gap
Every one of them assumes a testing programme: one construct domain, one blueprint, one calibrated scale, items reused across forms of the same instrument. A clinical publisher's situation is different in kind. Items are distributed across dozens of instruments measuring overlapping constructs, calibrated on different samples with no linking design, authored under different theoretical frameworks, and — the practical blocker — described with no controlled vocabulary that would let anyone find semantically equivalent items across instruments. Reuse also carries constraints these tools have no field for: an item's calibration may be sample-specific, its clinical interpretation may differ by population, and its use in a new instrument may raise validity questions the bank should surface rather than hide. The adaptation is a catalogue-wide bank where items carry construct tags against a controlled clinical vocabulary, semantic search finds near-equivalents across instruments regardless of wording, every calibration is retained with the sample and instrument context that produced it rather than reduced to a single parameter, and reuse suggestions arrive with explicit caveats about what transfers and what does not.

## Target Customer
Research directors and psychometric leads at assessment publishers, and the instrument authors who currently write from scratch because they have no view of what the catalogue already contains.

## Impact If Solved
Cuts the most expensive and slowest phase of instrument development by starting from characterized material instead of new items. It also makes catalogue-level construct overlap visible for the first time, which is both a product quality issue and a commercial opportunity — the redundancy between instruments in a common battery is exactly the argument for the shorter, better-linked battery the publisher cannot currently design.
