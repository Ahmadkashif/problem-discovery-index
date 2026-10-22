# Tendon-Versus-Rebar Calls Made on the Scan

**Niche:** [[niches/geophysical-survey-firms/concrete-scanning-before-coring/profile|Concrete Scanning Before Cutting & Coring]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distinguishing a post-tension tendon from a rebar or a conduit in a handheld GPR scan is a technician's learned eye for depth, spacing and drape, and every core drilled afterwards is a label that is thrown away.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #transfer-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to mark every tendon, rebar mat and conduit in a slab correctly before the core drill arrives, the same day it is called, and whoever's marks never lead to a cut tendon becomes the contractor's default scanner.

## The Problem
On a post-tensioned slab, tendons drape — high over beams, low at midspan — and bunch in bands; rebar sits in regular mats; conduits wander. A skilled technician reads this from hyperbola depth and pattern across a scanned grid and marks a safe core location. Newer technicians are less sure and either mark too conservatively, forcing relocations, or miss a tendon.

## Why Nobody Has Built This
Handheld units display data rather than classify it; the scans are often not saved with the marks; and whether the core hit anything is reported only when it goes wrong.

## What to Build
A classifier running on the scanner or a paired tablet that labels hyperbolas in each grid as tendon, rebar, conduit or other, fits tendon profiles across lines, and proposes clear zones with confidence. Training data comes from saved scans paired with core photos and X-ray images, which national firms could collect at scale by making a photo of the finished core part of every job.

## Target Customer
National and regional concrete scanning firms; technology vendors supplying them.

## Impact If Built
New technicians performing at senior level sooner, fewer relocated cores, and fewer cut tendons — each a costly repair and a liability claim (estimate).
