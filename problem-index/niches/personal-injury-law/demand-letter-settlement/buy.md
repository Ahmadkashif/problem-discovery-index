# Comparable Verdict & Settlement Research

**Niche:** [[niches/personal-injury-law/demand-letter-settlement/profile|Demand Letter & Settlement Valuation]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PI attorneys stop spending hours searching verdict databases and manually selecting comparable cases — AI-powered matching finds the 3-5 most persuasive comparable verdicts and settlements for any given case based on injury type, jurisdiction, and case characteristics.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #data-integration #revenue-impact

## The Problem
A demand letter is most persuasive when it cites 3-5 comparable verdicts or settlements — cases with similar injuries, similar liability facts, and similar venues that produced substantial awards. Finding these comparables requires searching verdict databases (VerdictSearch, JuryVerdictAlert, state-specific verdict reporters), filtering by injury type, jurisdiction, and date range, reading dozens of case summaries to assess similarity, and selecting the ones most likely to persuade the adjuster. This research takes 2-4 hours per demand letter. The selection is judgment-intensive: a $2M verdict for a cervical fusion in Dallas County is not comparable to a cervical fusion case in rural East Texas — venue matters as much as injury type. Experienced attorneys know which comparables to cite and which to avoid (some are outliers that adjusters will dismiss). Junior attorneys waste time citing irrelevant comparables or miss the most persuasive ones.

## What Already Exists
VerdictSearch (ALM) and JuryVerdictAlert provide searchable databases of verdicts and settlements with basic filtering by injury type, body part, jurisdiction, and amount. Westlaw and LexisNexis have verdict reporter modules. These tools provide the raw data but require manual search, manual reading of case summaries, and manual assessment of which results are truly comparable. The search interfaces are keyword-based with faceted filtering — they cannot understand that a "herniated disc at L4-L5 with epidural injection series, no surgery, in Harris County" has specific comparables that differ from a "herniated disc at C5-C6 with anterior cervical discectomy, in Collin County."

## The Customization Gap
The missing layer is ML-powered comparable matching that goes beyond keyword search. Input: current case profile (injury type with anatomical specificity, treatment received, surgery/no surgery, age of plaintiff, venue, liability strength). The model encodes both the query case and the database cases as feature vectors (body part, injury severity tier, surgical intervention, treatment duration, plaintiff age bracket, jurisdiction, verdict vs. settlement, year) and ranks database cases by similarity. The ranking model is trained on attorney preferences — which comparables do experienced PI attorneys actually select when they have the full database? This captures the tacit knowledge of comparable selection that no keyword search replicates. Output: top 5 recommended comparables with similarity scores, case summaries, and strategic notes ("this verdict was before the tort reform cap — adjust for current cap").

## Target Customer
Associate attorneys and senior paralegals responsible for demand letter preparation who currently spend 2-4 hours per demand on verdict research and often cite suboptimal comparables due to time pressure.

## Impact If Solved
Reduces comparable research from 2-4 hours to 15-30 minutes per demand. Improves comparable quality — better-matched comparables produce more persuasive demands, estimated to increase settlement offers by 5-10% because the adjuster takes the demand more seriously when the supporting verdicts are genuinely analogous. Standardizes comparable selection across the firm so junior associates cite the same caliber of comparables as the senior partner.
