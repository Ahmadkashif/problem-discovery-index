# Lineage: Data Marketplace Brokers

**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** Snowflake Secure Data Sharing — the "share" object, a named grant through which a provider exposes live tables to another account's read-only database, with no data copied and the consumer paying only for the compute it queries with (announced June 2017; storefront added as Snowflake Data Exchange, June 2019)
**Builder:** Snowflake Computing
**Builder in vault:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Verification:** partial — see Sources

## The Problem That Came First

Selling a dataset used to mean shipping a copy of it.

A provider exported files, the buyer loaded them into its own systems, and from that moment there were two datasets: the provider's, which kept changing, and the buyer's, which started going stale at once. Every refresh was another delivery and another load job. Every buyer built its own ingestion pipeline for every supplier.

**The copy was also where control ended.** Once the file sat in the buyer's warehouse, the licence — which uses were permitted, for how long, by whom — was a paragraph in a contract that nothing in the data path could read. A provider could not see what was done with its data and could not take it back.

## What Got Built

A pointer instead of a copy.

In Snowflake's documentation, a share is "a named Snowflake object that encapsulates all of the information required to share a database." The provider adds tables or secure views to it and names the accounts that may use it; each consumer creates a read-only database from the share. "No actual data is copied or transferred between accounts. All sharing uses Snowflake's services layer and metadata store." The consumer pays no storage for shared data — "the only charges to consumers are for the compute resources … used to query the imported data." Reader accounts, created and owned by the provider, let a buyer that is not a Snowflake customer query too.

Snowflake announced the feature in June 2017 — a Snowflake news item headlined as "another world first," the "data sharehouse," was posted to Hacker News on 23 June 2017. Wikipedia dates the Snowflake Data Exchange to June 2019 and records providers such as Knoema being added to the Snowflake Data Marketplace by December 2020.

## Who Built It, And Why Them

Snowflake Computing, founded on 23 July 2012 in San Mateo, California, by Benoît Dageville and Thierry Cruanes — both previously data architects at Oracle — and Marcin Żukowski, co-founder of Vectorwise.

The reason sharing came from a warehouse vendor and not a data broker is architectural. Snowflake kept storage and compute separate, with a central services layer holding the metadata about who owns which table. In that design, letting a second account read a table is a metadata grant, not a data movement — something an on-premises warehouse, with each customer's data on its own machines, had no natural way to do across company lines.

And the commercial reason is that every share pulls the buyer onto the platform. The consumer pays for compute, so each dataset a provider publishes is a reason for a buyer to become a customer. Snowflake's 2020 S-1 says so plainly: "Our business benefits from powerful network effects." A broker selling files had no such incentive to abolish the file.

## What It Cost

The share solved delivery and staleness, and it solved revocation — a provider can withdraw access — but only inside one vendor's cloud. Distribution moved from "any buyer who can load a file" to "any buyer on this platform, or willing to sit in a reader account."

Nor did it carry the licence. A share controls who can query; it says nothing machine-readable about what the querying is for. And a live pointer is exactly as hard to evaluate before purchase as a file was: coverage, freshness and accuracy against the buyer's own population are still discovered by trying it.

## What You Still Touch

Every "get this dataset" button on a warehouse marketplace is a share underneath. What arrives is live and never duplicated — and the permitted-use terms still arrive as PDF.

- [[problems/data-marketplace-brokers/low-impact-2|🟡 Licence Term Expression and Enforcement]] — the part the share did not carry
- [[problems/data-marketplace-brokers/high-impact|🔴 Evaluating a Dataset Before Buying It]]
- [[niches/data-marketplace-brokers/in-ecosystem-data-sharing/profile|In-Ecosystem Data Sharing]]
- [[niches/data-marketplace-brokers/data-distribution-platforms/profile|Data Distribution Platforms]]
- [[niches/data-marketplace-brokers/licence-term-enforcement/profile|Licence Term Enforcement]]

**Sources:** Snowflake documentation, *Introduction to Secure Data Sharing* (docs.snowflake.com; share definition, no-copy statement, consumer compute charges, reader accounts, quoted); Wikipedia, *Snowflake Inc.* (founding 23 July 2012, San Mateo, founders and their Oracle and Vectorwise backgrounds, Data Exchange June 2019, Knoema December 2020); Snowflake Inc., Form S-1 (SEC EDGAR, 2020; "network effects" and "without copying or moving the underlying data," incorporated July 2012); Hacker News item 14617174 via the Algolia HN API (link to Snowflake's "data sharehouse" announcement, posted 23 June 2017 — the linked Snowflake page now returns 404, so the announcement's exact date and wording were not read directly). WebSearch was unavailable this session (budget exhausted). ⚠️ **Not established:** who inside Snowflake designed sharing, or whether it was planned from the 2012 architecture or added later; the precise general-availability date; and the date the company changed its name from Snowflake Computing to Snowflake Inc. The pre-2017 file-delivery picture in the first section is described generally and not attributed to any specific broker.
