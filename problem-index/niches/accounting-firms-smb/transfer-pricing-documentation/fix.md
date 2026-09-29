# Local File Production Restarts From Zero Every Year
**Niche:** [[niches/accounting-firms-smb/transfer-pricing-documentation/profile|Transfer Pricing Documentation Studios]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Most of a local file is unchanged from last year, but because it is produced as a document rather than assembled from components, the team rewrites the whole thing annually across dozens of jurisdictions.
**Tags:** #workflow-orchestration #automation #data-integration #large-language-models #worker-facing #compliance #quick-win

## The Problem
A multinational client needs a local file in every jurisdiction with documentation requirements — often dozens, each annually, each with its own content rules and language requirements. Year over year the substance changes modestly: the functional analysis is largely stable, the entity description barely moves, the financials and benchmarking refresh. But because each file is produced as a document, the team works through it end to end every year, re-verifying unchanged content and re-formatting to each jurisdiction's requirements. It consumes the compliance season and it is the least interesting work in the practice.

## Why It's Still Broken
Documentation is authored in word processors from templates, so content and presentation are fused. There is no component layer — no notion that the functional analysis of an entity is an object reusable across jurisdictions and years, rendered differently per local requirement. Prior-year files exist as flat documents, so reuse means copy-paste, which carries stale content forward invisibly.

## What a Fix Looks Like
Separate content from rendering. Hold the substance as versioned components — entity descriptions, functional analyses, intercompany transaction records, benchmarking sets — each with a review date and an owner. Assemble a jurisdiction's local file by rendering the components its rules require into its required format and language. Annual production then becomes reviewing what actually changed, with the system flagging components whose underlying facts have moved and those merely aged past their review date. Where a jurisdiction adds a requirement, it is a rendering change rather than a rewrite.

## Who Feels the Pain
Analysts who spend compliance season re-producing documents that are substantially the same as last year's, and the documentation director accountable for filing dozens of jurisdictions on time.

## Impact If Fixed
Turns annual documentation from a rewrite into a review, which is where nearly all the recoverable capacity in the practice sits. Removes the risk of stale content propagating through copy-paste, and makes adding a jurisdiction cheap.
