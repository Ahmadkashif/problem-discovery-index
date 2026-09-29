# Expert-Tier Quality

**Parent Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to establish whether an expert judgement is correct when no ground truth exists and reasonable experts disagree — and whoever does that takes the frontier contracts, because consensus arithmetic is the industry's only quality signal and it does not work here.

## Profile
**Market Size:** ~$1.1B US expert-tier annotation and evaluation data
**Share of Parent Industry:** ~28% of category revenue and the fastest-growing tier
**Digital Adoption:** Low — the mechanisms in use were built for a different kind of task
**Target Buyer:** Frontier laboratories and enterprise model teams
**Automation Potential:** High for the measurement design; the underlying problem is genuinely hard

## What Makes This a Distinct Niche
This industry sells ground truth, which means it cannot check its output against ground truth. Every quality mechanism in the category — multi-annotator consensus, gold-standard seeding, reviewer sampling — is a proxy, and each degrades as tasks get harder. Three annotators agreeing on a bounding box is strong evidence; three experts agreeing that a legal argument is sound is weaker evidence and three disagreeing is not evidence of poor quality at all, because the task may have no single right answer. The market has moved decisively toward exactly these tasks, which means the industry is delivering its most expensive product with its weakest quality signal, and the buyers — who are sophisticated and are training models on this data — increasingly know it. The contest is a quality framework that holds when the task is genuinely hard.

## Current Tools & Gaps
Multi-annotator consensus with agreement statistics, gold-standard tasks seeded into batches, reviewer sampling, and contributor reputation scores. The gaps: agreement is reported as a quality measure when on hard tasks it partly measures task ambiguity, and the two are not separated; gold standards are unavailable for tasks where the vendor cannot produce a known answer either, which is the definition of the expert tier; adjudication of genuine disagreement is manual and rare; nothing estimates the achievable agreement ceiling for a task, so a project is judged against an implicit expectation nobody has set; and the downstream measure that matters — whether the data improved the model — is occasionally available and almost never used.

## Problems
- [[niches/data-labeling-services/expert-tier-quality/build|🔨 Build: Selling Ground Truth Without Access to It]]
- [[niches/data-labeling-services/expert-tier-quality/buy|🛒 Buy: Psychometrics for Tasks With No Answer Key]]
- [[niches/data-labeling-services/expert-tier-quality/fix|🔧 Fix: Agreement Reported as Quality]]
