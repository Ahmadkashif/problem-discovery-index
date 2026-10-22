# Automated Dust-Busting Tuned to the Film Stock

**Niche:** [[niches/postproduction-studios/film-scanning-and-restoration/profile|Film Scanning, Restoration & Library Remastering]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Restoration software already removes dirt and scratches automatically; it removes grain, rain and highlights along with them, so artists review every frame anyway.
**Tags:** #cnns #semantic-segmentation #transfer-learning #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a library title's surviving film elements into a 4K HDR master a platform will license, at a cost per title its licence fee can carry, and whoever cuts the hand clean-up hours per reel takes the library's slate.

## The Problem
A feature is around 130,000–170,000 frames. Automated dirt and scratch removal catches most defects, but it also takes out things that belong: film grain, specular highlights, rain, sparks, a star in the night sky. Artists therefore step through the whole film to approve or undo each fix, and the hand clean-up hours are the cost driver.

## What Already Exists
MTI DRS Nova, Filmworkz Phoenix, Diamant-Film and Resolve's restoration tools offer automated dust, scratch, flicker and stabilisation filters with artist review.

## The Customization Gap
The adaptation needs: defect detection tuned to the stock, gauge and generation of the element, so it can tell grain structure from dirt; a classifier for intended content (rain, sparks, highlights) trained on the lab's own past corrections; confidence per fix, so artists review only uncertain frames; and a record of every accepted and rejected fix to retrain on. The generic filters use the same thresholds for a 1950s three-strip print and a 1990s negative.

## Target Customer
Restoration leads at labs handling library remastering at volume.

## Impact If Solved
If artists review only the uncertain fixes, hand clean-up per feature could fall by a third or more (estimate), which decides whether a mid-catalogue title is worth remastering at all.
