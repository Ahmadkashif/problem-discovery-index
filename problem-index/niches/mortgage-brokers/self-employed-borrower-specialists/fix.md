# Add-Back & Depreciation Inconsistency Across Processors

**Niche:** [[niches/mortgage-brokers/self-employed-borrower-specialists/profile|Self-Employed Borrower Specialists]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Two processors at the same brokerage calculate different qualifying income for the same borrower file because add-back and depreciation rules are interpreted inconsistently.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #tacit-knowledge-ml

## The Problem
Self-employed income calculation requires judgment calls: Is this depreciation on a rental property or a business vehicle? Is this K-1 loss from a related entity that should be netted or an unrelated investment? Should meals/entertainment be added back at 50% or 100%? Experienced processors develop internal heuristics for these decisions over years, but those heuristics diverge between individuals. When a brokerage has 3-4 processors, the same file routed to different people can yield qualifying income differences of $2,000-5,000/month — enough to change which lenders are viable.

## Why It's Still Broken
Brokerages don't have written decision trees for add-back interpretation — the rules are too contextual and change with each lender's guidelines. Training new processors takes 6-12 months of shadowing experienced staff, and even then, judgment varies. Lender underwriters themselves aren't perfectly consistent, which creates a feedback loop where processors learn slightly different "right answers" from different submission outcomes.

## What a Fix Looks Like
A decision-support tool that flags ambiguous add-back scenarios during income calculation, presents the lender's specific guidance for that line item, and shows how the brokerage's historical submissions treated similar situations (with approval/denial outcomes). Not a replacement for processor judgment, but a consistency layer that surfaces the relevant context at the moment of decision.

## Who Feels the Pain
Loan processors who get files kicked back by underwriters for income calculation discrepancies, and brokerage owners who can't scale because processor quality is unpredictable and training takes too long.

## Impact If Fixed
Reduces income calculation variance between processors by 60-80%, cutting underwriter condition requests related to income by an estimated 30%. Shortens new processor ramp time from 6-12 months to 2-3 months by embedding institutional knowledge in the workflow.
