# Posting Extraction Adapted to Stated Versus Real Requirements

**Niche:** [[niches/corporate-training/labor-market-skills-data/profile|Labour Market & Skills Taxonomy Data Providers]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Text extraction pulls every skill mentioned in a posting; the analytically useful quantity is which of them the employer would actually reject a candidate for lacking, and postings do not say.
**Tags:** #bert #transformers #large-language-models #transfer-learning #word-embeddings #feature-engineering #evaluation-metrics #causal-inference #automation #data-integration

## The Problem
A job posting is a marketing document, not a specification. It lists aspirational requirements, boilerplate inherited from a template, skills copied from a competitor's ad, and a smaller set of things the employer genuinely will not hire without. Extraction treats them alike, so demand estimates are inflated in predictable directions — long-tail tools appear in demand because they appear in text, and the actual binding constraints are diluted among them. Employers and educators then plan capability investment against a signal that overstates breadth and understates depth. Analysts know this and correct for it informally in client conversations, which means the correction is neither systematic nor visible in the data product.

## What Already Exists
Text extraction and entity recognition are commodity capabilities. The transformer-based NER stacks, the commercial document AI services, and fine-tuned classification models all identify skill mentions in job text at high accuracy and low cost. Several vendors sell skill extraction as an API.

## The Customization Gap
All of them answer whether a skill is mentioned. None answers whether it is required, because that requires evidence from outside the document — who was actually hired, how long the posting stayed open, whether it was reposted with the requirement dropped, and how the requirement correlates with compensation. The adaptation is a requirement-weight model rather than a mention extractor: each extracted skill carries an estimated bindingness derived from posting dynamics, hiring outcomes where observable, phrasing signals that distinguish a hard requirement from a preference, and template detection so that inherited boilerplate is discounted. Posting duration and repost behaviour are strong available signals that no general extractor uses. The output is a weighted demand estimate rather than a count, which is a different and much more defensible product, and the weights can be validated against the subset of postings where hiring outcomes are observable.

## Target Customer
Heads of data science and taxonomy at labour market data providers, and the workforce planners who currently treat mention frequency as demand and plan training investment accordingly.

## Impact If Solved
Corrects the systematic bias in the flagship metric, which is the kind of improvement that shows up directly in whether clients trust the product against their own hiring experience. Requirement weighting also opens the analysis clients most want and nobody sells — which specific skills are actually gating hiring, as distinct from which appear most often in text.
