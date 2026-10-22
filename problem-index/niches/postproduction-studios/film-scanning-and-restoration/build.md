# Restoration Hours Predicted Before the Quote

**Niche:** [[niches/postproduction-studios/film-scanning-and-restoration/profile|Film Scanning, Restoration & Library Remastering]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A lab quotes a restoration from an inspection and a few test frames, and the real clean-up hours depend on damage nobody has measured yet.
**Tags:** #tacit-knowledge-ml #cnns #gradient-boosting #object-detection #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a library title's surviving film elements into a 4K HDR master a platform will license, at a cost per title its licence fee can carry, and whoever cuts the hand clean-up hours per reel takes the library's slate.

## The Problem
A library sends a list of 40 titles for remastering. For each, the lab inspects the best surviving element and quotes. A senior restoration artist looks at a few reels on a bench and a test scan and judges how bad it is: how much dirt, how many scratches, whether the emulsion is lifting, whether a reel is warped. Their judgement sets the price. They are often right, sometimes badly wrong, and the library either overpays or the lab eats the overrun.

## Why Nobody Has Built This
Restoration labs are small and specialised, and their inspection notes are handwritten. The hours per reel are known from timesheets but never linked to the condition that caused them. The expert's read of damage is tacit and has never been labelled.

## What to Build
A low-resolution triage scan of every reel, run through detectors for dirt, scratches, tears, warping, density flicker and emulsion damage, with counts and severity per reel. Combined with element type, stock, age and storage history, a model predicts clean-up hours per reel. It is trained on the lab's past jobs, with the senior artist's estimates recorded alongside for comparison.

## Target Customer
Heads of restoration at film labs; archive directors at studios and independent libraries planning remastering slates.

## Impact If Built
Quotes within a narrow band instead of a guess, and a library ranking titles by remastering cost against expected licence value before committing budget.
