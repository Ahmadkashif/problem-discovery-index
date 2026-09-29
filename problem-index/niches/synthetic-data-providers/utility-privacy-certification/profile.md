# Utility–Privacy Certification

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to certify that a synthetic dataset is simultaneously safe to release and useful to train on — and whoever issues that claim credibly takes the category, because it is the only claim customers are actually buying.

## Profile
**Market Size:** ~$420M US attributable to the guarantee rather than the generation
**Share of Parent Industry:** ~28% of category revenue
**Digital Adoption:** None — two separate metric sets that do not compose into the claim
**Target Buyer:** Privacy, legal and model teams jointly, which is why nobody owns it
**Automation Potential:** High for the measurement; the standard is a field-level problem

## What Makes This a Distinct Niche
Customers buy a guarantee that synthetic data is both safe to release and useful to train on, and the industry ships two separate sets of metrics that do not compose into that claim. The two properties trade off directly: turn up fidelity and the synthetic records begin to memorise real individuals; turn up privacy and the data stops supporting the models it was generated for. A vendor reports distribution comparisons on one side and a differential privacy parameter on the other, chosen by the vendor, and the customer is left to combine them into a decision nobody has given them a framework for. This is the category's defining gap and it is a certification problem rather than a generation problem — the generation is good, and what is missing is a defensible statement about the result.

## Current Tools & Gaps
Statistical fidelity comparisons, train-on-synthetic evaluation where customers run it, differential privacy with a chosen parameter, and membership and attribute inference attacks run inconsistently. The gaps: the two sides are reported separately and the frontier between them is not characterised, so a customer cannot see the trade-off they are making; the privacy parameter is frequently chosen for utility rather than for meaningful protection, which is a practice the field acknowledges and does not report; empirical attacks are run inconsistently and by the vendor, which is the party with an interest in the result; the utility measure is statistical similarity rather than downstream model performance, which is the thing that matters; and no independent certification exists, so every claim is the vendor's own.

## Problems
- [[niches/synthetic-data-providers/utility-privacy-certification/build|🔨 Build: Two Metric Sets That Do Not Compose Into the Claim]]
- [[niches/synthetic-data-providers/utility-privacy-certification/buy|🛒 Buy: Privacy Auditing Methods That Exist]]
- [[niches/synthetic-data-providers/utility-privacy-certification/fix|🔧 Fix: The Epsilon Chosen for Utility]]
