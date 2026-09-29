# Transparency Flattened by Surprise

**Niche:** [[niches/print-on-demand-platforms/preflight-and-colour/profile|Preflight & Colour]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A design with transparency, soft shadows or blend modes is flattened by the raster processor against an assumed background, and what the merchant sees and what prints diverge for a reason nobody surfaces.
**Tags:** #numerical-methods #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #compliance #quick-win #object-detection
**Contested on:** Every serious competitor in this niche is fighting to make the file check catch the things customers actually complain about — and whoever does that stops the reprints, because the current check passes almost everything that later fails.

## The Problem
A design has a soft drop shadow and a partially transparent overlay. On the merchant's screen and in the platform's mockup it composites against the garment colour and looks right. In production the file is flattened against white before printing and the shadow becomes a grey halo, or it is printed with an underbase that turns the transparency into a solid block. Which of those happens depends on the facility's raster settings. The merchant never saw a warning, the mockup actively reassured them, and the same file produces different results at different facilities for reasons nobody has written down.

## Why It's Still Broken
Transparency handling is decided by the raster processor's configuration, which is a facility-level setting nobody standardised across a partner network. The mockup composites in a rendering environment with no relationship to the print path. Preflight does not report transparency because it was written to check resolution. And the resulting defect looks like a printing error rather than a file handling decision.

## What a Fix Looks Like
Resolve it explicitly and show the result. Flatten transparency deterministically in the platform against the actual substrate colour before the file reaches any facility, which removes the facility-level variation at a stroke and is the fix — the same file then produces the same result everywhere. Report to the merchant what was flattened and how, so a surprising result is explained before it is printed. Generate the mockup from the flattened, substrate-composited file rather than from the original, since the mockup is currently the main source of the merchant's false confidence. Standardise raster configuration across the network and verify it, since unstandardised settings are the cause of the same-file-different-result problem generally. Detect blend modes and effects that do not survive the print path and warn specifically. Offer the merchant a preview against each substrate colour they have listed on, since a design that works on white and fails on black is common and currently invisible. Handle the underbase decision explicitly for coloured substrates rather than leaving it to the facility. And test the whole path with a standard file set per facility, which is a quick check that catches configuration divergence before customer orders do.

## Who Feels the Pain
Merchants whose designs print differently from what they approved; facilities blamed for a file handling decision; and customers receiving a grey halo where a soft shadow was intended.

## Impact If Fixed
Flattening deterministically in the platform against the real substrate removes facility-level variation at a stroke, so the same file produces the same result everywhere. Generating the mockup from the flattened file removes the main source of the merchant's false confidence.
