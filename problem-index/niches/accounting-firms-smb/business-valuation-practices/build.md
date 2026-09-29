# Precedent Engine Over the Firm's Own Valuation History
**Niche:** [[niches/accounting-firms-smb/business-valuation-practices/profile|Business Valuation Practices]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine that makes a firm's own prior valuations queryable by facts rather than by client name, so an appraiser sees how the firm valued forty comparable businesses — and how those opinions fared when challenged — before selecting a single input.
**Tags:** #gradient-boosting #feature-engineering #cross-validation #evaluation-metrics #large-language-models #data-integration #tacit-knowledge-ml #revenue-impact

## The Problem
Every valuation requires a chain of judgment calls: comparable company selection, discount rate build-up, marketability and minority discounts, normalisation adjustments. Each is defensible individually and each is challengeable. A firm that has issued two thousand opinions has made these calls thousands of times, in documented reports, often on closely comparable businesses. None of it is retrievable by anything except client name and date. An appraiser selects a 25% marketability discount from training and judgment, unaware the firm has applied discounts in the same industry and size band forty times, that the range was 18-32%, and that the two opinions above 30% were both adjusted on challenge.

## Why Nobody Has Built This
Reports are archived as delivered PDFs. The inputs that matter — the comps selected, the discounts applied, the rationale — are structured data trapped in document layout and narrative prose. Extracting them into a queryable base is a data engineering job no firm has funded, because the cost is visible and the benefit is diffuse until the moment a position is challenged. The precedent is also necessarily firm-specific: two credentialed appraisers can take different defensible positions, and a shared industry database would blur the position this firm has actually been defending.

## What to Build
A parser that reads the firm's report archive into a structured valuation base — subject characteristics, approach weightings, comps selected and rejected, discount rates and their build-up components, discounts applied with stated rationale, and where recoverable from engagement records, the outcome of any challenge. For a new engagement the appraiser enters subject characteristics and receives the firm's own distribution of prior treatments on comparable subjects, with rationale and challenge history attached. A pre-delivery pass flags positions that fall outside the firm's own historical range without a documented reason — the specific pattern that draws adjustment.

## Target Customer
Valuation practice leaders and national directors of valuation services at firms issuing 200+ opinions a year.

## Impact If Built
Makes the firm's accumulated judgment available at the moment of decision instead of resident in its most senior appraisers. Narrows unexplained variance between appraisers, which is the firm's real exposure on challenge. Turns the report archive from a storage cost into the practice's most defensible asset.
