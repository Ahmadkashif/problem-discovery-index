# Comparable Set Reuse and Jurisdiction Acceptance Memory
**Niche:** [[niches/accounting-firms-smb/transfer-pricing-documentation/profile|Transfer Pricing Documentation Studios]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A store of the firm's benchmarking history that records which comparable sets each tax authority accepted, rejected, or adjusted — so a new study starts from what has actually held in that jurisdiction rather than from a fresh database screen.
**Tags:** #bert #transformers #large-language-models #feature-engineering #evaluation-metrics #cross-validation #data-integration #compliance #revenue-impact

## The Problem
A transfer pricing study rests on a benchmarking set: comparable independent companies used to establish an arm's-length range. Building one means screening a commercial database, applying quantitative and qualitative criteria, and manually reviewing candidates for comparability — days of analyst work per tested transaction. Firms run hundreds of these a year across recurring industries and jurisdictions, and the sets substantially overlap. But each study is built fresh, because prior sets are archived inside delivered documentation rather than held as reusable objects with their acceptance history attached.

## Why Nobody Has Built This
Documentation is produced as a deliverable per entity per year and filed. The screening logic and the resulting set are embedded in appendices, not stored as structured data. Authority responses — an adjustment on audit, a rejected comparable, an accepted range — come back through the controversy side of the practice and are recorded against the audit, never against the benchmarking set that caused it. The join between what was filed and how it fared does not exist.

## What to Build
A benchmarking store holding each set as a structured object: tested party, transaction type, industry, jurisdiction, screening criteria applied, companies accepted and rejected with reasons, resulting range, and the authority outcome where known. New studies begin by retrieving the firm's prior sets for comparable fact patterns, with acceptance history attached, and the analyst refreshes and adjusts rather than rebuilding. Annual refresh — most of the volume — becomes an update against last year's documented set rather than a fresh screen. Sets whose comparables have been rejected in a jurisdiction are flagged before they are reused there.

## Target Customer
Transfer pricing practice leaders and global documentation directors running teams of 20-150.

## Impact If Built
Collapses the dominant cost in documentation production, which is benchmarking labour on studies that largely repeat year over year. Reduces adjustment risk by surfacing what a specific authority has actually accepted. The acceptance record is proprietary and compounding — no competitor can assemble it without the same filing history.
