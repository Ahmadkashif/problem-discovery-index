# Conversion Collection and Consent Gaps

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every measurement model depends on a conversion record that is now partial, consent-dependent and silently modelled by each platform in its own favour, and the plumbing to fix it is rebuilt from scratch at every client.
**Tags:** #bayesian-inference #gradient-boosting #confidence-intervals #probability-distributions #evaluation-metrics #data-integration #compliance #feature-engineering

## The Problem
Measurement starts with knowing what happened. That record has degraded on every axis: browser restrictions on third-party and now some first-party cookies, ad blockers, consent banners that suppress tracking for a meaningful share of European traffic, app-level restrictions on mobile, and platform conversion APIs that each fill their own gaps with their own modelling.

What arrives at a measurement vendor is a partial conversion record whose missingness is not random — it correlates with browser, region, device, consent behaviour and therefore with demographics and with channel. A model fed that record without correction attributes the pattern of missingness to the channels that happen to correlate with it.

Implementation is where most of the pain lands. Server-side tagging, conversion APIs for each platform, consent mode configuration, identity stitching across web, app and offline, deduplication between browser and server events — each a project, each rebuilt at every client, each capable of failing silently. A misconfigured deduplication doubles conversions for one channel and nobody notices for a quarter.

## What Already Exists
Server-side tag management from Google, Tealium and Segment is mature. Every major platform provides a conversion API — Meta's CAPI, Google's Enhanced Conversions, TikTok's Events API — with documentation and modelled-conversion features. Consent management from OneTrust, Didomi and Usercentrics is standard in regulated markets. Customer data platforms handle identity stitching. Mobile has SKAdNetwork and its successors, where aggregation and delay are imposed by the operating system rather than chosen.

## The Customisation Gap
The tools are generic and every client's stack is specific: a different commerce platform, a different consent posture, different offline conversion sources, a different tolerance for server-side data sharing. So the plumbing is bespoke consulting at each client, done once, documented poorly, and broken by the next site release.

The measurement-relevant gap is that the missingness is never modelled. A vendor that estimated the conversion record's completeness by segment — browser, region, consent state, device — and corrected for it explicitly would produce materially different answers from one that treats the observed record as the truth. The correction is estimable: consent rates are known, the completeness of the record is comparable against order totals from the client's own finance data, and the difference is informative.

Platform-modelled conversions are the sharpest version of the problem. Each platform fills its own gaps with its own model, in its own favour, and reports the result as a conversion count without distinguishing observed from modelled. A measurement vendor ingesting those numbers as data is ingesting another party's inference. Separating the two, where the platforms disclose it, and treating modelled conversions as an estimate with uncertainty rather than a count, is basic hygiene that nearly nobody performs.

## Impact If Solved
Everything downstream inherits this record, so an uncorrected bias here propagates into every contribution estimate and every reallocation decision. Modelling the missingness rather than ignoring it, reconciling against the client's own finance totals, and refusing to treat another party's modelled conversions as observations are corrections that change answers by more than most modelling refinements, and they are unglamorous enough that the category has largely skipped them.
