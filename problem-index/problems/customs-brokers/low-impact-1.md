# Commercial Invoice Data Extraction for Entry Preparation

**Industry:** [[customs-brokers|Customs Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic OCR and document parsing tools extract text from invoices but don't understand the customs-specific data fields needed for entry preparation — shipper/consignee parties, country of origin, marks and numbers, tariff value basis — or handle the multi-format, multi-language invoice variations common in import shipments.
**Tags:** #llm #ocr #named-entity-recognition #nlp #automation

## The Problem

Every customs entry requires extracting data from the commercial invoice: shipper/exporter identity, consignee, country of manufacture, quantity, unit of measure, invoice value, currency, and description of goods. Customs brokers manually key this data from paper or PDF invoices into their entry preparation system. For a broker filing 30-40 entries per day, this data entry consumes 1-2 hours of clerical time daily.

Commercial invoices arrive in every format imaginable: Excel spreadsheets, PDF documents, foreign-language invoices requiring translation, hand-written forms for lower-value shipments. A single entry may require reconciling data from 3-5 separate documents (invoice, packing list, bill of lading, certificate of origin). Generic OCR tools capture text but don't know that "origen" is "country of origin" in Spanish or that the "H.S." column is the importer's own HTS code suggestion.

## What Already Exists

TradeBeam and similar platforms have some document automation. Generic OCR (AWS Textract, Google Document AI) provides text extraction. No tool combines customs-specific field extraction with multi-format, multi-language invoice handling at the quality level brokers require for entry filing.

## The Customisation Gap

A customs invoice extraction tool needs: (1) customs-specific field taxonomy (the 15-20 data fields required for entry filing, with aliases across languages and formats); (2) multi-format handling (PDF invoices, Excel spreadsheets, image scans, emails with inline data); (3) confidence scoring per extracted field (high-confidence → auto-populate; low-confidence → flag for human review); (4) multi-document reconciliation (packing list quantity vs. invoice quantity check). The customs field taxonomy and the quality standards required for entry filing are the domain components.

## Impact If Solved

Reduces entry data entry time from 3-5 minutes per document to 60-90 seconds of review. Returns 1-2 hours per day to the customs clerk. Reduces keying errors that cause entry rejections and CBP holds.
