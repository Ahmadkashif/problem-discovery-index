# Desktop Appraisal Data Sufficiency Assessment

**Niche:** [[niches/real-estate-appraisers/desktop-and-hybrid-appraisers/profile|Desktop & Hybrid Appraisers]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Fix (Pain Point)
**One-liner:** Appraisers accept desktop appraisal orders before knowing whether sufficient remote data exists to produce a credible valuation — discovering 90 minutes into the assignment that the MLS has no interior photos, the tax records show a 15-year-old square footage, and no prior appraisal exists, forcing them to either produce a below-standard report or return the order and forfeit the fee.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
When an appraiser accepts a desktop appraisal order, they commit to producing a valuation without physical inspection. But whether a credible desktop valuation is possible depends on available data: does the MLS have recent listing photos showing interior condition? Does the tax assessor's square footage match other sources? Has the property been appraised recently (providing prior inspection data)? Are there sufficient comparable sales with desktop-verifiable data? The appraiser doesn't know the answers until they start working — and by then, they've committed time. If data is insufficient, they either produce a report with qualified assumptions (risking CU flags and professional liability) or return the order (forfeiting the fee and wasting 60-90 minutes of research).

## Why It's Still Broken
AMCs assign desktop orders based on property eligibility criteria (loan-to-value ratio, property type, market stability) without checking whether the specific property has sufficient remote data for a credible valuation. No pre-order data sufficiency check exists because it requires querying multiple data sources per property — the same data assembly step the appraiser does manually at the start of each assignment.

## What a Fix Looks Like
A pre-acceptance data sufficiency screening tool that: queries available remote data for the property before the appraiser accepts the order; provides a "desktop viability score" indicating data completeness; flags specific data gaps (no MLS photos, tax records > 5 years old, no prior appraisal); recommends desktop (sufficient data), hybrid (needs inspection for specific items), or traditional (insufficient for remote valuation). The appraiser reviews the viability score before accepting or declining the order.

## Who Feels the Pain
Appraisers who accept desktop orders that turn out to be uncompletable — approximately 20,000-30,000 appraisers performing desktop work, of whom 15-25% experience at least one uncompletable order per month.

## Impact If Fixed
Uncompletable order acceptance drops from 15-25% to under 5%. Wasted time on orders that must be returned drops from 60-90 minutes per incident. Appraiser confidence in accepting desktop orders increases, reducing desktop order decline rates (currently 30-40% of offered orders are declined due to data uncertainty).
