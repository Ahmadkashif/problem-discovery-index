# Closure Detection Before the Licensee's Audit

**Niche:** [[niches/directory-and-list-publishers/business-location-data-licensing/profile|Business Location Data Licensing]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A closed business does not announce itself; it simply goes quiet, and the compiler that notices the silence first keeps the platform contract.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the licensee's reference file for which businesses exist where right now — catching openings, moves and closures first — and whoever scores freshest in the licensee's own ground-truth audit takes the contract.

## The Problem
A licensee's quarterly audit samples places and checks them against field visits and user reports. The compiler loses points mostly on closures: the restaurant that shut in March still shows as open in June because every source that listed it still lists it — nobody deletes a dead business.

## Why Nobody Has Built This
Closure is an absence of evidence, which rule-based pipelines handle badly; the positive labels (confirmed closures) are scattered across calls, licensee reports and customer complaints and are rarely assembled into a training set.

## What to Build
A closure-hazard model per place: survival analysis by category and location type, fed by signal decay — review and check-in recency, website and menu staleness, phone status, registry lapses, new businesses filing at the same address — with change-point detection on activity series. High-hazard places are verified first or published with lowered confidence, and the model is graded continuously against licensee audit results.

## Target Customer
Place-data compilers and the platform data teams that license from them.

## Impact If Built
Closures surface weeks earlier, licensee audit scores improve where they are weakest, and verification calls go to places most likely to have changed.
