# The Load Typed Into a Workbook Cell

**Niche:** [[niches/reinsurers/property-cat-treaty-underwriting/profile|Property Catastrophe Treaty Underwriting]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Fix (Pain Point)
**One-liner:** The decision that moves a cat price most is a number typed into a spreadsheet cell, and a year later nobody, including the underwriter, can say what it was for.
**Tags:** #large-language-models #evaluation-metrics #feature-engineering #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a cedent's submission into a quoted own view of risk, with every load against the vendor model explained, before the broker's firm-order deadline, and whoever's loads still look right after the next large event takes the account.

## The Problem
An underwriter types a load of, say, 1.25 into the pricing workbook for a cedent and moves on to the next submission. When the programme renews, a colleague reprices it, sees the factor and has to guess whether it was for data quality, Florida litigation or wildfire. The guess becomes the next year's load.

## Why It's Still Broken
Workbooks belong to individuals, renewal weeks leave no time for notes, and nothing downstream asks for the reason until a large loss prompts a post-mortem.

## What a Fix Looks Like
Split the single factor into named components at the point of entry, with a one-line reason for each, drafted from the referral memo and confirmed by the underwriter. Carry the components forward to next year's pricing pack, so the renewal starts from the reasons rather than the number.

## Who Feels the Pain
Underwriters inheriting a portfolio; chief underwriting officers explaining price movements to brokers; capital teams asked by rating agencies how the firm adjusts vendor models.

## Impact If Fixed
A few seconds per programme turns an undocumented habit into a reviewable record and gives every renewal a starting point the underwriter can trust.
