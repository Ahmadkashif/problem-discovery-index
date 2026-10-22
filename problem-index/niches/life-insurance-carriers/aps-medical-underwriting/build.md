# A Page-Linked APS Timeline That Learns the Senior Read

**Niche:** [[niches/life-insurance-carriers/aps-medical-underwriting/profile|Full Medical Underwriting & APS Review]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Summarising an APS is becoming a commodity; capturing what a senior underwriter does with the summary, and teaching it to the next underwriter, is not.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn an attending physician statement into a defensible risk class in days rather than weeks, and whoever cuts APS-to-decision time without moving class agreement on blind re-underwriting takes the account.

## The Problem
A senior underwriter discounts one abnormal reading, weighs a trend across three normal ones and reads worry into a specialist's phrasing. None of that is recorded. When a junior underwriter or a summarisation tool handles the same file, the class shifts, and the carrier cannot see where or why.

## Why Nobody Has Built This
Summarisation vendors stop at the summary. Workbenches record the final class. The labels are noisy, because underwriters disagree with themselves, and the mortality outcome is slow, so the value is hard to prove in a pilot.

## What to Build
Extraction of every finding into a dated, page-linked timeline mapped to the carrier's manual, with a proposed worksheet. Senior underwriters confirm or edit in a few clicks, and each edit becomes a labelled adjustment. A model of those adjustments then flags, for juniors, the findings a senior would have weighed differently. Blind re-underwriting panels measure consistency every quarter.

## Target Customer
Chief underwriters at carriers with large fully underwritten permanent life and high-face term books, and the reinsurers' facultative units.

## Impact If Built
Days off every referred case, a measurable rise in class consistency, and senior judgement that stays when the senior retires.
