# Existing-Conditions Models From Scans and Archives

**Niche:** [[niches/architecture-firms/historic-rehabilitation-tax-credit/profile|Historic Rehabilitation & Tax-Credit Projects]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A historic building's real geometry is in a point cloud and its intended geometry in 1920s drawings, and a technician spends weeks reconciling them by hand.
**Tags:** #cnns #semantic-segmentation #object-detection #transfer-learning #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get a rehabilitation through State Historic Preservation Office and National Park Service review without costly redesign while documenting existing conditions accurately enough to price, and whoever secures the tax-credit approval first time takes the account.

## The Problem
Rehabilitation design starts with an accurate model of what exists: walls out of plumb, floors that sag, mouldings, window types, deteriorated masonry. Firms laser-scan the building, then modellers trace the point cloud into Revit element by element, consulting archival drawings to interpret what the scan cannot see. It takes weeks and is billed reluctantly.

## Why Nobody Has Built This
Scan-to-BIM automation targets regular modern buildings; historic fabric is irregular, ornamented and inconsistent. Training data — scans paired with finished historic models — sits in individual firms' archives.

## What to Build
A pipeline that segments point clouds of historic buildings into walls, openings, floors and character-defining features, matches window and door types across the building, aligns scanned archival drawings to the scan to fill hidden conditions, and produces a Revit model with deviation tolerances and a condition layer the preservation architect can verify.

## Target Customer
Preservation-focused firms and scanning service providers working on tax-credit rehabilitations.

## Impact If Built
Weeks of modelling cut to days, earlier and more accurate pricing, and a documentation package ready for the Part 2 application.
