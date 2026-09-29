# Lineage: Data Platform Integrators

**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** dbt, the "data build tool" — a command-line program that turns a folder of SQL `SELECT` files into tables and views in a warehouse, ordering them by the dependency graph that its `ref()` function records (first commit 10 March 2016, Apache 2.0)
**Builder:** RJMetrics
**Builder in vault:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

Once cloud warehouses such as Amazon Redshift made storage and compute cheap, companies stopped transforming data before loading it. They loaded raw data first and transformed it inside the warehouse — ELT rather than ETL.

That moved the transformation work to the people who wrote SQL: analysts. But the analyst's SQL lived in BI tools, saved queries and scripts, with no dependency order, no version control and no way to run the whole chain again in a new environment. **The logic that defined the business's numbers existed as a pile of statements that only their authors could rerun in the right sequence.** For a firm delivering a warehouse to a client, that pile was the deliverable — and it could not be handed over.

## What Got Built

A compiler for SQL files.

Each dbt model is one file containing one `SELECT`. dbt wraps it in the DDL to materialise it as a table or view. Instead of naming another table directly, a model writes `{{ ref('model_a') }}`; in the documentation's words, dbt uses "these references between models to automatically build the dependency graph," so `dbt run` builds everything in the right order. Because `ref()` interpolates the schema at compile time, the same project deploys to a developer's sandbox, staging and production without edits.

The repository's first commit is dated **10 March 2016**, by Christopher Merrick, with Drew Banin committing within the week; the project describes its aim as letting analysts transform data "using the same practices that software engineers use to build applications."

## Who Built It, And Why Them

dbt started at **RJMetrics** in 2016, per Wikipedia's *Data build tool*, "as a solution to add basic transformation capabilities to Stitch."

RJMetrics, founded in Philadelphia in January 2009 by Jake Stein and Robert J. Moore, sold a hosted BI platform on an analytics warehouse built on Redshift. Stitch was its data-loading product: it moved data into a customer's warehouse and stopped there. A loader that does no transformation leaves every customer to write the transformations themselves. **The company selling the "L" was the one exposed to the missing "T"** — and it needed that "T" to live in the customer's warehouse, as SQL, not in a proprietary engine of its own.

In August 2016 Magento acquired RJMetrics and Stitch was spun out. The tool went on with **Fishtown Analytics**, a Philadelphia firm founded in 2016 by Tristan Handy that, by its own later account, began as a consultancy. Handy says he had written a blog post in early 2016 arguing that analysts "needed to work in a fundamentally different way." A consultancy delivering warehouses to many clients needs exactly what dbt provides: a project it can version, rerun and hand over. Fishtown released a commercial product on dbt in 2018 and renamed itself dbt Labs on 30 June 2021, reporting 5,500 companies using dbt.

## What It Cost

dbt made adding a model almost free, and nothing in it asks whether a model is still needed.

A new requirement is a new file with a `ref()` to an old one. The graph records what depends on what; it does not record who queries the result. So projects grow by accretion — four similarly named models where one would do — and the migration or rationalisation that follows has no usage signal inside the tool to work from.

## What You Still Touch

The analytics engineer's job title, the folder of three hundred models, and the lineage graph an integrator shows at handover are all dbt's shape. The question the graph cannot answer — which of these is anyone reading — is where this industry's unsolved work sits.

- [[problems/data-platform-integrators/high-impact|🔴 Three Hundred Models Delivered and Nobody Counts Which Are Queried]]
- [[problems/data-platform-integrators/worker-life-1|🟢 The Analytics Engineer in the Ticket Queue]]
- [[problems/data-platform-integrators/low-impact-2|🟡 Legacy Warehouse and BI Migration]]
- [[niches/data-platform-integrators/model-discovery/profile|Model Layer Discovery]]
- [[niches/data-platform-integrators/retirement-and-rationalisation/profile|Retirement & Rationalisation]]

**Sources:** GitHub API, `dbt-labs/dbt-core` (repository created 10 March 2016; earliest commits by Christopher Merrick and Drew Banin, 10–16 March 2016; Apache-2.0; project description quoted); Wikipedia, *Data build tool* (started at RJMetrics in 2016 to add transformation to Stitch; commercial product 2018; Apache 2.0); Wikipedia, *RJMetrics* (founded January 2009, Philadelphia, Stein and Moore; Redshift-based warehouse; Magento acquisition and Stitch spin-out, August 2016); dbt documentation, *ref* (dependency-graph and schema-interpolation quotes); PR Newswire, 30 June 2021 (Fishtown founded 2016, began as a consultancy, rebrand to dbt Labs, 5,500 companies); TechCrunch, 22 April 2020 (Philadelphia; Handy's early-2016 blog post quote). WebSearch was unavailable this session; the Fishtown blog's own history posts ("On Two Years of dbt", 2018) are on a domain that no longer resolves and were not read. ⚠️ **Not established:** whether Handy worked at RJMetrics, and Merrick's and Banin's roles there; exactly how the project passed from RJMetrics to Fishtown. Keyed to RJMetrics as originator under the vault's originator-over-inheritor precedent; Fishtown is the inheritor that made it an integrator's tool.
