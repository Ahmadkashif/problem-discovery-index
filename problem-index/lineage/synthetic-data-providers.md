# Lineage: Synthetic Data Providers

**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** the Synthetic Data Vault (SDV) — an open-source Python library that learns a statistical model of a whole relational database, parent and child tables together, and samples a fake database with the same schema, keys and correlations
**Builder:** Massachusetts Institute of Technology
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The data scientist and the data were in different buildings, and the lawyers stood between them.

An organisation with a useful database — transactions, patient records, student logs — could hire outside analysts but could not hand them the rows. Access meant contracts, anonymisation reviews and months of delay, and anonymisation that stripped names often left enough behind to re-identify people. MIT News, reporting on the project in March 2017, calls this the "privacy bottleneck".

The obvious fix — generate fake rows with the same statistics — already existed for single tables. Real business data is not a single table. A customer has many orders; an order has many line items; the interesting patterns sit across those joins. Fake each table separately and the keys stop matching and the cross-table correlations vanish, which is the part an analyst actually needed.

## What Got Built

The Synthetic Data Vault, described in the paper *The Synthetic Data Vault* by Neha Patki, Roy Wedge and Kalyan Veeramachaneni at the IEEE International Conference on Data Science and Advanced Analytics, dated **October 2016**.

The method the paper and MIT News describe is "recursive conditional parameter aggregation". It walks the database schema from child tables up to parents. For each parent row it fits a model of that row's children, then folds those fitted parameters into the parent row as extra columns, so the parent's model learns how its children tend to look. Sampling runs the other way: generate a parent, then generate children consistent with it. The output keeps the schema, the foreign keys and the relationships between tables.

The team tested whether the fake data was good enough to work on. According to MIT News, 39 freelance data scientists were split into four groups, one given real data and three given synthetic versions; across 15 tests on 5 datasets, the synthetic groups' results were comparable to the real-data group's in 11.

## Who Built It, And Why Them

MIT — specifically the Data to AI Lab run by Veeramachaneni, then a principal research scientist in MIT's Laboratory for Information and Decision Systems. The SDV repository says the library was "first created at MIT's Data to AI Lab in 2016".

What made it this lab and not a data owner is where each party sat. A company with a sensitive database had no reason to invent a general method; it could say no to outsiders and stop there. A lab whose work depended on getting other people's data into the hands of analysts met the refusal over and over, and a method that removed the need to share was worth building once and reusing. That motive fits the MIT News framing but is my reading, not a statement from the team.

The artefact then left the university. The repository records that DataCebo was established in 2020 to maintain SDV, and the library is now under the Business Source License rather than a permissive open-source one.

## What It Cost

SDV's test of success was that analysts got similar answers — utility. The 2017 experiment measured whether analysts reached similar results, not whether the output was private in any formal sense — nothing I could read from the project reports such a test. A generator that copies the statistics faithfully enough to be useful can also reproduce rare, identifying records.

The industry inherited that gap. Utility became something a vendor could demonstrate with a quality report; privacy remained an argument.

## What You Still Touch

Commercial tabular synthesisers are sold on multi-table support — foreign keys preserved, relationships intact — and on side-by-side quality reports comparing real and fake distributions. Both are the shape SDV set. The certificate customers actually want, that one dataset is both useful and safe, is still missing.

- [[problems/synthetic-data-providers/high-impact|🔴 Certifying the Privacy-Utility Trade-Off]] — the half of the problem the 2016 design left open
- [[problems/synthetic-data-providers/low-impact-1|🟡 Relational and Constraint Preservation]] — the problem SDV was built to solve
- [[niches/synthetic-data-providers/relational-and-constraint-preservation/profile|Relational & Constraint Preservation]]
- [[niches/synthetic-data-providers/utility-privacy-certification/profile|Utility–Privacy Certification]]
- [[niches/synthetic-data-providers/tabular-privacy-synthesis/profile|Tabular & Privacy Synthesis]]

**Sources:** Semantic Scholar record for Patki, Wedge & Veeramachaneni, "The Synthetic Data Vault", IEEE DSAA 2016, DOI 10.1109/DSAA.2016.49 (publication date 1 October 2016; the abstract is withheld in that record); MIT News, "Artificial data give the same results as real data — without compromising privacy" (3 March 2017; method name, 39 data scientists, 11 of 15 tests, "privacy bottleneck"); GitHub `sdv-dev/SDV` README (MIT Data to AI Lab 2016 origin, DataCebo 2020, Business Source License). WebSearch was not used; research was by WebFetch on known URLs. The MIT copy of the paper PDF returned 404 and IEEE Xplore returned nothing readable, so the paper itself was not read. ⚠️ **Not established:** whether the 2016 paper makes any formal privacy claim — the privacy discussion above rests on MIT News and my reading of the method; the lab's motive is my inference; I did not confirm when SDV's licence changed.
