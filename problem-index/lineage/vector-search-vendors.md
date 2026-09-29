# Lineage: Vector Search Vendors

**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** FAISS — Facebook AI Research's C++/Python library for similarity search over dense vectors, built around an `Index` object (`IndexFlatL2`, inverted-file and product-quantisation indexes, with GPU drop-ins) that trades search time, recall and memory per vector; first committed to GitHub 22 February 2017
**Builder:** Facebook
**Builder in vault:** **ABSENT**
**Verification:** verified — dates from the repository and papers; see Sources for gaps

## The Problem That Came First

A neural network turns an image, a video frame or a sentence into a list of a few hundred numbers. Two similar things get nearby lists. That is useful only if you can ask, of a billion stored lists, *which are nearest to this one?* — fast.

A relational database cannot answer that question. Facebook's own launch post said so: traditional databases "are not adapted to these new representations," and SQL makes similarity matching over billions of high-dimensional vectors "inefficient if not impossible." Exact search compares the query with every stored vector, and a billion uncompressed vectors outgrow one server's memory.

**The constraint was memory first and arithmetic second.** Any practical answer had to compress the vectors, accept some loss of accuracy, and still search the compressed form directly.

## What Got Built

FAISS, which the first README describes as "built around an index type that stores a set of vectors."

That `Index` abstraction is the artefact. Each index type is an explicit trade-off, which the README lists: search time, search quality, memory per vector, training time, and need for training data. `IndexFlatL2` is exact brute force. The compressed indexes rest on **product quantisation**, which splits each vector into sub-vectors and replaces each with a short code, so that — in the README's words — they "can scale to billions of vectors in main memory on a single server." GPU indexes were drop-ins: `GpuIndexFlatL2` for `IndexFlatL2`.

The companion paper, "Billion-scale similarity search with GPUs" (arXiv, 28 February 2017), reported an 8.5x speedup over prior GPU work and built a k-nearest-neighbour graph on 1 billion vectors in under 12 hours on four GPUs. A graph index, HNSW, was added in a January 2018 sync.

## Who Built It, And Why Them

Jeff Johnson (Facebook AI Research, New York), Matthijs Douze and Hervé Jégou (both FAIR Paris), per the paper's title page.

**Why Facebook:** it was producing neural embeddings for its own images and video at a scale where exact search was out of reach. The launch post, dated 29 March 2017, frames the use cases as finding similar images across huge collections and searching "billions of vectors from images, videos, and text documents." The paper's "flagship application" is the k-NN graph — relating every item in a collection to its nearest neighbours — at a scale the paper says prior methods "cannot readily scale to."

**Why these people:** the method was theirs before the library was. The paper builds on "Product quantization for nearest neighbor search" by Jégou, Douze and Schmid, *IEEE TPAMI*, January 2011 — cited as the original PQ proposal.

## What It Cost

**Recall.** Every compressed index returns approximate neighbours. The README states the price directly: compact codes come "at the cost of a less precise search." FAISS made that trade tunable, but the tuning is measured against brute-force search, not against whether the retrieved item was the right answer.

**Mutation.** Quantisers and inverted lists are *trained* on a sample of the data. The design assumes a collection that is built, then searched — not one rewritten every minute.

The licence was also a cost, for a while. FAISS launched under Creative Commons NonCommercial-NoDerivatives, relaxed to CC-BY-NC on 9 March 2017, moved to BSD on 30 July 2017, and was relicensed "BSD+Patents -> MIT" on 28 May 2019.

## What You Still Touch

The vocabulary of every vector database — index type, recall at k, IVF lists, PQ codes, `nprobe` — is FAISS's vocabulary, and several engines embed FAISS directly. What the index measures is recall against exact search; what the customer needs to know is whether the right document came back.

- [[problems/vector-search-vendors/high-impact|🔴 Retrieval Quality Is Unmeasured in Production]] — recall-versus-brute-force, inherited as the category's metric
- [[problems/vector-search-vendors/low-impact-2|🟡 Index Maintenance Under Update Load]] — the cost of indexes trained on data that sits still
- [[problems/vector-search-vendors/worker-life-2|🟢 SRE on the Index Rebuild]]
- [[niches/vector-search-vendors/vector-index-infrastructure/profile|Vector Index Infrastructure]]
- [[niches/vector-search-vendors/index-drift-under-mutation/profile|Index Drift Under Mutation]]

**Sources:** GitHub, `facebookresearch/faiss` — initial commit and README (22 February 2017) read at `c670118`; LICENSE history via the GitHub API (commits of 22 February 2017, 9 March 2017, 30 July 2017, and the 28 May 2019 relicense message); commit search for the January 2018 HNSW sync; Johnson, Douze and Jégou, "Billion-scale similarity search with GPUs," arXiv:1702.08734 (28 February 2017) — affiliations, flagship application and reference [25] read from the PDF; Facebook Engineering, "Faiss: A library for efficient similarity search" (29 March 2017); Wikipedia, *FAISS*, for use inside OpenSearch, Milvus and Vearch. WebSearch was unavailable this session (budget exhausted). ⚠️ **Not established:** the authors' affiliation when the 2011 PQ paper was written (the CrossRef lookup did not return it); which specific Facebook product first ran FAISS in production; and whether any commercial vector database was built on FAISS first — not claimed. `nprobe` is confirmed as a parameter in the initial commit's `IndexIVF.h`.
