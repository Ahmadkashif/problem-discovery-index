# Campaign Delivery Verification and Makegoods Tracking

**Niche:** [[niches/podcasting-networks/podcast-ad-sales-houses/profile|Podcast Ad Sales Houses]]
**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Type:** Fix (Pain Point)
**One-liner:** Ad ops teams manually compare delivered impressions against IO commitments for every campaign — a 2–4 hour reconciliation process per campaign that catches underdelivery weeks after the advertiser expected results.
**Tags:** #automation #data-integration #compliance #quick-win

## The Problem
When a podcast ad campaign ends, the ad ops team must verify that the committed impressions were actually delivered. This requires: (1) pulling delivery reports from the insertion platform (Megaphone/AdsWizz), (2) comparing delivered impressions against the insertion order line items (which may specify delivery by show, by placement type, by geographic target), (3) identifying any shortfalls, (4) calculating the value of underdelivery, (5) negotiating makegoods (additional impressions in future campaigns to compensate) or credits, and (6) tracking outstanding makegood obligations for future campaign planning. This reconciliation is done in spreadsheets. For a sales house running 100 campaigns per month, it's a full-time job for one person. Discrepancies between the insertion platform's numbers and the advertiser's tracking (which uses a different measurement methodology) create disputes that take weeks to resolve.

## Why It's Still Broken
Dynamic insertion platforms report total impressions delivered but not in the granular format that matches IO line items. An IO might specify "200,000 impressions on true crime shows, split 60/40 pre-roll/mid-roll, excluding California." The insertion platform reports total impressions per campaign, but the breakdowns by placement type and geography require custom report generation or manual calculation. The reconciliation template is different for every advertiser because every IO has different terms. And makegoods accumulate: a sales house may have 50 outstanding makegood obligations from prior campaigns that affect how they allocate inventory for new campaigns — tracked in a spreadsheet that only one person understands.

## What a Fix Looks Like
An automated reconciliation system that: (1) imports IO terms (impressions by show/placement/geography/date) from the CRM or a structured IO template, (2) pulls actual delivery data from the insertion platform at campaign end, (3) auto-compares delivered vs. committed at the line-item level, (4) highlights underdelivery with calculated financial value, (5) generates a reconciliation report for the advertiser showing delivered vs. committed with explanations for shortfalls, (6) creates makegood obligations that appear in the inventory management system so future campaigns account for them, and (7) tracks makegood fulfillment across subsequent campaigns. A dashboard shows total outstanding makegood liability across all advertisers.

## Who Feels the Pain
Ad ops coordinators who spend 40+ hours per month on manual campaign reconciliation, and sales directors who lose advertiser trust when underdelivery is discovered late.

## Impact If Fixed
Reduces reconciliation time from 3 hours to 15 minutes per campaign, freeing 50+ hours per month of ad ops time. Catches underdelivery in real-time (during the campaign, not after) so corrective reallocation can be made before the campaign ends. Reduces outstanding makegood liability by 30% through systematic tracking that prevents makegoods from being "forgotten" (and the advertiser from double-claiming).
