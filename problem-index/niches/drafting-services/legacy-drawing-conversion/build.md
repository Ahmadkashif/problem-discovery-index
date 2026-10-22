# Confidence-Scored Conversion That Knows What to Field-Verify

**Niche:** [[niches/drafting-services/legacy-drawing-conversion/profile|Legacy Drawing Conversion & As-Built Documentation]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A converted floor plan looks equally authoritative everywhere, even where it was traced from a smudged 1968 blueprint of a wing that has since been rebuilt.
**Tags:** #cnns #semantic-segmentation #transformers #bayesian-inference #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to turn paper archives, scanned blueprints and field measurements into accurate, layered CAD that the owner's facilities team can maintain, and whoever proves dimensional fidelity without a return site visit takes the facility portfolio.

## The Problem
Owners commission conversion to get a reliable base for space planning and renovation design. The deliverable is clean CAD, and nothing in it says which walls were read from a crisp later drawing, which from a faded original, and which conflict with a renovation record. Design teams discover the errors during the next project, at their own cost.

## Why Nobody Has Built This
Conversion is priced per sheet, and bureaus are paid for clean output, not for disclosing uncertainty. Converters handle pixels, not provenance.

## What to Build
A conversion pipeline that segments walls, openings, dimensions and text from scans; reconciles overlapping sources (original, renovations, record sets) by date and legibility; and attaches a confidence score to every element and dimension. Low-confidence areas are marked for field verification, with a ranked list for the site visit.

## Target Customer
Facility directors at campuses, health systems and government agencies with large drawing archives; bureaus that want to sell accuracy rather than sheet counts.

## Impact If Built
Targeted field verification instead of none or all, and base drawings design teams can trust where they are marked as trustworthy.
