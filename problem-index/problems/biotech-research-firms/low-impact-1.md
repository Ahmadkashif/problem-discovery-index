# CRO Deliverables Into a Sponsor's Own Record

**Industry:** [[biotech-research-firms|Biotech Research Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A biotech that outsources chemistry, biology, DMPK and toxicology to five or more CROs receives its own data back as PDFs, Excel files and SEND packages in each vendor's layout, and rebuilds the record by hand before anyone can compare a compound across studies.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #data-integration #automation #workflow-orchestration

## The Problem
Most discovery-stage biotechs own little lab capacity. A typical Series A company might buy synthesis from one CRO, in vitro pharmacology from a second, DMPK from a third, in vivo efficacy from a fourth and IND-enabling toxicology from a fifth. Each returns results in its own format: a final report PDF with tables embedded as images, an Excel workbook with the CRO's compound codes, an interim email with a plot, and later a SEND dataset for GLP studies. A scientist at the sponsor copies values into the company's registry or a master spreadsheet, maps the CRO's sample IDs back to the company's compound IDs and batch numbers, normalises units, and notes the assay conditions that make two IC50s comparable or not. A single mistyped batch number can attribute a toxicity finding to the wrong salt form. Little of this work is scientific, and much of it is error-prone.

## What Already Exists
Benchling, Dotmatics and CDD Vault provide registries and assay data stores with import templates. Generic document AI and intelligent document processing tools (AWS Textract, Azure Document Intelligence, Google Document AI) extract tables. Some large CROs offer client portals that export structured data. Data platforms such as Snowflake hold whatever is loaded.

## The Customisation Gap
The generic tools extract tables and store rows; they do not know what a CRO deliverable means. The biotech-specific logic is: mapping CRO sample codes to the sponsor's compound, batch and salt-form identifiers; recognising assay types and conditions (cell line, ATP concentration, incubation time, species, matrix) so that results are only compared when comparable; reading DMPK report conventions (Cmax, AUC, half-life, dose-normalised or not); flagging when a CRO's report disagrees with its own interim email; and keeping the provenance chain that a partner's or acquirer's diligence team will ask for. Each vendor's layout changes between studies, so per-vendor templates break, and the generic tool's template approach does not survive the third CRO.

## Impact If Solved
A sponsor-side intake layer that turns every CRO deliverable into structured, compound-linked, provenance-tagged records within a day would remove an estimated several days of scientist time per month at a small biotech (estimate). It would also cut identifier errors and leave a diligence-ready data room as a by-product rather than a pre-financing scramble.
