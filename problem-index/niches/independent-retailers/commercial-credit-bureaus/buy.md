# Entity Resolution Where the Entity Keeps Changing

**Niche:** [[niches/independent-retailers/commercial-credit-bureaus/profile|Commercial Credit Bureaus]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The business identity graph is the product, and small businesses change name, address, legal entity and ownership constantly without telling anyone.
**Tags:** #named-entity-recognition #graph-ml #k-means-clustering #data-integration #evaluation-metrics

## The Problem
Everything the bureau sells attaches to an identified business. Trade lines from thousands of suppliers, public filings, licences, and firmographic records all have to resolve to the same entity — and the entity is a small retailer that trades under a name different from its registered name, moved premises last year, reorganized from a sole proprietorship to an LLC, and is reported by one supplier as "MAIN ST HARDWARE" and another as "Main Street Hdwe Inc".

Two failure modes, both expensive. Fragmentation splits one business across several files, so each looks thinner than it is and the score is worse than the evidence supports. Over-merging combines two unrelated businesses, which puts one company's delinquency on another's file — the error that generates complaints and, occasionally, litigation.

## What Already Exists
Entity resolution and master data management is a mature, well-tooled field — Senzing, Reltio, Informatica, Quantexa and the open-source record linkage libraries all handle fuzzy matching, clustering, and survivorship at scale.

## The Customization Gap
Generic resolution assumes the entity is stable and the records describe it inconsistently. Here the entity itself moves.

**Identity changes are events, not errors.** A business relocating, rebranding, or reorganizing its legal form is the same continuing operation, and the file should follow it. A different business opening at the same address a month later is not. Distinguishing succession from coincidence is the core judgment and generic MDM has no concept of it — it sees two records at one address.

**Legal entity and operating business are different objects.** One owner may run three stores under one LLC, or one store under three entities for tax reasons. Credit risk attaches to the operating business, liability attaches to the legal entity, and a resolution system that collapses them produces confident nonsense in both directions.

**Corporate family structure is a graph with real credit meaning.** Parents, subsidiaries, franchisors and franchisees carry risk relationships that a flat entity model cannot express, and the small business population is full of informal versions of them.

**Asymmetric, quantified error costs.** A false merge places one business's default on another's record — a dispute and a legal exposure. A false split makes a good business look thin. These should not sit at one similarity threshold, and the correct trade-off differs by how the file will be used.

**Resolution decisions need an audit trail.** When a business disputes what is on its file, the bureau must be able to show why those records were linked. Generic MDM stores the surviving golden record and discards the reasoning.

## Target Customer
Head of Data Engineering or VP of Data Quality at a commercial bureau, where the identity graph is simultaneously the core asset and the largest source of customer complaints.

## Impact If Solved
Fragmentation directly depresses scores for exactly the small businesses whose files are already thin, and over-merging produces the errors that damage the bureau's credibility. Modelling identity change as succession rather than as a matching accident improves both at once — and gives the dispute process something to point at.
