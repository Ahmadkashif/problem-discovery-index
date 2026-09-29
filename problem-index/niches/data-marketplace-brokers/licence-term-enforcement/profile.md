# Licence Term Enforcement

**Parent Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make permitted-use terms something the delivery path can read and enforce rather than prose somebody has to remember — and whoever does that takes the account, because compliance currently depends on institutional memory.

## Profile
**Market Size:** ~$420M US
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Very Low — prose enforced by nothing
**Target Buyer:** Data governance, legal and platform teams
**Automation Potential:** High — extraction and enforcement are both buildable

## What Makes This a Distinct Niche
Every dataset arrives with terms: which business units may use it, for what purposes, whether derivatives may be created, whether it may be combined with other sources, whether outputs may be shared externally, whether it may train a model, and for how long. Those terms are contract prose. Nothing in the pipeline, the warehouse, the catalogue or the model training path knows what they say. Two years later the person who negotiated them has moved on, the dataset is a table among thousands, and an analyst uses it for something the licence forbids without any possibility of knowing. The exposure is real, it grows with every purchase, and the fix is a translation problem from prose into structure that nobody has taken on.

## Current Tools & Gaps
Contract repositories, spreadsheets tracking obligations, and data catalogues with a free-text notes field. The gaps: terms are not extracted into structure, so nothing downstream can evaluate them; no propagation to derived tables, which is where most use actually happens; no enforcement point in the query or training path; expiry and termination are not tracked, so data is used past its licence; and no audit trail showing what a dataset was used for.

## Problems
- [[niches/data-marketplace-brokers/licence-term-enforcement/build|🔨 Build: Permitted Use Written in Prose]]
- [[niches/data-marketplace-brokers/licence-term-enforcement/buy|🛒 Buy: Policy Engines and Rights Expression]]
- [[niches/data-marketplace-brokers/licence-term-enforcement/fix|🔧 Fix: The Derived Table Nobody Tagged]]
