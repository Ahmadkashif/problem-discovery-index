# Every Scouting Report Graded Against the Career

**Niche:** [[niches/sports-teams/amateur-international-scouting/profile|Amateur & International Scouting]]
**Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clubs keep every scouting report and every player's career, and almost none join the two to learn which scouts' projections carry information.
**Tags:** #tacit-knowledge-ml #survival-analysis #gradient-boosting #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn scouts' reports, video and tracking into draft and signing decisions, and whoever's clubs get the most major-league value per signing-bonus dollar takes the account.

## The Problem
A club's archive holds a decade of amateur reports, and public sources hold the minor- and major-league careers of every drafted player. The director knows informally which scouts are "good on pitchers". Nobody has measured it, and the draft board weights every scout's grade the same.

## Why Nobody Has Built This
Old reports are messy (changing scales, free text, scouts who left), outcomes are slow and selected, and R&D groups prefer to model tracking data, which is cleaner. Scouting directors are wary of scoring their staff.

## What to Build
Reconstruct the report archive into structured records, link them to public draft and career outcomes, and model each scout's projections with survival models that control for what tracking and draft slot already predicted. Report each scout's calibration with honest intervals, and surface the free-text phrases that carried information. Use other clubs' picks as the comparison set for players the club passed on.

## Target Customer
Scouting directors and assistant general managers at MLB and NFL clubs, and at the 240+ Division I football programmes that recruit on the same reports.

## Impact If Built
Moving cross-checker visits and bonus dollars toward the best-calibrated scouts could add ~2–3 percentage points of hit rate per class, worth ~$20–40M of surplus player value to an MLB club over a decade (estimate).
