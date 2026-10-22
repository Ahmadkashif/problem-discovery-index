# Shelf-Findability Prediction From the Design File

**Niche:** [[niches/graphic-design-studios/packaging-brand-and-shelf-design/profile|Packaging Brand & Shelf Design]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Studios design redesigns blind to how fast shoppers will find the pack among real competitors, and the pack tests that measure it come too late and cost too much to run on every route.
**Tags:** #cnns #transformers #gradient-boosting #transfer-learning #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to prove, before the retailer's shelf reset, that a redesign will be found faster and chosen more often than the pack it replaces, and whoever brings shelf evidence the brand manager can defend takes the account.

## The Problem
A studio presents four redesign routes. A pack test, if the brand pays for one, comes back weeks later on the one or two routes the brand chose to test. Most routes are killed on opinion in a meeting. The question that matters — will a shopper scanning a crowded bay find this pack as fast as the old one, and pick it up — is answered once, late, for one candidate.

## Why Nobody Has Built This
Predicting shelf behaviour needs paired data: designs, the competitive shelf they sat in, and measured findability or sales. Research firms hold the test results; retailers and brands hold sales; studios hold the files. Nobody holds all three, and research firms have little reason to give their normative databases away.

## What to Build
A model that takes the design file, places it in a simulated bay built from photographs of the real category shelf, and predicts time-to-find and standout against competitors, compared with the current pack. Start from saliency and detection models pre-trained on general images, fine-tune on shelf eye-tracking and findability data licensed from or co-developed with a research partner, and validate each prediction against later pack-test results and in-market sales where the brand shares them.

## Target Customer
Packaging brand studios pitching redesigns to mid-sized consumer brands that cannot test every route, and the brand managers who need an early read.

## Impact If Built
Every route gets a defensible first read in minutes, weak routes are killed on evidence, and expensive consumer tests are spent on the finalists that deserve them.
