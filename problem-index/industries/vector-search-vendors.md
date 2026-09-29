# Vector Search Vendors

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$1.2B US vector database and retrieval infrastructure, heavily contested and rapidly commoditising
**Tech Maturity:** Excellent engineering on the wrong question — Pinecone, Weaviate, Qdrant, Milvus, Chroma, Turbopuffer and the pgvector extension have made approximate nearest neighbour search fast, scalable and cheap. Whether the results are the right documents is measured by nobody in production, which is the only question the customer actually has.
**Workforce:** Distributed systems engineers, retrieval researchers, solutions architects, developer advocates, support engineers, site reliability engineers

## Key Pain Themes
The category competes on latency, recall against a brute-force baseline, and cost per vector, none of which tells a customer whether their retrieval-augmented application is finding the documents that would answer the question. Real retrieval quality depends on the embedding model, the chunking strategy, the query distribution and the corpus, and the database vendor has visibility into all of them and measures none. Below that sit two persistent operational burdens: hybrid search tuning, where combining lexical and dense retrieval is known to outperform either and the weighting is set by guesswork; and index maintenance under high update rates, where the algorithms that make search fast were designed for mostly-static corpora and degrade in ways that are hard to observe. The engineers supporting it spend their days answering why a specific document was not returned, and rebuilding indexes during maintenance windows.

## Current Tech Landscape
HNSW is the dominant index structure with well-understood build and query trade-offs; IVF and product quantisation variants serve memory-constrained deployments; DiskANN-style approaches address larger-than-memory corpora. pgvector has commoditised the low end substantially by making a vector index a Postgres extension. Managed offerings compete on operational simplicity. Hybrid search combining BM25 with dense vectors is widely supported and inconsistently tuned. Reranking models have become a standard second stage. Embedding models are supplied by third parties and change under the customer, which is a dependency the database vendors have little control over.

## Problems
- [[problems/vector-search-vendors/high-impact|🔴 High Impact: Retrieval Quality Is Unmeasured in Production]]
- [[problems/vector-search-vendors/low-impact-1|🟡 Low Impact: Hybrid Search Weighting]]
- [[problems/vector-search-vendors/low-impact-2|🟡 Low Impact: Index Maintenance Under Update Load]]
- [[problems/vector-search-vendors/worker-life-1|🟢 Worker Life: Solutions Architect Explaining a Missing Document]]
- [[problems/vector-search-vendors/worker-life-2|🟢 Worker Life: SRE on the Index Rebuild]]
- [[problems/vector-search-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/vector-search-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These vendors sit at the exact point where retrieval quality is determined and have defined their product boundary just short of it. They see every query, every returned set, every corpus and — where the application is instrumented — every downstream generation. Whether the retrieval was good is answerable from that, and answering it would move the category from infrastructure competing on cost per vector to a quality layer competing on outcomes. The reason it has not happened is that quality measurement requires opinions about embeddings and chunking that the vendors have deliberately avoided having.
