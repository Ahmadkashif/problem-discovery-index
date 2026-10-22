# Claim Charts Built Outside the Search Platform

**Industry:** [[legal-support-services|Legal Support Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Patent search platforms find documents; the deliverable a search house sells is a claim chart mapping every claim element to a passage, and analysts still build it by hand in Word or Excel after the search ends.
**Tags:** #transformers #large-language-models #bert #evaluation-metrics #feature-engineering #automation #workflow-orchestration

## The Problem
An invalidity or patentability search is bought as a report, not a list. For each relevant reference the analyst records which claim elements it discloses, quotes the passage and figure that discloses each one, rates the reference (closest art, combinable art, background), and explains what is missing. For an invalidity search on a patent with three independent claims and forty dependents, that is hundreds of cells, assembled after the search from PDFs, machine translations of foreign references and screenshots of figures. The analyst then rewrites the chart in the client's format: an IPR petition chart, a district-court invalidity contention exhibit, an in-house review table.

Charting is where the hours go. It is also where errors enter: a passage pasted against the wrong element, a translated quote that does not match the certified translation the litigator later orders, a dependent claim silently skipped.

## What Already Exists
Derwent Innovation, Questel Orbit, PatSnap, LexisNexis TotalPatent and newer AI search tools rank and annotate documents, highlight claim terms and export result sets. Several now draft a first-pass claim chart with a language model. General document tools (Word, Excel, Adobe) carry the rest.

## The Customisation Gap
The platforms chart against the language they see, not against how a search house works. The gaps are: element-level parsing of the target claims that follows the client's construction rather than the literal wording; passage citation that survives to the certified translation and the figure numbering; a rating scheme that matches the house's own categories and the patent office's (X, Y and A citations in search reports); combination logic for obviousness charts across two or three references; output formats for IPR petitions, contentions and in-house tables from one underlying record; and a review trail showing which cells the analyst confirmed. Each house has rebuilt some of this in spreadsheets; none of the platforms holds the charted record as structured data.

## Impact If Solved
Turning the chart into structured output of the search rather than a document assembled afterwards could take an estimated third or more off the analyst hours in each invalidity report, and makes the house's charted history searchable for the next engagement on the same patent family — the start of the archive that the industry's insight layer depends on.
