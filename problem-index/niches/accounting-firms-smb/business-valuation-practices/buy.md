# Market Comp Databases Extended to Firm-Specific Selection Logic
**Niche:** [[niches/accounting-firms-smb/business-valuation-practices/profile|Business Valuation Practices]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Comp databases return every transaction matching a SIC code and revenue band, which is the easy half — the hard half is which of those comps this firm would actually select, and why.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #data-integration #automation

## The Problem
Comparable selection drives the valuation, and it is the input most attacked on challenge. An appraiser queries a transaction database, gets several hundred candidates, and narrows to eight or ten by judgment — screening for business model similarity, deal structure, data quality, and outliers that would distort the multiple. The screening logic is applied fresh each time and documented as a conclusion rather than a method, so it varies between appraisers and cannot be defended as a consistent firm methodology.

## What Already Exists
DealStats, BIZCOMPS, the Pratt's Stats lineage, and Capital IQ provide large, well-maintained transaction and public company comparables with solid search and filtering. Damodaran's datasets supply cost of capital inputs. These are accurate, current, and do their job.

## The Customization Gap
Every one of them returns candidates ranked by query match, not by fit with how this firm selects. The adaptation needed is a selection layer trained on the firm's own history — which candidates it has previously included and excluded for subjects of this type, so the return set is pre-ranked by likely selection and each exclusion carries the firm's precedent for excluding it. That converts comp selection from an unrecorded judgment into a documented, consistent methodology, which is what survives cross-examination.

## Target Customer
Appraisers performing comp selection and the practice leaders accountable for methodology consistency.

## Impact If Solved
Cuts screening time on every engagement and, more importantly, makes selection defensible as firm method rather than individual opinion.
