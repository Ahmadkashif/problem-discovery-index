# Building Condition Arrives as a Reserve Study PDF and a Manager's Answers

**Niche:** [[niches/hoa-management/community-association-insurance-underwriting/profile|Community Association Insurance Underwriting]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The information that decides whether a building is insurable sits in reserve studies, engineering reports and board minutes, and an underwriter reads them one submission at a time.
**Tags:** #transformers #large-language-models #cnns #data-integration #workflow-orchestration

## The Problem
An association submission is a document bundle. A reserve study running to a hundred pages with component inventories, remaining useful lives and funding analysis. An engineering or milestone inspection report where the state requires one. Financial statements. Board minutes discussing deferred projects. A loss run. An application form with answers supplied by a manager who may or may not know the building.

Underwriting means reading all of it and forming a view: what condition is this building actually in, what has been deferred, and is the association financially able to do the work it has been putting off.

That reading is the underwriting bottleneck. Submissions arrive in volume at renewal season, the documents are long and unstructured, and the specific facts that matter — roof replaced in what year, plumbing material, percent funded, an engineer's adverse finding buried in a section — are scattered.

Under-reading is the failure mode. In a hardened market with severe capacity constraints, missing an adverse engineering finding or a materially underfunded reserve is how a carrier writes the risk it least wants.

## What Already Exists
Document extraction platforms handle structured forms and financial statements competently. Insurance submission intake tooling exists and is improving. Language models read technical reports well. Property data vendors supply construction attributes from public records.

None targets this bundle. Reserve studies have no standard format — every provider structures them differently and the component tables are the least standardised part. Milestone inspection reports are engineering prose whose adverse findings are stated in professional language rather than flagged. And no generic tool knows which of the two hundred facts in a reserve study are the eight an underwriter actually prices on.

## The Customization Gap
**The target is a rating variable, not a summary.** Roof age and material, plumbing material, percent funded, deferred project list, adverse engineering findings, life safety status — extracted to a defined schema with page-level provenance.

**Reserve study component tables are the hard structure.** They are the richest single source about building condition and they are laid out differently by every provider. Extracting them into a comparable component inventory is the core technical problem here.

**Adverse findings must be recognised in prose.** An engineer writing that a condition "warrants further evaluation" is signalling something specific, and recognising that register is the difference between catching the risk and missing it.

**Financial capacity must be joined to physical condition.** A deferred roof in a well-funded association is a different risk from the same roof in an association that cannot assess for it. The two facts live in different documents and are reasoned about together by the underwriter.

**Confidence must route, not decide.** In a market this tight, the value is triage — surfacing the adverse facts with citations so the underwriter reads the right eight pages, not automating the decision.

**The archive is the training set.** Years of submissions paired with the underwriter's own extracted rating variables and with subsequent loss outcomes is supervision only these carriers hold.

## Target Customer
Chief Underwriting Officer or Head of Underwriting Operations at a community association insurer or programme manager.

## Impact If Solved
Submission reading is the constraint on how many associations a carrier can underwrite properly, at exactly the moment when the market needs more careful underwriting and has less capacity to do it. Extracting condition to a schema with provenance lets underwriters price on facts rather than on an application form — and creates the structured building-condition series the loss modelling above depends on.
