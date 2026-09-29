# Document and Geography Coverage

**Industry:** [[identity-verification-vendors|Identity Verification Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Thousands of document types across hundreds of jurisdictions, each with its own layout, security features and revision history, supported by a template library maintained by hand.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #bert #evaluation-metrics #feature-engineering #data-integration

## The Problem
A document verification system must recognise what it is looking at before it can read it. US driving licences alone vary by state and by issue year, each revision changing layout, fonts, security features and data encoding. Add passports, national identity cards, residence permits and regional documents across every country a customer operates in, and the library runs to thousands of types.

Each supported type requires knowing its layout, where fields sit, what security features should be present and how they appear under available capture conditions, and how to validate internal check digits and machine-readable zones.

Documents change without coordination. A state redesigns its licence, and until the library is updated the new document either fails or is processed by generic fallback logic that catches less.

Coverage is inevitably uneven. Common documents from large markets are supported well; documents from smaller jurisdictions, older revisions and less standard types are supported poorly or generically. The people carrying those documents experience the difference as a rejection.

Adding a type is a project: acquiring genuine samples, which is itself difficult, annotating, training or configuring, and validating.

## What Already Exists
Vendors maintain large template libraries and update them continuously. Machine-readable zones and barcodes provide structured data on many documents. Some public reference material on document specifications exists. Shared industry document databases exist in limited form. Generic fallback extraction handles unknown documents with reduced confidence.

## The Customisation Gap
New revisions are detected reactively. A document type whose failure rate suddenly rises has probably been redesigned, and that is visible in the vendor's own telemetry days or weeks before anyone reports it. Nobody monitors for it systematically.

Few-shot support for rare types is underexploited. Document layouts share enormous structure — a portrait, a machine-readable zone, a set of labelled fields — and modern vision models generalise across layouts far better than template matching. Rare documents are precisely where the template approach fails and where learned generalisation is most valuable.

Capture condition is not modelled as a variable. The same document photographed on a flagship phone in good light and a five-year-old device in a dim room are different problems, and accuracy is typically reported as a single number that averages over a device distribution that differs sharply between customer populations.

Synthetic generation is underused for a documented reason — genuine samples of rare documents are hard to obtain lawfully — and structured synthesis from published specifications is a legitimate way to bootstrap coverage where real samples cannot be collected.

## Impact If Solved
Coverage gaps are experienced by users as rejection and by customers as a limit on which markets they can serve. Detecting revisions from telemetry, generalising across layouts rather than templating each one, and modelling capture conditions explicitly extend coverage to exactly the documents and devices where the current approach fails hardest.
