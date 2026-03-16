# Comparative Rater Data Re-Entry Across Carrier Portals

**Industry:** [[independent-insurance-agents|Independent Insurance Agents]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The same ACORD application data gets typed into 5-10 carrier portals because commercial lines bridge rating doesn't exist the way personal lines raters do.
**Tags:** #llm #named-entity-recognition #nlp #automation #data-integration

## The Problem
For every commercial lines submission, a producer or CSR fills out an ACORD application (125/126 for general liability, 130 for workers' comp, 140 for property), then manually enters the same information — business name, FEIN, NAICS code, revenue, payroll, location details, loss history — into each carrier's proprietary quoting portal. A single commercial account submitted to 5 carriers means entering the same 40-60 fields five times, each portal with slightly different field names, dropdown options, and required attachments. This takes 15-30 minutes per carrier portal, totaling 1-3 hours per account before a single quote is returned.

## What Already Exists
Personal lines comparative raters (EZLynx, TurboRater, ITC) solve this for auto and homeowners by maintaining real-time API connections to carrier rating engines — enter the data once, get 8-12 quotes back. Commercial lines platforms like Bold Penguin and Tarmika are building toward this but cover a narrow slice of commercial classes and a limited carrier panel. IVANS and ACORD standards exist but carrier adoption of standardized API intake is inconsistent, with most carriers still requiring portal-based entry for anything beyond the simplest BOP.

## The Customisation Gap
The gap is not in the rater concept but in commercial lines data normalization. Each carrier maps ACORD fields differently, uses proprietary class codes alongside or instead of ISO codes, and requires supplemental questions that vary by state, class, and line of coverage. A solution must parse ACORD forms (often completed as PDFs or in AMS-generated XML), map fields to each carrier's portal schema, handle carrier-specific supplemental questions, and pre-fill portal forms via browser automation or API where available. This requires NER on insurance-specific documents and a carrier-by-carrier field mapping layer that general-purpose form-filling tools cannot provide.

## Impact If Solved
Eliminates 1-3 hours of data entry per commercial account submission, freeing CSRs and producers to handle 30-40% more submissions per day. Reduces transcription errors that cause carrier declinations on technicalities.
