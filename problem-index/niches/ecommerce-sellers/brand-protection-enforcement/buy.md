# Listing Detection Adapted to Adversarial Evasion

**Niche:** [[niches/ecommerce-sellers/brand-protection-enforcement/profile|Brand Protection & IP Enforcement Providers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Image similarity and text matching are commodity capabilities, and counterfeit sellers have spent a decade learning exactly how to defeat them.
**Tags:** #cnns #contrastive-learning #object-detection #bert #transformers #transfer-learning #evaluation-metrics #confidence-intervals #automation #data-integration

## The Problem
Detection means finding, among hundreds of millions of listings, the ones infringing a specific brand. The obvious approaches work on the obvious cases: exact logo matches, brand names in titles, copied product photography. Those are the listings a rights holder finds themselves. What generates value is the harder tier — deliberately altered imagery, misspelled or unicode-substituted brand names, listings that describe a product without naming it, and generic listings whose infringement is visible only in a secondary image. Analysts find these by search craft and pattern memory, which does not scale and does not transfer between analysts.

## What Already Exists
The building blocks are mature and cheap. Perceptual hashing and image embedding models handle visual similarity well; the vision APIs do logo and object detection out of the box; text similarity and fuzzy matching are commodity; several vendors sell general brand monitoring across web and social.

## The Customization Gap
Every one of those is built for a cooperative world where similar things look similar. Here the population is adversarial and specifically optimized against the standard detectors — an image cropped, mirrored, colour-shifted and overlaid defeats perceptual hashing by design, and a brand name rendered with a homoglyph defeats text matching. The adaptation is detection trained on the evasion patterns themselves, using the firm's own confirmed-infringement history as the labelled set: what altered imagery actually looks like after each common transformation, which text substitutions are in use, and which listing structures signal an infringing item without naming a brand. Detection has to operate on the full listing as an object rather than on one field, since infringement frequently lives in the fifth image or in a specification value. And precision must be calibrated per brand, because the cost of a false positive differs enormously between a rights holder that wants aggressive enforcement and one that sells through many legitimate resellers.

## Target Customer
Heads of detection and analyst operations at enforcement providers, and the brand protection teams who currently receive the easy cases and pay analysts to find the rest.

## Impact If Solved
Extends coverage into the tier where infringement actually concentrates and where a rights holder cannot self-serve, which is the part of the service worth paying for. Training on the firm's own confirmed history also makes detection improve with enforcement volume, converting operational work into a compounding capability.
