# Document Extraction Applied to Verification Packets

**Niche:** [[niches/proptech-platforms/affordable-housing-compliance/profile|Affordable Housing Compliance]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Extracting figures from pay stubs, benefit letters and bank statements is a commodity capability sold into lending and insurance, and affordable housing compliance staff retype them from photocopies.
**Tags:** #bert #transformers #large-language-models #cnns #evaluation-metrics #confidence-intervals #automation #compliance
**Contested on:** Every serious competitor in affordable housing software is fighting to produce a tenant file that passes a compliance review without a specialist rebuilding it by hand — and whoever gets first-pass audit rate highest takes the portfolio.

## The Problem
A verification packet arrives: photocopied pay stubs at an angle, a benefit letter, a handwritten self-employment summary, a bank statement, a completed verification form faxed by an employer. The specialist reads each one, extracts the figures, and types them into a worksheet. It is transcription of documents whose formats, while varied, are drawn from a bounded and repetitive set — the same employers, the same benefit agencies, the same payroll providers, again and again across a portfolio.

## What Already Exists
Pay stub and bank statement extraction is a mature commercial capability, sold heavily into mortgage lending, consumer credit and income verification, with multiple vendors and strong accuracy on the common payroll provider formats. Document layout analysis handles photocopies and photographs competently. Income verification data services exist that connect directly to payroll providers for a substantial share of employed households, bypassing documents entirely. Everything needed is available and most of it is in daily use one industry over.

## The Customization Gap
The adaptation is to the programme's evidentiary standards rather than to the extraction itself. It requires: (1) preserving provenance to the page and field, because the compliance file must show where each figure came from and an extracted number without a citation is worse than useless in a review; (2) extraction targeted at the specific fields the rules need — gross versus net, pay period, year-to-date, hours — rather than at a general summary, since the calculation depends on distinctions that a generic extractor collapses; (3) handling the awkward document types the lending industry has less need for, above all handwritten self-employment records and small-employer verification forms, which are common in this population and where accuracy must be low-confidence rather than wrong; (4) confidence thresholds set conservatively with specialist review below them, because the asymmetry here is severe; and (5) direct payroll verification where available, which removes the document entirely for a large share of households and is the single largest available improvement.

## Target Customer
Affordable housing owners, management agents and compliance service providers, and the affordable housing software vendors whose modules currently produce forms rather than fill them.

## Impact If Solved
Extraction plus direct payroll verification removes most of the transcription from the certification process at commodity cost, and the provenance requirement — which is the only real adaptation — also produces the audit trail the file needs anyway. The self-employment and small-employer cases remain manual and should be admitted as such rather than automated badly.
