# Guidelines Are Rewritten Per Project and Never Accumulate

**Niche:** [[niches/data-analytics-consultants/data-annotation-providers/profile|Data Annotation & Evaluation Providers]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Annotation guidelines are the accumulated resolution of every edge case the firm has ever argued about, and they are written fresh for each programme and archived with it.
**Tags:** #large-language-models #bert #transformers #word-embeddings #k-means-clustering #evaluation-metrics #contrastive-learning #tacit-knowledge-ml #data-integration #worker-facing

## The Problem
A guideline document is the firm's real intellectual property. It encodes how to treat the sarcastic response, the borderline harm case, the answer that is technically correct and unhelpful — every ambiguity discovered during a programme and resolved, usually after argument, usually more than once. When the programme ends the document is archived with the project. The next programme, frequently on a structurally similar task for a different client, starts with a new document written by a different team, which rediscovers the same edge cases and resolves them differently. Quality on a new programme is therefore worst at the start, in a predictable and preventable way, and the firm's accumulated definitional judgment does not compound.

## Why It's Still Broken
Guidelines are treated as project deliverables and are frequently client-owned in whole or part, which has made the entire category feel contractually untouchable rather than partially so — the client owns the task definition; the firm's craft knowledge about how to specify judgment tasks is not the same thing and nobody has separated them. Guidelines also live as prose documents with no structure, so even when a prior one is available it cannot be searched at the level of a specific edge case. And project economics reward getting the current programme running over investing in the next one.

## What a Fix Looks Like
Guidelines maintained as structured, versioned objects rather than documents: each rule an addressable item with its rationale, its worked examples, and the edge cases it was written to resolve, tagged against a task-type taxonomy. Client-specific content is separated from generalizable craft — how to specify a preference comparison, how to handle refusals, how to phrase a severity scale — so the reusable layer can accumulate without touching anything the client owns. When a new programme starts, the relevant prior patterns surface as a starting point rather than a blank page. During a programme, the contested-item clusters from the aggregation model feed directly back as candidate guideline gaps, which is how the document improves during the work rather than after it. And the change history is retained with the annotations it governed, so a dataset can state which guideline version produced it — currently unanswerable and increasingly asked by clients auditing their training data.

## Who Feels the Pain
Programme leads rebuilding definitional work the firm has done before; annotators receiving guidelines that are weakest at the start of a programme; clients whose early data is systematically worse for reasons nobody explains; and the firm, whose most transferable expertise is archived project by project.

## Impact If Fixed
Compresses the quality ramp at the start of every programme, which is where the largest reliable quality loss occurs. It also converts the firm's craft knowledge into an asset that is genuinely its own — in a market where workforce and platform are increasingly commoditized, knowing how to specify a judgment task is the part that is not.
