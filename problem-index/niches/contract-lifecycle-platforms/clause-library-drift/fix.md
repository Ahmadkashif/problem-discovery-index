# Nobody Knows Which Clauses Are Used

**Niche:** [[niches/contract-lifecycle-platforms/clause-library-drift/profile|Clause Library Drift]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A clause library grows to several hundred entries of which a few dozen are ever used, and nothing reports usage, so nothing is ever removed.
**Tags:** #descriptive-statistics #word-embeddings #dbscan #evaluation-metrics #confidence-intervals #quick-win #automation #compliance
**Contested on:** Every serious competitor here is fighting to keep the clause library and the playbook aligned with what the company has actually been agreeing to — and whoever closes that gap takes legal operations, because a library that describes a fiction makes every feature built on it wrong.

## The Problem
The clause library has four hundred entries. Six of them are variants of the same confidentiality provision differing in a phrase. Forty were added for a transaction type the company no longer does. Nobody knows which are used, so nobody removes any, so searching the library returns eleven plausible options and a lawyer picks whichever looks familiar — which is how two contracts signed in the same week end up with different liability language for no reason anybody chose.

## Why It's Still Broken
Library usage reporting is an obvious feature that has not been built, because the library is a secondary surface in every product and its curation is nobody's measured responsibility. Deleting carries an asymmetric risk — removing something someone needed is visible, keeping something stale is not — which is the same asymmetry that preserves dashboard and template sprawl elsewhere in this vault. And near-duplicates accumulate because nothing compares entries to each other.

## What a Fix Looks Like
Report usage and group duplicates. Insertions per clause over twelve months, by author and agreement type, with a last-used date — a query over data the platform already records and the whole unlock. Classify the library into active, occasional and dead, and propose archival rather than deletion for the tail, since archival is reversible and is therefore an action people will take. Group near-duplicate clauses by semantic similarity and show usage across the group, which turns six variants into a single keep-decision with evidence attached. Flag clauses whose author has left and which have not been reviewed since, which is a specific and common risk. Report negotiation outcomes per clause where available — this variant is accepted without comment and that one is redlined most of the time — which is a quality signal the library has never had and which is more useful than usage alone. And measure creation, since a library growing faster than it is curated will be back in the same state within a year.

## Who Feels the Pain
Lawyers choosing between eleven similar clauses with no basis; legal operations unable to curate what they cannot measure; and companies whose contracts differ in material language for no deliberate reason.

## Impact If Fixed
Usage reporting is a query over existing data and is the only thing preventing curation of a library everyone agrees is bloated. The per-clause negotiation outcome is the more valuable addition, since it distinguishes the clauses that work from the ones that merely exist.
