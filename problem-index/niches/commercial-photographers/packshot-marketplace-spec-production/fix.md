# The Rejection That Arrives After the Sample Went Back

**Niche:** [[niches/commercial-photographers/packshot-marketplace-spec-production/profile|Packshot & Marketplace-Spec Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Fix (Pain Point)
**One-liner:** A retailer rejects a batch for a margin or a missing angle four days after delivery, by which time the samples are back in the warehouse and the reshoot costs more than the original shot.
**Tags:** #object-detection #evaluation-metrics #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver every SKU's images right first time against each retailer's specification and the physical sample's true colour before the listing date, and whoever posts the lowest reshoot and rejection rate per SKU takes the account.

## The Problem
Specification checks happen at the end of the chain: the brand uploads, the retailer's ingest rejects, and the list of failures comes back to the studio days later. A reshoot means recalling samples, rebooking a set and paying a photographer again for an image the studio has already been paid for.

## Why It's Still Broken
Studios release samples as soon as capture is done to free shelf space and meet return deadlines. Retailer rules live in PDFs that change without notice. Nobody at the studio is responsible for checking delivery against every channel's rules before the samples leave.

## What a Fix Looks Like
An automated check that runs on the retouched files before samples are released: required views present, product fill and margins in range, background value correct, resolution and naming right for each channel. Samples whose images fail stay on the shelf. Retailer rejection reasons are logged against the rule that missed them, so the rule library improves.

## Who Feels the Pain
Studio producers absorbing reshoot costs; brand content managers missing listing dates; photographers re-shooting work they got right the first time.

## Impact If Fixed
Post-delivery rejections become rare, reshoot costs fall, and samples go back to the warehouse once.
