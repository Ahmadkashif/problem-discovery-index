# Feasibility — Commercial Invoice Data Extraction for Entry Preparation

**Industry:** [[customs-brokers|Customs Brokers]]
**Problem:** [[problems/customs-brokers/low-impact-1|Commercial Invoice Data Extraction for Entry Preparation]]
**Problem type:** Low Impact

**Problem summary:** Generic OCR and document parsing tools extract text from invoices but don't understand the customs-specific data fields needed for entry preparation — shipper/consignee parties, country of origin, marks and numbers, tariff value basis — or handle the multi-format, multi-language invoice variations common in import shipments.

## Solution Approach
Adapt OCR/document parsing with customs-specific field extraction, HTS lookups, and validations against ACE data requirements. Integrate with the broker's CMS so parsed invoices pre-fill entry drafts while surfacing confidence scores and exceptions for review.

## Open Source Data
Relevant public sources include the HTS schedule, country-of-origin reference data, and sample invoice formats; high-quality training still requires private commercial invoices and prior entries from the broker's clients.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
