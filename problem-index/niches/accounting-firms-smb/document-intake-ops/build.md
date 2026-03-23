# End-to-End Document Intake Pipeline with ML Classification

**Niche:** [[niches/accounting-firms-smb/document-intake-ops/profile|Client Document Intake & Processing Operations]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product provides a single pipeline that receives a batch of mixed client documents, classifies each by type, extracts structured data, validates against prior-year returns, and outputs import-ready files for tax prep software.
**Tags:** #cnn #bert #ocr #multiclass-classification #computer-vision #tacit-knowledge-ml #automation

## The Problem
A client emails a PDF containing 8 scanned pages: 2 W-2s, 3 1099s, a mortgage interest statement, a property tax bill, and a charitable donation receipt. A staff accountant must open the PDF, identify each document, manually extract the relevant data fields from each, enter them into the tax prep software, and file the originals in the engagement folder. For a business client, the batch might include K-1s from multiple partnerships, brokerage composite statements with 10+ pages of detail, and state tax forms from 3 different states. An experienced intake specialist develops pattern recognition for quickly classifying documents and knowing which fields matter — tacit knowledge that new hires take months to develop.

## Why Nobody Has Built This
The document classification challenge spans 40+ tax document types with visual layouts that vary by issuer (every employer's W-2 looks slightly different). Field extraction must be position-aware and context-aware — the correct box on a W-2 depends on the form year, the issuer's layout choices, and whether the document is a scan of an original, a photocopy, or a phone photo. Validation requires comparing extracted values against prior-year data and IRS e-file schema constraints. Building this end-to-end requires ML expertise in document layout analysis, a large labeled dataset of tax documents (which contain PII), and deep integration with 3-4 tax prep software platforms.

## What to Build
A document intake system that accepts mixed batches of client documents from any channel (email, portal upload, scanned mail), uses a trained document layout model (LayoutLMv3 or Donut architecture) to classify each page by document type, extracts structured fields using type-specific extraction models, validates extracted data against prior-year returns and IRS schema constraints, flags low-confidence extractions and anomalies for human review, and produces import-ready files for UltraTax, Lacerte, Drake, and ProSeries.

## Target Customer
Operations managers at CPA firms processing 300+ individual returns and 50+ business returns annually, where document intake consumes 2-3 FTEs of staff capacity during tax season.

## Impact If Built
Automates 60-70% of document intake labor, recovering 1-2 FTEs per firm during tax season ($60K-$120K in staff cost) and reducing data entry errors that cause e-file rejections and amended returns.
