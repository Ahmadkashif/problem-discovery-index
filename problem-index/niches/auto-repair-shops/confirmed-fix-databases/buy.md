# Retrieval Adapted to Symptom Description, Not Keyword

**Niche:** [[niches/auto-repair-shops/confirmed-fix-databases/profile|Confirmed-Fix Diagnostic Knowledge Databases]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise search products retrieve documents that match a query; a technician's query is a description of a car misbehaving, and matching it to prior cases requires knowing which parts of that description are diagnostically load-bearing.
**Tags:** #bert #transformers #word-embeddings #contrastive-learning #large-language-models #transfer-learning #evaluation-metrics #k-nearest-neighbors #automation #worker-facing #data-integration

## The Problem
The database's value is entirely gated by retrieval. A technician types what they are seeing — a rough idle that clears above two thousand RPM, present only when cold, with a lean code but no misfire — and needs the prior cases that are diagnostically similar, not the ones that share the most words. Keyword search returns everything mentioning the code, which on a common code is thousands of records, and the technician gives up or calls the hotline, which costs the publisher its most expensive resource. Vocabulary makes it worse: the same condition is described a dozen ways across the trade and across the records themselves, since fix records were written by different specialists over decades with no controlled terminology.

## What Already Exists
Search and retrieval are mature and inexpensive. Elasticsearch and OpenSearch handle hybrid keyword and vector search with faceting and relevance tuning; the managed vector databases and embedding APIs make semantic retrieval a weekend integration; commercial enterprise search products add ranking, personalization, and analytics. For general document retrieval, everything needed is available off the shelf.

## The Customization Gap
General semantic search embeds the whole query and finds textually similar records, which systematically retrieves the wrong things here. Diagnostic similarity is not textual similarity: two descriptions sharing most of their words can point to different root causes, while two sharing almost none can be the same fault. What determines relevance is which specific elements of the description discriminate — the cold-only condition, the absence of a misfire alongside a lean code — and general embeddings weight those the same as incidental detail. The adaptation is a symptom model in front of retrieval: the technician's description parsed into structured elements — condition, circumstance, code presence and absence, what has already been tested and ruled out — resolved against a controlled symptom vocabulary that carries the trade's synonyms, and matched on diagnostic discriminators rather than on text. Vehicle applicability has to constrain retrieval structurally, since a fix for a different engine family is noise regardless of how well the symptoms match. And ranking should be trained on what actually resolved cases, which the publisher can observe, rather than on click-through.

## Target Customer
Product leads and directors of content at confirmed-fix publishers, and the hotline managers whose call volume is a direct measure of retrieval failure.

## Impact If Solved
Every call avoided is margin, and call volume is the cleanest available signal of where retrieval fails — so improvement is measurable from the first week. More strategically, retrieval quality is what determines whether a subscriber renews: the corpus is already the best in the industry, and the product is judged on whether the technician can get to the right record while the car is still on the lift.
