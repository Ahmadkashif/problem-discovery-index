# Data-Rights and Distribution Markings on Every Deliverable

**Industry:** [[contract-research-labs|Contract Research Labs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every report, drawing, dataset and line of code a research firm delivers to the government needs the right data-rights legend, distribution statement and export-control warning, and a missing or wrong legend can hand away rights the firm spent years building.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
A contract research lab delivers paper all the time: monthly status reports, interim and final technical reports, test data, drawings, software. On government work each item must be marked according to who paid for what. Technology developed under an SBIR award carries an SBIR data-rights legend, which protects it for a single, non-extendable period of at least 20 years from award under the 2019 SBA Policy Directive; data developed at private expense can be delivered with limited or restricted rights; data developed with government money goes with unlimited or government-purpose rights. On top sit a distribution statement (A to F under DoD practice), an export-control warning where ITAR or EAR applies, and CUI banners where the contract requires them.

Unmarked SBIR data is delivered with unlimited rights. The firm has six months to correct marking errors, but only if someone notices. The person assembling the final report at 11 p.m. is usually a PI copying the legend block from the last report, which may have been funded differently. A single figure built on internal research inside a report funded by the government can change what legend that page needs.

## What Already Exists
Word templates, SharePoint or Google Drive, document-management systems with metadata fields, and the occasional contracts manager who reviews deliverables before they go out. Defense contractors with large programs run data-management staff and contract data requirements tracking in enterprise tools. Data-loss-prevention products can detect CUI banners and keywords in outgoing files.

## The Customisation Gap
Generic document tools store files and labels; they do not know where the content came from. The research-firm logic is: tracing each section, figure, dataset and code module back to the funding that generated it (this SBIR award, that cost-type contract, internal R&D, a prior commercial project); applying the legend and distribution statement that funding requires under the contract's data-rights clauses; checking export-control and CUI status against the technology; and logging every delivery so the firm can prove, years later, that a page went out with its legend. Data-loss tools look for marks that are present; this problem is about marks that should be present and are not.

## Impact If Solved
A small firm stops gambling its most valuable asset — its SBIR-protected technology — on whoever assembles the final report, and can show a contracting officer a delivery record in minutes when rights are challenged; for a firm whose Phase III value rests on that protection, one prevented marking error can be worth more than the original award (estimate).
