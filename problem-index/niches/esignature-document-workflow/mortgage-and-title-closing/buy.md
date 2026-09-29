# Package Completeness as Document Understanding

**Niche:** [[niches/esignature-document-workflow/mortgage-and-title-closing/profile|Mortgage & Title Closing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document classification and key-value extraction on standardised forms are mature and commoditised, and closing package assembly is checked against a printed list by a human at ten at night.
**Tags:** #cnns #transformers #bert #object-detection #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor in closing technology is fighting to get a loan to fund and an instrument to record without the parties being in a room — and whoever can do that across the widest set of counties, investors and lender overlays takes the volume.

## The Problem
A closing package arrives as a stack of PDFs from four sources. Somebody checks it against a stipulation list: is the disclosure present and dated correctly, is the note the right version for this product, does the name on the deed match the name on the loan, is the legal description the one from the title commitment. It takes an experienced person an hour or more per file, happens late in the process under time pressure, and the errors it misses surface at the closing table.

## What Already Exists
Document classification, layout-aware extraction and table understanding are commodity capabilities with strong open models and multiple mature commercial services. Mortgage documents are unusually favourable material: many are standardised agency forms with stable layouts, which is close to the best case for extraction. Cross-field consistency checking is ordinary logic once the fields are extracted. Several vendors already do parts of this for underwriting.

## The Customization Gap
The adaptation is to closing packages rather than to underwriting files. It requires: (1) a stipulation model per loan product, investor and state, since completeness is defined by a specific list that varies, and the list is the thing that is currently in a person's head; (2) cross-document consistency rather than per-document extraction, because the errors that matter are mismatches — the name, the legal description, the loan amount, the dates across the disclosure sequence — and a per-document extractor that never compares will not find them; (3) date-sequence validation against the disclosure timing rules, which is deterministic logic on extracted dates and catches a failure class with real regulatory consequence; (4) a confidence-routed workflow where low-confidence extractions go to a human rather than being asserted, since a false all-clear on a package is worse than no check; and (5) handling of the non-standard minority — hand-completed forms, unusual products, scanned faxes — which is where the extraction degrades and where the human attention should therefore be concentrated.

## Target Customer
Title agents and settlement service providers, lender closing operations, closing platform vendors, and the document automation vendors already serving mortgage origination.

## Impact If Solved
The source documents are standardised to a degree rare in this vault, which makes extraction unusually reliable, and the checking work is currently done manually under time pressure at the worst point in the process. Cross-document consistency is the half that matters and the half that per-document tooling does not attempt.
