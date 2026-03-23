# Rate Sheet Parsing & Overlay Tracking Fragmentation

**Niche:** [[niches/mortgage-brokers/lender-submission-routing/profile|Lender Submission & Routing]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Brokers receive 20-40 rate sheet emails daily and lender guideline updates weekly — all in different formats — with no systematic way to parse, compare, or track changes over time.
**Tags:** #ocr #named-entity-recognition #nlp #data-integration #automation #worker-facing

## The Problem
Every morning, a brokerage receives rate sheets from 20-40 wholesale lenders via email — each in a different format (PDF, Excel, HTML email, lender portal). A senior loan officer or pricing analyst must review these to identify rate changes, pricing specials, and competitive positioning. Separately, lender guideline updates arrive as PDF bulletins, emails, or webinar notifications — communicating overlay changes, program additions/removals, and underwriting policy shifts. There is no unified system to ingest, parse, and track these changes. Brokerages rely on individual memory, saved emails, and occasionally a shared spreadsheet that's perpetually out of date.

## Why It's Still Broken
Rate sheets and guidelines come in dozens of proprietary formats with no industry standard. A rate sheet from Lender A is a PDF matrix; from Lender B it's an Excel file with conditional formatting; from Lender C it's embedded in an HTML email. Guideline updates are free-text narratives that bury the material change (e.g., "effective March 1, minimum credit score for investment properties increased from 680 to 700") within pages of boilerplate. Parsing this variety requires document understanding across multiple formats and modalities, combined with domain knowledge to identify what's materially changed.

## What a Fix Looks Like
An ingestion pipeline that receives rate sheet emails, parses them regardless of format (PDF, Excel, HTML), normalizes pricing into a standard rate matrix, and highlights daily changes (rate moves, new specials, pricing adjustments). For guideline updates, an NLP parser that extracts material overlay changes, classifies them by impact (credit score, LTV, property type, documentation), and surfaces them as structured alerts — "Lender X increased investment property credit floor from 680 to 700, effective March 1." All tracked in a single dashboard with historical change log.

## Who Feels the Pain
Senior loan officers and pricing analysts who spend 30-60 minutes every morning reviewing rate sheets manually, and who periodically miss a guideline change that causes a submission failure. Also brokerage owners who've lost deals because a key overlay change was communicated via email and nobody caught it.

## Impact If Fixed
Saves 30-60 minutes daily on rate sheet review across the brokerage. Eliminates overlay-change surprises that cause an estimated 3-5% of submission failures. Creates an institutional knowledge base of lender pricing and guideline history that persists regardless of staff turnover.
