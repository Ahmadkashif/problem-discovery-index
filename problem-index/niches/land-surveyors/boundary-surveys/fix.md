# Deed Research Consuming Half of Every Boundary Survey

**Niche:** [[niches/land-surveyors/boundary-surveys/profile|Boundary Surveys]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Fix (Pain Point)
**One-liner:** Before a surveyor ever sets foot on a property, they spend 3-6 hours at the county recorder's office manually tracing the chain of title through handwritten deed books, unindexed plat maps, and microfilm records from the 1800s.
**Tags:** #ocr #named-entity-recognition #nlp #worker-facing #data-integration

## The Problem
Every boundary survey begins with deed research — the surveyor must trace the chain of title back through all conveyances, locate every recorded plat affecting the property, identify easements and encumbrances, and extract the legal descriptions from each deed to understand how the boundary has been described over time. In many counties, this requires physically visiting the recorder's office, reading handwritten deed books, scanning microfilm, and manually copying legal descriptions. Even in counties with online records, the documents are scanned images (not searchable text), the indexing is by grantor/grantee name (not by parcel), and cross-referencing multiple deeds requires manual assembly. Deed research typically consumes 40-50% of the total time for a boundary survey.

## Why It's Still Broken
County recorder's offices have digitized records at vastly different rates — some have fully searchable online databases back to the 1800s, while others have paper deed books with no digital index. Even digitized records are typically scanned images, not OCR'd text — you can view the deed but can't search within it. There is no standardized format for legal descriptions across jurisdictions (metes and bounds, lot-and-block, government survey all appear in the same county). The chain of title is a linked list of documents connected by names and reference numbers, requiring manual traversal.

## What a Fix Looks Like
A deed research acceleration platform that: (1) OCRs county recorder documents and extracts structured data (legal descriptions, bearings, distances, monument calls, lot numbers, reference plats); (2) builds a searchable parcel-based index from grantor/grantee records; (3) automatically traces the chain of title backward from the current deed; (4) extracts and compares legal descriptions across the chain to identify changes in boundary calls; (5) flags discrepancies between deeds that may indicate boundary issues. The system produces a deed research package — all relevant documents assembled, legal descriptions extracted and compared, chain of title mapped — in 30-60 minutes instead of 3-6 hours.

## Who Feels the Pain
Licensed surveyors and survey technicians who spend half their project time doing records research that is tedious, repetitive, and critically important — a missed deed or easement can invalidate the entire survey.

## Impact If Fixed
Reduces deed research time by 60-70%, saving 2-4 hours per boundary survey. At an average of 3-5 boundary surveys per week per firm, this recovers 6-20 billable hours weekly. Reduces the risk of missed encumbrances or easements that create liability exposure for the surveyor.
