# The Flash Before the Variant Loads

**Niche:** [[niches/conversion-optimization-firms/variant-implementation/profile|Variant Implementation Quality]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Half the variant group sees the original page for a moment before it changes, and that is in the result.
**Tags:** #quick-win #automation #evaluation-metrics #descriptive-statistics #confidence-intervals #data-integration #change-point-detection #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to change a live page without introducing effects that have nothing to do with the hypothesis — and whoever implements variants cleanly takes the account.

## The Problem
Flicker is the oldest known defect in client-side testing and it is still present in most implementations. The user sees the control briefly and then the variant appears. On a slow connection it is a visible flash; on a very slow one the user may act before the variant loads. The variant group therefore experiences something the control group does not, unrelated to the hypothesis, and it is not measured, reported or corrected for.

## Why It's Still Broken
Flicker is known and tolerated — a defect that everyone in the field can name and nobody measures persists because tolerating it is free and measuring it would complicate every result. Anti-flicker techniques have their own costs. It is worse on slow connections, which are underrepresented in the team's own testing. And it does not show up in the result as anything but a difference.

## What a Fix Looks Like
Measure it, reduce it, and report it. Measure the time between page render and variant application and report it with every test, which is the fix and makes an invisible artefact visible. Segment results by connection speed, since the flicker is worst exactly where it is most consequential and the effect may reverse there. Load the testing script as early as possible and minimise what it does, which is the standard mitigation and is frequently not applied. Use a hiding technique with a short timeout rather than a long one, since a blank page is its own artefact. Test on slow connections deliberately rather than on the office network. Consider server-side delivery for the tests where flicker would matter most, which are usually the important ones. Exclude sessions where the variant demonstrably failed to apply. Compare page performance between arms and report a difference, as a slower variant is a confound. Report the flicker figure in the result so the reader can weigh it. And treat a test where flicker is comparable to the effect as inconclusive rather than reporting a winner.

## Who Feels the Pain
Users who see a page change under them; clients acting on results contaminated by an artefact; strategists whose careful hypothesis is measured against a script defect; and the discipline's replication rate.

## Impact If Fixed
A defect everyone can name and nobody measures persists because tolerating it is free and measuring it complicates every result. Reporting flicker duration with each test makes the artefact weighable.
