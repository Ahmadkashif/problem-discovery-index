# Document Intake Automation

**Parent Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Category:** Highly Automatable

## Profile
**Market Size:** ~$3B in preparer labor costs dedicated to document intake (receiving, sorting, classifying, and extracting data from client tax documents) across independent tax prep firms
**Share of Parent Industry:** N/A (operational cost center — 30-40% of preparer time during filing season)
**Digital Adoption:** Low-Medium — client portals (SafeSend, TaxDome, Canopy) have improved document collection channels, but sorting, classification, and data extraction from submitted documents remain manual
**Target Buyer:** Firm owner or operations manager at firms processing 500+ returns per season
**Automation Potential:** High — document classification and field extraction are well-defined ML tasks with clear inputs (document images/PDFs) and outputs (structured tax data) that represent the single largest automation opportunity in tax preparation

## What Makes This a Distinct Niche
Document intake is the defining bottleneck of tax preparation: preparers spend 30-40% of their season receiving, sorting, classifying, and extracting data from client documents before any tax logic begins. The documents arrive in every format (photos, scans, PDFs, portal uploads, paper) and every quality level (crisp digital W-2s, photographed receipts, faded K-1 copies). The classification task is substantial: a client uploads 15-30 documents, and the preparer must identify each one (W-2 vs. 1099-INT vs. 1099-NEC vs. 1099-R vs. K-1 vs. mortgage statement vs. property tax bill) before extracting the relevant fields.

## Current Tools & Gaps
Client portals (SafeSend, TaxDome, Canopy) collect documents digitally. Some offer OCR (GruntWorx, SurePrep), but accuracy on photographed and handwritten documents remains 85-92% — below the threshold needed for tax data where a single incorrect digit triggers an IRS mismatch notice. No tool handles the full pipeline: receive document, classify type, extract fields, validate against prior year and IRS transcripts, and populate the tax software.

## Problems
- [[niches/tax-prep-firms/document-intake-automation/build|🔨 Build: End-to-End Tax Document Processing Pipeline]]
- [[niches/tax-prep-firms/document-intake-automation/buy|🛒 Buy: OCR Accuracy Enhancement for Tax Form Extraction]]
- [[niches/tax-prep-firms/document-intake-automation/fix|🔧 Fix: Missing Document Chase Workflow]]
