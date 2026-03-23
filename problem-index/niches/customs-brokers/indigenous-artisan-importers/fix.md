# Commercial Invoice Generation for Informal Suppliers

**Niche:** [[niches/customs-brokers/indigenous-artisan-importers/profile|Indigenous & Artisan Product Importers]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Artisan cooperatives and informal workshops in developing countries don't produce commercial invoices — they provide handwritten receipts, WhatsApp messages listing items and prices, or verbal agreements confirmed by the importer — forcing the importer to create a customs-compliant invoice from scratch for every shipment.
**Tags:** #large-language-models #automation #compliance #worker-facing

## The Problem
CBP requires a commercial invoice for every import entry with specific data elements: seller name and address, buyer name and address, detailed product description, quantity, unit value, total value, currency, and country of origin. A women's weaving cooperative in rural Peru provides a handwritten list: "20 scarves, 15 blankets, 10 table runners — total S/. 8,500." The importer must convert this into a commercial invoice with per-item pricing, English product descriptions detailed enough for classification, and proper formatting. This conversion takes 45-90 minutes per shipment and introduces errors when the importer estimates per-item values or writes product descriptions without sufficient detail.

## Why It's Still Broken
The global trade system was designed for commercial-scale B2B transactions between businesses with accounting departments. Informal artisan suppliers in developing countries operate outside this system — they don't have business registration numbers, don't issue invoices, and communicate through WhatsApp or handwritten notes. No tool bridges the gap between informal supplier documentation and CBP's formal invoice requirements. The importer is left to create the bridge document manually.

## What a Fix Looks Like
A supplier documentation converter that: (1) accepts informal supplier documentation in any format (photos of handwritten receipts, WhatsApp message screenshots, Excel lists); (2) extracts product information (items, quantities, prices) from the informal documentation; (3) generates a formatted commercial invoice with all CBP-required data elements; (4) prompts the importer for missing information (product description detail, per-item pricing if only total was provided); (5) stores supplier templates so that repeat shipments from the same supplier require only quantity/price updates.

## Who Feels the Pain
Fair trade importers who spend 30-90 minutes per shipment creating commercial invoices from informal supplier records — time that could be spent on supplier development, marketing, or growing the business.

## Impact If Fixed
Reducing invoice creation from 60 minutes to 10 minutes per shipment saves 50 minutes per import. For an artisan importer doing 20 shipments per year, this recovers 16+ hours annually. Standardized invoice formatting reduces CBP holds from insufficient documentation, preventing $500-$2,000 per hold.
