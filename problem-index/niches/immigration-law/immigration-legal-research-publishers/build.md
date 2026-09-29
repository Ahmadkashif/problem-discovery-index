# The Agency Corpus Nobody Has Structured

**Niche:** [[niches/immigration-law/immigration-legal-research-publishers/profile|Immigration Legal Research Publishers]]
**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Immigration practice turns on agency policy and appeal decisions, and the corpus is treated as documents to be read rather than a body to be queried.
**Tags:** #large-language-models #named-entity-recognition #graph-ml #text-classification #word-embeddings

## The Problem
Pass 1 states the gap directly: the general legal research platforms cover case law and not the USCIS policy memo and AAO decision landscape that matters most in this practice. That is where the publisher lives, and it publishes into the gap as annotated prose.

The underlying material is far more structured than the product treats it. An AAO decision has a petition type, a ground of denial, an evidentiary standard applied, the evidence the petitioner submitted, and a disposition. A policy manual provision has a version history, a superseded predecessor, and a set of memoranda it absorbed. Thousands of these exist, and the relationships between them are the substance of the practice — which is why an attorney facing an RFE spends hours reconstructing by reading what the corpus could answer directly.

Nobody can currently ask: what evidence has satisfied this ground in AAO decisions over the last three years; which provisions changed when this memorandum was rescinded; which of our published guidance rests on a provision that was superseded last month.

## Why Nobody Has Built This
The company is a publisher, and publishing's atomic unit is a document written by an expert. Value has always been added by the annotation — a treatise section explaining what a provision means — and the document remains the container. Structuring the underlying corpus is a different kind of investment than commissioning better annotations, and it competes for the same budget.

The material also looks unstructurable from a distance. AAO decisions are prose, the policy manual is prose, and memoranda are letters. Until recently, extracting a ground of denial and an evidentiary holding from a decision reliably would have meant hand-coding thousands of documents, which nobody could justify. That constraint no longer holds, and the product architecture has not caught up.

And the customers are lawyers, who ask for better commentary because that is what they have always been sold. Nobody is requesting a queryable corpus, so nobody is building one.

## What to Build
A structured layer under the published guidance.

**Extract decisions into fields.** Petition type, ground, standard applied, evidence categories present, disposition, date, and the provisions cited. This makes the AAO corpus answerable by the question an attorney actually has, which is what has ever worked on this ground.

**Model policy provisions as versioned entities with lineage.** Which memorandum a provision absorbed, what it superseded, when it changed, and what the previous text said. Immigration policy moves by memorandum and manual update far more than by rulemaking, and reconstructing the history of a provision is currently manual archaeology.

**Link published guidance to its authorities.** Every treatise section and advisory the publisher has written should be tied to the provisions and decisions it rests on. That single link makes the corpus maintainable: when a provision changes, the affected guidance names itself instead of waiting for an editor to remember.

**Surface evidentiary patterns.** Across AAO decisions on a given ground, which evidence recurs in grants and which in denials. This is a description of the corpus, not advice, and it is the closest legitimate approach to the adjudication pattern knowledge Pass 1 says lives only in individual attorneys' heads.

## Target Customer
Editor-in-chief or VP of Content at an immigration legal research publisher. The competitive logic is uncomfortable and real: a subscription product whose value is expert prose over a public corpus is directly exposed to general-purpose language models reading the same public corpus. The defensible position is the structured, linked, maintained layer — which the publisher can build and a general model cannot.

## Impact If Built
The most expensive task in immigration practice is the RFE response, at eight to twenty hours of attorney and paralegal time, and most of that is reconstructing what has satisfied this ground before. A corpus that answers the question directly attacks the industry's single largest cost item — and it does so from material the publisher already owns and currently ships as reading.
