# Automated Conduit & Wire Sizing from Single-Line Diagrams

**Niche:** [[niches/electrical-contractors/commercial-new-construction/profile|Commercial New Construction]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that reads a single-line electrical diagram, extracts load data, and auto-generates NEC-compliant conduit and wire sizing schedules — replacing hours of manual table lookups that are error-prone and must be redone every time the engineer issues a revision.
**Tags:** #cnns #object-detection #semantic-segmentation #feature-engineering #compliance #automation #evaluation-metrics #transfer-learning

## The Problem
Every commercial electrical project requires conduit and wire sizing calculations: given the electrical loads on each circuit, what gauge wire is required (NEC Article 310, adjusted for ambient temperature, conduit fill, and continuous load factors), and what size conduit is needed to contain those wires (NEC Chapter 9 tables). A medium commercial project has 50-200 circuits, each requiring its own calculation chain. Estimators perform these calculations manually using NEC tables, spreadsheet templates, or simple calculators — a process that takes 4-8 hours per project. When the engineer issues a revised single-line diagram (which happens 2-3 times on a typical project), every affected calculation must be redone. Errors in wire sizing are caught during inspection and require costly rework; errors in conduit sizing mean pulling wire that doesn't fit, requiring conduit replacement at the contractor's expense.

## Why Nobody Has Built This
The input data — single-line diagrams — are semi-standardized PDF drawings with varying symbol sets, line conventions, and annotation styles across engineering firms. Reading them requires both image recognition (identifying symbols for panels, transformers, disconnects, breakers) and contextual understanding (a line between two symbols represents a feeder with specific load characteristics annotated nearby). NEC calculations are deterministic once you have the inputs, but extracting those inputs from drawings is a computer vision problem that no one has solved for the electrical domain. The market is fragmented (70,000+ firms) and the willingness to pay for estimating tools tops out around $500-1,000/month for mid-market contractors.

## What to Build
A document intelligence pipeline: (1) CNN-based object detection model trained on electrical single-line diagram symbols (panels, transformers, disconnects, motors, breakers) to identify components and their connections; (2) OCR layer to extract annotations (voltage, amperage, kVA ratings, circuit numbers) associated with each component; (3) NEC calculation engine that takes the extracted loads and applies Article 310 ampacity tables (with temperature, conduit fill, and continuous load derating factors) and Chapter 9 conduit fill tables to produce wire gauge and conduit size for each circuit; (4) output as a formatted conduit and wire schedule matching the engineer's panel schedule format. When a revised diagram is uploaded, the system re-extracts and recalculates, highlighting changes from the previous version.

## Target Customer
Commercial electrical contractors bidding 5-20 projects per year in the $500K-5M electrical scope range, where conduit/wire sizing is a significant estimating bottleneck. Also electrical engineering firms producing construction documents who want to auto-verify their own specifications.

## Impact If Built
Reduces conduit/wire sizing calculation time from 4-8 hours to 15-30 minutes per project, with automatic recalculation on revisions. Eliminates wire sizing errors that cause inspection failures and rework (industry average: 3-5% of projects have wire sizing errors caught at inspection). Saves $2K-5K per project in estimating labor, worth $20K-100K annually for a firm bidding 10-20 projects per year.
