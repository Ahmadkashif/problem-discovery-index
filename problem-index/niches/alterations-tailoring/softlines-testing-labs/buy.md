# Four Hundred Brand Protocols, Each a Document, Each Slightly Different

**Niche:** [[niches/alterations-tailoring/softlines-testing-labs/profile|Softlines Testing & Quality Assurance Labs]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Deciding which tests a submission needs means reading the customer's protocol manual, and every customer has one.
**Tags:** #transformers #large-language-models #workflow-orchestration #compliance #data-integration

## The Problem
Before anything is tested, someone has to decide what to test. That depends on the brand's protocol, the product category, the destination markets, the fibre content, the intended end use and whichever regulations apply — children's sleepwear, restricted substances, care labelling, market-specific flammability.

Brand protocols are documents. Hundreds of pages, revised annually, specifying methods, sample sizes, conditioning, tolerances and pass criteria that differ in small but consequential ways from the published standard and from every other brand's version. A large lab holds hundreds of them.

So test plan selection is a reading exercise performed by technical staff, per submission, under a turnaround commitment. Errors run both ways and both are expensive: running tests the protocol did not require is unbillable waste, and missing a required test means a shipment clears on an incomplete gate.

Regulatory scope compounds it. A garment shipping to several markets picks up several regimes, and which apply depends on product attributes that arrive on a submission form filled in by a supplier.

## What Already Exists
Laboratory information management systems handle sample tracking, scheduling, instrument integration and reporting competently, and every large lab runs one. Standards bodies publish methods in structured catalogues. Document extraction and language models read technical specifications well.

The gap is between the protocol document and the LIMS. The LIMS knows how to run a test plan; it has no idea how to derive one. Protocol interpretation sits upstream of every system in the building, in the heads of technical reviewers, and is re-performed for every submission.

## The Customization Gap
**The protocol must become executable rules, not searchable text.** Encoding a brand manual as a decision structure — if fibre content, if category, if market, then this method at this tolerance — is the whole job, and it must be versioned because protocols revise and the lab has to show which version it tested against.

**Deviations from published methods are the hard part.** Brands modify standard methods constantly, and the deviations are exactly what generic standards catalogues do not carry.

**Regulatory scope must be derived from product attributes.** Destination markets, age grading and fibre content determine mandatory testing, and the rules differ by jurisdiction and change.

**Submission data is unreliable input.** Fibre content and category arrive from a supplier form and are frequently wrong or incomplete. The system must flag implausible combinations rather than silently generating a plan from a bad attribute.

**Ambiguity must route to a reviewer.** Protocols contain genuinely unclear provisions, and the correct behaviour is escalation with the passage cited, not a guess.

**The interpretation history is the asset.** How this lab has read an ambiguous clause for this brand, across years, is knowledge that currently lives with senior reviewers and should be a versioned artefact.

## Target Customer
Global Technical Director or Head of Softlines Operations at a testing and certification group.

## Impact If Solved
Test plan derivation is the pacing step ahead of every submission and the source of both over-testing and missed requirements. Turning protocol manuals into versioned executable rules removes the reading, makes the interpretation auditable when a brand disputes a result, and is the structural precondition for risk-weighting the panel at all.
