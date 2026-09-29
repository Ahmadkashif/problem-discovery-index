# Lineage: Database Platform Vendors

**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the cost-based query optimizer — System R's access-path selector, which picks a plan from catalog statistics
**Builder:** IBM
**Builder in vault:** **ABSENT**
**Verification:** verified — see Sources

## The Problem That Came First

Relational databases had a performance problem before they had a customer.

The relational model asked a user to say *what* data they wanted and never *how* to fetch it. That was the whole appeal and also the objection. A navigational database made the programmer walk the access path by hand, and a good programmer walked it well. A relational engine had to choose the path itself — which index, which join order, which table first — for queries it had never seen. If it chose badly, declarative queries would simply be slow, and the model would stay an academic idea.

## What Got Built

A program that prices every plan and runs the cheapest.

It was described in **"Access Path Selection in a Relational Database Management System"** — Patricia Selinger, Morton Astrahan, Donald Chamberlin, Raymond Lorie and Thomas Price, **ACM SIGMOD, 1979**. The optimizer looks up statistics about each table in the system catalog — cardinality, pages, distinct index keys — assigns every predicate a **selectivity factor**, estimates the cost of each access path as page fetches plus weighted CPU calls, and searches join orders by dynamic programming.

Where statistics are missing the paper simply guesses. An equality predicate on an unindexed column gets **F = 1/10**; an open range on a non-numeric column gets **F = 1/3**. "We assume that a lack of statistics implies that the relation is small, so an arbitrary factor is chosen."

PostgreSQL, MySQL, Oracle and every engine this industry sells still descend from this shape: statistics in, estimated cost out, one plan chosen.

## Who Built It, And Why Them

IBM, at its San Jose Research Laboratory, and the reason is that IBM had to prove the idea before it could sell it.

The relational model came from IBM's own research. **System R began at San Jose in 1974** with a stated purpose: to show that relational usability could be had "with the complete function and high performance required for everyday production use." That is a performance claim, and the optimizer is where the claim was either won or lost. No customer was going to trust an engine to choose its own access paths unless the engine chose as well as a programmer did.

Only a vendor with a research lab, a large installed base to protect and a product roadmap to feed could afford five years of work whose output was an argument. It fed that roadmap directly: **IBM shipped SQL/DS in 1981 and DB2 two years later**, both descended from System R.

## What It Cost

**The plan depends on statistics, and the statistics are deliberately allowed to go stale.**

The paper is explicit. Statistics are set at load and index creation, then "updated periodically by an UPDATE STATISTICS command." System R did **not** refresh them on every insert, update or delete "because of the extra database operations and the locking bottleneck this would create at the system catalogs."

That was a sound trade in 1979: concurrency now, accuracy later. It means the optimizer is always reasoning about a table as it was, not as it is. When a table grows past what its statistics describe, or a value's distribution shifts, the estimated cost of plans moves and the chosen plan can flip — silently, on a query that ran fine yesterday. The default guesses compound it: a 1/10 selectivity assumed for a missing statistic is a number nobody measured.

## What You Still Touch

Every `EXPLAIN` a developer runs today prints a cost estimate built on this design, and every `ANALYZE` job exists to pay down the staleness the 1979 paper chose to accept. The industry's defining pain — degradation that is gradual, then sudden — is very often a plan flipping because statistics drifted.

- [[problems/database-platform-vendors/high-impact|🔴 Degradation That Is Only Visible at the End]] — plan flips on drifted statistics are its commonest form
- [[problems/database-platform-vendors/worker-life-2|🟢 The Developer Writing Queries Blind]] — the price of never saying *how*: the engine chooses, and the author cannot predict what
- [[niches/database-platform-vendors/gradual-degradation-detection/profile|Gradual Degradation Detection]]
- [[niches/database-platform-vendors/the-application-developer/profile|The Application Developer]]

**Sources:** Selinger, Astrahan, Chamberlin, Lorie & Price, *Access Path Selection in a Relational Database Management System*, Proc. ACM SIGMOD 1979 (dl.acm.org/doi/10.1145/582095.582099; full text read from courses.cs.washington.edu) — selectivity factors, the UPDATE STATISTICS passage and the locking rationale are quoted from the paper itself; Wikipedia, *IBM System R* and *IBM Db2*, and dbdb.io, *System R* (1974 start, stated purpose, SQL/DS 1981, DB2 two years later); the morning paper (acolyer.org) summary. ⚠️ **Not established:** that PostgreSQL's or any other named engine's planner was built directly from the paper rather than from the common tradition it founded — "descend from this shape" is meant architecturally, not as a documented code lineage. IBM's internal commercial reasoning (protecting its IMS installed base) is inferred from the project's stated goal, not from a primary IBM planning document.
