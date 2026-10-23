# Verifying Labels You Did Not Print

**Industry:** [[contract-packagers|Contract Packagers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Artwork comparison and vision inspection are mature products, but a co-packer receives labels and cartons printed by the brand's suppliers and must prove at receiving and at the line that every one matches the approved version for that job.
**Tags:** #cnns #object-detection #transformers #evaluation-metrics #compliance #automation #quick-win

## The Problem
The labels, cartons and sleeves a co-packer applies are usually printed by someone else: the brand's label converter or carton printer, working from artwork the brand approved weeks earlier. The packager receives pallets of printed material and must confirm, before anything reaches a line, that it is the right version: the current ingredient statement, the right allergen declaration, the right barcode, the right language panel for the market, the right country-of-origin statement for an import. Then, at the line, it must confirm that only that version is present and that the lot code and expiry printed in-line are correct and legible.

Mistakes here are the costly kind. An old carton revision with a superseded allergen statement, a French-English label sent to a US-only job, or a club pack whose outer barcode scans as the single unit can cost a recall, a retailer rejection or a chargeback. In drug packaging, a label mix-up is the deviation regulators look for first, and the line must be cleared and documented before every run under 21 CFR 211.130. Most consumer co-packers check incoming print by eye against a printed proof, and check codes at the line by sampling.

## What Already Exists
Artwork and print comparison software from GlobalVision and Esko compares a printed sample or PDF against the approved file, and is used by brands, printers and packaging artwork studios (see [[graphic-design-studios|Graphic Design Studios]]). Smart cameras and verification systems from Cognex, Keyence and others read barcodes and lot codes in-line and grade print quality. Label management software such as Loftware or BarTender handles variable data for labels the packager prints itself (estimate).

## The Customisation Gap
The generic tools assume the user owns the artwork and the print. A co-packer needs a receiving workflow that pulls the approved artwork for the specific job and version from the brand, compares a scanned sample of each incoming lot against it, and records the result against the brand's purchase order. It needs line-side checks configured per job from the same job record: which barcodes are valid at unit, inner and case level, which lot and expiry format, which languages. Every check has to be logged in the form the brand's auditor or a cGMP batch record expects. Small packagers need this without a validation project or a fixed camera on every hand-pack line, so handheld or tablet capture matters as much as in-line vision.

## Impact If Solved
Catching a wrong-version component at receiving costs a phone call. Catching it after it ships can cost a recall. A job-driven verification record would cut the main cause of label recalls a co-packer can control. It would also cut the hours QA staff spend comparing printed proofs by eye, a task one QA technician may do dozens of times a week in a busy season (estimate).
