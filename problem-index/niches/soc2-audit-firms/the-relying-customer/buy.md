# Buy: Document Extraction From Contract Analysis

**Niche:** The Relying Customer
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Legal technology extracts structured obligations from thousands of contracts at scale, and attestation reports are read by a person with twenty minutes.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #data-integration #automation #compliance
**Contested on:** Whether the party the report exists for can extract anything from it beyond whether it is clean and current.

## The Problem

Extracting structured information from large volumes of long, semi-standardised documents is a solved commercial problem with a mature product category.

Contract analysis platforms process thousands of agreements, extract clauses, obligations, dates, parties and terms, and present them as structured data that can be queried, compared and monitored. They handle documents that are far less standardised than attestation reports, with far more variation in language, and they do it at volumes that make manual review impossible.

Attestation reports are more consistent than most contracts. They follow a prescribed structure, contain the same sections in the same order, and use standardised language for the opinion. They are among the easier document types to extract from.

Yet the reader of a SOC 2 report opens a PDF. The platform that stores it treats it as an attachment. And the content — scope, exclusions, exceptions, obligations on the customer — stays in the document.

## What Already Exists

Contract analysis: Kira, Luminance, Evisort, Icertis and the CLM category's analysis features, with clause extraction, obligation tracking and portfolio-level query.

Document extraction generally: the mature stack for pulling structured data from semi-structured documents, now substantially better than when these categories were built.

Obligation management: the contract lifecycle capability for tracking what a party must do, with routing and monitoring — which maps exactly onto complementary user entity controls.

Vendor risk platforms: Whistic, Panorays, Prevalent and the third-party risk modules, which store attestation reports as attachments.

Trust centres: supplier-published documentation hubs, some with structured metadata.

## The Customization Gap

**Vendor risk platforms store rather than extract.** The category treats the report as evidence of a process step. Extracting its content is a different product concept that nobody in the category has adopted.

**Complementary user entity controls are obligations and are treated as prose.** Contract platforms extract obligations, route them to owners and monitor completion. The report's list of things the customer must do is exactly that and is handled as narrative.

**Comparison across the portfolio is the contract platform's core value.** Querying across thousands of agreements is what these platforms do, and querying across hundreds of attestation reports is what a vendor risk function needs and cannot do.

**The reports are more standardised, not less.** Contract analysis handles far greater variation, which makes attestation extraction a simpler case than the one these tools were built for.

**Structured export would be better than extraction.** If reports were issued with a machine-readable companion, extraction would be unnecessary — which is a standards change and is the better long-term answer.

**The customer-side obligation has no owner.** Contract platforms route obligations to an owner. Complementary user entity controls have no owner on the customer side, which is why extracting them requires designing the destination as well.

## Target Customer

Vendor risk platform vendors, for whom report extraction is an obvious adjacent capability and would differentiate a category that currently competes on questionnaire workflow.

Contract analysis vendors, for whom attestation reports are an easier document type than what they already handle and a new use in accounts they may already serve.

Enterprise vendor risk functions, as the buyers, who process at a volume that makes manual extraction impossible and automated extraction obviously worthwhile.

## Impact If Solved

A mature extraction capability handles harder documents at greater volume, and attestation reports are a simpler case that nobody has pointed it at.

Treating complementary user entity controls as extractable obligations with an owner is the direct transfer from contract obligation management and would address a requirement currently listed in every report and met in almost none.

And portfolio-level query across hundreds of supplier reports is what contract platforms do best and what vendor risk functions most need, which makes this an unusually clean adaptation.
