# Seller Announcements Checked Against the 2026 Arbitration Rules

**Industry:** [[wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Since 1 June 2026 a seller's announcement protects them only if it names the specific defect, yet announcements are still typed free-hand at check-in and nobody checks them against the guideline categories, the VIN decode or open recalls before the car runs.
**Tags:** #large-language-models #logistic-regression #gradient-boosting #evaluation-metrics #compliance #automation #quick-win

## The Problem
Every car that runs at a wholesale auction carries a seller announcement: the sale light (green, yellow, red, blue for title absent) and a line of text such as "frame damage", "TMU", "engine noise" or, until June, "No Arb for oil leaks". The announcement decides what the buyer can and cannot arbitrate. At check-in it is keyed by the seller's representative, the auction's consignment desk or a commercial consignor's upload, often from a template, and attached to the condition report.

The NAAA's guidelines effective 1 June 2026 changed what an announcement is worth. Generic "No Arb for [defect]" lines are prohibited. Announcing only a warning light or trouble code no longer relieves the seller of the underlying condition. ADAS components such as adaptive cruise, lane departure warning and blind-spot monitoring are now in Appendix I. Cars at $50,000 and above have a 2% per-defect threshold instead of $800. A template that worked in May is now an arbitration waiting to happen, and the seller learns that only when the claim arrives.

## What Already Exists
Condition-report and consignment software from the auctions themselves (Manheim's, OPENLANE's and ACV's inspection apps, Auction Edge for independents) captures announcements as free text or picklists. NHTSA's vPIC decoder returns factory equipment by VIN. The NHTSA recalls API returns campaigns by make, model and year, with "park it" flags. Open-recall and VIN-decode feeds are sold commercially, mapped at [[niches/franchised-car-dealers/recall-outreach-vendors/profile|Recall Outreach & Open-Recall Data Vendors]] and [[niches/franchised-car-dealers/incentive-data-services/profile|Automotive Incentive Data Services]]. Generic text-compliance and grammar linters exist.

## The Customisation Gap
None of these reads an announcement the way an arbitration desk will. The auction-specific logic is:
- map free-text announcements to Appendix I defect categories and flag generic wording the 2026 rules no longer honour;
- compare announced equipment and condition against the vPIC decode, such as an ADAS-equipped trim with no ADAS note and a camera fault code in the scan;
- flag recall campaigns for that year, make and model, especially "park it" ones;
- apply the right threshold for the expected price band, $800 or 2%;
- show the seller, before the car runs, which lines will not protect them.

This is the two-week MVP: a rules-plus-model checker over the condition report, the vPIC decode and the recalls API, returning a list of arbitration risks with the guideline clause each one breaks. It is mapped at [[niches/wholesale-auto-auctions/announcement-disclosure-checks/profile|Announcement & Disclosure Checks]].

## Impact If Solved
Each prevented arbitration saves the seller the adjustment or unwind, typically several hundred to a few thousand dollars, and saves the auction a case. At an auction selling 25,000 cars a year, the NAAA member average, a checker that prevents one avoidable claim per thousand units sold saves ~25 claims and roughly $25,000–50,000 a year at ~$1,000–2,000 a claim (estimate). It also gives commercial consignors a documented reason to trust the announcement the auction writes for them.
