# Every Exception Plotted on the Survey

**Niche:** [[niches/title-and-settlement-offices/commercial-title-escrow/profile|Commercial Title & Escrow]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lender's counsel asks of every Schedule B exception "does it touch the property, and where?", and the answer is assembled by hand from recorded instruments and the survey.
**Tags:** #large-language-models #transformers #cnns #feature-engineering #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver a marked pro forma policy, with every exception reconciled to the ALTA/NSPS survey and the endorsements lender's counsel demands, before the loan's closing deadline, and whoever negotiates exceptions and endorsements fastest across states takes the national accounts.

## The Problem
A commercial commitment can carry dozens of recorded exceptions — easements, declarations, reciprocal easement agreements, utility grants. The surveyor must plot what is plottable; the title officer must say which exceptions are blanket, which are plotted, which no longer affect the parcel, and which can be removed or insured over with an endorsement. Every round of comments from lender's counsel restarts the cross-referencing.

## Why Nobody Has Built This
The instruments are scanned images with legal descriptions in metes and bounds, the survey is a PDF drawing, and the link between them is the officer's reading. Commercial volume is too small for production-system vendors to prioritise, and the national desks treat the work as expertise rather than data.

## What to Build
Extract each exception's legal description and type from the recorded instrument, parse it into geometry where possible, overlay it on the georeferenced survey and parcel boundary, and generate a schedule: exception, instrument link, plotted or blanket, affects or does not affect, and a recommended disposition (remove, keep, insure over with a named endorsement). Keep the whole redline history as structured comments.

## Target Customer
Commercial title officers at multi-state agencies and underwriter national commercial desks; also the surveyors and lawyers on the other side of the same review.

## Impact If Built
The first pro forma goes out with the survey reconciliation already done, review rounds shrink, and the office that turns commercial deals fastest wins the next deal from the same counsel.
