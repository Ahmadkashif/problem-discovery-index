# The Realisation Rate Nobody Computes by Carrier

**Niche:** [[niches/legal-practice-software/insurance-defense-platforms/profile|Insurance Defense & Panel Counsel Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Defense firms know their overall realisation rate and cannot decompose it by carrier, matter type, timekeeper or reduction reason, so they negotiate panel rates and accept work without knowing which clients actually pay.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #revenue-impact #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in insurance defense software is fighting to get a firm's invoice through the carrier's bill review engine unreduced on the first pass — and whoever predicts the reduction before submission takes the account.

## The Problem
A firm's managing partner knows realisation is around 88%. He does not know that one carrier runs at 94% and another at 79%, that the 79% is concentrated in a matter type the firm takes because the volume is attractive, or that a third of the reductions come from one avoidable narrative pattern. When the panel rate conversation comes around, he negotiates an hourly rate, which is the wrong variable — a $10 rate increase against a nine-point realisation gap is not a good trade, and he has no way to see that. The firm's most important commercial fact is an average.

## Why It's Still Broken
The adjudication data comes back into accounting as a payment amount and a reduction total, and the line-item detail, which the carrier does provide, is not parsed back to the originating entries. Nobody's job description covers doing it: the billing manager is measured on submitting and collecting, the accountant on closing the month, and there is no analyst. There is also an uncomfortable dynamic — a firm that discovers a carrier is unprofitable has to decide what to do about a client it depends on, and averages postpone that decision indefinitely.

## What a Fix Looks Like
Parse the line-item adjudication and join it to the originating time entries, which is a week of integration work. Then publish the decomposition as a standing report: realisation by carrier, by matter type, by timekeeper, by task code, and by reduction reason, with the trend. Add effective realised rate — what the firm actually collects per hour worked after reductions and write-offs, by carrier — because that, not the nominal panel rate, is the number that should drive whether the firm takes the work. Rank reduction reasons by dollars so the firm knows which single behaviour to change first. None of this is modelling; it is a join the industry has not made.

## Who Feels the Pain
Managing partners negotiating panel rates on the wrong variable; associates told to write better narratives without being told which ones failed; and billing managers who see every reduction individually and can never total them.

## Impact If Fixed
Firms that decompose realisation for the first time generally find a carrier or matter type running several points below the average and a small number of reduction reasons carrying most of the loss — both actionable within a quarter. The effective realised rate is the single most useful number this niche can produce, and it is available today from data every firm already receives and discards.
