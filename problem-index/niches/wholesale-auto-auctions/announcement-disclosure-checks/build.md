# An Arbitration-Risk Checker on Every Condition Report

**Niche:** [[niches/wholesale-auto-auctions/announcement-disclosure-checks/profile|Announcement & Disclosure Checks]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every input needed to predict an arbitration exists before the car runs, and is first read together by the arbitration desk after the claim.
**Tags:** #large-language-models #gradient-boosting #logistic-regression #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to make each seller announcement and condition report complete enough that buyers cannot win an arbitration on it, and whoever has the fewest arbitrations granted on announceable items per thousand units sold takes the account.

## The Problem
The announcement, the condition report, the trouble codes and the VIN all sit in the system at check-in. The arbitration desk reads them together for the first time when a buyer files a claim. By then the only choices left are an adjustment or an unwind.

## Why Nobody Has Built This
Pre-sale arbitration risk has been proposed before: [[niches/auto-dealers-independent/auction-condition-report-ops/build|Arbitration Says Whether the Report Was True and Nobody Adds It Up]] argues that arbitration is predictable before the vehicle runs, in order to score inspectors and target re-inspection. What has not been built is the disclosure check. The guideline categories lived in a PDF, not in code, so nothing compared a seller's wording, the price threshold, the VIN decode or recall campaigns with the rules at check-in. The June 2026 changes, which banned generic announcements and made warning lights and ADAS matter, are recent enough that no tool has been rebuilt around them.

## What to Build
This is the two-week MVP. Version one runs on public data. It decodes the VIN through NHTSA vPIC (trim, ADAS equipment, drivetrain) and pulls recall campaigns for the year, make and model from the NHTSA recalls API, flagging "park it" campaigns. An LLM maps the announcement and report notes to Appendix I categories and flags generic wording the 2026 rules no longer honour. A rules table applies the $800 or 2% threshold by expected price. It returns a ranked list of risks, each with its guideline clause and suggested wording. Version two adds a gradient-boosted model trained on the auction's own claims to estimate probability and expected cost per flag. Its features are the disclosure ones: announcement category and wording, sale light, threshold band, decoded equipment, recall flags and seller history. The inspector-accuracy model and the re-inspection targeting stay with the condition-report build; the two share claim labels but answer different questions (was the disclosure enough, against was the inspector right). The recalls API reports campaigns by model, not VIN-level open status, so a commercial open-recall feed is the upgrade path.

## Target Customer
Assurance and inspection leaders at the national auctions; independent auctions through their management software; commercial consignors checking their own uploads.

## Impact If Built
If 20–30% of granted claims trace to items the checker can flag (estimate), and sellers fix half of them before the sale, a national auction with 10,000 granted claims a year avoids 1,000–1,500 claims. That saves ~$1–3M at ~$1,000–2,000 a claim.
