# The One Actuary Who Knows the Model

**Niche:** [[niches/life-insurance-carriers/small-carriers-fraternals/profile|Small Carriers & Fraternal Benefit Societies]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** At many small carriers one person understands how the reserve model works, and the statutory calendar depends on them not leaving.
**Tags:** #large-language-models #workflow-orchestration #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a carrier with a handful of actuaries on the statutory calendar (PBR or its exemption, asset adequacy, filings and opinions), and whoever lets a five-person actuarial team meet every deadline without a consultant on retainer for each one takes the account.

## The Problem
The model was built years ago by an actuary still on staff, or by a consultant whose engagement ended. Its logic is in spreadsheet formulas and code comments. When that person is unavailable at year-end, the filing slips or the opinion is signed on trust.

## Why It's Still Broken
Documentation is never urgent until it is too late. Small teams have no slack for it, and regulators review results rather than maintainability.

## What a Fix Looks Like
Generate model documentation from the model itself: data flows, formulas, assumptions and their sources, with LLM-drafted explanations reviewed by the owner. Then keep it current automatically each time the model changes, and run a parallel "second person" close once a year.

## Who Feels the Pain
Appointed actuaries, CFOs, boards of small carriers and fraternals, and state examiners.

## Impact If Fixed
Key-person risk on the statutory calendar falls sharply at almost no cost in time.
