# The Corpus Nobody May Look At

**Niche:** [[niches/mlops-platforms/run-corpus-intelligence/profile|Run Corpus Intelligence]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The contract says the vendor may not use customer run data, the aggregate would benefit every customer, and nobody has asked whether a form of aggregation exists that everyone would agree to.
**Tags:** #compliance #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn millions of recorded training runs into answers the field currently gives as folklore — and whoever does that owns the empirical account of how machine learning actually works, which no individual product in the category can match.

## The Problem
Every customer would benefit from knowing what works across the population, and every customer's contract prohibits the vendor from using their data to build it. The prohibition was written to prevent something specific and reasonable — a competitor learning about their models — and it is applied to everything, including aggregate statistics that would identify nobody. The vendor's legal team advises against the whole subject. The product team stops asking. The corpus stays unread, the customers keep re-deriving what the population already knows, and nobody ever put the actual question to the customer.

## Why It's Still Broken
The contract language predates the use case and was drafted to be broadly protective, which is correct drafting. Renegotiating across a customer base is expensive and the benefit is speculative at the time of asking. The first vendor to raise it risks the conversation going badly in public. And there is no reference for what a safe aggregation looks like in this setting, so both sides are negotiating without a template.

## What a Fix Looks Like
Make the specific ask rather than abandoning the general one. Define precisely what would be derived — hyperparameter-to-outcome relationships, learning curve shapes, normalised meta-features — and precisely what would not, since customers refuse open-ended data use and frequently accept a specific, inspectable one, and the difference between those two asks is the whole problem. Offer the customer their own corpus analysis unconditionally, which needs no permission, delivers value immediately, and demonstrates what the aggregate would provide. Make participation opt-in with a visible benefit, so contributing customers receive population-derived recommendations and non-contributors do not, which is a fair exchange rather than an extraction. Publish the aggregation method and let customers or their auditors inspect it, because the objection is to the unknown rather than to the aggregate. Use techniques with stated guarantees where the aggregation is sensitive, and say which. Start with the least sensitive dimensions — learning curve shapes carry almost no competitive information and support the highest-value application — which makes the first ask easy to grant. And write the terms for new customers so the estate converts over time rather than requiring a renegotiation campaign.

## Who Feels the Pain
Customers re-deriving what the population already knows; vendors sitting on their only defensible asset; and the field, which has no empirical account of its own practice because the data is locked in commercial agreements nobody has revisited.

## Impact If Fixed
The prohibition is broad because nobody asked a narrow question. Starting with learning curve shapes — almost no competitive content, highest-value application — makes the first ask easy to grant and the rest follows from a precedent.
