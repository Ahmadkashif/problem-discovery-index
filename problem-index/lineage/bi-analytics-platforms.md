# Lineage: BI & Analytics Platforms

**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** the Business Objects universe — a semantic layer of named business "objects" mapped onto the tables and joins of a relational database, from which a query engine writes the SQL (US Patent 5,555,403, filed 27 November 1991)
**Builder:** Business Objects
**Builder in vault:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

By the end of the 1980s the numbers a manager wanted were already in a relational database. Oracle had sold the database; what it had not sold was a way for anyone outside IT to ask it anything.

Asking meant SQL, and SQL meant knowing the schema: which table held revenue, which column held the region code, and — the part that actually broke people — which join path connected them. Two tables can be connected by more than one route, and each route produces a different, perfectly valid number.

**So every business question had a queue in front of it, and the person at the head of the queue decided, silently, what the question meant.** Two programmers given the same request could return two answers, both right.

## What Got Built

A layer of vocabulary between the user and the database.

The patent Jean-Michel Cambot and Bernard Liautaud filed on 27 November 1991, granted on 10 September 1996 as US 5,555,403, *Relational database access system using semantically dynamic objects*, describes it plainly: a system that lets end users query relational databases "without knowing the relational structure or the structure query language (SQL)." The user picks business-named objects — *Customer*, *Revenue*, *Region* — and a query engine generates the SQL, joins included.

Business Objects called the finished model a **universe**. The part that matters most is the least visible: the patent's **contexts**, which resolve an ambiguous join path by fixing, in advance, which route a given object takes. That is a metric definition written down once, by a designer, so that the user never has to choose.

## Who Built It, And Why Them

Business Objects, founded in 1990 in Puteaux, outside Paris, by Bernard Liautaud and Denis Payre on roughly FFr 100,000 of capital.

The reason it was them is where Liautaud had been standing. He had worked for **Oracle France** in the 1980s, inside the company putting the relational database into French businesses (his exact role there is not established). From that seat the gap between what the database held and what a manager could reach was an everyday sight — and it was not Oracle's problem to close, because Oracle's business was selling the engine, not the question.

The code itself came from outside. The founders came across a program by an independent developer, Jean-Michel Cambot, that made Oracle databases simpler to query, and bought it; Wikipedia credits Cambot with "the concept of Business Objects and its initial implementation." The first customer, Coface, was signed in 1990. The product shipped as BusinessObjects in 1991 in English and French simultaneously, and the company listed on NASDAQ in September 1994.

**That shape — a reseller's view of the unusable database, plus a bought-in query generator — is why the answer was a layer on top of SQL rather than a better SQL.**

## What It Cost

The universe moved the definition problem; it did not remove it.

Someone still had to decide which join path "revenue" took, and that someone was now a universe designer in IT, working slowly and to IT's priorities. That friction is exactly what every later self-service tool sold its way around — and every one that removed the designer removed the single place where a metric was defined. This vault's own `history/bi-analytics-platforms.md` notes Looker's LookML, from 2012, as an openly stated rebuild of the same layer (vault material, not independent corroboration).

## What You Still Touch

When two dashboards disagree about "active customers", you are watching two tools that did not share a universe. The context — one fixed join path per object — is the piece most self-service estates dropped, and the one the semantic-layer revival keeps trying to rebuild.

- [[problems/bi-analytics-platforms/high-impact|🔴 Metric Definition Drift]] — the 1991 ambiguity, returned
- [[problems/bi-analytics-platforms/low-impact-1|🟡 Dashboard Sprawl and Certification]]
- [[niches/bi-analytics-platforms/metric-definition-drift/profile|Metric Definition Drift]]
- [[niches/bi-analytics-platforms/self-service-analytics-platforms/profile|Self-Service Analytics Platforms]]
- [[niches/bi-analytics-platforms/natural-language-query/profile|Natural Language Query]] — the newest attempt to let users skip SQL

**Sources:** Google Patents, US 5,555,403 A (inventors Cambot and Liautaud; priority 27 Nov 1991; granted 10 Sep 1996; abstract quoted); Wikipedia, *BusinessObjects* (1990 founding by Liautaud and Payre, Cambot attribution, Coface as first customer, "universe" defined as a semantic layer, NASDAQ listing Sept 1994); FundingUniverse, *Business Objects S.A. History* (Liautaud at Oracle France in the 1980s, Puteaux, FFr 100,000 capital, purchase of Cambot's program, 1991 introduction); this vault's `history/bi-analytics-platforms.md` (vault material, not independent corroboration). WebSearch was unavailable this session (budget exhausted); research was by WebFetch on specific pages only. ⚠️ **Not established:** whether Denis Payre also came from Oracle; when the term "universe" was first used in product documentation; and the exact release date of the first BusinessObjects version — Wikipedia names "Skipper SQL 2.0.x" in 1990 while FundingUniverse gives a 1991 introduction, and I could not reconcile the two.
