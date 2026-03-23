# TSB and Recall Lookup Fragmentation Across OEM Portals

**Niche:** [[niches/auto-repair-shops/european-luxury-repair/profile|European & Luxury Repair]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians must check 3-5 separate OEM portals for TSBs and recalls, so known fixes get missed and shops waste hours re-diagnosing documented problems.
**Tags:** #data-integration #automation #quick-win

## The Problem
Each European manufacturer maintains its own Technical Service Bulletin (TSB) database behind separate login portals — BMW TIS, Mercedes EPC/WIS, Audi erWin, etc. A shop working on BMW, Mercedes, and Audi must maintain paid subscriptions to three separate portals and manually search each one during diagnosis. TSBs frequently describe the exact symptom a technician is seeing, but if the tech doesn't check (or searches with the wrong keywords), they spend 2-3 hours diagnosing a problem that BMW already documented with a 30-minute fix.

## Why It's Still Broken
OEM portals are deliberately siloed — manufacturers have no incentive to make their TSBs easily searchable by independent shops. Mitchell 1 and ALLDATA aggregate some TSBs but with significant delays (months after publication) and incomplete coverage for European brands. The information exists but is scattered across portals that each require separate credentials, different search syntaxes, and different document formats.

## What a Fix Looks Like
A unified TSB search tool that aggregates bulletins from all major European OEM portals into a single searchable interface, indexed by symptom, fault code, and VIN range. During vehicle intake, the system automatically pulls all open TSBs and recalls for that specific VIN and surfaces them to the technician before diagnosis begins. New TSBs are ingested within 48 hours of OEM publication.

## Who Feels the Pain
Technicians who spend 30-60 minutes per vehicle checking multiple OEM portals for known issues, and shop owners who absorb diagnostic time that could have been avoided with a single TSB lookup.

## Impact If Fixed
Saves 30-60 minutes of diagnostic time per vehicle on TSB-documented issues, affecting roughly 25-35% of European vehicle repairs. For a shop doing 40 European vehicles per month, this recovers 15-25 billable hours monthly, worth $2,200-$5,500 at European-specialty labor rates.
