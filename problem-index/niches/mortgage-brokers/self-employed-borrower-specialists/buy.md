# Tax Return OCR Adapted for Mortgage Qualifying Income

**Niche:** [[niches/mortgage-brokers/self-employed-borrower-specialists/profile|Self-Employed Borrower Specialists]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** OCR tools like Ocrolus and LoanBeam extract tax return fields but don't perform the multi-step qualifying income calculation that processors actually need.
**Tags:** #ocr #named-entity-recognition #nlp #data-integration #automation

## The Problem
Processors receive tax returns as PDFs — often scanned, tilted, or partially redacted — and must extract 30-50 specific line items across multiple schedules and years. Existing OCR tools extract these fields with reasonable accuracy, but the extracted data dumps into a spreadsheet with no calculation logic. The processor still has to manually compute qualifying income, which is the actual time sink.

## What Already Exists
Ocrolus provides high-accuracy document parsing for tax returns and bank statements, outputting structured JSON with field-level data. LoanBeam offers tax return analysis specifically for mortgage, with some income calculation. Both integrate with major LOS platforms. However, Ocrolus stops at extraction without calculation, and LoanBeam's calculations follow generic Fannie Mae rules without lender-specific overlay variations.

## The Customization Gap
The missing layer is connecting extracted tax return fields to lender-specific income calculation rules. A self-employed borrower's qualifying income at Lender A might be $15,000/month higher than at Lender B because of how each treats depreciation add-backs, meal expense add-backs, or entity type income. The OCR output needs to flow into a rules engine that maps to each wholesale lender's specific self-employed income guidelines — not just generic agency rules.

## Target Customer
Processors at self-employed specialist brokerages who currently use Ocrolus or LoanBeam but still spend 1-2 hours per file on manual income calculation after extraction is complete.

## Impact If Solved
Eliminates the post-extraction calculation step that accounts for 50-60% of self-employed file processing time. Turns OCR from a "nice to have" extraction tool into an end-to-end income analysis pipeline that directly outputs lender-ready qualifying income figures.
