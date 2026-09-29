# Knowledge Retrieval Adapted to Analyst Position, Not Document

**Niche:** [[niches/cloud-infrastructure-consultants/it-research-advisory-firms/profile|IT Research & Advisory Firms]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise search finds the note; an analyst preparing for a call needs the firm's current position on a vendor, how it has moved, and whether a colleague published something last week that contradicts it.
**Tags:** #bert #transformers #large-language-models #word-embeddings #graph-neural-networks #contrastive-learning #evaluation-metrics #transfer-learning #workflow-orchestration #data-integration

## The Problem
An analyst taking an inquiry has minutes to establish what the house currently thinks about a vendor, a category, and their intersection. The corpus is tens of thousands of notes accumulated over decades, written by hundreds of analysts, many superseded and none marked as such. Search returns documents ranked by relevance to a query, which answers a different question — the analyst does not want documents, they want the position and its history. So the practical method is personal knowledge plus asking a colleague, which works within a coverage area and fails across them. The most visible symptom is the one that damages the brand: two analysts giving clients contradictory positions on the same vendor, discovered when the client mentions it.

## What Already Exists
Enterprise knowledge management and retrieval is a crowded, capable market. Glean, Coveo, Guru, and the retrieval-augmented generation stacks all provide semantic search across document corpora with permissions awareness, freshness signals, and generated summaries with citations. Deployment is fast and the base quality is good.

## The Customization Gap
Every one of them treats the corpus as documents and the answer as retrieval. A research firm's actual knowledge object is a position — the house view on a vendor's execution, a category's trajectory, a technology's maturity — which is expressed across many documents, revised over time, and sometimes disputed between analysts. Documents are how positions are published, not what they are. Nothing off the shelf models supersession, so a note from four years ago surfaces beside last quarter's with equal authority; nothing models disagreement, so contradictions stay invisible until a client finds them; and nothing distinguishes an analyst's tentative view from a ratified house position, which is the distinction that matters most when speaking to a client. The adaptation is a position layer over the corpus: positions as first-class entities with subject, stance, confidence, and revision history, extracted from published content and maintained as analysts write, with contradiction detection across analysts and coverage areas. Retrieval then answers the question actually being asked — here is the current house position, here is how it moved and when, here is where a colleague disagrees.

## Target Customer
Heads of research operations and knowledge management at advisory firms, and the analysts who currently prepare for inquiry calls by asking whoever they think might know.

## Impact If Solved
Removes the most common quality failure in the delivery model, which is inconsistency between analysts, and makes cross-coverage inquiry — the growing share, as technology decisions span categories — answerable at the same quality as within-coverage. The position graph is also the precondition for scoring predictions, since a prediction cannot be evaluated until the firm can say what it actually claimed and when.
