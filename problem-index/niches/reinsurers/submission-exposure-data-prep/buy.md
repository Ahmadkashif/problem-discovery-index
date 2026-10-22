# Document AI Taught Exposure Schemas

**Niche:** [[niches/reinsurers/submission-exposure-data-prep/profile|Submission & Exposure Data Preparation]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Intelligent document processing already extracts tables from spreadsheets and PDFs; it does not know that "JM" and "joisted masonry" are the same construction class.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a cedent's exposure submission into a model-ready file with a data-quality score within hours of arrival, and whoever's cleaned files need the fewest manual fixes in December takes the account.

## The Problem
Generic extraction tools return the cedent's columns faithfully, leaving all the catastrophe-specific mapping still to do.

## What Already Exists
Intelligent document processing and ETL platforms (Alteryx and others), spreadsheet automation, and vendor import utilities.

## The Customization Gap
The adaptation needs: mapping dictionaries for construction, occupancy and secondary modifiers into each model's codes and the Open Exposure Data format; geocoding with resolution flags; value plausibility checks by region and occupancy; policy-term structuring for financial modules; and memory of each cedent's prior mapping so the second year is nearly automatic.

## Target Customer
Exposure teams at reinsurers and brokers already licensing a document processing platform.

## Impact If Solved
Two to three days of mapping per large submission become hours (estimate), with analysts reviewing only what the tool is unsure of.
