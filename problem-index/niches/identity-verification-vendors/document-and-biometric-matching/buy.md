# Presentation Attack Detection Standards

**Niche:** [[niches/identity-verification-vendors/document-and-biometric-matching/profile|Document & Biometric Matching]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Biometrics developed formal standards and testing regimes for presentation attack detection, and commercial liveness is marketed rather than certified.
**Tags:** #cnns #evaluation-metrics #confidence-intervals #contrastive-learning #compliance #object-detection #hypothesis-testing #diffusion-models
**Contested on:** Every serious competitor in this niche is fighting to tell a genuine document from a good forgery and a live person from a presentation attack, on a photograph taken by whoever happens to be holding the phone — and whoever does it best under bad capture conditions wins the populations everyone else rejects.

## The Problem
Biometrics has standards for presentation attack detection: defined attack instrument categories, testing protocols, attack presentation classification error rates, and independent laboratory certification. A vendor can be tested against known attack types and given a result. Commercial liveness claims in identity verification are largely self-asserted, tested against attacks chosen by the vendor, and reported as a marketing statement.

## What Already Exists
Presentation attack detection standards and taxonomies; independent laboratory testing regimes; attack instrument categorisation; error rate reporting conventions; and certification schemes.

## The Customization Gap
The adaptation is to an attack surface that includes generated media and injection. It requires: (1) synthetic and generated faces and documents as attack categories, which the standards contemplate incompletely and which are now the fastest-moving threat — this is the substantive gap; (2) injection attacks that bypass the camera entirely, where the standards assume something presented to a sensor; (3) uncontrolled consumer devices rather than a specified capture apparatus, so the testing condition is not reproducible; (4) an attack landscape that changes monthly, which a periodic certification cannot track; and (5) a document as well as a face, where document attack taxonomy is far less developed than biometric.

## Target Customer
Product and security leadership, regulated customers relying on liveness claims, certification bodies, and biometric testing laboratories.

## Impact If Solved
The standards regime exists and predates generated media and injection attacks. Extending attack taxonomy and continuous testing to cover them is what would make a liveness claim mean something again.
