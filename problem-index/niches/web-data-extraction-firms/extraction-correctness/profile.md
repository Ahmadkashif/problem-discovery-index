# Extraction Correctness

**Parent Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to detect when an extraction is returning plausible wrong values rather than no values — and whoever does that takes the account, because silent corruption is the failure customers cannot defend against.

## Profile
**Market Size:** ~$480M US attributable to correctness rather than to collection
**Share of Parent Industry:** ~24% of category revenue
**Digital Adoption:** None — silent wrongness is undetected
**Target Buyer:** Every customer consuming extracted data in a decision pipeline
**Automation Potential:** High — the signals are present in the data itself

## What Makes This a Distinct Niche
A scraper that fails returns nothing, which is obvious and gets fixed in an hour. A scraper that keeps working after a site redesign, and now reads a different element, returns values with the right type and a plausible range and is invisible. The customer's pricing model, market research or training corpus consumes it for weeks. Every firm in this industry has this problem, none has solved it, and it is the difference between a service a customer can build on and one they must independently verify. The detection signals — distributional shifts, cross-source disagreement, internal inconsistency, plausibility against known constraints — all exist in data the firms already hold.

## Current Tools & Gaps
Structural checks for empty responses and failed selectors, HTTP status monitoring, and spot checks. The gaps: no semantic validation, so a correct-looking wrong value passes everything; no distributional monitoring per field per source; no cross-source consistency checking, though the same entity is frequently collected from several sites; no confidence attached to delivered values; and no way for a customer to know which records to distrust.

## Problems
- [[niches/web-data-extraction-firms/extraction-correctness/build|🔨 Build: The Right Shape and the Wrong Field]]
- [[niches/web-data-extraction-firms/extraction-correctness/buy|🛒 Buy: Data Quality Monitoring and Drift Detection]]
- [[niches/web-data-extraction-firms/extraction-correctness/fix|🔧 Fix: Delivered With No Confidence Attached]]
