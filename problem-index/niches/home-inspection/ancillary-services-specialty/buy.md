# Spectora Ancillary Test Integration

**Niche:** [[niches/home-inspection/ancillary-services-specialty/profile|Ancillary Services & Specialty]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Inspectors using Spectora must deliver ancillary test results (radon, mold, sewer scope) as separate PDF attachments because Spectora doesn't integrate with testing equipment or lab results — creating a fragmented customer experience where the buyer receives a polished interactive report plus 2-3 disconnected PDFs.
**Tags:** #data-integration #automation #quick-win #workflow-orchestration

## The Problem
A buyer who orders a standard inspection plus radon, sewer scope, and mold testing receives: one interactive Spectora web report for the standard inspection, one PDF from the radon monitor's companion app, one video file plus PDF summary from the sewer scope camera, and one lab report PDF from the mold sampling lab (delivered 3-5 days later). These are separate documents with separate formatting, separate terminology, and no cross-referencing. The buyer must synthesize findings across 4 documents — the Spectora report mentions "moisture staining in the basement" but doesn't link it to the mold sampling results that come separately. The inspector must manually compile and send these documents, often forgetting to send the lab results when they arrive days later.

## What Already Exists
Spectora handles photo management, report generation, and customer-facing delivery for the standard inspection. Radon monitors (Sun Nuclear 1028, Airthings) output digital results via Bluetooth or cloud platforms. Sewer scope cameras record video with timestamp and location data. Mold labs (EMSL, ProLab) deliver results via online portals with structured data.

## The Customization Gap
Direct integration between Spectora and the three most common ancillary data sources: (1) radon monitor integration — pull results from Sun Nuclear or Airthings platforms via API, display radon levels within the Spectora report's environmental section with EPA action level comparison and chart of readings over the monitoring period; (2) sewer scope integration — embed scope video within the Spectora report's plumbing section, with defect annotations (crack, offset, root intrusion, bellied section) tagged at video timestamps; (3) mold lab integration — pull EMSL or ProLab results via API when available, display spore counts within the Spectora report's environmental section with normal range comparisons by species. The result is one unified report with all findings cross-referenced rather than 4 separate documents.

## Target Customer
Spectora-using inspectors who offer 2+ ancillary services and currently manage test results as separate deliverables. Spectora as a platform seeking competitive differentiation through ancillary service integration.

## Impact If Solved
Eliminates the fragmented multi-document delivery that confuses buyers and creates follow-up questions. Saves inspectors 15-20 minutes per inspection in manual compilation and formatting of ancillary results. Reduces the "forgot to send the lab results" problem that occurs on 10-15% of mold-tested inspections. Creates a premium Spectora tier or add-on revenue stream worth $20-40/month per inspector.
