# Batch Record Review & Release by Exception

**Parent Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to cut QA's review of each executed batch record to the entries that need a human, and whoever releases the highest share of batches with no documentation error found after release takes the account.

## Profile
**Market Size:** ~$800M a year in eBR and MES review modules, document capture and the QA review labour they replace at US drug-product sites (estimate)
**Share of Parent Industry:** ~0.5% of US receipts (estimate)
**Digital Adoption:** Medium — large plants run eBR, but many generic and CDMO plants still review paper or hybrid records page by page
**Target Buyer:** Director of QA Operations / Head of Batch Release
**Automation Potential:** High — entry checks, calculations, signature completeness and trend flags are mechanical; the release decision stays with QA

## What Makes This a Distinct Niche
No batch ships until QA has reviewed its executed production and control records (21 CFR 211.188 and 211.192) and every deviation is closed or assessed. The work is the most repetitive in the quality unit: the same master record reviewed batch after batch, against the same limits, for the same documentation errors. Review time is release time, and release time is inventory and service level. The packaging-stage version, where the contract packager releases serialised packs, sits in [[niches/contract-packagers/commercial-drug-packaging-serialisation/profile|Commercial Drug Packaging & Serialisation]].

## Current Tools & Gaps
Körber PAS-X, Emerson Syncade and Siemens Opcenter for eBR with review-by-exception reports; Tulip, Apprentice.io, Leucine and Seal as newer frontline platforms; ABBYY-style capture for paper. Gaps: exception rules are configured product by product and rarely finished; legacy paper and handwriting are unread; exceptions are not linked to open deviations or to the product's trend history.

## Problems
- [[niches/pharmaceutical-manufacturers/batch-record-review-release/build|🔨 Build: Exception Rules Learned From Years of QA Corrections]]
- [[niches/pharmaceutical-manufacturers/batch-record-review-release/buy|🛒 Buy: eBR Review by Exception, Configured Product by Product]]
- [[niches/pharmaceutical-manufacturers/batch-record-review-release/fix|🔧 Fix: The Record That Bounces Between QA and Production]]
