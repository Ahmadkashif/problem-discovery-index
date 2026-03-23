# Green Bean Inventory and Sourcing Coordination

**Niche:** [[niches/coffee-shops-independent/specialty-roaster-cafes/profile|Specialty Roaster-Cafes]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Green bean purchasing is a high-stakes guessing game — order too much and capital is tied up in aging inventory; too little and your best-selling origin runs out mid-season.
**Tags:** #time-series-forecasting #gradient-boosting #data-integration #revenue-impact

## The Problem
Specialty green coffee is purchased in 60-150 lb bags from importers (Royal, Cafe Imports, Genuine Origin) with lead times of 2-8 weeks and limited availability windows tied to harvest seasons. A roaster-cafe owner must forecast demand 2-3 months ahead to secure enough green bean inventory, but their demand data lives in a disconnected POS system while their purchasing history lives in importer invoices and email confirmations. Ordering decisions are made from gut feel and past experience, leading to either capital-heavy over-purchasing (2,000 lbs of a single origin sitting in storage) or mid-season stockouts that force blend reformulation.

## Why It's Still Broken
Green bean importers have their own ordering portals (Royal's The Crown, Cafe Imports' platform) but these don't connect to the roaster's production or sales data. The roaster has no automated way to match current sales velocity of a particular origin against remaining green bean inventory and upcoming importer availability. The information exists across 3-4 systems and the owner's memory, but no one has built the bridge because the market is too small for importers to invest in downstream integration.

## What a Fix Looks Like
A simple inventory dashboard that tracks green bean stock by origin (manual weigh-ins or scale integration), connects to POS sales velocity for each origin/blend, and surfaces reorder alerts with importer availability windows. When Ethiopian Yirgacheffe consumption is 15 lbs/week and current stock is 45 lbs with a 4-week importer lead time, the alert fires 3 weeks before stockout.

## Who Feels the Pain
The owner-roaster who spends 2-3 hours per week checking storage bins, cross-referencing importer catalogs, and mentally calculating runway for each origin — and still gets surprised by stockouts twice a year.

## Impact If Fixed
Prevents 2-4 origin stockouts per year that each cost $2,000-$5,000 in lost sales and brand damage (regulars notice when their favorite single-origin disappears). Reduces excess green bean inventory carrying cost by 10-20%.
