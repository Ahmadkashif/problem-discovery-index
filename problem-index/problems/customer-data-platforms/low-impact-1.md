# Audience Definitions and Segment Sprawl

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every CDP ships an audience builder, every organisation ends up with two thousand segments, and nobody can say which ones overlap, which are stale, or which are three people's versions of the same idea.
**Tags:** #k-means-clustering #dimensionality-reduction #word-embeddings #graph-neural-networks #gradient-boosting #evaluation-metrics #data-integration #automation

## The Problem
Audience building is the CDP's most-used feature: filter customers by attributes and behaviours, save the result, activate it downstream. It works, which is why after two years an organisation has hundreds or thousands of saved audiences created by marketers who have since changed roles.

The sprawl has real costs. Several segments describe nearly the same population under different names, built by different teams with slightly different rules, producing inconsistent numbers in different reports. Audiences reference event names and attributes that no longer exist, so they quietly return fewer people every month. Overlapping audiences mean the same customer is in six campaigns at once, which no individual campaign owner can see. And nobody deletes anything, because nobody knows what is in use.

The governance question underneath is semantic. What counts as an active customer, a high-value customer, a churn risk — these are business definitions that ought to be agreed once and reused, and instead each is re-implemented as filter logic inside each audience, diverging quietly.

## What Already Exists
Every platform has an audience builder with computed traits and behavioural filters; Segment, mParticle, ActionIQ and Bloomreach all do this competently. Warehouse-native stacks express audiences as dbt models or SQL, which is better for version control and worse for marketer self-service. Some platforms report audience size over time and basic overlap between pairs. Reverse-ETL tools handle the activation. Data catalogues like Alation and Atlan exist for tables and are rarely applied to audiences.

## The Customisation Gap
The tools treat an audience as a saved query; the organisation needs it treated as a governed definition. That means a shared semantic layer where core concepts are defined once with an owner and a version history, and audiences are composed from those definitions rather than re-implementing them — so that changing what counts as an active customer changes it everywhere, deliberately, with a record of who agreed.

Overlap analysis is the second gap and is straightforward to compute at scale: a clustering over audience membership vectors immediately reveals that forty segments describe six populations. Presenting that, with names and owners attached, is the conversation that lets an organisation rationalise its own sprawl. Nobody ships it, presumably because a product that says half your segments are redundant is an awkward sell.

Staleness and dependency tracking is the third. An audience that references a deprecated event should be flagged on the day the event stopped arriving, and the downstream campaigns that depend on it should be identifiable before someone deletes it. This is ordinary lineage, applied to a layer nobody has applied it to.

And total contact pressure — how many audiences a given customer sits in and how many messages that implies — is computable centrally and invisible to every individual campaign owner, which is why over-contacting happens without anyone deciding to do it.

## Impact If Solved
Segment sprawl produces inconsistent reporting, silent decay and uncoordinated contact, and it worsens with every year a platform is in use. A governed semantic layer with overlap analysis and lineage turns an accumulating liability into a maintained asset, and the contact pressure view surfaces a harm that no current owner is positioned to see.
