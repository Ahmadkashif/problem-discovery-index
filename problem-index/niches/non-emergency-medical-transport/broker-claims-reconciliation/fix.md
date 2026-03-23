# Remittance File Parsing Across Broker Formats

**Niche:** [[niches/non-emergency-medical-transport/broker-claims-reconciliation/profile|Broker Claims Reconciliation]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Fix (Pain Point)
**One-liner:** Every NEMT broker sends remittance data in a different format — CSV, PDF, portal export, EDI 835 — and billing staff spend hours manually reformatting each one before reconciliation can even begin.
**Tags:** #automation #data-integration #quick-win

## The Problem
An NEMT provider working with 3 brokers receives remittance information in 3 different formats: Broker A sends a CSV with trip ID, paid amount, and a cryptic status code. Broker B provides a PDF summary with page-level totals and no line-item detail — the line items are only accessible through their portal, requiring manual export of 500-1,000 records per month. Broker C sends an EDI 835 file that the provider's accounting software cannot parse. Before any reconciliation work can begin, a billing specialist must: download data from 3 different sources, normalize column names and formats, decode broker-specific status codes, and load everything into a single spreadsheet. This formatting step alone consumes 5-8 hours per month per broker — 15-24 hours of work before a single claim is actually reconciled.

## Why It's Still Broken
NEMT brokers have no incentive to standardize remittance formats — they are monopoly or oligopoly providers in their state markets, and the NEMT providers who need the data have no leverage to demand a format change. The EDI 835 standard exists for healthcare remittance, but NEMT brokers implement it inconsistently or not at all. Each broker updates their portal and export formats without notice, breaking any custom parsing scripts the provider has built. The formatting problem is so persistent that many providers simply do not reconcile — they accept the payment received and absorb the losses from underpayments and missed denials.

## What a Fix Looks Like
A remittance ingestion layer that connects to each broker's data source (API, portal scrape, file upload, EDI 835 parser), normalizes the data into a standard schema (trip ID, authorization number, service date, billed amount, paid amount, adjustment codes, denial codes), and outputs a clean, reconciliation-ready dataset. The parser maintains broker-specific mapping tables that are updated when formats change. The provider loads all broker remittance data through a single interface, eliminating the 15-24 hours of monthly formatting work.

## Who Feels the Pain
Billing specialists who spend a quarter of their time reformatting data rather than analyzing it, provider owners who forgo reconciliation entirely because the formatting burden makes it impractical, and revenue cycle managers who cannot produce accurate revenue reports because payment data is fragmented across incompatible formats.

## Impact If Fixed
Eliminates 15-24 hours per month of manual data formatting, enables reconciliation for providers who currently skip it (recovering 5-10% of revenue from undetected underpayments), and provides the data foundation for all downstream revenue cycle improvements.
