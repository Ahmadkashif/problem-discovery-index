# The Sub-Identifier Nobody Set Up

**Niche:** [[niches/affiliate-networks/publisher-earnings-intelligence/profile|Publisher Earnings Intelligence]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The tracking parameter that would have answered every question was optional, required manual discipline on every link, and almost nobody used it.
**Tags:** #automation #workflow-orchestration #data-integration #quick-win #evaluation-metrics #descriptive-statistics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a creator which piece of their work earned the money — and whoever attributes earnings back to content changes what a creator makes next.

## The Problem
Every network supports a sub-identifier: an optional parameter the publisher can add to a link to record where it was placed. Used consistently it would answer which page, which position and which campaign earned the money. Using it consistently means remembering, on every link, in every article, for years, to type a structured value into a field. Almost nobody does. Those who start are inconsistent within a month. So the capability that would solve the category's biggest publisher complaint exists, is free, and is unused, because it was designed as a manual field rather than as something the tooling fills in.

## Why It's Still Broken
The parameter was built for sophisticated publishers with their own link management and treated as sufficient for everyone — a classic case of a capability shipped without the workflow that would make it usable. Link generation happens in the network's interface, the browser extension or a plugin, none of which know what page the link will end up on. Nobody has taken responsibility for populating it. And networks consider the feature delivered.

## What a Fix Looks Like
Populate the identifier automatically. Set it at insertion time from the page, section and position the link is placed in, through the creator's publishing tool or plugin, which is the fix and converts an unused optional field into a complete dataset with no behaviour change — the tool knows exactly where the link is going and the human does not need to. Backfill historical links by crawling the creator's site and matching link identifiers to their locations, which recovers years of history that would otherwise be lost. Standardise the value format across networks, so a creator's data is comparable rather than five incompatible conventions. Validate and report coverage, telling creators what share of their links are attributable so they know what their reporting is worth. Make it work in the common publishing tools rather than requiring a bespoke workflow, since that is where the links are actually inserted. Handle updates when content is edited or restructured, because links move and a stale identifier is worse than none. Push the convention as an industry standard, since cross-network comparability is the point and no single network delivers it. Expose the identifier in reporting in a usable form rather than as a raw string. Warn on links created without it, which is a cheap prompt at the moment of creation. And measure attribution coverage as a publisher-success metric, because a free capability with near-zero adoption is a product failure rather than a user failure.

## Who Feels the Pain
Creators whose reporting is useless despite the data existing; networks whose publisher complaints have a free remedy nobody can operate; and merchants who cannot tell which placements work.

## Impact If Fixed
The capability that answers the category's biggest publisher complaint is free, shipped and unused because it was a manual field rather than a workflow. Populating it at insertion time from the tool that knows the placement makes it complete with no behaviour change.
