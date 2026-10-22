# HUBB Uploads Rebuilt From Spreadsheets Every Deadline

**Niche:** [[niches/wired-broadband-providers/subsidy-buildout-compliance/profile|Subsidy & Buildout Compliance]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Each reporting deadline, someone rebuilds the list of newly served subsidised locations from billing exports and construction spreadsheets, and the errors surface in USAC verification.
**Tags:** #k-nearest-neighbors #compliance #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche (regulatory consultants, compliance and grants software vendors and carriers' own regulatory staff) is fighting to prove, location by location, that each subsidised address was served on time at the required speed with evidence USAC verification and state BEAD audits accept, and whoever produces that evidence best takes the account.

## The Problem
High-cost support recipients upload deployed locations to USAC's HUBB portal; verification samples them and asks for evidence. The upload is assembled from whatever the billing and construction teams can export, with mismatched addresses and coordinates, duplicates and locations counted before they were really serviceable.

## Why It's Still Broken
The person doing it does it once or twice a year, under deadline, and starts from scratch each time. Nobody owns the mapping between billing accounts, construction records and obligation locations.

## What a Fix Looks Like
A standing matched table between obligation locations, Fabric IDs, construction completion and billing accounts, updated as work completes; validation checks before upload (duplicates, coordinates outside the eligible area, speeds below obligation); and evidence attached to every row so a verification sample can be answered immediately.

## Who Feels the Pain
Regulatory managers at small carriers; CFOs exposed to support recovery; consultants charging to redo the same reconciliation.

## Impact If Fixed
Clean uploads, quick verification responses and no support withheld over avoidable errors.
