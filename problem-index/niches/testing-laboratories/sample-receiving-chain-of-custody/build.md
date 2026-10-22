# Reading the Handwritten Chain of Custody into the LIMS

**Niche:** [[niches/testing-laboratories/sample-receiving-chain-of-custody/profile|Sample Receiving, Login & Chain of Custody]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A receiving clerk retypes every chain-of-custody form — sample IDs, times, matrices, analyses — from handwriting, and every typo becomes a data defect downstream.
**Tags:** #large-language-models #transformers #cnns #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a cooler and a handwritten chain-of-custody form into correctly logged, preserved and scheduled work within minutes of arrival, and whoever logs fastest with the fewest transcription errors controls the turnaround the client actually experiences.

## The Problem
A busy environmental or food lab may receive hundreds of coolers a week. Each chain-of-custody form lists samples, collection dates and times, matrices, preservation and requested analyses, often in handwriting, sometimes with abbreviations specific to the client. Login takes several minutes per form and more when something doesn't match the bottles.

## Why Nobody Has Built This
Template OCR fails on varied, handwritten forms, and LIMS vendors have pushed electronic forms that samplers don't use. Until multimodal models, reading a smudged form reliably was not practical.

## What to Build
A login assistant that reads a photo of the form, extracts each field, matches the client and project to the quote and bottle order, maps requested analyses to the lab's method codes, checks holding times and preservation against collection times, and proposes the full LIMS login for the clerk to confirm field by field, with every value linked to its place on the form. Corrections become training data.

## Target Customer
Operations managers at environmental, water and food labs with high cooler volumes.

## Impact If Built
Login time per form cut sharply, transcription errors caught before they reach the bench, and holding-time risks flagged at the door instead of discovered at analysis.
