# EDR Radius Report Parser for Automated Finding Summaries

**Niche:** [[niches/environmental-consultants/phase-i-esa-providers/profile|Phase I ESA Providers]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** EDR and GeoSearch provide consolidated database reports, but the output is a 200-page PDF that the scientist must manually read and summarize — the parsing and summarization should be automated.
**Tags:** #bert #named-entity-recognition #nlp #automation #quick-win

## The Problem
An EDR radius report for a single property is typically 100-300 pages containing hits from 50+ federal and state databases. The environmental scientist must read through every hit, determine which facilities are at the subject property vs. nearby, evaluate regulatory status (open case vs. closed, compliance vs. violation), and write a narrative summary for each relevant database. This review-and-summarize task takes 4-8 hours per Phase I and is the single most time-consuming component of the database review section. The work is deterministic — the scientist is extracting structured information from semi-structured text and reformatting it into standard narrative patterns.

## What Already Exists
EDR and GeoSearch deliver their reports in PDF format with some structured data tables interspersed with narrative summaries. EDR offers a digital data deliverable (DDD) in XML format for some databases, but it covers only a subset of the full report content and still requires manual interpretation. Some firms have built internal Excel parsers for EDR data, but these are fragile and require maintenance when EDR changes its report format.

## The Customization Gap
The gap is a robust parsing engine that: (1) extracts all facility records from the EDR report (PDF or XML), (2) classifies each record by relevance to the subject property (on-site, adjacent, within search radius, outside search radius), (3) evaluates regulatory status using standardized criteria (open/closed case, compliance/violation, proximity and direction relative to subject), and (4) generates draft narrative summaries per database in the firm's preferred style. The parser must handle EDR's evolving format, including the mix of structured tables and free-text narratives within a single report. An NER model trained on environmental regulatory text handles the entity extraction (facility names, addresses, database IDs, violation types, cleanup status), and template-based generation produces the narrative summaries.

## Target Customer
Environmental scientists at Phase I firms who spend 4-8 hours per report manually reading and summarizing EDR radius reports.

## Impact If Solved
Reduces EDR review time from 4-8 hours to 30-60 minutes of verification per report. For a firm completing 300 Phase Is/year, this saves 1,050-2,250 hours annually — a direct capacity increase equivalent to hiring one full-time environmental scientist.
