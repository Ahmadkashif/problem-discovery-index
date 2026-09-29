# Predicate Strategy Chosen From Memory Over a Public Corpus

**Niche:** [[niches/medical-device-mfg/device-regulatory-affairs-consulting/profile|Medical Device Regulatory Affairs Consulting]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The single most consequential decision in a submission is which prior device to claim equivalence to, and it is made by a consultant recalling what they have seen.
**Tags:** #word-embeddings #graph-ml #large-language-models #text-classification #compliance

## The Problem
Most devices reach the US market by demonstrating substantial equivalence to a legally marketed predicate. Choosing that predicate governs everything downstream: what testing is required, whether clinical data is needed, how long review takes, and whether the submission clears at all. A good choice saves a year; a poor one produces additional information requests, testing the sponsor did not budget for, or a not-substantially-equivalent finding.

The choice is made by an experienced consultant using judgment, a keyword search of the public clearance database, and recollection of comparable devices they have worked on.

Meanwhile the corpus is entirely public. Decades of clearance decisions, with device descriptions, product codes, indications for use, and summaries describing the testing that supported each. Predicate relationships form a citation graph. Review times, additional information cycles, and outcomes are all published. Nobody has assembled it into anything a consultant can query by the question they actually have, which is: for a device like this, with these indications and this technology, what has cleared, against what predicates, with what evidence, and how long did it take.

## Why Nobody Has Built This
Regulatory affairs is a judgment profession with a strong apprenticeship culture, and predicate selection is understood as the exercise of expertise rather than as a search problem. That framing was correct when the alternative was keyword matching against device names, which genuinely does not work — a device's regulatory neighbours are defined by indications and technological characteristics, not by nomenclature.

The economics also did not push. Engagements are priced on consultant time, so faster is not obviously better, and a firm's differentiation is precisely the senior person's recall.

And the database is unpleasant to work with — inconsistent free-text summaries, evolving product codes, and no structured representation of what testing supported what claim. That is exactly the extraction problem current tooling handles well and did not handle five years ago.

## What to Build
A structured, queryable representation of the clearance corpus.

**Extract submissions into fields.** Indications for use, technological characteristics, testing performed, standards cited, and the predicates claimed. The summaries are formulaic enough to make this tractable at scale.

**Build the predicate graph.** Which devices cite which, forming lineages within a product code. That graph reveals which predicates are heavily relied on, which lineages have drifted far from their origin, and where the agency has questioned the chain — all of which bear directly on strategy.

**Retrieve by device, not by keyword.** Given a description of the device under development, return the regulatory neighbourhood: comparable clearances, the predicates they used, the evidence packages that supported them.

**Model review burden.** Time to decision and additional information cycles are published and vary systematically by product code, technology type, and evidence package. Predicting them lets a sponsor choose between a faster pathway and a stronger claim with the trade-off quantified.

**Flag the evidence pattern.** For a given product code and claim, what testing appears in cleared submissions and what appears in the ones that took three cycles. This is the closest available approximation to knowing what reviewers will ask for.

## Target Customer
Practice leader or managing director at a device regulatory consultancy. The pressure is capacity: qualified regulatory professionals are scarce, the European transition has absorbed enormous consulting bandwidth, and firms are turning work away.

## Impact If Built
Time to market is the dominant economic variable for a device company, and it turns on a strategy decision made from individual recall over a public corpus nobody has structured. Making the corpus queryable improves the decision, shortens the analysis from weeks to days, and lets a firm serve the smaller manufacturers who currently cannot afford senior time at all.
