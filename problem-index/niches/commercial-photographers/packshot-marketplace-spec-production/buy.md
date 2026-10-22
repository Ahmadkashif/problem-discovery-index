# Automated Capture Rigs Adapted to Multi-Retailer Specifications

**Niche:** [[niches/commercial-photographers/packshot-marketplace-spec-production/profile|Packshot & Marketplace-Spec Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated packshot rigs already light, shoot and cut out products at volume; they output one image style while each retailer the brand sells through wants a different one.
**Tags:** #object-detection #semantic-segmentation #feature-engineering #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to deliver every SKU's images right first time against each retailer's specification and the physical sample's true colour before the listing date, and whoever posts the lowest reshoot and rejection rate per SKU takes the account.

## The Problem
A brand sells through its own site, Amazon, two department stores and a European marketplace. Each wants different margins, background values, shadow treatment, image counts, aspect ratios and file names. The rig shoots once and the variants are produced by hand afterwards, or not at all, which leads to rejections.

## What Already Exists
Automated product photography systems (Orbitvu, PhotoRobot, StyleShoots) combine controlled lighting, turntables or fixed stations, and software that captures, removes backgrounds and exports presets. Retailer ingest portals validate files after upload.

## The Customization Gap
The adaptation needs: a maintained library of retailer specifications as machine-checkable rules, updated when retailers change them; export presets generated per retailer from one capture; validation at capture time (product fill, margin, background value, shadow, resolution) using detection and segmentation; multi-angle completeness checks against each retailer's required views; and rejection feedback from ingest portals fed back to the preset that caused it.

## Target Customer
Studio directors and production managers at ecommerce studios running automated rigs for brands that sell across several retailers.

## Impact If Solved
One capture produces every retailer's variant correctly the first time, and the reshoots and re-exports that follow ingest rejections, a recurring cost on every season, largely disappear.
