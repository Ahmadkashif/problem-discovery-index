# The False Rejects Nobody Counts

**Industry:** [[identity-verification-vendors|Identity Verification Vendors]]
**Type:** High Impact
**One-liner:** A person who fails verification abandons and disappears, so the error that matters most to real people is the one the industry has no measurement of and no incentive to produce.
**Tags:** #cnns #object-detection #gradient-boosting #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

## The Problem
Someone opens an account. They photograph their licence, take a selfie, and their details are checked against databases. A score comes back. Below the threshold, they fail.

What happens next is nothing, from the vendor's perspective. The person tries again, perhaps in better light, perhaps not. They give up. They try a different provider. They visit a branch if one exists for that product, which increasingly it does not.

The vendor observes a pass rate and a fraud rate among those who passed. It does not observe whether the people who failed were genuine, because there is no subsequent event that reveals it. Manual review recovers some, and those recoveries are the only real evidence available — and they are evidence about the subset persistent enough to appeal, which is not a random subset.

This would be an ordinary measurement gap except for how the failures distribute. NIST's evaluations have found demographic differentials in face recognition error rates across algorithms and demographic groups, with the magnitude varying enormously by algorithm — which means the differential is a property of the specific system deployed, not an inherent limit, and is therefore measurable and improvable. Document verification carries its own skew: newer and more standard documents read better, newer phones capture better images, and some document types are simply better supported. Database verification skews toward people with stable addresses and thick credit files, and away from those who move often, share housing, are recent immigrants, or are young.

Each of those is defensible individually. Stacked in an orchestration flow, they compound in the same direction, and the population most likely to fail is substantially the population least able to absorb being denied a bank account.

The vendor's incentives do not point at this. Customers buy on fraud caught and on pass rate. A vendor that measured and published error rates by population would produce a number competitors do not publish, in a domain where the number will be uncomfortable.

And the threshold is not the vendor's alone. Customers configure it, often conservatively, because a fraud loss is attributable and a rejected applicant is invisible — the same asymmetry, one layer up.

## Why It's Unsolved
The counterfactual is genuinely unobservable through ordinary operation. A rejected person produces no outcome, and unlike a declined transaction there is not even a retry pattern in most flows. Only deliberate measurement produces evidence.

Demographic measurement requires demographic data, which most vendors do not collect and have good privacy reasons not to. Measuring disparity requires either inferring the attribute — itself problematic — or a deliberate, consented audit population. Neither is free, and the privacy objection to collecting it is real rather than a pretext, which is why the honest approach is a bounded audit rather than pervasive collection.

The liability structure diffuses responsibility. The vendor supplies a score, the customer sets the threshold, the orchestration layer routes between vendors, and no single party owns the outcome. Everyone can point elsewhere.

And biometric privacy law, BIPA especially, makes retaining the images that would enable rigorous error analysis legally risky. The regime that protects people from surveillance also obstructs the audit that would show them being wrongly excluded, which is a real tension and not a rhetorical one.

## What a Solution Looks Like
A consented audit population. A recruited, demographically documented set of genuine identities passed through the system periodically produces a direct measurement of false reject rates by group, document type, device class and capture condition. It is a panel study rather than a research programme, it is affordable, and it is the only clean evidence available.

Recovery-path instrumentation as the second-best measurement. Every person who fails automated verification and is subsequently confirmed genuine through manual review or an alternative path is a confirmed false reject. Instrumenting that path fully, and reporting it stratified by document type, device and capture condition, is available today with no new data collection at all.

Error decomposition by cause. Failure because the image was blurred, because the document type is unsupported, because the face match scored low, or because the address history is thin are four different problems with four different remedies, and they are currently collapsed into one outcome.

Capture assistance rather than rejection. A large share of document failures are image quality problems solvable at capture time with real-time feedback, which converts a rejection into a retake and disproportionately helps people on older devices.

Threshold guidance to customers based on measured error, so a customer choosing a conservative setting is told what it costs in rejected genuine applicants rather than being allowed to assume it is free.

Published methodology. The first vendor to publish its false reject rate and its error distribution with a credible method sets the standard that every competitor is then asked about in procurement.

## Impact If Solved
These systems are the gate to the financial system and their error distribution is unmeasured by anyone, including the firms that operate them. A consented audit panel and fully instrumented recovery paths would produce that measurement at modest cost, and would let a vendor compete on a dimension the industry currently cannot discuss — which matters commercially and matters considerably more to the people who are currently turned away without explanation or recourse.
