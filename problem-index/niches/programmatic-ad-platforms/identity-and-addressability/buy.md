# Entity Resolution Practice

**Niche:** [[niches/programmatic-ad-platforms/identity-and-addressability/profile|Identity & Addressability]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution is a mature discipline with probabilistic matching and calibrated confidence, and adtech treats an identifier as a primary key.
**Tags:** #graph-theory #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #hypothesis-testing #dimensionality-reduction #data-integration
**Contested on:** This niche is not terminal — assembling a legitimate deterministic graph and performing well with no identifier at all are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Deciding whether two records refer to the same entity, under uncertainty, with calibrated confidence, is a well-developed field. Record linkage in official statistics, master data management in enterprises, and customer resolution in financial services all handle it with probabilistic matching, explicit match scores, clerical review of the uncertain middle, and measured precision and recall. Adtech, which has the same problem at vastly greater scale, has treated identity as a key that is either present or absent, and is now discovering what that assumption cost.

## What Already Exists
Probabilistic record linkage with calibrated match scores; master data management and golden record construction; blocking and indexing at scale; clerical review workflows for uncertain matches; and match quality measurement against truth sets.

## The Customization Gap
The adaptation is to real-time bidding with adversarial incentives and consent constraints. It requires: (1) resolution at auction latency over billions of entities, where record linkage practice assumes batch processing and a clerical reviewer — there is no human in this loop and no time, which is the central engineering change; (2) consent and permitted-use as part of the match, since a legally valid link and a technically valid one are different things and only one of them may be used; (3) truth sets that barely exist, because nobody knows the real identity graph and match quality is therefore measured against proxies — a validation problem the statistical agencies solve with census data and adtech cannot; (4) participants with an incentive to inflate match rates, which corrupts the metric the practice relies on and requires outcome-based validation instead; and (5) graceful degradation to no match as a normal operating state rather than as an exception, which the golden-record mindset treats as failure.

## Target Customer
Identity providers, demand and supply-side platforms, publishers with first-party data, and data quality vendors for whom real-time consented resolution is unserved.

## Impact If Solved
Record linkage assumes batch processing and a clerical reviewer, and there is neither here. Consent as part of the match and the absence of any truth set are the two adaptations that make adtech identity harder than the statistical version.
