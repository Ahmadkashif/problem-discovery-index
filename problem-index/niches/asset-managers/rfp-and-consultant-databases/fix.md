# The Quarterly Database Refresh

**Niche:** [[niches/asset-managers/rfp-and-consultant-databases/profile|RFP & Consultant Database Responses]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Every quarter the team re-keys performance, characteristics, holdings and narrative into several consultant databases by their deadlines, and a late or wrong upload removes the strategy from searches.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to answer each consultant question correctly for the exact strategy, vehicle and quarter, consistent with everything previously submitted — and whoever does that clears the consultant screen faster and without the inconsistency that disqualifies a manager.

## The Problem
Consultants screen managers on database fields. Each database has its own template, field definitions and upload deadline after quarter-end. The team assembles data from performance, holdings and portfolio management, reconciles definitional differences, uploads, and fixes rejections.

## Why It's Still Broken
Field definitions differ subtly across databases and change over time; the mapping lives with one or two people. Data owners in operations treat database feeds as a marketing request.

## What a Fix Looks Like
A versioned mapping from the firm's book of record to each database's fields, with automated extraction, validation against last quarter for anomalies, and a reconciliation report showing where two databases will display different numbers for the same strategy and why.

## Who Feels the Pain
Database and RFP analysts at quarter-end; strategies that silently drop out of consultant screens.

## Impact If Fixed
Database maintenance becomes a checked pipeline instead of a quarterly scramble.
