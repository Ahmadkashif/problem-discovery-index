# The Model Never Learns What the Appraiser Knew

**Niche:** [[niches/real-estate-appraisers/avm-collateral-valuation-analytics/profile|Automated Valuation Models & Collateral Analytics]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Fix (Pain Point)
**One-liner:** Millions of appraisals record which comparables a human chose and what dollar adjustment they made for each difference, and none of it reaches the model that is replacing them.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #data-integration #causal-inference #automation

## The Problem
Pass 1 states the profession's core expertise precisely: adjustment development. An experienced appraiser derives supportable dollar adjustments for physical and locational differences between a comparable sale and the subject property from matched-pair analysis, calibrated to how buyers in that specific market actually respond. Junior appraisers use mechanical tables; experienced ones do not. Pass 1 calls this the most economically significant tacit knowledge in the industry.

Automated valuation models are built without it. They are fitted to transaction prices and property attributes, and they learn adjustments implicitly from the data, which is a defensible approach and discards a large body of expert judgment that exists in structured form.

Because appraisals are structured. A completed report names the comparables selected, states the difference on each line, and gives the dollar adjustment applied and the adjusted value. That is a human expert's explicit statement of what a specific difference is worth in a specific micro-market on a specific date, and there are millions of them, on standardised forms, machine-readable.

They sit in three places, none of which is the model: the appraisal software the report was written in, the appraisal management company that reviewed it, and the secondary market entity it was delivered to. The last of these holds essentially every conforming appraisal for over a decade, joined to what the loan then did.

The loss runs both ways. The models do not learn from appraiser judgment. And the appraisers — whose adjustments are, per Pass 1, what separates a senior from a junior — get no feedback either, because nobody compares their adjustments to what the transaction data implies or to what other appraisers in the same market concluded.

## Why It's Still Broken
The data is fragmented across parties whose interests do not align. The appraisal belongs to the lender and the appraiser; the software vendor holds it under terms that do not permit pooling; the secondary market entity holds the deepest corpus and is a policy body rather than a data vendor.

Appraiser independence rules are also a genuine constraint, correctly designed to stop anyone influencing a valuation. They are frequently read to forbid any feedback loop at all, which is broader than the rules require and has had the effect of preventing measurement as well as pressure.

And there is a competitive edge to it. Automated valuation providers are commercially displacing appraisers, and building a product that depends on appraiser output is an awkward position to explain — even though the appraisers whose reports are already in the corpus are largely retired.

## What a Fix Looks Like
**Extract adjustments as structured data.** Comparable selected, feature difference, dollar adjustment, market, date, appraiser. The forms are standardised and the extraction is a solved problem; nobody has been motivated to run it at scale.

**Treat expert adjustments as a prior, not as truth.** Appraiser adjustments carry real market knowledge and also carry convention, anchoring and habit. Using them to inform a model — and measuring where they agree with transaction-implied adjustments and where they diverge — is more valuable than either source alone.

**Measure the divergence and publish it internally.** Where a market's appraisers systematically adjust differently from what paired sales imply, one of the two is wrong, and knowing which market that happens in is directly useful to a lender's collateral risk function.

**Give appraisers the comparison back.** How an appraiser's adjustments compare to the distribution of adjustments in their market for the same feature is information, not influence — it says nothing about any specific value. Establishing that distinction with counsel is the work that unlocks the loop.

**Close on outcomes.** The secondary market corpus joins appraisals to loan performance, which means it can say which valuation practices preceded losses. Nothing in residential valuation approaches the value of that link, and it is used for policy rather than for measurement.

## Who Feels the Pain
Lenders relying on models that ignore the largest body of expert market knowledge in existence; appraisers whose central professional skill is never evaluated and cannot be transferred to the next generation, in a profession Pass 1 describes as under structural pressure; and the modellers, who are re-deriving from transactions what a hundred thousand people already wrote down.

## Impact If Fixed
Residential valuation is being automated on data that excludes the one thing the humans it replaces were actually expert at. Bringing millions of explicit, dated, market-specific adjustment judgments into the modelling — and using the comparison to give appraisers the calibration nobody has ever given them — improves both sides of a transition that is happening regardless.
