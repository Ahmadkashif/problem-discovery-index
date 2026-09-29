# Document Standards and Machine-Readable Travel Documents

**Niche:** [[niches/identity-verification-vendors/document-and-geography-coverage/profile|Document & Geography Coverage]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** International standards define machine-readable and chip-based identity documents that can be verified cryptographically, and much of the industry still reads them as pictures.
**Tags:** #object-detection #cnns #data-integration #evaluation-metrics #compliance #confidence-intervals #automation #transfer-learning
**Contested on:** Every serious competitor in this niche is fighting to support thousands of document types across hundreds of jurisdictions, each with its own layout, security features and revision history — and whoever stops maintaining that library by hand supports the documents everyone else declines.

## The Problem
Machine-readable travel document standards, electronic passport chips with issuer signatures, and emerging mobile driving licence standards all exist to make identity documents verifiable rather than merely readable. A chip read with a valid issuer signature is far stronger evidence than any visual inspection of a photograph. Adoption in commercial verification is partial, uneven and often treated as an enhancement rather than as the primary path.

## What Already Exists
Machine-readable zone standards; electronic passport chip reading with passive and active authentication; mobile driving licence and verifiable credential standards; issuer certificate infrastructure; and reader implementations on consumer devices.

## The Customization Gap
The adaptation is to consumer devices and partial coverage. It requires: (1) a flow that prefers the cryptographic read and falls back to visual only when unavailable, which is the substantive inversion — most products do the opposite; (2) chip reading on the applicant's own phone, where hardware support, positioning and user instruction all determine success; (3) certificate infrastructure and issuer trust management, which is real operational work most vendors have not taken on; (4) a long transition where most documents are not chip-enabled, so both paths must be excellent; and (5) emerging mobile credential standards whose verification model differs again and is arriving now.

## Target Customer
Coverage and product leadership, customers wanting the strongest available evidence, standards bodies and issuers, and document reader vendors.

## Impact If Solved
A signed chip read is stronger evidence than any photograph and is treated as an enhancement. Inverting the flow to prefer it, with visual reading as the fallback, is the adaptation and it also removes the template dependency where it applies.
