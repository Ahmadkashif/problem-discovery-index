# Combat Zone Filing Extension Tracking

**Niche:** [[niches/tax-prep-firms/military-expatriate-filers/profile|Military & Expatriate Filer Specialists]]
**Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Military clients deployed to combat zones receive automatic filing extensions that can stack for years, but no practice management tool tracks these extended deadlines — preparers lose track and either file unnecessarily early or miss the true deadline.
**Tags:** #compliance #automation #workflow-orchestration #worker-facing

## The Problem
Military personnel serving in a combat zone (or qualifying hazardous duty area) receive an automatic extension of at least 180 days after leaving the combat zone for all filing, payment, and assessment deadlines. These extensions stack: if a service member deploys for 12 months and then has 180 days, their filing deadline may extend 18+ months beyond April 15. When deployments span multiple tax years, the filing deadlines for 2-3 returns may overlap. The preparer must track each client's deployment dates, calculate the applicable extension for each tax year, and ensure returns are filed before the extended deadlines expire. This tracking is done in the preparer's personal calendar or a spreadsheet.

## Why It's Still Broken
Tax software calculates the return but does not track combat zone extensions — it defaults to the standard April 15 deadline (or October 15 with an extension). Practice management tools (Canopy, TaxDome) track standard deadlines but have no concept of combat zone extensions. The preparer must manually calculate the extension based on the client's deployment orders and maintain it outside any system. When a preparer retires or a client switches firms, the extension tracking is lost.

## What a Fix Looks Like
A military client extension tracker that ingests deployment information (deployment start date, return date, combat zone designation), calculates the applicable extension for each affected tax year, generates a calendar of deadlines, and integrates with the firm's practice management system. The tracker alerts the preparer when an extended deadline is approaching, prevents premature filing (which wastes the opportunity for tax planning during the extension period), and documents the extension calculation for IRS correspondence in case the deadline is challenged.

## Who Feels the Pain
Preparers specializing in military returns who manage 50-200 clients with overlapping combat zone extensions and track deadlines through personal systems that do not transfer when the preparer is unavailable.

## Impact If Fixed
Prevents missed extended deadlines that result in late-filing penalties (the IRS occasionally challenges combat zone extensions, and documentation is essential). Enables tax planning during the extension period (the service member can make retirement contributions and other elections up to the extended deadline). Reduces the 30-60 minutes per client currently spent on manual extension calculations.
