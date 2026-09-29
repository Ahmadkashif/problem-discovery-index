# Financial Statements That Arrive as PDFs Eighteen Months Late

**Niche:** [[niches/municipal-services/municipal-credit-rating-analysis/profile|Municipal Credit Rating & Public Finance Analysis]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every input to a municipal credit analysis is a several-hundred-page audited document with no standard format, filed whenever the auditor finishes.
**Tags:** #ocr #large-language-models #named-entity-recognition #data-integration #anomaly-detection

## The Problem
A municipal analyst's raw material is the annual comprehensive financial report: several hundred pages of fund-level statements, notes, schedules, and statistical sections, prepared under governmental accounting standards, laid out however that government's auditor chose, and filed months to well over a year after the fiscal year it covers.

Everything the analysis needs is in there — fund balances, revenue composition, debt service coverage, pension funding, and the disclosures that reveal a problem before the numbers do. Getting it out is manual. Analysts key figures into spreadsheets, and the same issuer's statements are re-keyed every year by whoever covers it.

The lag compounds it. By the time a statement is filed, the fiscal picture may have moved materially, and the interim signals that would fill the gap — budget amendments, bond disclosures, local news — are unstructured and scattered.

## What Already Exists
Financial document extraction is a mature commercial capability for corporate filings, where structured taxonomies exist. Document processing platforms handle classification, table extraction, and review routing well.

## The Customization Gap
Corporate extraction works because filings are standardized and machine-readable. Municipal reporting is neither.

**Fund accounting is a different data model.** Governmental statements report by fund with a reconciliation to government-wide statements, and the analytically meaningful figures often require combining across funds under rules that vary with how the government structured its reporting. Generic financial extraction has no concept of it.

**No two layouts match.** Every auditor formats differently, and a given government's presentation changes when it changes auditors. Layout-based extraction has nothing stable to anchor to; the extraction has to be semantic.

**The notes carry the signal.** Pension assumptions, contingent liabilities, subsequent events, and going-concern language sit in prose and are frequently the earliest indication of trouble. That is reading comprehension over long documents, not table extraction.

**Interim signals must be fused.** Between annual filings, the useful evidence is budget documents, continuing disclosure notices, bond offering statements, and local reporting — different sources with different structures, and each government publishes on its own schedule.

**Comparability across time and standards.** Accounting standards change and reshape presentation, so a series has to be reconciled across standard versions or the trend is an artefact.

## Target Customer
Chief Data Officer or head of research operations at a rating agency or municipal data provider, where analyst time spent extracting is time not spent analysing.

## Impact If Solved
Extraction is the bottleneck on coverage depth and surveillance frequency across tens of thousands of credits. Making the statements into a comparable panel is what makes any modelling possible at all — and reading the notes systematically catches the disclosures that today depend on an analyst noticing a sentence on page 180.
