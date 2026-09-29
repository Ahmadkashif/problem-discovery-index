# Document Summarisation Pointed at the Counterparty

**Niche:** [[niches/esignature-document-workflow/signer-side-experience/profile|The Signer Side]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Contract summarisation and clause extraction are sold to legal departments reviewing agreements they receive, and the identical capability pointed at the other party is built by nobody.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #cross-validation #worker-facing
**Contested on:** Every serious competitor that takes the counterparty seriously is fighting to make the person receiving an agreement able to understand it, trust it and ask about it without leaving the envelope — and whoever does that raises completion, which is the only number the sender buys on.

## The Problem
Contract review products summarise agreements, extract obligations and flag unusual terms — for the legal team of a company receiving a contract. The individual contractor, patient, tenant or small supplier receiving an agreement through a signature platform has the same need and none of the tooling, because they are not a customer of anybody. The capability exists and is aimed exclusively at the party who already has lawyers.

## What Already Exists
Clause extraction and classification over contracts is a mature commercial category with public benchmark datasets and strong open models. Language models summarise legal text and answer questions about it well. Obligation and term extraction — parties, dates, amounts, renewal, termination, liability — is standard. Plain-language rewriting works. Retrieval over a clause corpus to judge whether a term is unusual is ordinary. None of it needs inventing.

## The Customization Gap
The adaptation is to an unrepresented signer at the moment of signing. It requires: (1) scoping to description rather than advice, which is the real constraint — saying what a clause commits the signer to and how it compares to typical terms is description; saying whether they should sign is not, and the line must be drawn in the product rather than in a disclaimer; (2) grounding every statement in a clause citation the signer can open, because an ungrounded summary of a legal document is worse than none and because the citation is what makes the description checkable; (3) an unusualness signal built from a corpus of comparable agreements, which is the single most valuable output for a signer with no basis for comparison and is the one thing the sender would prefer not to surface; (4) a genuinely different register from legal-team products — short, concrete, on a phone, in the signer's language, which is a design problem as much as a modelling one; and (5) explicit independence, since a summary presented by the sender's platform will be trusted only if it demonstrably flags things against the sender's interest, and that credibility is the whole asset.

## Target Customer
Signature platform vendors, contract intelligence vendors with an unexploited second market, consumer and worker advocacy organisations, and the high-volume senders whose completion rates depend on counterparty confidence.

## Impact If Solved
Every component is mature and aimed at one side of every agreement. The unusualness signal is the part that makes it genuinely useful to the signer and the part a sender-funded product will be tempted to soften, which is precisely why it determines whether the thing is worth building.
