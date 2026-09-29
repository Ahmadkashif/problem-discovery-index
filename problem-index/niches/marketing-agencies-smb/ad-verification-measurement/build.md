# Fraud Detection Judged by Detection Rate on an Unknown Denominator

**Niche:** [[niches/marketing-agencies-smb/ad-verification-measurement/profile|Ad Verification & Measurement]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The company reports how much invalid traffic it caught and has no way to say how much it missed.
**Tags:** #anomaly-detection #graph-ml #binary-classification #evaluation-metrics #hypothesis-testing

## The Problem
Invalid traffic detection is the core of this business. The product reports what proportion of a campaign's impressions were fraudulent, and advertisers withhold payment or shift spend accordingly.

The reported figure is a detection rate. It says what the system flagged. It says nothing about what it did not flag, because there is no independent measurement of true fraud volume — and a sophisticated scheme that evades detection contributes zero to the reported number, which makes it look like a clean environment.

The incentive structure quietly rewards this. A vendor reporting 2% invalid traffic looks better to a nervous advertiser than one reporting 8%, and neither number is verifiable. So the industry's headline metric is a measure of the detector rather than of the problem, and the detectors compete on a number that improves when they get worse.

Meanwhile the company holds enormous signal: measurement telemetry across trillions of impressions, with device, network, publisher, and behavioural features, and — through its own client base — the campaign outcomes that followed.

## Why Nobody Has Built This
Detection has always been rule and signature driven, because fraud schemes are discrete and identifiable once found, and a signature is explainable to a publisher who disputes a finding. That explainability requirement is real and it has kept the approach adversarially reactive.

Estimating what is missed is also uncomfortable. A company that publishes an estimate of its own false negative rate has published a limitation, and no competitor is doing it.

And the ground truth problem looks intractable — nobody labels fraud independently. It is more tractable than it looks: honeypots, deliberate spend on known-invalid inventory, injected test traffic, and post-hoc conversion analysis all give partial visibility, and partial is infinitely better than none.

## What to Build
Estimate the fraud that is not caught, and detect schemes rather than signatures.

**Build measurement of the unmeasured.** Controlled experiments — placing measurable traffic through inventory of known character, running holdouts, and injecting labelled test impressions — give an estimate of detection coverage rather than detection count. This is the number nobody in the industry publishes.

**Model at the network level, not the impression level.** Fraud is coordinated: shared infrastructure, correlated behaviour across devices and publishers, timing structure. Graph and clustering methods over the telemetry find rings that signature matching cannot, because the entity is the scheme rather than the impression.

**Detect novelty explicitly.** The commercially important cases are the ones no signature covers. Anomaly detection on population behaviour — traffic that is unlike anything seen and unlike everything else in its cohort — is the complement to signature matching and is where the missed volume lives.

**Join to downstream outcomes.** Impressions that were passed as valid and produced no measurable engagement or conversion, at rates far below cohort, are evidence about the detector. The company's client relationships give it that view and it is not used as feedback.

**Report coverage, with an interval.** "We detected 3.1% and estimate total invalid traffic at 5-9%" is a harder sell and a vastly more useful product, and the first vendor to publish it changes the terms of the category.

## Target Customer
Chief Product Officer or VP of Data Science at a verification provider. The pressure is that accreditation bodies and large advertisers are increasingly sophisticated about the detection-rate problem, and the vendor that gets ahead of it rather than being caught by it owns the argument.

## Impact If Built
Very large advertising budgets are allocated on a number that measures the measurer. Estimating unmeasured fraud, and finding schemes structurally rather than by signature, changes what the industry knows about a problem it has been reporting on for a decade without ever sizing.
