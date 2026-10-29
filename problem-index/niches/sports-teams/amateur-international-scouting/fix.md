# The 60 Grade That Means 55 From One Scout

**Niche:** [[niches/sports-teams/amateur-international-scouting/profile|Amateur & International Scouting]]
**Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Type:** Fix (Pain Point)
**One-liner:** Scouts use the 20–80 scale differently, so the same number on the draft board means different things depending on who wrote it.
**Tags:** #bayesian-inference #descriptive-statistics #evaluation-metrics #quick-win #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to turn scouts' reports, video and tracking into draft and signing decisions, and whoever's clubs get the most major-league value per signing-bonus dollar takes the account.

## The Problem
Some scouts grade generously and others hold back their 60s. Cross-checkers adjust in their heads ("he's always a half-grade high on bats"). The board aggregates the raw grades.

## Why It's Still Broken
Every director knows it and corrects informally. Formal normalisation looks like second-guessing staff, and nobody has the data structured to do it.

## What a Fix Looks Like
Estimate each scout's grading tendency from players seen by several scouts (a hierarchical model with scout and player effects), show adjusted grades next to raw ones on the board, and let the director see both.

## Who Feels the Pain
Scouting directors reconciling boards in the week before the draft, and scouts whose accurate reads are diluted by a colleague's inflation.

## Impact If Fixed
A normalised board removes a known bias in a decision allocating ~$5–17M of bonus pool per club per year (estimate) at almost no cost.
