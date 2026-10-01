# The Collection Analyst at 2 a.m. in Earnings Season

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Type:** Worker Life Changing
**One-liner:** The analyst who standardises a US company's quarter is often working a night shift in Hyderabad or Manila against a timeliness SLA, re-keying values the XBRL already contains and resolving the hard ones alone.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #feature-engineering #worker-facing #tacit-knowledge-ml #automation

## The Problem
US filings and press releases arrive after the market closes in New York, which is the middle of the night in the operations centres where most collection happens. For six weeks four times a year, the analyst's shift is aligned to EDGAR, not to daylight. Each filing comes with a timeliness target — standardised fundamentals within a set number of hours — and a quality target enforced by sample re-keying.

The work is uneven. Most of the template is pre-populated from XBRL and the analyst confirms it field by field, because the tool does not distinguish the fields that are always right from the ones that are often wrong. Then come the five items per filing that require judgement — a footnote, a reclassification, a non-GAAP reconciliation — where the analyst either knows the issuer's history or has to reconstruct it from prior quarters, an internal wiki and whichever senior colleague is awake.

## Why It Matters to the Worker
The confirmation work is dull and the judgement work is lonely. An analyst is graded on errors found in a sample, so the rational strategy under deadline is to follow the XBRL tag even where they suspect it is wrong, because an override that turns out wrong is an error charged to them and a tag followed wrongly is the issuer's mistake. The incentive punishes exactly the judgement that makes them valuable.

Feedback arrives late and abstractly. A client ticket weeks later becomes a QA finding, rarely with the explanation of what the right reasoning was. Skill accumulates slowly, is not certified, and does not show on a CV beyond the employer's name. Night-shift seasons drive attrition, and attrition takes issuer knowledge with it.

## What a Solution Looks Like
Pre-population with confidence. Fields the model is confident about, based on this issuer's history, are shown as confirmed and skipped; the analyst's attention goes to the handful flagged as uncertain, with the reason for the flag.

Precedent on the screen. For each judgement item, the issuer's own prior treatment, how comparable issuers' similar footnotes were mapped, and the relevant house policy paragraph — the colleague who is not awake, made retrievable.

Override protection. An override supported by cited evidence is recorded as judgement, not counted against the analyst if adjudication later goes the other way on a genuinely ambiguous item.

Fast, specific feedback. When a client ticket changes a mapping the analyst made, they see the ticket, the corrected treatment and the reasoning, within days.

## Impact If Solved
Confirmation work shrinks to exceptions, which shortens shifts in the peak and lets the same team cover more issuers without more nights. The bigger change is that judgement stops being a liability on the analyst's scorecard, which is the condition for retaining the people who have it.
