# Lien, Title & Auction Processing for Impound

**Parent Industry:** [[industries/towing-companies|Towing Companies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $600M-900M (services)
**Share of Parent Industry:** ~6% (services revenue)
**Digital Adoption:** Low — Most lien processing involves handwritten forms, courthouse visits, certified mail, and wall calendars; TowLien offers partial automation but adoption is limited
**Target Buyer:** Office manager or impound lot administrator processing 50-300 abandoned vehicles per year through the lien-to-auction pipeline
**Automation Potential:** High — Lien processing is entirely rule-based: jurisdiction determines the exact sequence of notifications, hold periods, filing requirements, and auction rights

## What Makes This a Distinct Niche
When a vehicle is abandoned on an impound lot, the towing company must follow a specific legal process to obtain title or auction rights. This process is entirely rule-based but varies by jurisdiction: notification methods (certified mail, publication, both), hold periods (15-90 days), lien amounts (capped differently by state/county), title search requirements (DMV lookup for registered owner and lienholder), and auction procedures. A single error — mailing a notification 1 day late, omitting a lienholder, using the wrong form — invalidates the entire process, leaving the company storing a vehicle they can't sell. Processing 200 vehicles/year through this pipeline, each with 5-8 sequential steps and jurisdiction-specific rules, is a full-time job done with paper forms, spreadsheets, and a wall calendar.

## Current Tools & Gaps
TowLien offers outsourced lien processing in some states but not all, and doesn't integrate with dispatch or lot management. TOPS tracks impound inventory but has limited lien workflow automation. AutoIMS manages vehicle records but doesn't generate jurisdiction-specific forms or track notification deadlines. No tool provides an end-to-end lien workflow that auto-determines jurisdiction, generates the correct forms, tracks notification delivery, calendars deadlines, and initiates auction listing when eligible.

## Problems
- [[niches/towing-companies/lien-title-processing/build|🔨 Build: Jurisdiction-Aware Lien Processing Automation Engine]]
- [[niches/towing-companies/lien-title-processing/buy|🛒 Buy: Automated Title Search and Owner Notification]]
- [[niches/towing-companies/lien-title-processing/fix|🔧 Fix: Revenue Lost to Expired Lien Deadlines]]
