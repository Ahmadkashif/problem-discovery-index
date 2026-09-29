# Methodology Precedent and Challenge-History Engine
**Niche:** [[niches/accounting-firms-smb/forensic-litigation-support/profile|Forensic Accounting & Litigation Support]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine over the firm's engagement history that tells an expert which damages methodologies the firm has used on comparable facts, and which of them survived Daubert challenge and cross-examination.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #feature-engineering #data-integration #tacit-knowledge-ml #compliance

## The Problem
Methodology selection determines whether an expert report survives. Lost profits, unjust enrichment, reasonable royalty, benefit-of-the-bargain — the choice depends on the claim, the jurisdiction, and the available data, and it is attacked directly under Daubert. A practice that has run six hundred engagements has selected methodologies six hundred times and learned, case by case, which held. That learning sits in individual experts' memories. A newer expert selects from training rather than from the firm's record, and nobody can say the firm has been excluded twice on this approach in this circuit.

## Why Nobody Has Built This
Engagement files are organised around the matter and stored for retention, not analysis. The methodology used, the challenge raised, and the ruling are recorded across reports, motions, and orders with no common structure and no key linking them. Outcomes arrive months or years after the report and often reach only the engagement partner. Building the record means a deliberate capture discipline no practice has imposed on itself.

## What to Build
A structured engagement record capturing claim type, jurisdiction, methodology selected and rejected, data available, and — critically — challenge outcome: was the expert challenged, on what ground, and how did the court rule. The store is queryable by fact pattern, so an expert scoping a new matter sees the firm's own precedent with outcomes attached. A pre-filing pass flags where the proposed methodology has previously drawn successful challenge on comparable facts in that jurisdiction, so the expert either strengthens the support or changes approach before filing rather than after.

## Target Customer
Forensic practice leaders and managing directors of disputes and investigations at firms running 100+ engagements a year.

## Impact If Built
Makes exclusion risk visible before filing. Raises newer experts toward the standard of the firm's most experienced ones. Converts challenge history — currently pure sunk cost — into the practice's most differentiating asset, and into a credibility claim that is directly sellable to referring counsel.
