# Three People's Version of the Same Idea

**Niche:** [[niches/customer-data-platforms/audience-and-segment-sprawl/profile|Audience & Segment Sprawl]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** High-value customers exists eleven times with eleven slightly different definitions, and every report and campaign using one of them is reporting something different.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #workflow-orchestration #quick-win #automation #graph-theory #compliance
**Contested on:** Every serious competitor in this niche is fighting to tell an organisation which of its two thousand segments overlap, are stale or are the same idea three times — and whoever does that makes an unmanageable artefact governable.

## The Problem
Someone needs a high-value customer segment. They search, find three with unhelpful names built by people who have left, cannot tell what any of them do, and build a new one. Now there are four. Each uses a slightly different threshold and lookback. Campaigns run against different ones, reports quote different counts, and a meeting about high-value customers involves three people quoting numbers that are all correct and all different. The organisation has no shared definition of its own most important customer concept, and the platform helpfully made it easy for everyone to create their own.

## Why It's Still Broken
Creating a new segment is easier than understanding an existing one, and the interface optimises for creation — the path of least resistance produces duplication by design. Names are unstructured and meanings are not documented. There is no canonical definition anywhere, so nobody is wrong. And the confusion appears in meetings rather than in systems, so no alert ever fires.

## What a Fix Looks Like
Make the existing one easier to find than a new one is to build. Search by what a segment does rather than by its name, which is the fix — a search that understands the definition means someone looking for high-value customers finds the four that exist rather than making a fifth. Show similar existing segments at the moment of creation, which is where the decision is made and where an intervention actually works. Require a description and an owner, which is a small friction that pays for itself immediately. Establish canonical definitions for the organisation's core concepts and mark them, so there is a right answer to point at. Report where definitions diverge and by how much, since the eleven versions differ in specific ways and naming them resolves most of the argument. Show counts side by side for the variants, which makes the divergence concrete in a way a description does not. Migrate consumers onto the canonical definition with the differences stated, rather than deleting variants and breaking things. Enforce naming conventions automatically, since unstructured names are why nobody can find anything. Track which definition each report and campaign uses, so a meeting can establish quickly why two numbers differ. And measure how many distinct definitions exist for each core concept, because that count is the state of the organisation's data governance in one number.

## Who Feels the Pain
Marketers who cannot find an existing segment and build another; leadership receiving three different numbers for the same concept; and organisations with no shared definition of their own key customer groups.

## Impact If Fixed
Creating is easier than understanding, so the interface produces duplication by design. Search that understands definitions rather than names, plus similar-segment suggestions at creation, stops the fifth version from being built.
